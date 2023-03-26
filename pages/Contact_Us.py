import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")


st.header("Contact Me")
with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    user_message = f"""From: New message from {user_email}\n
    To: To Mahmoud Choumar<mahmoudchoumar@ieu.edu.ua>\n
    Subject: {user_email}\n
    
    {raw_message}
    """
    button = st.form_submit_button("submit")
    if button:
        send_email(user_message)
        st.success("Your message was sent successfully!", icon="✅")


