from django.contrib import admin
from .models import User,Hr,Finance,Emp,Company

class Useradmin(admin.ModelAdmin):
    list_display = ['username','is_hr', 'is_finance', 'is_emp']
    class meta:
        model = User

class Companyadmin(admin.ModelAdmin):
    list_display = ['cmpid', 'cmpname', 'cmpadd', 'loc']
    list_filter = ['loc']
    class meta:
        model=Company
admin.site.register(User,Useradmin)
admin.site.register(Company,Companyadmin)