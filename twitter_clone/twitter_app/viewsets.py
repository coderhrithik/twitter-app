from rest_framework import viewsets
from django.contrib.auth.models import User
from . import models
from . import serializers
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTweetOwner

class TweetViewSet(viewsets.ModelViewSet):
    queryset = models.Tweet.objects.all().order_by('-updated_at')
    serializer_class=serializers.TweetSerializer
    permission_classes=[IsAuthenticated,IsTweetOwner]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)    