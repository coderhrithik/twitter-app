from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from twitter_app.models import Tweet

class TweetModelTest(TestCase):
    #@classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        Tweet.objects.create(user=test_user, content='This is a test tweet')

    def test_content(self):
        test_tweet = Tweet.objects.create(id=1, content='This is a test tweet')

        # Retrieving the tweet
        tweet = Tweet.objects.get(id=1)

        # Asserting the content
        self.assertEqual(tweet.content, test_tweet.content)

class TweetAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.tweet = Tweet.objects.create(user=self.user, content='Test tweet content')

    def test_list_tweets(self):
        response = self.client.get('/api/tweets/')
        self.assertEqual(response.status_code, 200)

    def test_create_tweet(self):
        data = {'content': 'New tweet'}
        response = self.client.post('/api/tweets/', data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve_tweet(self):
        response = self.client.get(f'/api/tweets/{self.tweet.id}/')
        self.assertEqual(response.status_code, 200)

    def test_update_tweet(self):
        data = {'content': 'Updated tweet'}
        response = self.client.patch(f'/api/tweets/{self.tweet.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_tweet(self):
        response = self.client.delete(f'/api/tweets/{self.tweet.id}/')
        self.assertEqual(response.status_code, 204)

