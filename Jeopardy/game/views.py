from django.shortcuts import render
import json
from django.http import JsonResponse
from django.conf import settings
from game.__init__ import topics
import random

file_path = settings.FILE_PATH
question_selection = settings.QUESTION_SELECTION
values = settings.VALUES

def quizboard(request):
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