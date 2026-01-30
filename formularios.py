import streamlit as st
from utils import data_atual, conecta_planilha, escreve_linha

# ===============================
# FUNÇÕES DE FORMULÁRIOS
# ===============================

CAMPOS = [
    "Cliente", "Data", "Raiva", "Quem", "Pressão", "QuemPressao",
    "Inferioridade", "DetalhesInferioridade", "Outros"
]

def formulario_psicologico(secret, nome_planilha):
    """
    Exibe o formulário psicológico dinâmico e salva no Google Sheets
    """
    st.header("Formulário Psicológico")
    cliente = st.session_state.usuario.get("usuario")
    data = data_atual()

    # Campos principais
    raiva = st.radio("Sente raiva de alguém?", ["Não", "Sim"])
    quem = st.text_input("Quem?", key="raiva_quem") if raiva == "Sim" else ""

    pressao = st.radio("Sente pressão de alguém?", ["Não", "Sim"])
    quem_pressao = st.text_input("Quem?", key="pressao_quem") if pressao == "Sim" else ""

    inferioridade = st.radio("Sente inferioridade em alguma situação?", ["Não", "Sim"])
    detalhes_inferioridade = st.text_area("Detalhes", key="inferioridade_detalhes") if inferioridade == "Sim" else ""

    outros = st.text_area("Outros comentários")

    if st.button("Enviar"):
        planilha = conecta_planilha(secret, nome_planilha)
        dados = {
            "Cliente": cliente,
            "Data": data,
            "Raiva": raiva,
            "Quem": quem,
            "Pressão": pressao,
            "QuemPressao": quem_pressao,
            "Inferioridade": inferioridade,
            "DetalhesInferioridade": detalhes_inferioridade,
            "Outros": outros
        }
        escreve_linha(planilha, "FORMULÁRIO 1", dados, CAMPOS)
        st.success("Formulário enviado com sucesso!")
        # Limpa campos após envio
        for key in ["raiva_quem", "pressao_quem", "inferioridade_detalhes"]:
            if key in st.session_state:
                st.session_state[key] = ""

