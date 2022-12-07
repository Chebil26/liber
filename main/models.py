from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
  title = models.CharField(max_length=255)
  author  = models.CharField(max_length=255)
  description = models.TextField()
  genres = (
        ("roman", "roman"),
        ("historique", "historique"),
        ("scientifique", "scientifique"),
    
        )
  genre  = models.CharField(
        max_length = 20,
        choices = genres,
        default = "scientifique"
        )
  publish_year = models.IntegerField()
  def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
  
  def get_absolute_url(self):
        return reverse("", kwargs={"id": self.id})
  
  
  
class Annonce(models.Model):
    
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    publisher = models.ForeignKey(User, default=None , on_delete=models.CASCADE , null=True)
    publish_date = models.DateTimeField(auto_now_add = True)
    price = models.FloatField()
    states = (
        ("Neuf jamais utilisé", "Neuf jamais utilisé"),
        ("Neuf", "Neuf"),
        ("Bon", "Bon"),
    
        )
    state = models.CharField(
        max_length = 20,
        choices = states,
        default = "neuf_jamais_utilise"
        )
    
    
    
    def get_absolute_url(self):
          return reverse("annonce_detail", kwargs={"id": self.id})
    
    def __str__(self):
      """String for representing the MyModelName object (in Admin site etc.)."""
      idd = self.id.__str__() 
      b = self.book.__str__() 
      p = self.publisher.__str__()
      sp = " "
      st =  b + sp + idd + sp + p
      return st
          
        

	
    
  
