# from django.db import models
from django.contrib.auth.models import User
from accounts.models import Enterprise

from djongo import models
from bson import ObjectId


# Create your models here.
class Journal(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    last_updated = models.DateField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return F"{self.title} | {self.user}"

class Comment(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    last_updated = models.DateField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return F"{self.journal} | {self.user}"