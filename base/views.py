from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Conversation

# Create your views here.


@login_required(login_url='login_page')
def index(request):
    conversations = []
    for conversation in Conversation.objects.all():
        name = conversation.users.all()[1]
        message = conversation.messages.all()[0].content
        conversations.append({'name': name, 'message': message, 'id': conversation.id})
    context = {
        'conversations': conversations
    }
    return render(request, 'index.html', context)


def chat(request, id):
    conversations = []
    for conversation in Conversation.objects.all():
        name = conversation.users.all()[1]
        message = conversation.messages.all()[0].content
        conversations.append({'name': name, 'message': message, 'id': conversation.id})
    context = {
        'conversations': conversations
    }
    return render(request, 'chat.html',  context)


def contacts_page(request):
    return render(request, 'contacts.html')


def test_page(request):
    return render(request, 'test.html')

