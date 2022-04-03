from statistics import mode
from django.db import models

class Question(models.Model):
    QID = models.CharField(max_length=30, primary_key=True)
    question = models.CharField(max_length=500)
    answers = models.CharField(max_length=500)
    question_word = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    topic_name = models.CharField(max_length=100)
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.QID} - {self.question} - {self.answers} - {self.topic_name}"
    class Meta:
      db_table = "Question"    