import streamlit as st
from utils import salvar_resposta, get_data_atual, conecta_planilha

CAMPOS_PADRAO = ["ID", "Nome", "Data", "Observação"]

def obter_id_nome(planilha, usuario_logado):
    """Busca o ID e nome do cliente na aba CLIENTES pelo login."""
    try:
        aba = planilha.worksheet("CLIENTES")
        registros = aba.get_all_records()
        for linha in registros:
            # Normaliza para evitar problemas com maiúsculas/minúsculas
            if str(linha.get("id_usuario", "")).strip().lower() == usuario_logado.strip().lower():
                return linha.get("id_cliente", ""), linha.get("nome", "")
    except Exception as e:
        st.error(f"Erro ao buscar ID/Nome: {e}")
    return "", ""  # caso não encontre

# Formulário genérico para reutilização
def formulario_generico(secret, nome_planilha, aba_formulario, titulo):
    st.subheader(titulo)
    planilha = conecta_planilha(secret, nome_planilha)
    usuario_logado = st.session_state.get("usuario", "")

    cliente_id, nome_cliente = obter_id_nome(planilha, usuario_logado)

    if not cliente_id or not nome_cliente:
        st.warning("Não foi possível identificar o ID ou Nome do cliente. Verifique a aba CLIENTES.")
        return

    st.text(f"ID do cliente: {cliente_id}")
    st.text(f"Nome do cliente: {nome_cliente}")

    data_atual = get_data_atual()
    observacao = st.text_area("Observação")

    if st.button(f"Enviar {titulo}"):
        dados = {
            "ID": cliente_id,
            "Nome": nome_cliente,
            "Data": data_atual,
            "Observação": observacao
        }
        salvar_resposta(planilha, aba_formulario, dados, CAMPOS_PADRAO)
        st.success(f"{titulo} enviado com sucesso!")

# Três formulários padrão
def formulario_1(secret, nome_planilha):
    formulario_generico(secret, nome_planilha, "FORMULÁRIO 1", "Formulário 1")

def formulario_2(secret, nome_planilha):
    formulario_generico(secret, nome_planilha, "FORMULÁRIO 2", "Formulário 2")

def formulario_3(secret, nome_planilha):
    formulario_generico(secret, nome_planilha, "FORMULÁRIO 3", "Formulário 3")

# Dicionário de formulários para o app.py
FORMULARIOS = {
    "Formulário 1": formulario_1,
    "Formulário 2": formulario_2,
    "Formulário 3": formulario_3
}




