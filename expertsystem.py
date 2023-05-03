# Define the rules and knowledge base
rules = {
    "rule1": {
        "condition": lambda score: score >= 80,
        "consequence": "Excellent performance"
    },
    "rule2": {
        "condition": lambda score: score >= 60 and score < 80,
        "consequence": "Good performance"
    },
    "rule3": {
        "condition": lambda score: score < 60,
        "consequence": "Poor performance"
    }
}

# Define the questions and their weights
questions = {
    "question1": {
        "text": "\nHas the employee met their targets consistently? (yes/no)\n",
        "weight": 0.2
    },
    "question2": {
        "text": "\nDoes the employee actively participate in team activities? (yes/no)\n",
        "weight": 0.1
    },
    "question3": {
        "text": "\nIs the employee proactive in identifying and solving problems? (yes/no)\n",
        "weight": 0.15
    },
    "question4": {
        "text": "\nHow would you rate the employee's communication skills? (1-5)\n",
        "weight": 0.15
    },
    "question5": {
        "text": "\nHow would you rate the employee's time management skills? (1-5)\n",
        "weight": 0.1
    },
    "question6": {
        "text": "\nHow would you rate the employee's ability to work under pressure? (1-5)\n",
        "weight": 0.2
    },
    "question7": {
        "text": "\nDoes the employee demonstrate leadership qualities? (yes/no)\n",
        "weight": 0.1
    }
}

# Define the expert system function
def evaluate_performance(answers):
    score = 0
    for question_id, answer in answers.items():
        weight = questions[question_id]["weight"]
        if isinstance(answer, bool):
            score += weight if answer else 0
        elif isinstance(answer, int):
            score += (answer / 5) * weight

    for rule in rules.values():
        condition = rule["condition"]
        consequence = rule["consequence"]
        if condition(score):
            return consequence

    return "Unable to evaluate performance"

# Prompt the user for input
answers = {}
for question_id, question in questions.items():
    answer = input(question["text"] + " ")
    if answer.lower() == "yes":
        answers[question_id] = True
    elif answer.lower() == "no":
        answers[question_id] = False
    elif answer.isdigit():
        answers[question_id] = int(answer)

# Evaluate performance and provide analysis
result = evaluate_performance(answers)
print("Performance evaluation:", result)