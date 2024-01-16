from django.conf import settings
from django.db import models
from django.utils import timezone

MAX_TITLE_NAME = 50
MAX_INTERVIEW_TEXT = 200

class AddInterview(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=MAX_TITLE_NAME)
    text = models.TextField(max_length=MAX_INTERVIEW_TEXT)

    created_date = models.DateTimeField(default=timezone.now)
    interview_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.interview_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title