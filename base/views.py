from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Conversation

# Create your views here.

def get_contacts(request):
    contacts = []
    for contact in Conversation.objects.all():
        if request.user in contact.users.all():
            contacts.append(contact)
    return contacts

@login_required(login_url='login_page')
def index(request):
    conversations = []
    contacts = get_contacts(request)
    for conversation in contacts:
        other_user = conversation.users.all()[1]
        name = other_user
        image = other_user.avatar
        message = conversation.messages.all()[0].content
        time = conversation.messages.all()[0].created_at
        conversations.append({'name': name, 'image': image, 'message': message, 'id': conversation.id, 'time': time, 'contacts': contacts})
    context = {
        'conversations': conversations
    }
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
