# models.py
import openai
from django.conf import settings
from django.db import models

openai.api_key = settings.OPENAI_API_KEY  # OpenAI API 키 설정

class ChatbotModel:
   def __init__(self):
       self.model_engine = "text-davinci-002"
       self.max_tokens = 2048

   def generate_response(self, prompt):
       """
       OpenAI GPT-3 API를 사용하여 사용자 입력에 대한 응답을 생성합니다.
       """
       response = openai.Completion.create(
           engine=self.model_engine,
           prompt=prompt,
           max_tokens=self.max_tokens,
           n=1,
           stop=None,
           temperature=0.7,
       )

       return response.choices[0].text.strip()

class DrugModel(models.Model):
   name = models.CharField(max_length=255)
   image_url = models.URLField()
   ingredients = models.TextField()
   indications = models.TextField()
   dosage = models.TextField()
   precautions = models.TextField()

   def __str__(self):
       return self.name