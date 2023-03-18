from django.db import models
from accounts.models import User
# Create your models here.




class Message(models.Model):
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

class Conversation(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    messages = models.ManyToManyField(Message)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return ', '.join([str(user) for user in self.users.all()])

    def get_last_message(self):
        return self.messages.order_by('-created_at').first()
    