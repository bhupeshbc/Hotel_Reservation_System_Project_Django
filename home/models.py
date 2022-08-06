from django.db import models


# Create your models here.


class Chambre(models.Model):
    nom = models.CharField(max_length=20)
    prix = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='media/pics')
    disponibilité = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
class Catalogue(models.Model):
    image = models.ImageField(upload_to='pics')
class Testimonial(models.Model):
    nom = models.CharField(max_length=20)
    avis = models.TextField()
    image = models.ImageField(upload_to='media/pics')
    def __str__(self):
        return self.nom
class Reservation(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField(default=0)
    Email = models.EmailField(max_length=40)
    Date_Check_In = models.DateField(auto_now=False)
    Date_Check_Out  = models.DateField(auto_now=False)
    Adulte = models.IntegerField (default=0)
    Children = models.IntegerField(default=0)
    Note = models.TextField()
    def __str__(self):
        return self.Name
