# app.py
import streamlit as st
from login import login
from formularios import formulario_principal
from utils import conecta_planilha

# Configuração de secrets e planilha
GOOGLE_SECRET = st.secrets["google_credentials"]
NOME_PLANILHA = "Banco de dados"

# Inicializa sessão
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None
    st.session_state["tipo"] = None

# Tela de login
if st.session_state["usuario"] is None:
    login(GOOGLE_SECRET, NOME_PLANILHA)
else:
    # Tela principal após login
    st.sidebar.write(f"Usuário: {st.session_state['usuario']}")
    st.sidebar.write(f"Tipo: {st.session_state['tipo']}")
    
    formulario_principal(GOOGLE_SECRET, NOME_PLANILHA)


