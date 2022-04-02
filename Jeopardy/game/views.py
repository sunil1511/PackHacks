from django.shortcuts import render
import json
from django.http import JsonResponse
from django.conf import settings

file_path = settings.USERS_FILE_PATH

class Question:
    def __init__(self, value, question, topic):
        self.value = value
        self.question = question
        self.topic = topic


