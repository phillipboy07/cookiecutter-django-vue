from django.db import models
from django.contrib.auth.models import User

from .Expense import Expense
from .Profile import Profile

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Budget(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='profile_budget',
                                blank=True,
                                null=True)
