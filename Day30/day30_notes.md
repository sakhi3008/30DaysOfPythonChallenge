# 🗓️ Day 30 – Final Project Completion: Python Interview Quiz App (Frontend + Docs)

Today marks the final day of the **30 Days of Python Challenge**, and I proudly completed the final project by building an interactive full-stack **Python Interview Preparation Quiz App**.

On **Day 29**, the backend API was developed using **FastAPI**, and today, for **Day 30**, I focused on finalizing the project by adding a **frontend using Streamlit**, improving user interaction, and documenting the entire workflow.

---

## 🔹 Topics Covered

### 🔹 Streamlit Basics

* Simple UI creation for web apps
* Widgets like dropdowns, radio buttons, and buttons
* Data interaction between user input and backend

### 🔹 Project Structure

```
python-interview-quiz-app/
├── app.py              # Streamlit frontend (Day 30)
├── main.py             # FastAPI backend (Day 29)
├── scraper.py          # GFG question scraper
├── quiz_bot.py         # CLI quiz 
├── data/
│   ├── questions.json   # Scraped questions with category + difficulty
│   └── users.json       # User progress tracking
```

---

## 🎯 Challenge

### 🔹 Day 30 Challenge

**✨ Complete your project with documentation**

### 🔹 What I Did

* Added a **Streamlit interface** to interact with the backend
* Created a smooth quiz flow: choose topic ➔ take quiz ➔ submit ➔ view progress
* Integrated APIs from `main.py` to get questions, submit answers, and show progress
* Deployed locally and tested the full app end-to-end

---

## 🏋️ Streamlit App Features (`app.py`)

### ✅ Main Functionalities:

* User can **enter their name**
* Select **category**, **difficulty level**, and **number of questions**
* Take a quiz by selecting answers
* Submit answers and view score, accuracy, and streak
* See their **overall progress** in real-time

### ⚖️ Code Highlights:

```python
st.text_input("Enter your name")
st.selectbox("Choose category", [...])
st.radio("Select difficulty", [...])
st.button("Start Quiz")
```

These Streamlit widgets made it easy to build a user-friendly interface.

---

## 🔗 How the Backend and Frontend Connect

* The frontend (Streamlit in `app.py`) makes **HTTP requests** to FastAPI (`main.py`)
* Streamlit sends data like username, selected category, and answers to the API
* Backend handles logic like filtering questions, evaluating score, and tracking progress

### Endpoints Used:

* `GET /quiz`
* `POST /submit`
* `GET /progress`

---

## 🚀 How to Run This Project

### Step 1: Start Backend

```bash
uvicorn main:app --reload
```

Visit API docs at `http://127.0.0.1:8000/docs`

### Step 2: Run Frontend

```bash
streamlit run app.py
```

Interact with the full app in your browser at `http://localhost:8501`

---

## 🫠 Key Learnings

* Streamlit is a powerful tool to turn scripts into apps quickly
* FastAPI handles data flow and validation beautifully with Pydantic
* JSON-based storage can be a great lightweight alternative to databases for small projects
* Combining **CLI + Web Interface** gives users flexibility to practice Python MCQs

---

## 🔥 Why This Project Matters

Interview preparation often lacks structure. This project:

* Gives **category-wise quizzes**
* Encourages **daily practice** with streaks
* Tracks **performance over time**
* Has both **API & GUI** for varied use cases (CLI bot, Streamlit, Swagger UI)

---

## 🌟 Final Thoughts

This final project tied together everything I learned during the 30 days:

* API building
* JSON handling
* Data scraping
* CLI tools
* Streamlit apps

> A complete mini ecosystem for Python interview preparation built in just 30 days!

---

## 🎉 Completed: 30 Days of Python Challenge ✔️

Thank you for following along! 🚀
