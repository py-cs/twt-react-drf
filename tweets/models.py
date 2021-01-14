from django.db import models
from django.conf import settings

import random

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    @property
    def is_retweet(self):
        return self.parent is not None

    # def __str__(self):
    #     return str(self.content)
