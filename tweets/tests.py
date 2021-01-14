from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweet

from rest_framework.test import APIClient

User = get_user_model()


class TweetTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='somepass')
        self.user2 = User.objects.create_user(username='user2', password='somepass')
        self.tweet1 = Tweet.objects.create(user=self.user, content='test1')
        self.tweet2 = Tweet.objects.create(user=self.user, content='test2')
        self.tweet3 = Tweet.objects.create(user=self.user2, content='test3')


    def test_user_created(self):
        self.assertEqual(self.user.username, 'user1')

    def test_tweet_created(self):
        tweet = self.tweet1
        self.assertEqual(tweet.id, 1)
        self.assertEqual(tweet.user, self.user)
    
    def get_client(self):
        client=APIClient()
        client.login(username=self.user.username, password='somepass')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get('/api/tweets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_action_likes(self):
        client = self.get_client()
        response = client.post('/api/tweets/action/', {'id': 1, 'action': 'like'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['likes'], 1)
        response = client.post('/api/tweets/action/', {'id': 1, 'action': 'unlike'})
        self.assertEqual(response.json()['likes'], 0)
    
    def test_action_retweet(self):
        client = self.get_client()
        response = client.post('/api/tweets/action/', {'id': 1, 'action': 'retweet'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['parent']['id'], 1)

    def test_create_tweet(self):
        data = {
            'content': 'test4',
            'user': self.user
        }
        client = self.get_client()
        response = client.post('/api/tweets/create/', data)
        self.assertEqual(response.status_code, 201)

    def test_get_tweet(self):
        client = self.get_client()
        response = client.get('/api/tweets/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('content'), self.tweet1.content)

    def test_delete_tweet(self):
        client = self.get_client()
        response = client.delete('/api/tweets/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = client.delete('/api/tweets/1/delete/')
        self.assertEqual(response.status_code, 404)
        response = client.delete('/api/tweets/3/delete/')
        self.assertEqual(response.status_code, 403)
