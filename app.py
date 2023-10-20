import pandas as pd
import streamlit as st
df = pd.read_csv("data.csv")
st.dataframe(data=df)
df[["Equity"]].hist()