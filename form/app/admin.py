from django.contrib import admin
from app.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['Sid','Sname','Sclass','Scourse']

class CourseAdmin(admin.ModelAdmin):
    list_display=['Cname','Cfee']

admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)