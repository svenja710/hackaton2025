
import streamlit as st
from openai import OpenAI


# Tabs erstellen
tab1, tab2, tab3, tab4 = st.tabs([
    "Tab 1", "Tab 2", "Tab 3", "Tab 4"
])


with tab1:
    st.markdown(
        """
        <style>
        div.stButton > button {
            width: 70px !important;
            height: 70px !important;
            border-radius: 12px !important;
            font-size: 2rem !important;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 8px 8px 8px 0;
            padding: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.logo(image="images/image.png")
    st.title("Mein Lotto-Maerchen")
    st.write("Lasse dir dein persoenliches Lotto-Maerchen generieren!"
             "So hast du Lotto 6 aus 49 noch nie erlebt! 🧚")
    st.write(
        "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
        "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
        "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
    )
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("🍕", key="pizza")
    with col2:
        st.button("⚽", key="fussball")
    with col3:
        st.button("🎵", key="note")
    with col4:
        st.button("📚", key="buch")
    with col5:
        st.button("🎲", key="zufall")


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
