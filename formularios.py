import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ===============================
# CONFIGURAÇÕES
# ===============================

NOME_PLANILHA = "Banco de dados"
ABA_CLIENTES = "CLIENTES"
ABA_FORMULARIO = "FORMULÁRIO 1"

CAMPOS = [
    "id_usuario",
    "nome",
    "data",
    "observacao"
]

# ===============================
# CONEXÃO GOOGLE SHEETS
# ===============================

def conecta_planilha():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["google_credentials"],
        scopes=scopes
    )
    client = gspread.authorize(creds)
    return client.open(NOME_PLANILHA)

# ===============================
# UTILIDADES
# ===============================

def data_atual():
    return datetime.now().strftime("%d/%m/%Y")

def obter_cliente(planilha, usuario_logado):
    aba = planilha.worksheet(ABA_CLIENTES)
    registros = aba.get_all_records()

    usuario_logado = usuario_logado.strip().lower()

    for linha in registros:
        id_usuario = str(linha.get("id usuario", "")).strip().lower()
        if id_usuario == usuario_logado:
            return {
                "id_usuario": linha.get("id usuario", ""),
                "nome": linha.get("nome", "")
            }
    return None

def salvar_resposta(planilha, dados):
    try:
        sheet = planilha.worksheet(ABA_FORMULARIO)
    except gspread.WorksheetNotFound:
        sheet = planilha.add_worksheet(
            title=ABA_FORMULARIO,
            rows="100",
            cols=str(len(CAMPOS))
        )

    # Cria cabeçalho se não existir
    if sheet.row_values(1) == []:
        sheet.append_row(CAMPOS)

    linha = [dados.get(campo, "") for campo in CAMPOS]
    sheet.append_row(linha)

# ===============================
# FORMULÁRIO
# ===============================

def formulario_1(usuario_logado):
    st.header("Formulário 1")

    planilha = conecta_planilha()

    cliente = obter_cliente(planilha, usuario_logado)

    if not cliente:
        st.error("Cliente não encontrado na aba CLIENTES.")
        return

    st.text(f"ID do usuário: {cliente['id_usuario']}")
    st.text(f"Nome do cliente: {cliente['nome']}")

    observacao = st.text_area("Observação")

    if st.button("Enviar"):
        dados = {
            "id_usuario": cliente["id_usuario"],
            "nome": cliente["nome"],
            "data": data_atual(),
            "observacao": observacao
        }

        salvar_resposta(planilha, dados)
        st.success("Formulário enviado com sucesso!")





