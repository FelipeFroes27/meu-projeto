import streamlit as st
from utils import salvar_resposta, get_data_atual, conecta_planilha

# Campos padrão para todos os formulários
CAMPOS_PADRAO = ["ID", "Nome", "Data", "Observação"]

# Formulário 1
def formulario_1(secret, nome_planilha):
    st.subheader("Formulário 1")
    cliente_id = st.session_state.get("usuario", "")
    nome_cliente = st.text_input("Nome do cliente", value=cliente_id)
    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button("Enviar Formulário 1"):
        planilha = conecta_planilha(secret, nome_planilha)
        dados = {
            "ID": cliente_id,
            "Nome": nome_cliente,
            "Data": data_atual,
            "Observação": observacao
        }
        salvar_resposta(planilha, "FORMULÁRIO 1", dados, CAMPOS_PADRAO)
        st.success("Formulário 1 enviado com sucesso!")

# Formulário 2
def formulario_2(secret, nome_planilha):
    st.subheader("Formulário 2")
    cliente_id = st.session_state.get("usuario", "")
    nome_cliente = st.text_input("Nome do cliente", value=cliente_id)
    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button("Enviar Formulário 2"):
        planilha = conecta_planilha(secret, nome_planilha)
        dados = {
            "ID": cliente_id,
            "Nome": nome_cliente,
            "Data": data_atual,
            "Observação": observacao
        }
        salvar_resposta(planilha, "FORMULÁRIO 2", dados, CAMPOS_PADRAO)
        st.success("Formulário 2 enviado com sucesso!")

# Formulário 3
def formulario_3(secret, nome_planilha):
    st.subheader("Formulário 3")
    cliente_id = st.session_state.get("usuario", "")
    nome_cliente = st.text_input("Nome do cliente", value=cliente_id)
    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button("Enviar Formulário 3"):
        planilha = conecta_planilha(secret, nome_planilha)
        dados = {
            "ID": cliente_id,
            "Nome": nome_cliente,
            "Data": data_atual,
            "Observação": observacao
        }
        salvar_resposta(planilha, "FORMULÁRIO 3", dados, CAMPOS_PADRAO)
        st.success("Formulário 3 enviado com sucesso!")

# Dicionário de formulários para o app.py
FORMULARIOS = {
    "Formulário 1": formulario_1,
    "Formulário 2": formulario_2,
    "Formulário 3": formulario_3
}

