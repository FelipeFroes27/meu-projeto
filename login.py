# ===============================
# login.py
# Tela de login
# ===============================

import streamlit as st
from utils import conectar_planilha

# Conecta com planilhas
_, aba_usuarios, _, _ = conectar_planilha()

def tela_login():
    st.title("🔐 Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        for u in aba_usuarios.get_all_records():
            if (
                usuario.strip().lower() == str(u.get("usuario", "")).strip().lower()
                and senha.strip() == str(u.get("senha", "")).strip()
            ):
                st.session_state.update({
                    "logado": True,
                    "usuario": usuario.strip().lower(),
                    "tipo": str(u.get("tipo", "")).strip().lower(),
                    "pagina": "home"
                })
                return

        st.error("Usuário ou senha inválidos")
