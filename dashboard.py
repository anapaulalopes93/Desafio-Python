import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")
st.sidebar.header("Vendas de carros")
st.sidebar.text("Ana Paula Lopes Cruz - PDITA 174")

df = pd.read_csv("cars.csv")

# st.write(df) Exibir o DataFrame

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.month) + "/" + str(x.year))
meses = st.sidebar.selectbox("Selecione o mês:", df["Month"].unique())

df_filtered = df[df["Month"] == meses]
# st.write(df_filtered) Exibir o DataFrame filtrado

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_mes = px.bar(df_filtered, x = "Date", y = "Price ($)", color = "Company", title = "Faturamento por mês")
col1.plotly_chart(fig_mes, use_container_widht = True)

fig_tipo = px.bar(df_filtered, x = "Date", y = "Model", color = "Company", title = "Vendas por tipo de carro")
col2.plotly_chart(fig_tipo, use_container_width = True)

revenda = df_filtered.groupby("Dealer_Name")[["Price ($)"]].sum().reset_index()
fig_revenda = px.bar(revenda, x = "Price ($)", y = "Dealer_Name", title = "Total por revendedor")
col3.plotly_chart(fig_revenda, use_container_width = True)

regiao_revenda = df_filtered.groupby("Dealer_Region")[["Price ($)"]].sum().reset_index()
fig_regiao = px.bar(df_filtered, x = "Dealer_Region", y = "Price ($)", title = "Faturamento por região do revendedor")
col4.plotly_chart(fig_regiao, use_container_width = True)

cor = df_filtered.groupby("Month")[["Color"]].sum().reset_index()
fig_cor = px.bar(df_filtered, x = "Month", y = "Color", title = "Vendas por cor")
col5.plotly_chart(fig_cor, use_container_width = True)
