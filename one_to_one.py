import streamlit as st
from datetime import datetime

st.set_page_config(page_title="One-to-One Chat App", page_icon="💬")

st.markdown("""
<style>
.main{background:#f0f2f6}
.header{background:#25D366;color:white;padding:15px;border-radius:10px;
font-size:28px;text-align:center;font-weight:bold}
.john{background:#DCF8C6;padding:10px;border-radius:15px;margin:5px;text-align:right}
.alice{background:white;padding:10px;border-radius:15px;margin:5px;text-align:left}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="header"> One-to-One Chat App</div>',
            unsafe_allow_html=True)
if "messages" not in st.session_state:
    st.session_state.messages = []
user = st.selectbox("Select User",["John","Alice"])
message = st.chat_input("Type Your Message.....")
if message:
    st.session_state.messages.append(
        (user,message,datetime.now().strftime("%H:%M"))
    )
for user,message,time in st.session_state.messages:
    css="john" if "John" in user else "alice"
    st.markdown(
        f'<div class="{css}"></b><br>{message}</br>'
        f'<small>{time}</small></div>',
        unsafe_allow_html=True
    )
if st.button("Clear Chat"):
    st.session_state.messages=[]
    st.rerun()