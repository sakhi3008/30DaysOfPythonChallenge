from fastapi import FastAPI, Query
from pydantic import BaseModel
import json
import random
from datetime import datetime

app = FastAPI(
    title="🐍 Python Interview Preparation API",
    description="An interactive API to help users practice Python interview questions with quiz, streaks, and progress tracking.",
    version="1.0.0"
)

# Load questions
def load_questions():
    with open("data/questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Load users
def load_users():
    try:
        with open("data/users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save users
def save_users(users):
    with open("data/users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

# Dummy wrong options (for demo purposes)
WRONG_OPTIONS = [
    "Used to fry eggs", "Part of hardware", "Not related to Python", "Something else"
]

# 🏠 Root Endpoint
@app.get("/", summary="🏠 Welcome", description="Test if the API is running properly.")
def welcome():
    return {"message": "Welcome to Python Interview Preparation API"}

# ❓ Get Raw Questions
@app.get("/questions", summary="❓ Get Questions", description="Fetch raw Python questions based on category and difficulty.")
def get_questions(category: str = None, difficulty: str = None, limit: int = 5):
    questions = load_questions()
    filtered = [
        q for q in questions
        if (category is None or q["category"] == category)
        and (difficulty is None or q["difficulty"] == difficulty)
    ]
    return random.sample(filtered, min(limit, len(filtered)))

# 🧠 Generate MCQ Quiz
@app.get("/quiz", summary="🧠 Generate Quiz", description="Create a quiz with MCQs for a specific user based on selected topic and difficulty.")
def generate_quiz(username: str, category: str = None, difficulty: str = None, num: int = 5):
    questions = load_questions()
    filtered = [
        q for q in questions
        if (not category or q["category"] == category)
        and (not difficulty or q["difficulty"] == difficulty)
    ]
    selected = random.sample(filtered, min(num, len(filtered)))

    quiz = []
    for q in selected:
        options = [q["answer"]] + random.sample(WRONG_OPTIONS, 3)
        random.shuffle(options)
        quiz.append({
            "question": q["question"],
            "options": options
        })

    users = load_users()
    if username not in users:
        users[username] = {
            "attempted": 0,
            "correct": 0,
            "streak": 0,
            "last_attempt": None
        }
        save_users(users)

    return {"quiz": quiz}

# ✅ Submit Answers
class AnswerRequest(BaseModel):
    username: str
    answers: list[str]

@app.post("/submit", summary="✅ Submit Answers", description="Submit your answers and get score, accuracy, and streak update.")
def submit_answers(payload: AnswerRequest):
    correct_answers = []
    questions = load_questions()

    for ans in payload.answers:
        for q in questions:
            if ans.strip().lower() == q["answer"].strip().lower():
                correct_answers.append(ans)
                break

    users = load_users()
    user = users.get(payload.username)

    user["attempted"] += len(payload.answers)
    user["correct"] += len(correct_answers)
    accuracy = round((user["correct"] / user["attempted"]) * 100, 2)

    today = datetime.today().date().isoformat()
    if user.get("last_attempt") == today:
        pass  # already counted today
    else:
        user["streak"] += 1
        user["last_attempt"] = today

    save_users(users)

    return {
        "score": len(correct_answers),
        "total": len(payload.answers),
        "accuracy": accuracy,
        "streak": user["streak"]
    }

# 📊 Track Progress
@app.get("/progress", summary="📈 User Progress", description="Get the user's overall progress: attempts, accuracy, and streaks.")
def get_progress(username: str):
    users = load_users()
    user = users.get(username)
    if not user:
        return {"message": "User not found"}
    attempted = user["attempted"]
    correct = user["correct"]
    accuracy = round((correct / attempted) * 100, 2) if attempted else 0
    return {
        "attempted": attempted,
        "correct": correct,
        "accuracy": accuracy,
        "streak": user["streak"]
    }
