import json
from django.http import JsonResponse
from django.conf import settings
from game.__init__ import topics, question_answers
import random
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from game.forms import CustomUserCreationForm
from game.models import *


question_selection = settings.QUESTION_SELECTION
values = settings.VALUES

def quizboard1(request):
    if request.method == "GET":
        board = {}
        for topic in topics:
            questions = []
            for type, number in question_selection.items():
                selected_questions = random.sample(topic['questions'][type], number)
                for q in selected_questions:
                    questions.append({"id" : q, "question": question_answers[q]['question'], "questionword" : question_answers[q]['questionword']}) 
            board[topic['topic']] = questions
        data = {
            "quizboard" : board,
            "values" : values
        }
        return JsonResponse(data=data, status=200)

def quizboard(request):
    if request.method == "GET":
        board = {}
        topics = Question.objects.all().values_list('topic_name', flat=True).distinct()
        print(topics)
        for topic in topics:
            questions = []
            for type, number in question_selection.items():
                qids = Question.objects.filter(topic_name=topic).filter(type=type).values_list('QID', flat=True)
                print(qids)
                selected_questions = random.sample(qids, number)
                for qid in selected_questions:
                    question = Question.objects.get(QID=qid)
                    questions.append({"id" : question.QID, "question": question.question, "questionword" : question.questionword}) 
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
