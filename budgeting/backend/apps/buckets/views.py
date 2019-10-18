from django.shortcuts import render
from rest_framework import generics


from apps.users.models import User
from apps.buckets.models import Expense, Profile, Budget

from .serializers import ExpenseSerializer


# List of generic views - https://www.django-rest-framework.org/api-guide/generic-views/#generic-views

# Create your views here.


class ExpenseList(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
