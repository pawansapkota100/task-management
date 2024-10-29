from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task
from rest_framework import status
from django.urls import reverse
import json

User = get_user_model()


class TaskManagementTest(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(email="user1@gmail.com", password="user123")
        self.client.login(email="user1@gmail.com", password="user123")

        self.task= Task.objects.create(name="task1", description="task1 description", created_by=self.user)
        self.url = reverse('task-detail', kwargs={'pk': self.task.pk})


    def test_list_task(self):
        response=self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data={
            "name":"testing task",
            "description": "this is testing description",
            "priority": "L",
            "status": "P"
            }
        
        response=self.client.post(reverse("task-list"),data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(),2)
        self.assertEqual(Task.objects.last().name, data["name"])
    
    def test_update_task(self):
        data = {
            "name": "Updated Task"
        }

        response = self.client.patch(reverse('task-detail', kwargs={'pk': self.task.pk}), data=data, format='json',content_type='application/json' )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])
    
    def list_task_without_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def create_task_without_authentication(self):
        self.client.logout()
        data={
            "name":"testing task",
            "description": "this is testing description",
            "priority": "L",
            "status": "P"
            }
        response=self.client.post(reverse("task-list"),data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def check_action_complete(self):
        response= self.client.post(reverse('task-complete', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_task_created_by_other_user(self):
        User.objects.create_user(email="user2@gmail.com", password="user123")
        self.client.login(email="user2@gmail.com", password="user123")
        data = {
            "name": "Updated Task"
        }
        response = self.client.patch(reverse('task-detail', kwargs={'pk': self.task.pk}), data=data, format='json',content_type='application/json' )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    
    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_task_created_by_other_user(self):
        user2 = User.objects.create_user(email="user2@gmail.com", password="user123")
        self.client.login(email="user2@gmail.com", password="user123")
        response = self.client.delete(reverse('task-detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    

