from django.db import models
# from django.contrib.auth.models import User

class Step(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=4)
    text = models.TextField()
    completed = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name + ' - ' + self.number

class Page(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title