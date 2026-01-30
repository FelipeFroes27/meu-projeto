# ===============================
# app.py
# Ponto de entrada do app
# ===============================

import streamlit as st
from login import tela_login
from formularios import tela_cliente, tela_formulario_f1

# ===============================
# NAVEGAÇÃO
# ===============================

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "login"

if not st.session_state["logado"]:
    tela_login()
else:
    if st.session_state["tipo"] == "cliente":
        if st.session_state["pagina"] == "home":
            tela_cliente()
        elif st.session_state["pagina"] == "formulario":
            if st.session_state.get("formulario_atual") == "F1":
                tela_formulario_f1()


