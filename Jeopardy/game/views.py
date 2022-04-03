import json
from django.http import JsonResponse
from django.conf import settings
import random
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from game.forms import CustomUserCreationForm
from game.models import *
from game import lobbies


question_selection = settings.QUESTION_SELECTION
values = settings.VALUES

def quizboard(request):
    if request.method == "GET":
        board = {}
        topics = Question.objects.all().values_list('topic_name', flat=True).distinct()
        for topic in topics:
            questions = []
            for difficulty, number in question_selection.items():
                selected = random.sample(list(Question.objects.filter(topic_name=topic).filter(difficulty=difficulty)), number)
                for question in selected:
                    questions.append({
                        "id" : question.QID,
                        "question": question.question,
                        "questionword" : question.question_word
                    })
            board[topic] = questions
        data = {
            "quizboard" : board,
            "values" : values
        }
        return JsonResponse(data=data, status=200)    

def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))    
            
def create_lobby(request):
    lobby = Lobby(request.user)
    lobbies[lobby.code] = lobby
    return 

def connect_to_lobby(request, code):
    pass