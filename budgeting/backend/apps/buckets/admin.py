from django.contrib import admin
from apps.users.models import User
from apps.buckets.models import Expense, Profile, Budget

# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


# Register the admin class with the associated model
admin.site.register(Expense, ExpenseAdmin)

admin.site.register(Budget)
admin.site.register(Profile)
