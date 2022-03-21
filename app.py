import streamlit as st
import pandas as pd

url="https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv"
df = pd.read_csv(url)

st.table(df.iloc[0:10])
