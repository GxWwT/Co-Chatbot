import requests
import streamlit as st


# url = 'http://127.0.0.1:8718/app.conversation/run'

with st.sidebar:
    temperature = st.text_input("Temperature", placeholder="0.7")
    max_tokens = st.text_input("Max tokens", placeholder="250")
    "[Temperature: creativity of LLM](https://baidu.com)"
    "[Max tokens: 用于控制生成文本的最大长度](https://baidu.com)"

headers={"temperature": temperature, "max_tokens": max_tokens}

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    try:
        response = requests.post(url, json=dict(question=prompt), headers=headers)
        msg = {"role": "assistant", "content": response['text']}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])
    except Exception as e:
        error=str(e)
        st.chat_message("assistant").write(error)
