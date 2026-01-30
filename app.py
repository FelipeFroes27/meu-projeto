import streamlit as st
from login import login, logout
from formularios import formulario_psicologico
from utils import conecta_planilha

# ===============================
# CONFIGURAÇÕES GERAIS
# ===============================
st.set_page_config(page_title="Sistema de Consultoria", layout="wide")

# ===============================
# CREDENCIAIS E PLANILHA
# ===============================
# Substitua pelo seu st.secrets ou dicionário de credenciais
GOOGLE_SECRET = st.secrets["google_credentials"]
NOME_PLANILHA = "Banco de dados"

# ===============================
# NAVEGAÇÃO
# ===============================

login(GOOGLE_SECRET, NOME_PLANILHA)

if st.session_state.get("logado"):
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Escolha a tela:", ["Formulário", "Logout"])

    if opcao == "Formulário":
        formulario_psicologico(GOOGLE_SECRET, NOME_PLANILHA)
    elif opcao == "Logout":
        logout()




