# from django.db import models
from django.contrib.auth.models import User
from djongo import models
from bson import ObjectId


# Create your models here.
ROLE_CHOICES = (
    ('administrator', 'Administrator'),
    ('student', 'Student'),
    ('enterprise_manager', 'Enterprise Manager'),
)

class Data_user(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=200)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def is_administrator(self):
        return self.role == 'administrator'
    def is_student(self):
        return self.role == 'student'
    def is_enterprise_manager(self):
        return self.role == 'enterprise_manager'

    def __str__(self):
        return self.full_name

class Enterprise(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    full_name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    telephone = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.full_name

class Internship(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    academic_year = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return F"{self.academic_year} | {self.user}【{self.enterprise}】"