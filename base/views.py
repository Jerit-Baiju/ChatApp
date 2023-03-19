from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Conversation

# Create your views here.


@login_required(login_url='login_page')
def index(request):
    conversations = []
    for conversation in Conversation.objects.all():
        name = conversation.users.all()[1]
        image = conversation.users.all()[1].avatar
        message = conversation.messages.all()[0].content
        time = conversation.messages.all()[0].created_at
        conversations.append({'name': name, 'image': image, 'message': message, 'id': conversation.id, 'time': time})
    context = {
        'conversations': conversations
    }
    print(context)
    return render(request, 'main.html', context)


def chat(request, id):
    conversations = []
    for conversation in Conversation.objects.all():
        name = conversation.users.all()[1]
        message = conversation.messages.all()[0].content
        conversations.append({'name': name, 'message': message, 'id': conversation.id})
    context = {
        'conversations': conversations
    }
    return render(request, 'main.html',  context)
