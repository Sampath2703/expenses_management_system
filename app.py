from click import option
import cloudinary
import streamlit as st
from db_c import cursor_obj, conn_obj   

st.title("Expenses Tracker Management System")


cloudinary.config(
    cloud_name = st.secrets["cloud_name"],
    api_key = st.secrets["api_key"],
    api_secret = st.secrets["api_secret"]
)


