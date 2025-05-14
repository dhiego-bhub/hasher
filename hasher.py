import streamlit as st
import bcrypt

st.set_page_config(
    page_title="Password Hasher for Streamlit",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Hasher for Streamlit")
st.write("""
This tool generates Bcrypt password hashes compatible with Streamlit Authenticator.
Enter your password below, then copy the hash and send it to your administrator.
""")

def hash_password(password):
    """Generate a bcrypt hash for streamlit-authenticator compatibility"""
    # Generate a salt and hash the password (12 is the default rounds in streamlit-authenticator)
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Return the hash as a string
    return hashed.decode('utf-8')

with st.form("hash_form"):
    password = st.text_input("Enter your password", type="password")
    password_confirm = st.text_input("Confirm your password", type="password")
    submit_button = st.form_submit_button("Generate Hash")
    
    if submit_button:
        if not password:
            st.error("Please enter a password")
        elif password != password_confirm:
            st.error("Passwords don't match. Please try again.")
        else:
            try:
                # Generate the bcrypt hash
                hashed_password = hash_password(password)
                
                st.success("Password successfully hashed!")
                
                st.markdown("### Your Password Hash:")
                
                text_area = st.text_area("Copy this hash:", value=hashed_password, height=100, key="hash_result")
                
                # Display a sample YAML format
                st.markdown("### Example YAML format:")
                
                yaml_example = f"""
username:
  email: username@example.com
  name: User Name
  password: '{hashed_password}'
"""
                st.code(yaml_example, language="yaml")
                
                st.info("📋 Select the hash above, copy it (Ctrl+C or Cmd+C), and send it to your administrator")
                                
            except Exception as e:
                st.error(f"Error generating hash: {e}")

# Footer
st.write("---")
st.write("Password Security Note: This tool uses Bcrypt with 12 rounds, compatible with Streamlit Authenticator.")
