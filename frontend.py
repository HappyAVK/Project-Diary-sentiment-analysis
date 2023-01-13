import streamlit as st
import glob
from main import diary_compile
import plotly.express as px
path = glob.glob("diary/*.txt")

diaries, emotions = diary_compile(path)

st.subheader("Positive")
pos_range = [i['pos'] for i in emotions]
neg_range = [i['neg'] for i in emotions]
dates = [i for i in diaries]

st.title("Diary  sentiment analysis")

st.subheader("Positive Range")

pos_figure = px.line(x=dates, y=pos_range)

st.plotly_chart(pos_figure)

st.subheader("Positive Range")

neg_figure = px.line(x=dates, y=neg_range)

st.plotly_chart(neg_figure)