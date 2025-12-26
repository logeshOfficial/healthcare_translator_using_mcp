import streamlit as st
import streamlit.components.v1 as components
from ai_utils import translate_medical_text
import config
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Healthcare Translator", layout="wide", initial_sidebar_state="collapsed")

st.title("🩺 Healthcare Translation App")
st.caption("Real-time multilingual communication for patients and providers")

# ---------------- Language Selection ----------------
col1, col2 = st.columns(2)

with col1:
    input_lang = st.selectbox("Input Language", config.language_map.keys())

with col2:
    output_lang = st.selectbox("Output Language", config.language_map.keys())

lang_code = config.language_map

# ---------------- Voice Input (Browser Speech) ----------------
st.markdown("### 🎙️ Speak (Browser Speech Recognition)")

components.html(
    f"""
    <script>
    let recognition;
    let finalTranscript = "";

    function startRecording() {{
        recognition = new webkitSpeechRecognition();
        recognition.lang = "{lang_code[input_lang]}";
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onresult = function(event) {{
            let interim = "";
            for (let i = event.resultIndex; i < event.results.length; i++) {{
                if (event.results[i].isFinal) {{
                    finalTranscript += event.results[i][0].transcript + " ";
                }} else {{
                    interim += event.results[i][0].transcript;
                }}
            }}
            document.getElementById("browserTranscript").value =
                finalTranscript + interim;
        }};

        recognition.start();
    }}

    function stopRecording() {{
        recognition.stop();
    }}

    function copyToClipboard() {{
        const text = document.getElementById("browserTranscript").value;
        navigator.clipboard.writeText(text);
        alert("Transcript copied. Paste it below to translate.");
    }}
    </script>

    <button onclick="startRecording()">🎙️ Start</button>
    <button onclick="stopRecording()">⏹️ Stop</button>
    <button onclick="copyToClipboard()">📋 Copy Transcript</button>

    <br><br>
    <textarea id="browserTranscript"
        placeholder="Live transcript appears here..."
        style="width:100%; height:150px;"></textarea>
    """,
    height=330,
)

# ---------------- Original Transcript ----------------
st.markdown("### 🗣️ Original Transcript (Paste here)")
original_text = st.text_area(
    "Paste the copied transcript here",
    height=150
)

# ---------------- Translation ----------------
if st.button("🌍 Translate"):
    if not original_text.strip():
        st.warning("Please provide speech input first")
    else:
        with st.spinner("Translating with Generative AI..."):
            translated_text = translate_medical_text(
                original_text,
                output_lang
            )

        st.session_state["translated"] = translated_text

# ---------------- Translated Output ----------------
if "translated" in st.session_state:
    st.markdown("### 🌍 Translated Text")
    st.text_area(
        label="Translated Text",
        value=st.session_state["translated"],
        height=150,
        label_visibility="collapsed"
    )

    # ---------------- Speak Button (Browser TTS) ----------------
    components.html(
        f"""
        <script>
        function speakTranslation() {{
            const msg = new SpeechSynthesisUtterance();
            msg.text = `{st.session_state["translated"]}`;
            msg.lang = "{lang_code[output_lang]}";
            window.speechSynthesis.speak(msg);
        }}
        </script>

        <button onclick="speakTranslation()">🔊 Speak Translation</button>
        """,
        height=80,
    )