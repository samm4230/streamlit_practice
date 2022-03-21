pip install matplotlib

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url="https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv"
df = pd.read_csv(url)

plot = sns.pairplot(df)
st.pyplot(plot)
