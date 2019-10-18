from django.db import models
from apps.users.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    # https://www.thebalancesmb.com/what-is-a-pay-period-what-are-types-of-pay-periods-398392
    PAY_PERIOD = [
        ('Weekly', 'Weekly'),
        ('Bi-Weekly', 'Bi-Weekly'),
        ('Semi-Monthly', 'Semi-Monthly'),
        ('Monthly', 'Monthly'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    pay_period = models.CharField(max_length=15,
                                  choices=PAY_PERIOD,
                                  blank=True,
                                  null=True)
    income = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 blank=True,
                                 null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
