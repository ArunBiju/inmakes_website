from django.db import models

# Create your models here.
class home_page_db_1(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')
    details = models.TextField()

    def __str__(self):
        return self.name
    

class home_page_db_2(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')
    details = models.TextField()

    def __str__(self):
        return self.name