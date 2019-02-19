from django.contrib import admin

# Register your models here.

from .models import ccpr,emp

class ccprview(admin.ModelAdmin):
    list_display=['Name','CompanyName','EmployeeStrength','phone','Email','city']

admin.site.register(ccpr,ccprview)

class empview(admin.ModelAdmin):
    list_display = ['empname','password']

admin.site.register(emp,empview)