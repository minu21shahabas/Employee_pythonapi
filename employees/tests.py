from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee,User

class EmployeeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        
    def test_create_employee(self):
        url = reverse('employee-list-create')
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post(url, data, format='json')
        self.assetEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_duplicate_email(self):
        url = reverse('employee-list-create')
        Employee.objects.create(name='Jane Doe', email='jane@example.com')
        data = {'name': 'John Doe', 'email': 'jane@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_list_employees(self):
        url = reverse('employee-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_employee(self):
        employee = Employee.objects.create(name='Jane Doe', email='jane@example.com')
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_employee(self):
        employee = Employee.objects.create(name='Jane Doe', email='jane@example.com')
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
