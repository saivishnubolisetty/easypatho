from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import ccpr,sup,register,emp

# Create your views here.

def Index(request):
    return render(request,'index.html',{})


def addinfo(request):
        if request.method == "POST":
            cust = ccpr()
            cust.Name = request.POST.get("namecorp")
            cust.CompanyName = request.POST.get("cncorp")
            cust.EmployeeStrength = request.POST.get("escorp")
            cust.phone=request.POST.get("phonecorp")
            cust.Email=request.POST.get("emailcorp")
            cust.city=request.POST.get("citycorp")
            cust.message=request.POST.get("messagecorp")
            cust.save()


            return render(request,'thankyou.html', {})
        else:
            return render(request,'corporate.html', {})



def workculture(request):
    return render(request,'workculture.html',{})

def currentopenings(request):
    return render(request,'currentopenings.html',{})

def signin(request):
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            #s=sin()
            un=request.POST.get("siname")
            ps=request.POST.get("sipass")
            users=sup.objects.all()
            #return render(request,'test.html',{"u":users,"u1":un,"p":ps})

            for u in users:
                if str(un).strip()==str(u.username).strip() and str(ps).strip()==str(u.Password).strip():
                    return render(request,"customerhome.html",{})
            else:
                    return render(request, "signin.html", {})

        elif request.POST.get("form_type") == 'formTwo':
            p=sup()
            p.uid=request.POST.get("suid")
            p.username=request.POST.get("suname")
            p.Password=request.POST.get("spass")
            p.save()

            return render(request, "signin.html", {})
        else:
            return render(request, "signin.html", {})

    else:
        return render(request,'signin.html',{})




def cardiology(request):
    return render(request,'cardiology.html',{})

def radiology(request):
    return render(request,'radiology.html',{})

def laboratory(request):
    return render(request,'laboratory.html',{})

def tmt(request):
    return render(request,'tmt.html',{})

def echo(request):
    return render(request,'echo.html',{})

def ecg(request):
    return render(request,'ecg.html',{})

def dst(request):
    return render(request,'dualct.html',{})

def osix(request):
    return render(request,'16channel.html',{})
def us(request):
    return render(request,'ultrasound.html',{})

def dxr(request):
    return render(request,'digital.html',{})

def dma(request):
    return render(request, 'digitalma.html', {})

def dexa(request):
    return render(request, 'dexa.html', {})

def cb (request):
    return render(request, 'clinical.html', {})

def pac(request):
    return render(request, 'pathology.html', {})

def ser(request):
    return render(request, 'serology.html', {})

def haem(request):
    return render(request, 'haematology.html', {})

def md(request):
    return render(request, 'molecular.html', {})

def hisp(request):
    return render(request, 'histopathology.html', {})

def hpp(request):
    return render(request, 'healthpackages.html', {})

def employee(request):
    if request.method == 'POST':
            #s=sin()
            un=request.POST.get("user")
            ps=request.POST.get("password")
            users=emp.objects.all()
            item=register.objects.all()
            for u in users:
                if str(un).strip()==str(u.empname).strip() and str(ps).strip()==str(u.password).strip():
                    return render(request,"emphome.html",{"plist":item})
            else:
                return render(request, 'employee.html', {})
    else:
        return render(request, 'employee.html', {})



def reginfo(request):
        if request.method == "POST":
            c = register()
            c.name= request.POST.get("rname")
            c.pack=request.POST.get("rpack")
            c.service=request.POST.get("rservice")
            c.test=request.POST.get("rtest")
            c.mail = request.POST.get("rmail")
            c.std=request.POST.get("rstd")
            c.phone = request.POST.get("rphone")
            c.month = request.POST.get("rmonth")
            c.day=request.POST.get("rday")
            c.year=request.POST.get("ryear")
            c.gender=request.POST.get("rgender")
            c.date=request.POST.get("rdate")
            c.time=request.POST.get("rtime")
            c.country=request.POST.get("rcountry")
            c.save()



            return render(request,'thankyou.html', {})
        else:
            return render(request, 'signup.html', {})


def overview(request):
    return render(request, 'CorrectFile.html', {})


def vav(request):
    return render(request, 'CF2.html', {})

def qpo(request):
    return render(request, '3rdpage.html', {})

def eb(request):
    return render(request, '4thpage.html', {})

def sf(request):
    return render(request, 'SUPPORT & FACILITY.html', {})

def tt(request):
    return render(request, 'TechnicalTeam.html', {})








