from django.contrib import admin
from . models import items

class itemsAdmin(admin.ModelAdmin):
    list_display=['item_name','image','link','price','off_price','off_p','publish','created','updated','site','company','item']
    list_filter=('item_name','price','created','site','company','item')
    search_fields=('item_name','company','item','site')


# Register your models here.
admin.site.register(items,itemsAdmin)
