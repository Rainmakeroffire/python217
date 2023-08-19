from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)

    def __str__(self):
        return self.title
