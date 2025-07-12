import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="🐍 Python Interview Quiz", layout="centered")
st.title("🐍 Python Interview Quiz App")

# --- USER INPUT SECTION ---
username = st.text_input("Enter your name:", value="sakhi")
category = st.selectbox("Choose Topic (Category):", ["", "OOP", "Functions", "Loops", "Data Structures", "Modules & Packages", "Exception Handling", "General"])
difficulty = st.selectbox("Choose Difficulty:", ["", "Easy", "Medium", "Hard"])
num = st.slider("How many questions?", 1, 10, 3)

if st.button("🎯 Start Quiz"):
    if not username.strip():
        st.warning("⚠️ Please enter your name.")
    else:
        params = {
            "username": username,
            "category": category if category else None,
            "difficulty": difficulty if difficulty else None,
            "num": num
        }

        response = requests.get(f"{BASE_URL}/quiz", params=params)
        if response.status_code == 200:
            quiz_data = response.json()
            st.session_state.quiz_questions = quiz_data["quiz"]
            st.session_state.answers = [None] * len(st.session_state.quiz_questions)
            st.success("✅ Quiz loaded!")
        else:
            st.error("❌ Failed to load quiz. Please try again.")

# --- DISPLAY MCQ QUESTIONS ---
if "quiz_questions" in st.session_state:
    st.subheader("📝 Answer the Questions:")

    for i, item in enumerate(st.session_state.quiz_questions):
        st.markdown(f"**Q{i+1}: {item['question']}**")
        st.session_state.answers[i] = st.radio(
            label="Select one:",
            options=item["options"],
            key=f"q{i}"
        )

    if st.button("✅ Submit Answers"):
        if None in st.session_state.answers:
            st.warning("⚠️ Please answer all questions before submitting.")
        else:
            answers = list(st.session_state.answers)

            payload = {
                "username": username,
                "answers": answers
            }

            st.write("📦 Submitting this data:")
            st.json(payload)

            response = requests.post(f"{BASE_URL}/submit", json=payload)
            if response.status_code == 200:
                result = response.json()
                st.success(f"🎉 Score: {result['score']} / {len(answers)}")
                st.info(f"📊 Accuracy: {result['accuracy']}%")
                st.info(f"🔥 Streak: {result['streak']} days")
            else:
                st.error(f"❌ Failed to submit answers. Status: {response.status_code}")

# --- PROGRESS SECTION ---
if st.button("📈 Check My Progress"):
    progress = requests.get(f"{BASE_URL}/progress", params={"username": username})
    if progress.status_code == 200:
        user = progress.json()
        st.subheader("📊 Your Progress:")
        st.write(f"✅ Attempted: {user['attempted']}")
        st.write(f"🎯 Correct: {user['correct']}")
        st.write(f"📈 Accuracy: {user['accuracy']}%")
        st.write(f"🔥 Streak: {user['streak']} days")
    else:
        st.error("❌ User not found.")
