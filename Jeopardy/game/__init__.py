from django.conf import settings
import json

topics_file_path = settings.TOPICS_FILE_PATH
question_answers_file_path = settings.QUESTION_ANSWERS_FILE_PATH
topics = None
question_answers = None
try:
    with open(topics_file_path, "r") as topics_file:
        topics = json.load(topics_file)
    with open(question_answers_file_path, "r") as question_answers_file:
        question_answers = json.load(question_answers_file)    
except (ValueError, FileNotFoundError):
    print("Problem with question configuration. Service Unavailable!")