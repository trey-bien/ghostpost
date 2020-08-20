from django.db import models
from django.utils import timezone

class Post(models.Model):
    text = models.CharField(max_length=300)
    is_boast = models.BooleanField()
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.text
