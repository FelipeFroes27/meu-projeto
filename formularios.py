import streamlit as st
from utils import salvar_resposta, get_data_atual, conecta_planilha

CAMPOS_PADRAO = ["ID", "Nome", "Data", "Observação"]

def obter_id_nome(planilha, usuario):
    """Busca o ID e nome do cliente na aba CLIENTES pelo login."""
    aba = planilha.worksheet("CLIENTES")
    registros = aba.get_all_records()
    for linha in registros:
        if str(linha.get("usuario", "")).strip().lower() == usuario.lower():
            return linha.get("id", ""), linha.get("nome", "")
    return "", ""  # caso não encontre

# Formulário 1
def formulario_1(secret, nome_planilha):
    st.subheader("Formulário 1")
    planilha = conecta_planilha(secret, nome_planilha)
    usuario_logado = st.session_state.get("usuario", "")

    cliente_id, nome_cliente = obter_id_nome(planilha, usuario_logado)
    st.text(f"ID do cliente: {cliente_id}")
    st.text(f"Nome do cliente: {nome_cliente}")

    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button("Enviar Formulário 1"):
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
    planilha = conecta_planilha(secret, nome_planilha)
    usuario_logado = st.session_state.get("usuario", "")

    cliente_id, nome_cliente = obter_id_nome(planilha, usuario_logado)
    st.text(f"ID do cliente: {cliente_id}")
    st.text(f"Nome do cliente: {nome_cliente}")

    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button("Enviar Formulário 2"):
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
    planilha = conecta_planilha(secret, nome_planilha)
    usuario_logado = st.session_state.get("usuario", "")

    cliente_id, nome_cliente = obter_id_nome(planilha, usuario_logado)
    st.text(f"ID do cliente: {cliente_id}")
    st.text(f"Nome do cliente: {nome_cliente}")

    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button("Enviar Formulário 3"):
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



