import json
import random
from datetime import datetime
from supabase import create_client, Client

def load_questions(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def ask_questions(questions):
    answers = []
    for question in questions:
        while True:
            try:
                answer = int(input(question["text"] + "\nRate from 1 to 10: "))
                if 1 <= answer <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        answers.append({"answer": answer, "category": question["category"]})
    return answers

def calculate_compatibility(user1_answers, user2_answers):
    total_difference = 0
    category_scores = {"career": 0, "love": 0, "feelings": 0}
    category_count = {"career": 0, "love": 0, "feelings": 0}

    for u1, u2 in zip(user1_answers, user2_answers):
        difference = abs(u1["answer"] - u2["answer"])
        total_difference += difference
        category_scores[u1["category"]] += difference
        category_count[u1["category"]] += 1

    overall_score = ((90 - total_difference) / 90) * 100

    for category in category_scores:
        if category_count[category] > 0:
            max_diff_category = category_count[category] * 9
            category_scores[category] = ((max_diff_category - category_scores[category]) / max_diff_category) * 100
        else:
            category_scores[category] = 100

    return overall_score, category_scores

def save_results_to_supabase(supabase, data):
    try:
        response = supabase.table("compatibility_results").insert(data).execute()
        # If no exception is raised, we assume the insertion was successful
        print("Results saved successfully.")
    except Exception as e:
        # If an exception is raised, it means the insertion failed
        print("Error saving to Supabase:", e)


def main():
    url: str = "https://random.supabase.co"
    key: str = "key"
    supabase: Client = create_client(url, key)

    question_data = load_questions("static/Questions.json")

    all_questions = []
    for category, questions in question_data.items():
        for question in questions:
            all_questions.append({"text": question, "category": category})

    selected_questions = random.sample(all_questions, 10)

    print("User 1, please answer the following questions:")
    user1_answers = ask_questions(selected_questions)

    print("\nUser 2, please answer the same questions:")
    user2_answers = ask_questions(selected_questions)

    overall_compatibility, category_compatibility = calculate_compatibility(user1_answers, user2_answers)
    print(f"\nYour overall compatibility score is: {overall_compatibility:.2f}%")

    for category, score in category_compatibility.items():
        print(f"Compatibility in {category}: {score:.2f}%")

    data = {
    "date": datetime.now().isoformat(),  # Ensure this is lowercase 'date'
    "overall_compatibility": overall_compatibility,
    "career_compatibility": category_compatibility.get('career', 100),
    "love_compatibility": category_compatibility.get('love', 100),
    "feelings_compatibility": category_compatibility.get('feelings', 100)
}


    save_results_to_supabase(supabase, data)

if __name__ == "__main__":
    main()
