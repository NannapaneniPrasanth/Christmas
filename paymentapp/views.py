from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponse
from .models import  Emp_Leaves,Emp_basic_update,Hr_Data,Finance_Login,Emp_account,Emp_Data,Company,Finance_Data,Hr_Login,Emp_Login
from.forms import Hr_LoginForm
# Create your views here.
def home(request):
    return render(request, 'home.html')
@login_required
def mylogin(request):
    if request.user.is_authenticated:
        qs = Company.objects.all()
        if request.user.is_hr:
            return render(request,'hr.html',{"qs":qs})
        elif request.user.is_finance:
            return render(request,'finance.html',{"qs":qs})
        elif request.user.is_emp:
            return render(request,'emp.html',{"qs":qs})
def hr_pwd_chg(request):
    ot="12345" #random.randint(100000,999999)
    #request.session["pwd"]=request.POST["t1"]
    request.session["details"]=request.POST
    request.session["otp"]=ot
    return render(request, "hr_otpvalid.html")
def hr_otpvalid(request):
    reeotp=request.POST["ot"]
    print(request.session["otp"])
    if request.session["otp"]==reeotp:
        data=request.session["details"]

        hd=Hr_Data(hrid=data['hrid'],fname=data['fname'],lname=data['lname'],
                   email=data['email'],mobno=data['mobno'],comapny_id=data['cmpid'])
        hd.save()
        hrlg=Hr_Login(hrid=data['hrid'],company_id=data['cmpid'],uname=data["uname"],pwd=data["pwd"])
        hrlg.save()
        return render(request,"hr_home.html")
    else:
        return render(request, "hr_update.html")

def hr_login(request):
    if request.method == "POST":
        MyLoginForm = Hr_LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un =MyLoginForm.cleaned_data['user']
            pw=MyLoginForm.cleaned_data['pwd']
            dbuser = Hr_Login.objects.filter(uname=un,pwd=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                for p in dbuser:
                    request.session["cmpid"] = p.company_id
                return render(request,'hr_dashbord.html')
    else:
        form = Hr_LoginForm()
        return render(request,'hr_login.html',
                      {'form': form})

def emp_pwd_chg(request):
    ot="12345" #random.randint(100000,999999)
    #request.session["pwd"]=request.POST["t1"]
    request.session["details"]=request.POST
    request.session["otp"]=ot
    return render(request, "emp_otpvalid.html")
def emp_otpvalid(request):
    reeotp=request.POST["ot"]
    print(request.session["otp"])
    if request.session["otp"]==reeotp:
        data=request.session["details"]

        hd=Emp_Data(empid=data['empid'],fname=data['fname'],lname=data['lname'],
                   email=data['email'],mobno=data['mobno'],company_id=data['cmpid'])
        hd.save()
        hrlg=Emp_Login(empid=data['empid'],company_id=data['cmpid'],uname=data["uname"],pwd=data["pwd"])
        hrlg.save()
        return render(request,"emp_home.html")
    else:
        return render(request, "emp_update.html")

def emp_login(request):
    if request.method == "POST":
        MyLoginForm = Hr_LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un =MyLoginForm.cleaned_data['user']
            pw=MyLoginForm.cleaned_data['pwd']
            dbuser = Emp_Login.objects.filter(uname=un,pwd=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                for p in dbuser:
                    request.session["empid"] = p.empid
                    request.session["cmpid"] = p.company_id
                return render(request,'emp_dashbord.html')
    else:
        form = Hr_LoginForm()
        return render(request,'emp_login.html',
                      {'form': form})


def accountupdate(request):
    if request.method=="GET":
        return render(request,'accountupdate.html')
    else:
        ea=Emp_account(acno=int(request.POST['accno']),
                       bankname=request.POST['bankname'],
                       ifsccode=request.POST['ifsccode'],
                       branchname=request.POST['branchname'],
                       empid=request.session['empid'],cmpid=request.session['cmpid'])
        ea.save()
        return render(request,'emp_dashbord.html')








def finance_pwd_chg(request):
    ot="12345" #random.randint(100000,999999)
    #request.session["pwd"]=request.POST["t1"]
    request.session["details"]=request.POST
    request.session["otp"]=ot
    return render(request, "finance_otpvalid.html")
def finance_otpvalid(request):
    reeotp=request.POST["ot"]
    print(request.session["otp"])
    if request.session["otp"]==reeotp:
        data=request.session["details"]

        hd=Finance_Data(acid=data['acid'],fname=data['fname'],lname=data['lname'],
                   email=data['email'],mobno=data['mobno'],
                        company_id=data['cmpid'])
        hd.save()
        hrlg = Finance_Login(acid=data['acid'], company_id=data['cmpid'], uname=data["uname"], pwd=data["pwd"])
        hrlg.save()
        return render(request,"finance_home.html")
    else:
        return render(request, "finance_update.html")
def finance_login(request):
    if request.method == "POST":
        MyLoginForm = Hr_LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un =MyLoginForm.cleaned_data['user']
            pw=MyLoginForm.cleaned_data['pwd']
            dbuser = Finance_Login.objects.filter(uname=un,pwd=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                rec=dbuser.get(uname=un)
                request.session["cmpid"]=rec.company_id
                return render(request,'finance_dashbord.html')
    else:
        form = Hr_LoginForm()
        return render(request,'finance_login.html',
                      {'form': form})

def empdetails(request):
    emps=Emp_account.objects.filter(cmpid=request.session['cmpid'])
    return render(request,"empdetails.html",{"emps":emps})

def activate(request):
   myacno= request.GET["acno"]
   Emp_account.objects.filter(acno=myacno).update(isactivated=True)
   emps = Emp_account.objects.filter(cmpid=request.session['cmpid'])
   return render(request, "empdetails.html", {"emps": emps})


def empactive(request):
    emps = Emp_account.objects.filter(cmpid=request.session['cmpid'],isactivated=True)
    return render(request, "empactive.html", {"emps": emps})
def empbasicupdate(request):
    emps = Emp_account.objects.filter(cmpid=request.session['cmpid'],isactivated=True)
    return render(request, "empbasicupdate.html", {"emps": emps})
def basicpay(request):
    if request.method=="GET":
        empid=request.GET["empid"]
        return render(request,'basicupdate.html',{'empiid':empid})
    else:
        empid1=request.POST['eid']
        bpay1=float(request.POST['bpay'])
        dbuser=Emp_Data.objects.filter(empid=empid1)
        rec=dbuser.get(empid=empid1)
        cid=rec.company_id
        e1=Emp_basic_update(empid=empid1,basicpay=bpay1,comapny_id=cid)
        e1.save()
        return render(request,'hr_dashbord.html')
def empleavesupdate(request):
    if request.method == "GET":
        empid = request.GET["empid"]
        return render(request,'leaves_update.html',{'empid':empid})
    else:
        empid1 = request.POST['eid']
        tnwd1 = int(request.POST['tnwd'])
        pl1 = int(request.POST['pl'])
        npl1 = int(request.POST['npl'])

        dbuser = Emp_Data.objects.filter(empid=empid1)
        rec = dbuser.get(empid=empid1)
        cid = rec.company_id
        e1 = Emp_Leaves(empid=empid1,total_no_of_leaves=tnwd1,paid_leaves=pl1,non_paid_leaves=npl1, comapny_id=cid,)
        e1.save()
        return render(request, 'hr_dashbord.html')
