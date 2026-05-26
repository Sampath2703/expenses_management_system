import mysql.connector
import streamlit as st
from fastapi import FastAPI

conn_obj = mysql.connector.connect(
    host= st.secrets["host"],
    user= st.secrets["user"],
    database = st.secrets["database"],
    password = st.secrets["password"],
    port = st.secrets["port"]
    )

cursor_obj = conn_obj.cursor()

app = FastAPI()
