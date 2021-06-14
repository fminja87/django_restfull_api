from django.db import models

# Create your models here.


class PhoneModelClass(models.Model):
    phone_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model_number = models.IntegerField()
    storage = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    camera_front = models.CharField(max_length=50)
    camera_back = models.CharField(max_length=50)
    os_name = models.CharField(max_length=100)

    def __str__(self):
        return self.phone_name
