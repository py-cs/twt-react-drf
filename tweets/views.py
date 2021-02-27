from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html')


def tweets_list_view(request, *args, **kwargs):
    return render(request, 'tweets/list.html')


def tweets_feed_view(request, *args, **kwargs):
    return render(request, 'tweets/list.html', context={'feed': True})


def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, 'tweets/detail.html', context={'tweet_id': tweet_id})
    

def tweets_profile_view(request, username, *args, **kwargs):
    return render(request, 'tweets/profile.html', context={'profile_username': username})

