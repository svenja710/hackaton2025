
import streamlit as st
from openai import OpenAI


# Wald-Header mit Emojis
st.markdown(
    """
    <div style='text-align:center; font-size:2.2rem; margin-bottom: 0.5em;'>
        🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲
    </div>
    """,
    unsafe_allow_html=True
)


# Tabs erstellen
tab1, tab2, tab3, tab4 = st.tabs([
    "Tab 1", "Tab 2", "Tab 3", "Tab 4"
])


with tab1:
    st.markdown(
        """
        <style>
        .icon-btn button {
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
    st.title("Mein LOTTO-Maerchen")
    
    st.image("images/image copy.png", use_container_width=True)
    st.write("Lasse dir dein persoenliches Lotto-Maerchen generieren! "
             "So hast du Lotto 6 aus 49 noch nie erlebt! 🧚")
    # st.write(
    #     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
    #     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
    #     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
    # )
    st.subheader("Schreibe eine Geschichte zu deinem Lotto-Glück!")
    st.text_input("Sei kreativ und gib ein paar Stichworte ein...")
    st.subheader("Wähle ein Thema aus:")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown('<div class="icon-btn">', unsafe_allow_html=True)
        st.button("🍕", key="pizza")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="icon-btn">', unsafe_allow_html=True)
        st.button("⚽", key="fussball")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="icon-btn">', unsafe_allow_html=True)
        st.button("🎵", key="note")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="icon-btn">', unsafe_allow_html=True)
        st.button("📚", key="buch")
        st.markdown('</div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="icon-btn">', unsafe_allow_html=True)
        st.button("🎲", key="zufall")
        st.markdown('</div>', unsafe_allow_html=True)

    st.button("Jetzt Maerchen generieren!")
    with open("images/image.png", "rb") as img_file:
        st.download_button(
            label="Bild herunterladen",
            data=img_file,
            file_name="lotto_maerchen.png",
            mime="image/png"
        )

with tab2:
    st.write("Inhalt für Tab 2")
    st.markdown(
        """
        <style>
        .dice {
            width: 60px;
            height: 60px;
            margin: 40px auto;
            position: relative;
            perspective: 200px;
        }
        .cube {
            width: 60px;
            height: 60px;
            position: absolute;
            transform-style: preserve-3d;
            animation: roll 1.5s infinite linear;
        }
        .face {
            position: absolute;
            width: 60px;
            height: 60px;
            background: #fff;
            border: 2px solid #888;
            border-radius: 10px;
            font-size: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .face1 { transform: rotateY(0deg) translateZ(30px); }
        .face2 { transform: rotateY(180deg) translateZ(30px); }
        .face3 { transform: rotateY(90deg) translateZ(30px); }
        .face4 { transform: rotateY(-90deg) translateZ(30px); }
        .face5 { transform: rotateX(90deg) translateZ(30px); }
        .face6 { transform: rotateX(-90deg) translateZ(30px); }
        @keyframes roll {
            0% { transform: rotateX(0deg) rotateY(0deg); }
            100% { transform: rotateX(360deg) rotateY(360deg); }
        }
        </style>
        <div class="dice">
            <div class="cube">
                <div class="face face1">⚀</div>
                <div class="face face2">⚁</div>
                <div class="face face3">⚂</div>
                <div class="face face4">⚃</div>
                <div class="face face5">⚄</div>
                <div class="face face6">⚅</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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
