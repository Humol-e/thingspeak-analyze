import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.sidebar.header('Thingspeak analytycs `v1.0`')
st.sidebar.markdown('`demo`')

img = "data:image/jpeg;base64,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"
st.sidebar.link_button("Documentación", "https://github.com/Humol-e/Graficator")

@st.cache_data
def get_data():
    r = f"https://api.thingspeak.com/channels/2338840/feeds.json?results=300000"
    response = requests.get(r)
    data = response.json()
    return pd.DataFrame(data['feeds'])

with st.sidebar:
    st.image(img)

get_data()
data = get_data()
df = pd.DataFrame(data)

st.title("Mi Streamlit")


def eliminar_filas_cero(df, field1, field2):
    return df[(df[field1].notna()) & (df[field2].notna())]

df = eliminar_filas_cero(df, "field1", "field2")
df = df.drop(df[df['field1'] == 0].index)
df = df.drop(df[df['field2'] == 0].index)
eliminar_filas_cero(df, field1 = "field1", field2 = "field2")

df["field1"] = pd.to_numeric(df["field1"], errors='coerce')
df = df[df['field1'] != 0]

df["field2"] = pd.to_numeric(df["field2"], errors='coerce')
df = df[df['field2'] != 0]

print(df.to_string())




with st.expander("Ver datos"):
    st.dataframe(df, width=1000, height=500)
juanito = st.empty()


def graficar():
    figura = go.Figure()
    figura.add_trace(go.Scatter(x=df["entry_id"], y=df["field1"], name="Field1"))
    figura.add_trace(go.Scatter(x=df["entry_id"], y=df["field2"], name="Field2"))
    figura.update_layout(title="Grafica de Field1 y Field2", xaxis_title="Entry ID", yaxis_title="Valor")
    st.plotly_chart(figura)

graficar()