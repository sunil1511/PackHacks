from django.shortcuts import render
import json
from django.http import JsonResponse
from django.conf import settings
import random

file_path = settings.FILE_PATH
question_selection = settings.QUESTION_SELECTION
values = settings.VALUES

def quizboard(request):
    try:
        topics = read_json_file()
    except (ValueError, FileNotFoundError):
        print(
            "Problem with question configuration. Service Unavailable!"
        )
        data = {
            "status": 500,
            "message": "Users module is currently unavailable. Please try again later!",
        }
        return JsonResponse(data=data, status=data["status"])

    if request.method == "GET":
        board = {}
        for topic in topics:
            questions = []
            for type, number in question_selection.items():
                selected_questions = random.sample(topic['questions'][type].keys(), number)
                questions.extend(selected_questions)
            board[topic['topic']] = questions
        data = {
            "quizboard" : board,
            "values" : values
        }
        return JsonResponse(data=data, status=200)    
    




def read_json_file():
    topics = None
    with open(file_path, "r") as topics_file:
        topics = json.load(topics_file)
    return topics