import streamlit as st
import bcrypt

st.set_page_config(
    page_title="Gerador Hasher",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Gerador Hasher")
st.write("""
Essa ferramenta gera um hasher que você deverá copiar e enviar ao Dhiego.
""")

def hash_password(password):
    """Generate a bcrypt hash for streamlit-authenticator compatibility"""
    # Generate a salt and hash the password (12 is the default rounds in streamlit-authenticator)
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Return the hash as a string
    return hashed.decode('utf-8')

with st.form("hash_form"):
    password = st.text_input("Insira uma senha desejada", type="password")
    password_confirm = st.text_input("Confirme a senha", type="password")
    submit_button = st.form_submit_button("Gerar Hash")
    
    if submit_button:
        if not password:
            st.error("Insira a senha")
        elif password != password_confirm:
            st.error("As senhas não conferem, por favor, verifique.")
        else:
            try:
                # Generate the bcrypt hash
                hashed_password = hash_password(password)
                
                st.success("Hash gerado com sucesso!")
                
                st.markdown("### Seu Hash:")
                
                text_area = st.text_area("Copie esse texto e envie para o Dhiego:", value=hashed_password, height=100, key="hash_result")
                
            except Exception as e:
                st.error(f"Erro ao gerar hash: {e}")

# Footer
st.write("---")
st.write("Nota: A senha original não pode ser recuperada a partir deste hash.")
