import streamlit as st
from utils import (
    salvar_resposta,
    atualizar_resposta,
    get_data_atual,
    conecta_planilha,
    buscar_resposta_por_id
)

CAMPOS_PADRAO = ["ID_USUARIO", "NOME", "DATA", "OBSERVAÇÃO"]

# 🔹 Busca id_usuario na aba USUARIOS
def obter_id_usuario(planilha, usuario_login):
    aba = planilha.worksheet("USUARIOS")
    registros = aba.get_all_records()

    usuario_login = str(usuario_login).strip().lower()

    for linha in registros:
        if str(linha.get("usuario", "")).strip().lower() == usuario_login:
            return linha.get("id_usuario", "")

    return ""


# 🔹 Busca nome do cliente na aba CLIENTES
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

    usuario_login = st.session_state.get("usuario", "")
    if not usuario_login:
        st.warning("Usuário não identificado.")
        return

    id_usuario = obter_id_usuario(planilha, usuario_login)
    if not id_usuario:
        st.warning("ID do usuário não encontrado.")
        return

    nome_cliente = obter_nome_cliente(planilha, id_usuario)
    if not nome_cliente:
        st.warning("Cliente não encontrado.")
        return

    # 🔎 Verifica se já existe resposta
    resposta_existente = buscar_resposta_por_id(
        planilha,
        aba_formulario,
        id_usuario
    )

    modo_edicao = resposta_existente is not None

    st.caption(f"Cliente: {nome_cliente}")
    st.caption(f"ID Usuário: {id_usuario}")

    # 🔹 Preenchimento automático se estiver em edição
    observacao = st.text_area(
        "Observação",
        value=resposta_existente.get("OBSERVAÇÃO", "") if modo_edicao else ""
    )

    botao_label = "Atualizar resposta" if modo_edicao else "Enviar resposta"

    if st.button(botao_label):
        dados = {
            "ID_USUARIO": id_usuario,
            "NOME": nome_cliente,
            "DATA": get_data_atual(),
            "OBSERVAÇÃO": observacao
        }

        if modo_edicao:
            atualizar_resposta(
                planilha,
                aba_formulario,
                id_usuario,
                dados,
                CAMPOS_PADRAO
            )
            st.success("Resposta atualizada com sucesso!")
        else:
            salvar_resposta(
                planilha,
                aba_formulario,
                dados,
                CAMPOS_PADRAO
            )
            st.success("Resposta enviada com sucesso!")


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

