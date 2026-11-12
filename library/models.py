from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()




class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/', null=True, blank=True)

class Orders(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    order_data = models.DateField()
    muhlati_kitoba_ovardan = models.DateField(null=True, blank=True)