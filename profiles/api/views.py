from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from ..models import Profile
from django.contrib.auth import get_user_model
from ..serializers import PublicProfileSerializer


User = get_user_model()


@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def user_follow_view(request, username):
    user = request.user
    try:
        profile = Profile.objects.get(user__username=username)
        data = PublicProfileSerializer(instance=profile, context={'request': request})
        return Response(data.data, status=200)
    except:
        return Response({'detail': 'Profile not found'}, status=404)
    action = request.data.get('action')
    if user != profile.user:
        if action == 'follow':
            profile.followers.add(user)
        elif action == 'unfollow':
            profile.followers.remove(user)
    data = PublicProfileSerializer(instance=profile, context={'request': request})
    return Response(data.data, status=200)


@api_view(['GET'])
def profile_detail_api_view(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
        data = PublicProfileSerializer(instance=profile, context={'request': request})
        return Response(data.data, status=200)
    except:
        return Response({'detail': 'Profile not found'}, status=404)
