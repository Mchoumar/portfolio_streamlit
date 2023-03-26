import streamlit
import streamlit as sq
import pandas as pd

sq.set_page_config(layout="wide")
col1, col2 = sq.columns(2)
with col1:
    sq.image("images/photo.png", width=300)

with col2:
    sq.title("Mahmoud Choumar")
    content = """
    Hi, I am Mahmoud Choumar! I am a Python programmer, and a 3rd year IT
    student at International European University(IEU). I will graduate at the end
    of 2024 with a Bachelor of science in IT from IEU in Poznań, Poland with a focus
    on Python Development. I have also studied CCNA(Cisco Certified Network Associate) with CIS college,
    CS50:Introduction to Computer Science by EDX Harvard, and Python Development training program with Brainnest.
    """
    sq.info(content)

sq.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, col4 = sq.columns(2)
df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:11].iterrows():
        sq.title(row["title"])
        sq.write(row["description"])
        sq.image("images/"+row["image"])
        sq.write(f"[Source code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        sq.title(row["title"])
        sq.write(row["description"])
        sq.image("images/" + row["image"])
        sq.write(f"[Source code]({row['url']})")