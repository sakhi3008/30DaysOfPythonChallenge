# 🗓️ Day 29: Backend of Python Interview Quiz App – FastAPI + JSON + Project Design

Welcome to Day 29 of the **30 Days of Python Challenge**!
Today marks the beginning of the final capstone project — a **Python Interview Quiz App**. In this part, we focused entirely on building the **backend** of the app using **FastAPI**, **JSON files**, and some Python logic for filtering, scoring, and tracking user progress.

---

## 📃 Project Goal

Build a robust, interactive backend API that:

* Serves Python interview questions (scraped from GeeksForGeeks)
* Generates topic-wise MCQ quizzes
* Tracks user progress & streaks
* Stores everything locally using JSON files

---

## 📒 Files Used in Day 29

| File Name             | Description                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| `main.py`             | FastAPI backend server with endpoints to fetch questions, generate quiz, track progress, and submit answers |
| `scraper.py`          | Web scraper to extract interview questions and answers from GeeksForGeeks and categorize/difficulty them    |
| `quiz_bot.py`         | Command-line interface to interact with the API by taking a quiz (for testing/demo)                         |
| `data/questions.json` | Stores all scraped interview questions with category and difficulty                                         |
| `data/users.json`     | Stores user progress data (attempts, correct answers, streaks, etc.)                                        |

---

## 🔹 Topics Covered

### 📑 FastAPI

FastAPI is a modern Python web framework used to create fast, interactive APIs.

* Easy-to-use and automatically generates Swagger UI for testing.

### 📊 Working with JSON

* We used `.json` files as a local database to store:

  * Questions data (`questions.json`)
  * User data (`users.json`)
* We performed reading, writing, and updating these files using Python's `json` module.

### 📌 Pydantic Models

* Used `BaseModel` from `pydantic` for request validation (`AnswerRequest` for answer submission).

### 🧠 Quiz Logic

* Filter questions based on `category`, `difficulty`, and `limit`
* Generate MCQs by mixing right answers with dummy wrong options
* Shuffle answers for fairness
* Calculate accuracy and streak tracking per user

### 💡 Web Scraping

* `scraper.py` uses `BeautifulSoup` to scrape Python questions and their answers from GeeksForGeeks
* Auto categorizes based on keywords (e.g. loops, OOP)
* Assigns difficulty based on question length

---

## 🎯 API Endpoints Overview

| Endpoint     | Method | Description                                                 |
| ------------ | ------ | ----------------------------------------------------------- |
| `/`          | GET    | Welcome endpoint                                            |
| `/questions` | GET    | Fetch raw questions (filtered by category/difficulty/limit) |
| `/quiz`      | GET    | Generate MCQ quiz for user                                  |
| `/submit`    | POST   | Submit answers & update progress                            |
| `/progress`  | GET    | View user's progress                                        |

---

## 🏡 How to Run the Backend Locally

1. **Install dependencies:**

```bash
pip install fastapi uvicorn pydantic beautifulsoup4 requests
```

2. **Scrape questions (only once):**

```bash
python scraper.py
```

3. **Run the FastAPI app:**

```bash
uvicorn main:app --reload
```

4. **Visit Swagger Docs:**

* Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

5. **Use quiz\_bot.py (Optional CLI quiz):**

```bash
python quiz_bot.py
```

---

## 🚀 Highlights of Features

* ✅ **Interactive Quiz Generator**: Quiz questions with randomized options
* ✅ **User Progress Tracking**: Streaks, accuracy, attempts all saved and updated
* ✅ **Category + Difficulty Filters**: Tailored quizzes for focused practice
* ✅ **CLI & API Integration**: Testable both through Swagger UI and command-line

---

## 🧠 Key Learnings

* Built a practical FastAPI project from scratch
* Learned to structure backend logic for scalability
* Practiced web scraping & intelligent categorization
* Implemented real-world concepts like tracking streaks and accuracy
* Demonstrated how APIs can power apps with clean endpoints and docs
