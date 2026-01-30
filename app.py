# app.py
import streamlit as st
from login import login
from formularios import FORMULARIOS
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
    st.sidebar.markdown("---")

    # Sidebar com "abas" de formulários
    st.sidebar.write("### Formulários/Testes")
    for nome_formulario, func_formulario in FORMULARIOS.items():
        if st.sidebar.button(nome_formulario):
            st.session_state["formulario_selecionado"] = nome_formulario

    # Nova aba Visualizar Respostas apenas para usuários master
    if st.session_state["tipo"] == "master":
        if st.sidebar.button("Visualizar Respostas"):
            st.session_state["formulario_selecionado"] = "Visualizar Respostas"

    # Corpo da página: exibe formulário selecionado ou aba de visualização
    if st.session_state["formulario_selecionado"]:
        if st.session_state["formulario_selecionado"] == "Visualizar Respostas":
            st.header("Visualizar Respostas")
            st.write("Aqui serão exibidas todas as respostas (em breve).")
        else:
            st.header(st.session_state["formulario_selecionado"])
            func = FORMULARIOS[st.session_state["formulario_selecionado"]]
            func(GOOGLE_SECRET, NOME_PLANILHA)
    else:
        st.write("Selecione um formulário na aba à esquerda para começar.")
