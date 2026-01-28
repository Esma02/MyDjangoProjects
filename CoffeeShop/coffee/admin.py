from django.contrib import admin
from .models import Coffee,Dessert


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantitiy')

class DessertAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantitiy')

#admin panelinden yönetebileyim diye kaydettim
admin.site.register(Coffee, CoffeeAdmin)  
admin.site.register(Dessert, DessertAdmin)