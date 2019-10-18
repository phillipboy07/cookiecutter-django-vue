from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from .Budget import *
from .Profile import *

# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    value = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                blank=True,
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='profile_expense',
                                blank=True,
                                null=True)

    def __str__(self):
        return self.name
