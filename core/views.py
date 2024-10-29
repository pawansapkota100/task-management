from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['priority', 'status']
    search_fields=['name']

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
    
    def perform_destroy(self, instance):
        self.check_object_permissions(self.request, instance)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task= self.get_object()
        task.status= 'C'
        task.save()
        seriallizer = TaskSerializer(task)
        return Response(data=seriallizer.data,status=status.HTTP_200_OK)
