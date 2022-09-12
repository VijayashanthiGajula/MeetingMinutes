from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Action(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=255,null=True, blank=True)
    Description=models.TextField(null=True,blank=True)
    Responsible=models.TextField(null=True,blank=True)
    DueDate=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete',]

    
    