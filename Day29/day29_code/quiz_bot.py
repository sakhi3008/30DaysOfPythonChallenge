import requests
import random

BASE_URL = "http://127.0.0.1:8000"

def start_quiz():
    score = 0
    print("\n🤖 Welcome to the Python Interview Prep Bot!\n")
    
    for _ in range(5):
        res = requests.get(f"{BASE_URL}/question/random")
        if res.status_code != 200:
            print("⚠️ Couldn't fetch question.")
            break
        q = res.json()
        print(f"Q: {q['question']}")
        user_ans = input("Your Answer: ").strip().lower()
        correct_ans = q["answer"].strip().lower()

        if user_ans in correct_ans or correct_ans in user_ans:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. Correct Answer:\n{q['answer']}\n")

    print(f"🏁 Quiz Finished! Your Score: {score}/5")

if __name__ == "__main__":
    start_quiz()
