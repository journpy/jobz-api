from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.permissions import IsSuperUserOrReadOnly
from .serializers import UserSerializer


UserModel = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    """Get all users or create a user."""
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """Get or update details of a user."""
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    


