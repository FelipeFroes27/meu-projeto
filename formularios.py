import streamlit as st
from utils import salvar_resposta, get_data_atual, conecta_planilha

CAMPOS_PADRAO = ["ID_USUARIO", "NOME", "DATA", "OBSERVAÇÃO"]

# 🔹 1. Busca id_usuario na aba USUARIOS usando o login
def obter_id_usuario(planilha, usuario_login):
    aba = planilha.worksheet("USUARIOS")
    registros = aba.get_all_records()

    usuario_login = str(usuario_login).strip().lower()

    for linha in registros:
        if str(linha.get("usuario", "")).strip().lower() == usuario_login:
            return linha.get("id_usuario", "")

    return ""


# 🔹 2. Busca nome do cliente na aba CLIENTES usando id_usuario
def obter_nome_cliente(planilha, id_usuario):
    aba = planilha.worksheet("CLIENTES")
    registros = aba.get_all_records()

    id_usuario = str(id_usuario).strip().lower()

    for linha in registros:
        if str(linha.get("id_usuario", "")).strip().lower() == id_usuario:
            return linha.get("nome", "")

    return ""


def formulario_generico(secret, nome_planilha, aba_formulario, titulo):
    st.subheader(titulo)

    planilha = conecta_planilha(secret, nome_planilha)

    # login (USUARIOS.usuario)
    usuario_login = st.session_state.get("usuario", "")

    if not usuario_login:
        st.warning("Usuário não identificado.")
        return

    # 🔗 etapa 1
    id_usuario = obter_id_usuario(planilha, usuario_login)

    if not id_usuario:
        st.warning("ID do usuário não encontrado na aba USUARIOS.")
        return

    # 🔗 etapa 2
    nome_cliente = obter_nome_cliente(planilha, id_usuario)

    if not nome_cliente:
        st.warning("Cliente não encontrado na aba CLIENTES.")
        return

    st.text(f"ID do usuário: {id_usuario}")
    st.text(f"Nome do cliente: {nome_cliente}")

    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button(f"Enviar {titulo}"):
        dados = {
            "ID_USUARIO": id_usuario,
            "NOME": nome_cliente,
            "DATA": data_atual,
            "OBSERVAÇÃO": observacao
        }

        salvar_resposta(planilha, aba_formulario, dados, CAMPOS_PADRAO)
        st.success(f"{titulo} enviado com sucesso!")


def formulario_1(secret, nome_planilha):
    formulario_generico(secret, nome_planilha, "FORMULÁRIO 1", "Formulário 1")


def formulario_2(secret, nome_planilha):
    formulario_generico(secret, nome_planilha, "FORMULÁRIO 2", "Formulário 2")


def formulario_3(secret, nome_planilha):
    formulario_generico(secret, nome_planilha, "FORMULÁRIO 3", "Formulário 3")


FORMULARIOS = {
    "Formulário 1": formulario_1,
    "Formulário 2": formulario_2,
    "Formulário 3": formulario_3
}



