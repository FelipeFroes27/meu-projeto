# formularios.py
import streamlit as st
from utils import salvar_resposta, get_data_atual, conecta_planilha

# Campos do formulário 1
CAMPOS_FORM1 = [
    "Cliente", "Data", "Raiva", "Quem", "Pressão", "Inferioridade", "Observações"
]

def formulario_principal(secret, nome_planilha):
    st.header("Formulário Psicológico")
    
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
        salvar_resposta(planilha, "FORMULÁRIO 1", dados, CAMPOS_FORM1)
        st.success("Resposta enviada com sucesso!")

# Aqui você pode adicionar mais formulários, por exemplo:
def formulario_secundario(secret, nome_planilha):
    st.header("Formulário Secundário")
    
    cliente = st.session_state.get("usuario", "")
    data_atual = get_data_atual()
    
    resposta = st.text_input("Digite algo para o formulário secundário:")
    
    if st.button("Enviar"):
        planilha = conecta_planilha(secret, nome_planilha)
        dados = {
            "Cliente": cliente,
            "Data": data_atual,
            "Resposta": resposta
        }
        salvar_resposta(planilha, "FORMULÁRIO 2", dados, ["Cliente", "Data", "Resposta"])
        st.success("Resposta enviada com sucesso!")

# Dicionário de formulários
FORMULARIOS = {
    "Formulário Psicológico": formulario_principal,
    "Formulário Secundário": formulario_secundario
}


