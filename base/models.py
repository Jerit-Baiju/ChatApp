from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # Fields that are required for authentication
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # Additional fields
    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', null=True, blank=True)
    online = models.BooleanField(default=False)

    # Relationships
    contacts = models.ManyToManyField(
        'self', related_name='contact_of', blank=True, symmetrical=False)

    def __str__(self):
        return self.username




class Conversation(models.Model):
    users = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return ', '.join([str(user) for user in self.users.all()])

    def get_last_message(self):
        return self.messages.order_by('-created_at').first()


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sender} to {self.recipient}: {str(self.content)[:20]}...'
