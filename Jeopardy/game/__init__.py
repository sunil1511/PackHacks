from django.conf import settings
import json

file_path = settings.FILE_PATH
topics = None
try:
    with open(file_path, "r") as topics_file:
        topics = json.load(topics_file)
except (ValueError, FileNotFoundError):
    print("Problem with question configuration. Service Unavailable!")