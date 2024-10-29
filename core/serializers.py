from .models import Task


from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User=get_user_model()
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "email"]

class TaskSerializer(ModelSerializer):
    created_by= UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields=[ 'id','name', 'description', 'created_by', 'priority', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data["created_by"]= self.context["request"].user
        return super().create(validated_data)