import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

def conecta_planilha(secret, nome_planilha):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(secret, scopes=scopes)
    client = gspread.authorize(creds)
    return client.open(nome_planilha)


def salvar_resposta(planilha, aba_nome, dados, campos):
    try:
        sheet = planilha.worksheet(aba_nome)
    except gspread.WorksheetNotFound:
        sheet = planilha.add_worksheet(
            title=aba_nome,
            rows="100",
            cols=str(len(campos))
        )

    if sheet.row_values(1) == []:
        sheet.append_row(campos)

    linha = [dados.get(campo, "") for campo in campos]
    sheet.append_row(linha)


def buscar_resposta_por_id(planilha, aba_nome, id_usuario):
    try:
        sheet = planilha.worksheet(aba_nome)
    except gspread.WorksheetNotFound:
        return None

    registros = sheet.get_all_records()

    for idx, linha in enumerate(registros, start=2):
        if str(linha.get("ID_USUARIO", "")).strip() == str(id_usuario).strip():
            linha["_row"] = idx  # guarda número da linha
            return linha

    return None


def atualizar_resposta(planilha, aba_nome, id_usuario, dados, campos):
    resposta = buscar_resposta_por_id(planilha, aba_nome, id_usuario)
    if not resposta:
        return False

    sheet = planilha.worksheet(aba_nome)
    row_number = resposta["_row"]

    valores = [dados.get(campo, "") for campo in campos]

    sheet.update(
        f"A{row_number}:{chr(64 + len(campos))}{row_number}",
        [valores]
    )
    return True


def get_data_atual():
    return datetime.now().strftime("%d/%m/%Y")


def normalize_text(texto):
    if texto is None:
        return ""
    return str(texto).strip().lower()


