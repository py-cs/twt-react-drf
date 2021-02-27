from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from ..models import Tweet
from ..forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
from ..serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination


def get_paginated_tweets(tweets, request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    paginated_tweets = paginator.paginate_queryset(tweets, request)
    serializer = TweetSerializer(paginated_tweets, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def tweet_list_view(request):
    tweets = Tweet.objects.all().order_by('-id')
    username = request.GET.get('username')
    if username:
        tweets = tweets.filter(user__username__iexact=username)
    return get_paginated_tweets(tweets, request)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tweet_feed_view(request):
    me = request.user
    print(me.is_authenticated)
    tweets = Tweet.objects.feed(me)
    return get_paginated_tweets(tweets, request)


@api_view(['GET'])
def tweet_detail_view(request, id):
    tweet = Tweet.objects.get(id=id)
    serializer = TweetSerializer(tweet)
    return Response(serializer.data, status=200)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, id):
    try:
        tweet = Tweet.objects.get(id=id)
        if request.user == tweet.user:
            tweet.delete()
            return Response({"message": "Tweet deleted"}, status=200)
        else:
            return Response({"message": "You don't have permission to delete this tweet"}, status=403)
    except:
        return Response({"message": "Tweet not found"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request):
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('id')
        action = data.get('action')
        content = data.get('content')

        tweet = Tweet.objects.get(id=tweet_id)
        user = request.user

        if action == 'like':
            tweet.likes.add(user)
        elif action == 'unlike':
            tweet.likes.remove(user)
        elif action == 'retweet':
            parent_tweet = tweet
            new_tweet = Tweet(
                parent=parent_tweet, 
                user=request.user, 
                content=content
                )
            new_tweet.save()
            tweet = new_tweet
            serializer = TweetSerializer(tweet)
            return Response(serializer.data, status=201)

        serializer = TweetSerializer(tweet)
        return Response(serializer.data, status=200)


@api_view(['POST'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request):
    serializer = TweetCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user = request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)
