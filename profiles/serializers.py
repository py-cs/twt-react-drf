from rest_framework import serializers
from django.conf import settings

from .models import Profile


class PublicProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)
    follower_count = serializers.SerializerMethodField(read_only=True)
    following_count = serializers.SerializerMethodField(read_only=True)
    is_following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'location',
            'bio',
            'follower_count',
            'following_count',
            'username',
            'is_following'
        ]

    def get_username(self, profile):
        return profile.user.username
    
    def get_first_name(self, profile):
        return profile.user.first_name

    def get_last_name(self, profile):
        return profile.user.last_name

    def get_follower_count(self, profile):
        return profile.followers.count()

    def get_following_count(self, profile):
        return profile.user.following.count()

    def get_is_following(self, profile):
        request = self.context.get('request')
        if request:
            return profile in request.user.following.all()
