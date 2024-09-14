from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import User
from rest_framework import generics
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer


# List or create clients
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Retrieve, update, or delete a client
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



# Create a project for a client and assign users
class ProjectCreateView(APIView):
    def post(self, request, client_id):
        client = Client.objects.get(id=client_id)
        users = request.data.get('users')
        project = Project.objects.create(
            project_name=request.data.get('project_name'),
            client=client,
            created_by=request.user
        )
        project.users.set(users)
        project.save()

        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

# List projects for the logged-in user
class UserProjectsListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.request.user.projects.all()