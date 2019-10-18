from rest_framework import serializers
from apps.buckets.models import Expense, Profile, Budget


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'value',
            'created_at',
        )
        model = Expense
