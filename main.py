import streamlit as sq
sq.set_page_config(layout="wide")
col1, col2 = sq.columns(2)
with col1:
    sq.image("images/photo.png", width=300)

with col2:
    sq.title("Mahmoud Choumar")
    content = """<h4>Hi, I would like to introduce myself</h4>"""
    sq.write(content, unsafe_allow_html=True)

sq.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")
