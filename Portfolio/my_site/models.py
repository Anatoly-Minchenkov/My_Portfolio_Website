from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)