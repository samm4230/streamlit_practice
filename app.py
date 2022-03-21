import streamlit as st
import pandas as pd

url="https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv"
df = pd.read_csv(url)

st.line_chart(df)
