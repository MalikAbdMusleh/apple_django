from django.db import models

# Create your models here.
class Apples(models.Model):
    name=models.CharField(max_length=100)
    info=models.CharField(max_length=100)
    rare_choice=(("High","H"),("Medium","M"),("Low","L"))
    rarity=models.CharField(choices=rare_choice,max_length=100)
    photo=models.ImageField(upload_to="photos/%y/%m/%d")
