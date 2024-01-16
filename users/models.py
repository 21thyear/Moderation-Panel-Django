from django.conf import settings
from django.db import models
from django.utils import timezone

MAX_MODERATOR_NAME = 32
MAX_BLACKLIST_REASON = 64

MAX_MODERATOR_DISCORD_LEN = 20
MAX_MODERATOR_TELEGRAM_LEN = 12
MAX_VK_MODERATOR_LEN = 32
MAX_FORUM_MODERATOR_LEN = 24

class CreateUser(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    Name = models.CharField(max_length=MAX_MODERATOR_NAME)
    Reason = models.TextField(max_length=MAX_BLACKLIST_REASON)

    Discord_ID = models.CharField(max_length=MAX_MODERATOR_DISCORD_LEN)
    Telegram_ID = models.CharField(max_length=MAX_MODERATOR_TELEGRAM_LEN)
    VK_ID = models.CharField(max_length=MAX_VK_MODERATOR_LEN)
    Forum_ID = models.CharField(max_length=MAX_FORUM_MODERATOR_LEN)

    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title