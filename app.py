import streamlit as st
import pandas as pd

st.title('My first app!')

st.write('Hello world! :smile:')

slide = st.slider('Pick a number!', 1, 15)
slide

button = st.button('Press here for cold')
if button:
    st.snow()

button2 = st.button('Press here for helium')
if button2:
    st.balloons()

cities = ['Manchester', 'Tokyo', 'Berlin', 'Brasilia', 'Ottawa', 'Wellington', 'Nairobi']
st.selectbox('Choose a city', cities)

check = st.checkbox('Tick')
# if check:
