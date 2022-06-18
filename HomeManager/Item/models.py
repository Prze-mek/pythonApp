from django.db import models


# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=256)
    status = models.BooleanField(default=False)


class Item(models.Model):
    name = models.CharField(max_length=256, default='')
    #activity = models.ForeignKey(Activity, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name





