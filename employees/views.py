from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import LimitOffsetPagination


class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['department', 'role']
    ordering_fields = ['date_joined']
    ordering = ['-date_joined']
    pagination_class = LimitOffsetPagination

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=HTTP_204_NO_CONTENT)
