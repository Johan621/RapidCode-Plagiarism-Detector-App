import streamlit as st
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(page_title="Smart Code Plagiarism Tool", layout="wide")

st.title("🛡️ RapidCode Plagiarism Detector")

if "prev_text" not in st.session_state:
    st.session_state.prev_text = ""

if "prev_time" not in st.session_state:
    st.session_state.prev_time = time.time()

if "typing_speeds" not in st.session_state:
    st.session_state.typing_speeds = []

if "paste_detected" not in st.session_state:
    st.session_state.paste_detected = False

col1, col2 = st.columns(2)

# Code similarity checker
# (used to check the both codes of user and internet respectively.)
with col1:
    st.header("🔍 Code Similarity Checker")

    code1 = st.text_area("Code Submission 1", height=200)
    code2 = st.text_area("Code Submission 2", height=200)

    if st.button("Check Plagiarism"):
        if code1.strip() and code2.strip():
            vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
            tfidf = vectorizer.fit_transform([code1, code2])
            sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100
            sim = round(sim, 2)

            st.metric("Plagiarism Score", f"{sim} %")

            if sim >= 80:
                st.error("🚨 High Plagiarism Detected!")
            elif sim >= 50:
                st.warning("⚠️ Moderate Similarity")
            else:
                st.success("✔ Low Similarity — Looks Original")

        else:
            st.error("Please paste both code samples.")

    st.divider()


# Typing time cheating detector simultaneously
with col2:
    st.header("⏱️ Real-Time Typing Cheating Detector")

    st.caption("Start typing — the app will automatically detect typing speed and paste events.")

    typed_code = st.text_area("Student's Typing Box (auto-monitored)", key="typing_box", height=200)

    current_time = time.time()
    previous_text = st.session_state.prev_text

    # Detect text change
    if typed_code != previous_text:
        old = previous_text
        new = typed_code

        old_len = len(old)
        new_len = len(new)

        added = new_len - old_len
        elapsed = current_time - st.session_state.prev_time

        if added > 0:
            time_per_char = elapsed / max(added, 1)
            st.session_state.typing_speeds.append(time_per_char)

            # Detect paste
            if added > 10 and time_per_char < 0.01:
                st.session_state.paste_detected = True

        st.session_state.prev_text = new
        st.session_state.prev_time = current_time

    if st.button("Analyze Typing"):
        st.subheader("Typing Analysis Result")

        fastest_human = 0.055  # 55 ms per character

        if st.session_state.paste_detected:
            st.error("🚨 Paste Detected: User inserted too many characters instantly!")

        if st.session_state.typing_speeds:
            avg_speed = sum(st.session_state.typing_speeds) / len(st.session_state.typing_speeds)

            st.metric("Average Typing Time per Character", f"{avg_speed:.4f} sec")

            if avg_speed < fastest_human:
                st.error("⚠️ Too Fast — Looks Like Copy-Paste!")
            else:
                st.success("✔ Typing Speed Looks Normal")

        st.expander("Show Typing Logs (Debug)").write(st.session_state.typing_speeds)

    st.divider()

st.caption("Built with 💖💖(Love) — using Streamlit")
st.caption("Thanks for using the App - Learn,Evolve,Excel")
