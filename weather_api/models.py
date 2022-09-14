from cgitb import text
from django.db import models


class weather(models.Model):
    city_name=models.CharField(max_length=50)

    def __str__(self):
        return self.city_name