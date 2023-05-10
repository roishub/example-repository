from django.test import TestCase, Client
from django.urls import reverse
from .models import Task

class TaskListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.task1 = Task.objects.create(name='Task 1')
        self.task2 = Task.objects.create(name='Task 2', completed=True)

    def test_task_list(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
