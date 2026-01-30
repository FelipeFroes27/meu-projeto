# app.py
import streamlit as st
from login import login
from formularios import formulario_principal, FORMULARIOS
from utils import conecta_planilha

# Configuração de secrets e planilha
GOOGLE_SECRET = st.secrets["google_credentials"]
NOME_PLANILHA = "Banco de dados"

# Inicializa sessão
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None
    st.session_state["tipo"] = None
    st.session_state["formulario_selecionado"] = None

# Tela de login
if st.session_state["usuario"] is None:
    login(GOOGLE_SECRET, NOME_PLANILHA)
else:
    # Sidebar com info do usuário
    st.sidebar.write(f"Usuário: {st.session_state['usuario']}")
    st.sidebar.write(f"Tipo: {st.session_state['tipo']}")

    # Abas principais
    aba = st.radio("Navegação", ["Formulários/Testes"])

    if aba == "Formulários/Testes":
        st.header("Escolha um formulário para preencher:")

        # Botões para cada formulário
        for nome_formulario, func_formulario in FORMULARIOS.items():
            if st.button(nome_formulario):
                st.session_state["formulario_selecionado"] = nome_formulario

        # Se algum formulário foi selecionado, chama a função correspondente
        if st.session_state["formulario_selecionado"]:
            func = FORMULARIOS[st.session_state["formulario_selecionado"]]
            func(GOOGLE_SECRET, NOME_PLANILHA)
