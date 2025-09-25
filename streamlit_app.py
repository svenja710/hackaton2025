

import streamlit as st
from openai import OpenAI



# --- Custom CSS for modern look ---
st.markdown(
    """
    <style>
    .main-logo {
        display: flex;
        align-items: center;
        gap: 18px;
        margin-bottom: 0.5em;
    }
    .main-logo img {
        height: 38px;
    }
    .slogan {
        color: #d72638;
        font-size: 1.3rem;
        font-weight: 600;
        margin-left: 8px;
    }
    .header-img {
        border-radius: 16px;
        margin-bottom: 1.5em;
        box-shadow: 0 4px 24px 0 #0001;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
    .rounded-box {
        background: #f7f7fa;
        border-radius: 18px;
        padding: 1.5em 2em 1.2em 2em;
        margin-bottom: 2em;
        box-shadow: 0 2px 12px 0 #0001;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    .themen-grid {
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 1.5em;
    }
    .themen-btn button {
        min-width: 270px;
        max-width: 270px;
        width: 100%;
        height: 54px;
        border-radius: 28px !important;
        font-size: 1.15rem !important;
        font-weight: 500;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px 0 #0001;
        border: 1.5px solid #e0e0e0;
        background: #fff;
        color: #222;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 10px;
        padding-left: 18px !important;
        transition: border 0.2s;
        margin-left: auto;
        margin-right: auto;
    }
    .themen-btn button:hover {
        border: 1.5px solid #d72638;
    }
    .action-row {
        display: flex;
        justify-content: flex-end;
        gap: 16px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 2em;
    }
    .stButton>button.green-btn {
        background: #6fdc8c !important;
        color: #222 !important;
        font-weight: 600;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.5em 1.6em !important;
        font-size: 1.1rem !important;
        box-shadow: 0 2px 8px 0 #0001;
    }
    .stButton>button.secondary-btn {
        background: #fff !important;
        color: #222 !important;
        border: 1.5px solid #bbb !important;
        border-radius: 8px !important;
        padding: 0.5em 1.6em !important;
        font-size: 1.1rem !important;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo und Slogan ---
st.logo("images/image.png")

# --- Headerbild ---
st.image("images/image copy.png", use_container_width=False, output_format="PNG", caption=None, clamp=False, channels="RGB")
st.markdown("<div class='header-img'></div>", unsafe_allow_html=True)

# --- Überschrift und Beschreibung ---
st.markdown("""
<h2>Dein LOTTO Märchen</h2>
<p style='font-size:1.1rem; margin-bottom:2em;'>
Stell dir vor, ein paar Zahlen könnten eine kleine Geschichte auslösen – persönlich, witzig, überraschend. Gib ein paar Infos zu dir ein – und wir generieren daraus eine Lotto-Geschichte mit deinen ganz eigenen Zahlen. Natürlich rein fiktiv – aber garantiert unterhaltsam.
</p>
""", unsafe_allow_html=True)

# --- Eingabebox für Story ---
st.markdown("""
<div class='rounded-box'>
<b>Erzähl uns ein wenig von dir.</b><br>
<span style='color:#666;'>Damit wir deine persönliche Geschichte schreiben können, brauchen wir ein paar Details. Keine Sorge – alles bleibt anonym und wird nicht gespeichert. Je mehr du uns verrätst, desto individueller wird deine Story.</span>
<br><br>
<input style='width:100%;padding:0.7em 1em;border-radius:8px;border:1.5px solid #ccc;font-size:1.05rem;margin-bottom:1em;' placeholder='Zeig mir meine Geschichte...'></input>
<span style='color:#888;font-size:0.98rem;'>
<i>Ich heiße Tom, bin 38 Jahre alt und wohne in Hamburg. Ich bin am 2. August 1987 geboren. Ich habe zwei Kinder – Emma ist 6 und Jonas 11. Ich bin verheiratet mit Lea, unser Hochzeitstag ist der 10. Oktober 2010. Wenn ich Zeit habe, bin ich im Garten oder grille mit Freunden. Mein Herz schlägt für den FC St. Pauli – sonst koche ich gern, ich hasse Tomaten. Meine absolute Lieblingszahl? Ganz klar: die 10.</i>
</span>
<br><br>
<div style='display:flex;gap:12px;margin-bottom:1em;'>
    <button style='background:#fff;border:1.5px solid #bbb;border-radius:8px;padding:0.4em 1.2em;font-size:1.05rem;cursor:pointer;'>🔵 Real</button>
    <button style='background:#fff;border:1.5px solid #bbb;border-radius:8px;padding:0.4em 1.2em;font-size:1.05rem;cursor:pointer;'>🕵️‍♂️ Krimi</button>
    <button style='background:#fff;border:1.5px solid #bbb;border-radius:8px;padding:0.4em 1.2em;font-size:1.05rem;cursor:pointer;'>🧚 Fantasy</button>
    <button style='background:#fff;border:1.5px solid #bbb;border-radius:8px;padding:0.4em 1.2em;font-size:1.05rem;cursor:pointer;'>🔥 Action</button>
    <button class='green-btn' style='float:right;margin-top:0.5em;'>Meine Geschichte generieren</button>
</div>

</div>
""", unsafe_allow_html=True)

# --- Alternative Themenauswahl ---
st.markdown("""
<h4 style='margin-top:2.5em;'>Alternative: Lass dich durch Fragen inspirieren</h4>
<p style='font-size:1.05rem;'>
Du hast gerade keine eigene Idee für deine Geschichte? Kein Problem! Wähle einfach die Themen aus, die dich interessieren – und wir stellen dir ein paar passende Fragen dazu. Wähle <b>bis zu 6 Kategorien</b>, die zu dir passen. Alternativ kannst du dir auch per Zufall eine Auswahl zusammenstellen lassen.
</p>
""", unsafe_allow_html=True)

# --- Themen-Grid ---
themen = [
    ("👤 Persönliche Angaben", "person"),
    ("❤️ Beziehungen & Familie", "beziehung"),
    ("⚽️ Freizeit & Interessen", "freizeit"),
    ("🪄 Träume & Fantasien", "traeume"),
    ("🔮 Erinnerung & Kindheit", "kindheit"),
    ("💼 Beruf & Alltag", "beruf"),
    ("� Glück & Aberglaube", "glueck"),
    ("� Popkultur & Medien", "popkultur"),
    ("🤔 Kuriose Entscheidungen", "kurios"),
    ("✈️ Reisen & Abenteuer", "reisen"),
    ("🌲 Natur & Tiere", "natur"),
    ("📡️ Technologie & Zukunft", "tech"),
]
st.markdown("<div class='themen-grid'>", unsafe_allow_html=True)
for i in range(0, len(themen), 2):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="themen-btn">', unsafe_allow_html=True)
        st.button(themen[i][0], key=themen[i][1])
        st.markdown('</div>', unsafe_allow_html=True)
    if i+1 < len(themen):
        with col2:
            st.markdown('<div class="themen-btn">', unsafe_allow_html=True)
            st.button(themen[i+1][0], key=themen[i+1][1])
            st.markdown('</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Action Buttons unten rechts ---
st.markdown("<div class='action-row'>", unsafe_allow_html=True)
colA, colB = st.columns([1,1])
with colA:
    st.button("Zufällige Auswahl", key="zufall", help="Stellt eine zufällige Themenauswahl zusammen.", type="secondary")
with colB:
    st.button("Weiter zu meinen Fragen", key="weiter", help="Weiter zu den ausgewählten Fragen.", type="primary")
st.markdown("</div>", unsafe_allow_html=True)
