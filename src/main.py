import streamlit as st
import pandas as pd
import plotly.express as px
import clickhouse_connect
from pathlib import Path

# ========================
# Configuração ClickHouse
# ========================

client = clickhouse_connect.get_client(
    host='localhost', port=8123, username='default', password=''
)

# Criar database e tabela se não existirem
client.command("CREATE DATABASE IF NOT EXISTS portfoliodb")
client.command("""
CREATE TABLE IF NOT EXISTS portfoliodb.temperature (
    device_id String,
    temperature Float32,
    timestamp DateTime
) ENGINE = MergeTree()
ORDER BY (device_id, timestamp)
""")

# ========================
# Inserção de dados CSV
# ========================

def load_csv_data(file_path='data/temperature.csv'):
    # Lê o arquivo CSV usando pandas
    data = pd.read_csv(file_path)
    return data


# ========================
# Função de consulta
# ========================

def load_data(query):
    return client.query_df(query)


# ========================
# Dashboard Streamlit
# ========================

st.title("📊 Dashboard IoT com ClickHouse")

# Gráfico 1: Média de Temperatura por Dispositivo
st.header("📊 Média de Temperatura por Dispositivo")
df_avg = load_data("""
    SELECT device_id, AVG(temperature) AS temperatura_media 
    FROM portfoliodb.temperature 
    GROUP BY device_id
""")
fig1 = px.bar(
    df_avg,
    x="device_id",
    y="temperatura_media",
    labels={"device_id": "Dispositivo", "temperatura_media": "Temperatura Média (°C)"},
    title="Temperatura Média por Dispositivo"
)
st.plotly_chart(fig1)

# Gráfico 2: Leituras por Hora
st.header("⏰ Leituras Registradas por Hora")
df_hora = load_data("""
    SELECT toHour(timestamp) AS hora, COUNT() AS quantidade 
    FROM portfoliodb.temperature 
    GROUP BY hora 
    ORDER BY hora
""")
fig2 = px.line(
    df_hora,
    x="hora",
    y="quantidade",
    labels={"hora": "Hora do Dia", "quantidade": "Número de Leituras"},
    title="Quantidade de Leituras por Hora"
)
st.plotly_chart(fig2)

# Gráfico 3: Variação de Temperatura por Hora (em um único dia)
st.header("🌡️ Variação de Temperatura Máxima e Mínima por Hora")

df_temp = load_data("""
    SELECT 
        toStartOfHour(timestamp) AS hora,
        max(temperature) AS temperatura_maxima,
        min(temperature) AS temperatura_minima
    FROM portfoliodb.temperature
    GROUP BY hora
    ORDER BY hora
""")

# Converte hora para datetime
df_temp["hora"] = pd.to_datetime(df_temp["hora"])


df_temp = df_temp.rename(columns={
    "hora": "Hora",
    "temperatura_maxima": "Temperatura Máxima (°C)",
    "temperatura_minima": "Temperatura Mínima (°C)"
})

# Formato longo para plotagem
df_melted = df_temp.melt(
    id_vars="Hora",
    value_vars=["Temperatura Máxima (°C)", "Temperatura Mínima (°C)"],
    var_name="Tipo de Temperatura",
    value_name="Temperatura (°C)"
)

# Gráfico
fig3 = px.line(
    df_melted,
    x="Hora",
    y="Temperatura (°C)",
    color="Tipo de Temperatura",
    markers=True,  # adiciona pontos nas linhas do gráfico
    title="🌡️ Temperatura Máxima e Mínima por Hora"
)

st.plotly_chart(fig3)


