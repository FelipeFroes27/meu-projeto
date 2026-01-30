# utils.py
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

def conecta_planilha(secret, nome_planilha):
    """Conecta ao Google Sheets usando o secret e retorna o objeto da planilha."""
    scopes = ["https://www.googleapis.com/auth/spreadsheets",
              "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(secret, scopes=scopes)
    client = gspread.authorize(creds)
    return client.open(nome_planilha)

def salvar_resposta(planilha, aba_nome, dados, campos):
    """Salva os dados em uma aba da planilha, criando cabeçalho se necessário."""
    try:
        sheet = planilha.worksheet(aba_nome)
    except gspread.WorksheetNotFound:
        sheet = planilha.add_worksheet(title=aba_nome, rows="100", cols=str(len(campos)))
    
    # Cria cabeçalho se vazio
    if sheet.row_values(1) == []:
        sheet.append_row(campos)
    
    # Adiciona os dados na próxima linha
    linha = [dados.get(campo, "") for campo in campos]
    sheet.append_row(linha)

def get_data_atual():
    """Retorna a data atual no formato DD/MM/AAAA."""
    return datetime.now().strftime("%d/%m/%Y")

def normalize_text(texto):
    """Normaliza texto para string minúscula sem espaços, tratando None."""
    if texto is None:
        return ""
    return str(texto).strip().lower()


