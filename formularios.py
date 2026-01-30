import streamlit as st
from utils import salvar_resposta, get_data_atual, conecta_planilha

CAMPOS_PADRAO = ["ID_USUARIO", "NOME", "DATA", "OBSERVAÇÃO"]

def obter_dados_cliente(planilha, id_usuario):
    """Busca nome do cliente na aba CLIENTES usando id_usuario"""
    try:
        aba = planilha.worksheet("CLIENTES")
        registros = aba.get_all_records()

        id_usuario_norm = str(id_usuario).strip().lower()

        for linha in registros:
            if str(linha.get("id_usuario", "")).strip().lower() == id_usuario_norm:
                return linha.get("nome", "")

    except Exception as e:
        st.error(f"Erro ao buscar cliente: {e}")

    return ""


def formulario_generico(secret, nome_planilha, aba_formulario, titulo):
    st.subheader(titulo)

    planilha = conecta_planilha(secret, nome_planilha)

    # 🔹 id_usuario vem da aba USUARIOS (login)
    id_usuario = st.session_state.get("usuario", "")

    if not id_usuario:
        st.warning("Usuário não identificado.")
        return

    # 🔹 busca nome na aba CLIENTES usando id_usuario
    nome_cliente = obter_dados_cliente(planilha, id_usuario)

    if not nome_cliente:
        st.warning("Não foi possível localizar o cliente na aba CLIENTES.")
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




