# login.py
import streamlit as st
from utils import conecta_planilha, normalize_text

def autenticar_usuario(secret, nome_planilha, usuario_input, senha_input):
    planilha = conecta_planilha(secret, nome_planilha)
    aba = planilha.worksheet("usuarios")
    dados = aba.get_all_records()
    
    usuario_input_norm = normalize_text(usuario_input)
    senha_input_norm = normalize_text(senha_input)
    
    for linha in dados:
        if normalize_text(linha.get("usuario", "")) == usuario_input_norm and \
           normalize_text(linha.get("senha", "")) == senha_input_norm:
            return {"usuario": usuario_input_norm, "tipo": linha.get("tipo", "cliente")}
    return None

def login(secret, nome_planilha):
    st.title("Login")
    usuario_input = st.text_input("Usuário")
    senha_input = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        usuario = autenticar_usuario(secret, nome_planilha, usuario_input, senha_input)
        if usuario:
            st.session_state["usuario"] = usuario["usuario"]
            st.session_state["tipo"] = usuario["tipo"]
            st.success(f"Bem-vindo, {usuario['usuario']}!")
        else:
            st.error("Usuário ou senha incorretos")


