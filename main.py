import streamlit as st
import numpy as np
import pandas as pd
import csv

st.title("Pokeman Data Visualization Tool")
st.divider()

st.subheader("Pokeman Name")

#load data
@st.cache_data
def load_data():
    data = pd.read_csv('pokemon.csv')
    return data

data = load_data()

#create a dataframe with the pokemon data
df = pd.DataFrame(data)

#create a datafram with pokemon data
st.dataframe(df)