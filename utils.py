# ===============================
# utils.py
# Funções auxiliares e configuração geral
# ===============================

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import streamlit as st

# ===============================
# CONFIGURAÇÕES GERAIS
# ===============================

PLANILHA_NOME = "Banco de dados"

CAMPOS_F1 = [
    "Cliente", "Data",
    "O que você pensa a seu respeito?",
    "Como foi o seu primeiro relacionamento amoroso?",
    "Qual papel você exerce na vida hoje?",
    "Vítima ou Responsável?",
    "Qual o ganho secundário?",
    "Em quais situações você desempenha o papel de vítima?",
    "Em quais situações você desempenha o papel de responsável?",
    "Se considera vitoriosa(o) ou derrotada(o)?",
    "Perfil nos relacionamentos",
    "Quem é o culpado pelos seus problemas?",
    "Sente raiva ou rancor de alguém?",
    "Raiva direcionada a quem?",
    "Sente-se pressionada(o)?",
    "De que maneira se sente pressionada(o)?",
    "Você se acha uma pessoa controladora?",
    "Sente-se inferior aos outros?",
    "Por que se sente inferior?",
    "Raiva", "Medo", "Culpa", "Tristeza",
    "Ansiedade", "Ciúme", "Frustração",
    "Solidão", "Cansaço"
]

# ===============================
# CONEXÃO COM GOOGLE SHEETS
# ===============================

def conectar_planilha():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["google_credentials"],
        scopes=scope
    )

    client = gspread.authorize(creds)
    planilha = client.open(PLANILHA_NOME)

    aba_usuarios = planilha.worksheet("USUARIOS")
    aba_formularios = planilha.worksheet("FORMULÁRIOS")
    aba_acessos = planilha.worksheet("ACESSOS")

    return planilha, aba_usuarios, aba_formularios, aba_acessos

# ===============================
# FUNÇÃO AUXILIAR
# ===============================

def buscar_resposta(aba, usuario):
    registros = aba.get_all_records()
    for i, linha in enumerate(registros, start=2):
        if linha.get("Cliente", "").strip().lower() == usuario:
            return i, linha
    return None, None
