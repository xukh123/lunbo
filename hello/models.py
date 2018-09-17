from django.db import models

class Lunbo(models.Model):
    id=models.AutoField(primary_key=True,max_length=10)
    name=models.CharField(max_length=10)
    image=models.CharField(max_length=255,blank=True,null=True)
    title=models.CharField(max_length=255)

    class Meta:
        db_table='imgs'

# Create your models here.
