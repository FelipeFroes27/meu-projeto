import streamlit as st
from utils import normaliza_texto, conecta_planilha, le_aba

# ===============================
# FUNÇÕES DE LOGIN
# ===============================

def autenticar_usuario(secret, nome_planilha, usuario_input, senha_input):
    """
    Verifica login do usuário na aba 'USUARIOS' do Google Sheets
    Retorna dicionário do usuário se válido, senão None
    """
    planilha = conecta_planilha(secret, nome_planilha)
    usuarios = le_aba(planilha, "USUARIOS")
    usuario_input_norm = normaliza_texto(usuario_input)
    senha_input_norm = normaliza_texto(senha_input)

    for u in usuarios:
        if normaliza_texto(u.get("usuario")) == usuario_input_norm and \
           normaliza_texto(u.get("senha")) == senha_input_norm:
            return u  # Retorna o dicionário do usuário
    return None

def login(secret, nome_planilha):
    """
    Tela de login do Streamlit
    """
    if "logado" not in st.session_state:
        st.session_state.logado = False
        st.session_state.usuario = None

    if not st.session_state.logado:
        st.title("Login")
        usuario_input = st.text_input("Usuário")
        senha_input = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            usuario = autenticar_usuario(secret, nome_planilha, usuario_input, senha_input)
            if usuario:
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.experimental_rerun()
            else:
                st.error("Usuário ou senha incorretos")

def logout():
    """Faz logout do usuário"""
    if st.session_state.get("logado"):
        st.session_state.logado = False
        st.session_state.usuario = None
        st.experimental_rerun()

