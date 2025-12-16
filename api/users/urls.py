from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users'),
    path('users/<uuid:pk>/', UserRetrieveUpdateView.as_view(), name='update-user'),
]
