import streamlit as st
from io import StringIO

with st.sidebar:
    temperature = st.text_input("Temperature", placeholder="0.7")
    max_tokens = st.text_input("Max tokens", placeholder="250")
    "[Temperature: creativity of LLM](https://baidu.com)"
    "[Max tokens: 用于控制生成文本的最大长度](https://baidu.com)"

st.title("📝 File Q&A with Anthropic")
uploaded_file = st.file_uploader("Upload a File")
question = st.text_input(
    "Ask something about the file",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write("### Answer")
    st.write(string_data)
