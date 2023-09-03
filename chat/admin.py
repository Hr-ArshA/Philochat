from django.contrib import admin
from .models import GroupChat, GroupChatMessage, PrivateChat, PrivateChatMessage
from datetime import datetime
from django.utils.html import format_html

# Register your models here.

class GroupChatAdmin(admin.ModelAdmin):
    model = GroupChat
    list_display = ("name", "members_count", 'chat_id', "time")
    list_filter = ("members", "timestamp")
    search_fields = ("name",)

    def members_count(self, model: GroupChat):
        return model.members.count()

    def time(self, model: GroupChat):
        date: datetime = model.timestamp.astimezone()
        format_date = datetime.strftime(date, "%b %d, %H:%M:%S")
        return format_date

    fieldsets = ((None, {"fields": ("name", 'members',)}),)

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("name", 'members')}
        ),
    )


class PrivateChatAdmin(admin.ModelAdmin):
    model = PrivateChat
    list_display = ("author", 'contact', 'chat_id',"time")
    list_filter = ("author", 'contact', "timestamp")

    def time(self, model: PrivateChat):
        date: datetime = model.timestamp.astimezone()
        format_date = datetime.strftime(date, "%b %d, %H:%M:%S")
        return format_date

    fieldsets = ((None, {"fields": ("author", 'contact', 'chat_id')}),)

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("author", 'contact', )}
        ),
    )


class PrivateChatMessageAdmin(admin.ModelAdmin):
    model = PrivateChatMessage
    list_display = ("author", 'message', 'private_chat',"time")
    list_filter = ("author", 'private_chat', "timestamp")
    search_fields = ("type", "timestamp")


    def time(self, model: PrivateChatMessage):
        date: datetime = model.timestamp.astimezone()
        format_date = datetime.strftime(date, "%b %d, %H:%M:%S")
        return format_date
    
    def message(self, model: PrivateChatMessage):
        content = ' '.join(str(model.content).split()[:5])
        if model.type == "image":
            return format_html(f'<a href="{content}">تصویر</a>')
        return content
    

class GroupChatMessageAdmin(admin.ModelAdmin):
    model = GroupChatMessage
    list_display = ("author", 'message', 'room',"time")
    list_filter = ("author", 'room', "timestamp")
    search_fields = ("type", "timestamp")


    def time(self, model: GroupChatMessage):
        date: datetime = model.timestamp.astimezone()
        format_date = datetime.strftime(date, "%b %d, %H:%M:%S")
        return format_date
    
    def message(self, model: GroupChatMessage):
        content = ' '.join(str(model.content).split()[:5])
        if model.type == "image":
            return format_html(f'<a href="{content}">تصویر</a>')
        return content


admin.site.register(GroupChat, GroupChatAdmin)
admin.site.register(GroupChatMessage, GroupChatMessageAdmin)
admin.site.register(PrivateChat, PrivateChatAdmin)
admin.site.register(PrivateChatMessage, PrivateChatMessageAdmin)