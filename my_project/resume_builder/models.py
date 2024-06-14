from django.db import models
from django.contrib.auth.models import User

class ResumeBuilder(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100, default='Enter Name')
    title = models.CharField(max_length=75, default='None')
    email = models.EmailField(default='durga@gmail.com')
    address = models.CharField(max_length=255, default='Hyderabad, Telangana')
    number = models.IntegerField(default=1234567890)
    linkedin = models.URLField(default='http://www.linkedin.com/default',null=True)
    github = models.URLField(default='gihub',null=True,blank=True)

    def __str__(self):
        return self.title
