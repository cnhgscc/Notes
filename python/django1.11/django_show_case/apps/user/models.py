from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女"),
    )

    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机")
    gender = models.CharField(max_length=6, choices=[], default="female", verbose_name="性别")
