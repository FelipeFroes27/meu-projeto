# ===============================
# formularios.py
# Funções de formulários e área do cliente
# ===============================

import streamlit as st
from utils import conectar_planilha, CAMPOS_F1, buscar_resposta
from datetime import datetime

# Conecta com planilhas
planilha, _, aba_formularios, aba_acessos = conectar_planilha()

# ===============================
# ÁREA DO CLIENTE
# ===============================

def tela_cliente():
    st.title("👤 Área do Cliente")
    st.write(f"Bem-vindo, **{st.session_state['usuario']}**")

    acessos = aba_acessos.get_all_records()
    formularios = aba_formularios.get_all_records()

    ids_liberados = [
        a.get("formulario_id")
        for a in acessos
        if a.get("usuario", "").strip().lower() == st.session_state["usuario"]
    ]

    liberados = [
        f for f in formularios
        if f.get("id") in ids_liberados
        and f.get("ativo", "").strip().lower() == "sim"
    ]

    st.subheader("📝 Formulários disponíveis")

    if not liberados:
        st.info("Nenhum formulário liberado para você.")
        return

    for f in liberados:
        if st.button(f.get("nome", "Formulário")):
            st.session_state["formulario_atual"] = f.get("id")
            st.session_state["pagina"] = "formulario"

# ===============================
# FORMULÁRIO 1
# ===============================

def tela_formulario_f1():
    aba = planilha.worksheet("FORMULÁRIO 1")

    st.title("📝 Avaliação Pessoal")

    usuario = st.session_state["usuario"]
    linha, dados = buscar_resposta(aba, usuario)

    respostas = {campo: "" for campo in CAMPOS_F1}
    if dados:
        respostas.update(dados)

    respostas["Cliente"] = usuario
    respostas["Data"] = datetime.now().strftime("%d/%m/%Y")

    for campo in CAMPOS_F1[2:]:
        respostas[campo] = st.text_area(campo, respostas.get(campo, ""))

    if st.button("Salvar formulário"):

        if not aba.row_values(1):
            aba.append_row(CAMPOS_F1)

        valores = [respostas[c] for c in CAMPOS_F1]

        if linha:
            aba.update(f"A{linha}:AB{linha}", [valores])
            st.success("Formulário atualizado!")
        else:
            aba.append_row(valores)
            st.success("Formulário enviado!")

        st.session_state["pagina"] = "home"
