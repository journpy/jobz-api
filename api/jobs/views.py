from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS
from api.permissions import IsSuperUserOrReadOnly
from jobs.models.models import Job
from .serializers import JobSerializer


class JobListCreateView(ListCreateAPIView):
    """Get all jobs and create a job"""
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]
    queryset = Job.objects.all()
    serializer_class = JobSerializer
