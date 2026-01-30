import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

secret = st.secrets["google_credentials"]

scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(secret, scopes=scopes)
client = gspread.authorize(creds)

planilha = client.open("NOME_PLANILHA")  # coloque exatamente o nome da planilha
print(planilha.sheet1.get_all_records())
