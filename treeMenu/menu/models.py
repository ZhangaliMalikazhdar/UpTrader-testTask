from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)


class List(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
