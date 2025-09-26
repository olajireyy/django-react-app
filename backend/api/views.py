from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import Userserializer, Noteserializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = Noteserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)