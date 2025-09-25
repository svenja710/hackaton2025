
import streamlit as st
from openai import OpenAI


# Tabs erstellen
tab1, tab2, tab3, tab4 = st.tabs([
    "Tab 1", "Tab 2", "Tab 3", "Tab 4"
])

with tab1:
    st.logo(image="images/image.png")
    st.title("Mein Lotto-Maerchen")
    st.write(
        "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
        "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
        "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
    )

with tab2:
    st.write("Inhalt für Tab 2")

with tab3:
    st.write("Inhalt für Tab 3")

with tab4:
    st.write("Inhalt für Tab 4")


# Tab 1 enthält die Chatbot-Logik
with tab1:
    # ...existing code...
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:
        client = OpenAI(api_key=openai_api_key)
        if "messages" not in st.session_state:
            st.session_state.messages = []
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            with st.chat_message("assistant"):
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
