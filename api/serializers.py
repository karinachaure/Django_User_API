from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Assuming 'username' represents the user's name in the User model

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name', read_only=True)  # Fetch client name
    users = UserSerializer(many=True, read_only=True)  # Fetch user details
    created_by = serializers.CharField(source='created_by.username', read_only=True)  # Assuming 'created_by' is a ForeignKey to User
    
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
    
    def create(self, validated_data):
        # Handle the creation of a project and assigning users
        users_data = self.context['request'].data.get('users')
        project = Project.objects.create(**validated_data)
        
        for user_data in users_data:
            user = User.objects.get(id=user_data['id'])
            project.users.add(user)  # Add users to the project
        
        return project