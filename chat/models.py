from django.db import models
from django.urls import reverse
from random import randint, choice
from django.db.models import QuerySet
from django.contrib.auth import get_user_model
from datetime import datetime
from hashlib import sha256
from django.utils.crypto import get_random_string

# Create your models here.


def unique_group_chat_id() -> str:
    hash = sha256(str(get_random_string(16)).encode('utf-8')).hexdigest()

    all_chat_id: QuerySet[GroupChat] = GroupChat.objects.all()
    chat_id = list(map(lambda chat: chat.chat_id, all_chat_id))
    while hash in chat_id:
        hash = sha256(str(get_random_string(16)).encode('utf-8')).hexdigest()
        
    return hash


def unique_private_chat_id() -> str:
    hash = sha256(str(get_random_string(16)).encode('utf-8')).hexdigest()

    all_chat_id: QuerySet[PrivateChat] = PrivateChat.objects.all()
    private_chat_id = list(map(lambda chat: chat.chat_id, all_chat_id))
    while hash in private_chat_id:
        hash = sha256(str(get_random_string(16)).encode('utf-8')).hexdigest()
        
    return str(hash)


class GroupChat(models.Model):
    name = models.CharField(max_length=512, blank=False, null=False)
    members = models.ManyToManyField(get_user_model(), blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    chat_id = models.CharField(
        max_length=64,
        default=unique_group_chat_id,
        blank=False,
        null=False,
    )
    

    class Meta:
        verbose_name = ("Group Chat")
        verbose_name_plural = ("Group Chats")

    def __str__(self):
        return self.name
    

class PrivateChat(models.Model):
    author = models.ForeignKey(get_user_model(), blank=False, on_delete=models.CASCADE, related_name='chat_author')
    contact = models.ForeignKey(get_user_model(), blank=False, on_delete=models.CASCADE, related_name='chat_contanted')
    timestamp = models.DateTimeField(auto_now_add=True)
    chat_id = models.CharField(
        max_length=64,
        default=unique_private_chat_id,
        blank=False,
        null=False,
    )
    

    class Meta:
        verbose_name = ("Private Chat")
        verbose_name_plural = ("Private Chats")

    def __str__(self):
        return f"{self.author}/{self.contact}"


class AbstractMessage(models.Model):
    TYPES = (
        ('message', 'message'),
        ('image', 'image'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=32,
        choices=TYPES,
        default='message',
    )


    def get_author_username(self):
        return self.author.username


    def get_time(self):
        time = datetime.strftime(
            self.timestamp.astimezone(),
            "%I:%M %p"
        )

        return time

    class Meta:
        abstract = True


class GroupChatMessage(AbstractMessage):
    room = models.ForeignKey(GroupChat, on_delete=models.CASCADE, blank=False, null=False)


class PrivateChatMessage(AbstractMessage):
    private_chat = models.ForeignKey(PrivateChat, on_delete=models.CASCADE, blank=False, null=False)