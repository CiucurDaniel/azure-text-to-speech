FROM python:3.10

RUN pip install azure.cognitiveservices.speech

COPY * *


