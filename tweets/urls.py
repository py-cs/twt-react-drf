from django.contrib import admin
from django.urls import path, include
from .views import tweets_detail_view, tweets_profile_view, tweets_list_view, tweets_feed_view

urlpatterns = [
    path('', tweets_feed_view),
    path('all/', tweets_list_view),
    path('api/tweets/', include('tweets.api.urls')), 
    path('api/profile/', include('profiles.api.urls')),
    path('<int:tweet_id>', tweets_detail_view),
    # path('<str:username>', tweets_profile_view),
]
