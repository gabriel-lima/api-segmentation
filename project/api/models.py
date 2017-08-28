from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.SmallIntegerField()
    state = models.CharField(max_length=2)
    position = models.CharField(max_length=255)


class Segmentation(models.Model):
    query = models.TextField(max_length=255)
