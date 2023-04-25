from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Lists'

    def __str__(self):
        return self.name
