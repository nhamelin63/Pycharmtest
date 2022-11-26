from django.contrib import admin
from .models import news
# Register your models here.

class newsAdmin(admin.ModelAdmin):

    list_display = ('Titre', 'Auteur', 'pub_date')
    search_fields = ('Titre', 'Auteur', 'pub_date')
    list_filter = ('Titre', 'Auteur', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)

admin.site.register(news, newsAdmin)