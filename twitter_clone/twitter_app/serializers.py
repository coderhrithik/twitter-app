from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet,Reply

class TweetSerializer(serializers.ModelSerializer):
    is_edited = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'created_at', 'updated_at', 'is_edited')

    def get_is_edited(self, obj):
        return obj.created_at != obj.updated_at
    
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'    
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user        