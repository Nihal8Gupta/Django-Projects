from django.contrib import admin
from .models import *
# Register your models here.
class CapitalAdmin(admin.ModelAdmin):
    list_display=['id','Capital_name']
    
admin.site.register(Capital,CapitalAdmin)
admin.site.register(Country)
admin.site.register(DEPT)
admin.site.register(EMP)



