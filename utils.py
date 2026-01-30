import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ===============================
# FUNÇÕES UTILITÁRIAS
# ===============================

def normaliza_texto(texto: str) -> str:
    """Remove espaços extras e coloca em minúsculas"""
    return texto.strip().lower() if texto else ""

def data_atual() -> str:
    """Retorna a data atual no formato DD/MM/AAAA"""
    return datetime.now().strftime("%d/%m/%Y")

def conecta_planilha(secret, nome_planilha):
    """Conecta na planilha do Google Sheets"""
    creds = Credentials.from_service_account_info(secret)
    client = gspread.authorize(creds)
    return client.open(nome_planilha)

def le_aba(planilha, nome_aba):
    """Lê todas as linhas da aba como lista de dicionários"""
    aba = planilha.worksheet(nome_aba)
    dados = aba.get_all_records()
    return dados

def escreve_linha(planilha, nome_aba, dados: dict, cabeçalho: list):
    """Escreve uma linha na planilha garantindo a ordem do cabeçalho"""
    aba = planilha.worksheet(nome_aba)
    # Garante que o cabeçalho exista
    if not aba.row_values(1):
        aba.insert_row(cabeçalho, 1)
    linha = [dados.get(campo, "") for campo in cabeçalho]
    aba.append_row(linha)

