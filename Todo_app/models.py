from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ToDo(models.Model):
    Title = models.CharField(max_length=100,null=False,blank=False)
    Description=models.TextField(max_length=1000,null=False,blank=False)
    Time_stamp=models.DateTimeField(auto_now=True,editable=False)
    Due_date=models.DateTimeField()
    STATUS_CHOICES = (
        ('open','open'),
        ('working', 'working'),
        ('done', 'done'),
        ('over_due', 'over_due'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    tags = models.CharField(max_length=255,default='task')


    def __str__(self):
        return self.Title