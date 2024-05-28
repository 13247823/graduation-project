# views.py
from django.shortcuts import render
from .models import ChatbotModel, DrugModel

def home_view(request):
   return render(request, 'home.html')

def chatbot_view(request):
   if request.method == 'POST':
       user_input = request.POST.get('user_input')
       chatbot = ChatbotModel()
       response = chatbot.generate_response(user_input)
       context = {'response': response}
       return render(request, 'chatbot.html', context)
   else:
       context = {'response': ''}
       return render(request, 'chatbot.html', context)

def drug_detail_view(request):
   return render(request, 'drug_detail.html')