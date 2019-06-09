from django.db import models


# class JobsConfig(models.Model):
class Job(models.Model):
    image = models.ImageField(upload_to='')
    summary = models.CharField(max_length=200)
