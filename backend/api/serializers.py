from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']    
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class Noteserializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'author', 'title', 'content', 'created_at']
        extra_kwargs = {'author': {'read_only': True}}