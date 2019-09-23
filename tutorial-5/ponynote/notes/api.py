from rest_framework import viewsets, permissions

from .models import Note
from .serizlizers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NoteSerializer

