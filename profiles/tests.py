from django.test import TestCase
from .models import Profile, FollowerRelation
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='somepass')
        self.user2 = User.objects.create_user(username='user2', password='somepass')

    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_following(self):
        first = self.user
        second = self.user2
        first.profile.followers.add(second)
        self.assertEqual(first.profile.followers.count(), 1)
        self.assertEqual(second.following.count(), 1)


