import streamlit as st
import pandas as pd

# Carregar dados do CSV
df = pd.read_csv("Mesas e Assentos.csv")

# Limpar e padronizar os dados
df['Assento'] = df['Assento'].astype(str).str.strip()
df['Nome'] = df['Nome'].astype(str).str.strip()
df['Mesa'] = df['Mesa'].astype(str).str.strip()

# Título do app
st.title("🔍 Consulta de Assento - Show Tingo Santi")

# Campo de input
assento = st.text_input("Digite o número do assento:")

if assento:
    assento = assento.strip()
    resultado = df[df['Assento'] == assento]

    if not resultado.empty:
        mesa = resultado.iloc[0]['Mesa']
        nome = resultado.iloc[0]['Nome']

        if nome:
            st.success(f"✅ Mesa: {mesa}\n👤 Nome: {nome}")
        else:
            st.info(f"✅ Mesa: {mesa}\n🪑 Assento disponível")
    else:
        st.error("❌ Assento não encontrado.")
        
st.image("Mapa.PNG", use_container_width=True)
