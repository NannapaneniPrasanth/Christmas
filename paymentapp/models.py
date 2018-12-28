from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    is_hr = models.BooleanField(default=False)
    is_finance = models.BooleanField(default=False)
    is_emp = models.BooleanField(default=False)

class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
class Finance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
class Emp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
class Company(models.Model):
    cmpid=models.CharField(primary_key=True,max_length=5)
    cmpname=models.CharField(max_length=20)
    cmptype=models.CharField(max_length=10)
    cmpadd=models.CharField(max_length=50)
    loc=models.CharField(max_length=10)
class Hr_Data(models.Model):
    hrid=models.CharField(max_length=6,primary_key=True)
    comapny=models.ForeignKey(Company,on_delete=models.CASCADE)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    mobno=models.CharField(max_length=15)
class Emp_Data(models.Model):
    empid=models.CharField(max_length=7,primary_key=True)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    mobno = models.CharField(max_length=15)
    add = models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
class Finance_Data(models.Model):
    acid=models.CharField(max_length=7,primary_key=True)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    mobno = models.CharField(max_length=15)
    add = models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

class Hr_Login(models.Model):
    uname = models.CharField(max_length=20, primary_key=True)
    pwd = models.CharField(max_length=10)
    hrid=models.CharField(max_length=8)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
class Emp_Login(models.Model):
    uname = models.CharField(max_length=20, primary_key=True)
    pwd = models.CharField(max_length=10)
    empid=models.CharField(max_length=8)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
class Emp_account(models.Model):
    acno=models.IntegerField(primary_key=True)
    bankname=models.CharField(max_length=20)
    ifsccode=models.CharField(max_length=11)
    branchname=models.CharField(max_length=15)
    empid=models.CharField(max_length=7)
    cmpid=models.CharField(max_length=5)
    isactivated=models.BooleanField(default=False)
class Finance_Login(models.Model):
    uname = models.CharField(max_length=20, primary_key=True)
    pwd = models.CharField(max_length=10)
    acid=models.CharField(max_length=8)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
class Emp_basic_update(models.Model):
    empid=models.CharField(max_length=8,primary_key=True)
    basicpay=models.DecimalField(max_digits=10,decimal_places=2)
    comapny = models.ForeignKey(Company, on_delete=models.CASCADE)
class Emp_Leaves(models.Model):
    empid = models.CharField(max_length=8, primary_key=True)
    comapny = models.ForeignKey(Company, on_delete=models.CASCADE)
    total_no_of_work_days=models.IntegerField(2)
    paid_leaves=models.IntegerField(2)
    non_paid_leaves=models.IntegerField(2)
class Emp_pal_slip(models.Model):
    empid = models.CharField(max_length=8, primary_key=True)
    comapny = models.ForeignKey(Company, on_delete=models.CASCADE)
    empname=models.CharField(max_length=20)
    basicpay = models.DecimalField(max_digits=8, decimal_places=2)
    da=models.DecimalField(max_digits=8,decimal_places=2)
    hra=models.DecimalField(max_digits=8,decimal_places=2)
    pf=models.DecimalField(max_digits=8,decimal_places=2)
    tax=models.DecimalField(max_digits=8,decimal_places=2)
    tsal=models.DecimalField(max_digits=8,decimal_places=2)



