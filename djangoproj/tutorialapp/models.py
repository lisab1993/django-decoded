from django.db import models

class Step(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=4)
    text = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name