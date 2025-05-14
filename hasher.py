import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Password Hasher Tool",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Hasher Tool")
st.write("""
This simple tool generates a secure password hash.
Enter your password below, then copy the hash and send it to your administrator.
""")

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
            # Generate the password hash
            hashed_password = stauth.Hasher([password]).generate()[0]
            
            st.success("Password successfully hashed!")
            
            st.markdown("### Your Password Hash:")
            
            st.code(hashed_password, language="text")
            
            st.info("📋 Copy this hash and send it to your administrator")
            
            # Add a copy button
            st.button(
                "Copy to Clipboard",
                help="Click to copy the hash to your clipboard",
                on_click=lambda: st.write(f"<script>navigator.clipboard.writeText('{hashed_password}');</script>", unsafe_allow_html=True)
            )

# Footer
st.write("---")
st.write("Password Security Note: The original password cannot be recovered from this hash.")
