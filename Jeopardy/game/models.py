import random
import uuid

from django.conf import settings
from django.db import models

question_selection = settings.QUESTION_SELECTION

DIFFICULTIES = [
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard"),
]

class Question(models.Model):
    QID = models.CharField(max_length=30, primary_key=True)
    question = models.CharField(max_length=500)
    answers = models.CharField(max_length=500)
    question_word = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTIES, default="Easy")
    topic_name = models.CharField(max_length=100)
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.QID} - {self.question} - {self.answers} - {self.topic_name}"
    class Meta:
      db_table = "Question"

class Quizboard:
    def __init__(self):
        self.store = {}
        self.answers = {}
        board = {}
        topics = Question.objects.all().values_list('topic_name', flat=True).distinct()
        for topic in topics:
            questions = []
            for type, number in question_selection.items():
                selected = random.sample(list(Question.objects.filter(topic_name=topic).filter(type=type)), number)
                for question in selected:
                    questions.append({
                        "id" : question.QID,
                        "question": question.question,
                        "questionword" : question.question_word
                    })
            board[topic] = questions

class Lobby:
    def __init__(self):
        self.code = uuid.uuid4()
        self.users = {}
        self.quizboard = Quizboard()
    
    def add_user(self, user):
        if len(self.users) < 4:
            self.users[user.username] = self.users.get(user.username, 0)    

    def add_score(self, user, question_id, answer):
        score = self.users.get(user.username, 0)
        self.users[user.username] = score + self.quizboard.check_answer(question_id, answer)
    
    def get_scores(self):
        return self.users
