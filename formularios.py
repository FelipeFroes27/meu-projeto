# formularios.py
import streamlit as st
from utils import salvar_resposta, get_data_atual

# Campos do formulário
CAMPOS = [
    "Cliente", "Data", "Raiva", "Quem", "Pressão", "Inferioridade", "Observações"
]

def formulario_principal(secret, nome_planilha):
    st.header("Formulário Psicológico")
    
    # Dados básicos
    cliente = st.session_state.get("usuario", "")
    data_atual = get_data_atual()
    
    raiva = st.radio("Sentiu raiva de alguém?", ["Não", "Sim"])
    quem = st.text_input("Quem?", "") if raiva == "Sim" else ""
    
    pressao = st.radio("Sentiu pressão?", ["Não", "Sim"])
    inferioridade = st.radio("Sentiu-se inferior?", ["Não", "Sim"])
    
    observacoes = st.text_area("Observações")
    
    if st.button("Enviar"):
        planilha = conecta_planilha(secret, nome_planilha)
        dados = {
            "Cliente": cliente,
            "Data": data_atual,
            "Raiva": raiva,
            "Quem": quem,
            "Pressão": pressao,
            "Inferioridade": inferioridade,
            "Observações": observacoes
        }
        salvar_resposta(planilha, "FORMULÁRIO 1", dados, CAMPOS)
        st.success("Resposta enviada com sucesso!")


