from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    img = models.ImageField(null=True, upload_to='people/')
    dep = models.CharField(max_length=80)
    univ = models.CharField(max_length=80)
    re_area = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name