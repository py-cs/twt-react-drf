from django.db import models
from django.conf import settings
from django.db.models import Q


import random

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class TweetQuerySet(models.QuerySet):
    def feed(self, user):
        following_exist = user.following.exists()
        followed_users_ids = []
        if following_exist:
            followed_users_ids = user.following.values_list('user__id', flat=True)
        return self.filter(
            Q(user__id__in=followed_users_ids) |
            Q(user=user)
        ).order_by('-timestamp')


class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)


class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    objects = TweetManager()

    @property
    def is_retweet(self):
        return self.parent is not None

    # def __str__(self):
    #     return str(self.content)
