import requests
from bs4 import BeautifulSoup
import json

def get_category(question):
    q = question.lower()
    if any(word in q for word in ["class", "object", "inheritance", "polymorphism", "self", "init", "encapsulation"]):
        return "OOP"
    elif any(word in q for word in ["loop", "for", "while", "iteration"]):
        return "Loops"
    elif any(word in q for word in ["list", "tuple", "dictionary", "set", "data structure", "stack", "queue"]):
        return "Data Structures"
    elif any(word in q for word in ["function", "def", "lambda", "return", "arguments"]):
        return "Functions"
    elif any(word in q for word in ["exception", "error", "try", "catch", "raise"]):
        return "Exception Handling"
    elif any(word in q for word in ["module", "import", "package", "os", "sys"]):
        return "Modules & Packages"
    else:
        return "General"

def get_difficulty(question):
    q_len = len(question.split())
    if q_len < 8:
        return "Easy"
    elif q_len < 15:
        return "Medium"
    else:
        return "Hard"

def scrape_gfg_python_questions():
    url = "https://www.geeksforgeeks.org/python-interview-questions/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    questions_data = []

    for tag in soup.find_all(["h2", "h3"]):
        question_text = tag.get_text().strip()
        next_sibling = tag.find_next_sibling()
        if next_sibling:
            answer_text = next_sibling.get_text().strip()
        else:
            answer_text = ""

        if "?" in question_text and len(answer_text) > 15:
            questions_data.append({
                "question": question_text,
                "answer": answer_text,
                "category": get_category(question_text),
                "difficulty": get_difficulty(question_text)
            })

    return questions_data

def save_to_json(data, filename="data/questions.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print("🔍 Scraping GeeksforGeeks Python questions...")
    questions = scrape_gfg_python_questions()
    save_to_json(questions)
    print(f"✅ Scraped {len(questions)} questions with categories and difficulty levels!")
