import html
import random

import requests
from getkey import getkey

from data import BColours


def restart():
    import os
    import sys

    # print("argv was", sys.argv)
    # print("sys.executable was", sys.executable)
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    BColours.pretty_print("Restarting...", BColours.OKGREEN)

    os.execv(sys.executable, ['python'] + sys.argv)


def get_questions() -> dict:
    '''Get 10 questions from the Open Trivia Database AP'''
    url: str = "https://opentdb.com/api.php?amount=10"
    BColours.pretty_print(
        "Getting 10 questions...", BColours.OKBLUE)
    response = requests.get(url, timeout=10)
    return response.json()


questions = get_questions()["results"]

# shuffle the questions
random.shuffle(questions)
# decode special characters in questions
for question in questions:
    question["question"] = html.unescape(question["question"])
    question["correct_answer"] = html.unescape(question["correct_answer"])
    for i in range(len(question["incorrect_answers"])):
        question["incorrect_answers"][i] = html.unescape(
            question["incorrect_answers"][i])


SCORE = 0
TOTAL_SCORE = 0


def answer_input() -> str:
    """Get the answer from the user"""
    try:
        answer_val = getkey()
        if answer_val == 's':
            return "stop"
        if answer_val == 'r':
            return "restart"
        if answer_val not in ('1', '2', '3', '4'):
            BColours.pretty_print(
                "Please enter a valid number", BColours.FAIL)
            return answer_input()
    except ValueError:
        BColours.pretty_print("Please enter a number", BColours.FAIL)
        return answer_input()
    return str(answer_val)


BColours.pretty_print("press S to stop playing", BColours.WARNING)
BColours.pretty_print("press R to restart", BColours.FAIL)
for i in range(len(questions)):
    # pick a random question
    question = random.choice(questions)
    TOTAL_SCORE += 1
    BColours.pretty_print(question["category"], BColours.UNDERLINE)
    # print("Difficulty:", question["difficulty"].capitalize())
    BColours.pretty_print("Difficulty: " +
                          question["difficulty"].capitalize(), BColours.FAIL)
    BColours.pretty_print(question["question"], BColours.OKBLUE)
    answers = question["incorrect_answers"]
    answers.append(question["correct_answer"])
    random.shuffle(answers)
    for i, answer in enumerate(answers):
        print(str(i+1) + ". " + answer)
    answer = answer_input()
    # make sure it does not fail if index is out of range

    try:
        if answer.lower() == "stop":
            break
        if answer.lower() == "restart":
            restart()
        if answers[int(answer)-1] == question["correct_answer"]:
            BColours.pretty_print("Correct!", BColours.OKGREEN)
            SCORE += 1
            print(f"Your score is {str(SCORE)}/{str(TOTAL_SCORE)}")
        else:
            BColours.pretty_print("Incorrect!", BColours.FAIL)
            BColours.pretty_print("Correct answer: " +
                                  question["correct_answer"], BColours.OKGREEN)
            print(f"Your score is {str(SCORE)}/{str(TOTAL_SCORE)}")
        print("")
    except IndexError:
        print("")
        print(f"Your score is {str(SCORE)}/{str(TOTAL_SCORE)}")

    # remove the question from the list so it does not get picked again
    questions.remove(question)


print(f"You got {str(SCORE)} out of {str(TOTAL_SCORE)} correct!")
