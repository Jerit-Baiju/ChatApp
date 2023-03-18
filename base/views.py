from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Conversation

# Create your views here.

@login_required(login_url='login_page')
def index(request):
    context = {
        'conversations': Conversation.objects.all()
    }
    return render(request, 'main.html', context)

def chat(request, id):
    return HttpResponse(id)
