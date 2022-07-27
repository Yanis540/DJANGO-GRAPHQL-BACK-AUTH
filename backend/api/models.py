from django.db import models
from djongo.models.fields import ObjectIdField
# Create your models here.
class User(models.Model):
    _id=ObjectIdField(primary_key=True)
    name=models.CharField(max_length=256)
    email=models.CharField(max_length=256,unique=True)
    password=models.CharField(max_length=256)
    def __str__(self):
        return str(self._id)
    class Meta: 
        db_table='users'