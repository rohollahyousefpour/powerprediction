import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

title = '<p style="font-family:B Titr; color:Red; font-size: 40px; text-align: center; direction: RT">' \
                 'سیستم پیش بینی بار</p>'
st.markdown(title, unsafe_allow_html=True)

original_title = '<p style="font-family:B Nazanin; color:Blue; font-size: 30px; text-align: center; direction: RT">' \
                 'شرکت دانش بنیان هوشیار فراپویشگران داده</p>'

st.markdown(original_title, unsafe_allow_html=True)

descriptions = '<p style="font-family:B Nazanin; font-size: 25px; text-align: justify; direction: RTL">' \
    'این سیستم براساس روش‌های یادگیری عمیق آموزش طراحی و آموزش داده شد. پیش بینی ۴۸ ساعت آینده را براساس'\
               ' اطلاعات ۷ روز گذشته انجام می دهد. '\
               'لازم است برای پیش اطلاعات هواشناسی شامل دما و رطوبت نسبی ۴۸ ساعت آینده و وضعیت تعطیلات پیش رو وارد سیستم گردد.'
st.markdown(descriptions, unsafe_allow_html=True)

st.sidebar.title('Visualization Selector')
st.sidebar.markdown('Select the Charts/Plots accordingly:')

st.sidebar.title('Visualization Selector2')
st.sidebar.markdown('Select the Charts/Plots accordingly:')

@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()