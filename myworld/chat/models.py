from django.db import models


class Logins(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

