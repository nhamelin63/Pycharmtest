from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class news(models.Model):
    Titre = models.CharField(max_length=250)
    Auteur = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='Titre')
    subtitle = models.CharField(max_length=250)
    contenue = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Titre