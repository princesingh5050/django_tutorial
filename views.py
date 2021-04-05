from django.shortcuts import render
from myapp.models import Account
from myapp.models import student

# Create your views here.
def signup(request):
    resp=render(request,'signup.html')
    return resp

def forgotpass(request):
        if (request.method == 'GET'):
            return render(request, 'forgotpass.html')
        else:
            u = request.POST.get('user')
            e = request.POST.get('email')
            t = request.POST.get('type')
            if(t=='Teacher'):
                qs = Account.objects.filter(userid=u, email=e)
                count = qs.count()
                if (count > 0):
                    pswd = qs[0].password
                    return render(request, 'forgotpass.html', {'msg': 'password is:'+pswd})
                else:
                     return render(request, 'forgotpass.html', {'msg': 'Invalid userid or E-mail,Try again'})

            elif(t=='Student'):
                qs = student.objects.filter(studentid=u, student_email=e)
                count = qs.count()
                if (count > 0):
                    pswd = qs[0].student_password
                    return render(request, 'forgotpass.html', {'msg': 'password is :'+pswd})
                else:
                  return render(request,'forgotpass.html',{'msg':'Invalid userid or E-mail,Try again'})
            else:
               return render(request,'forgotpass.html',{'msg':'Invalid select Type'})
def newuser(request):
    resp=render(request,'newuser.html')
    return resp
def login(request):
    u = request.POST.get('user')
    p = request.POST.get('pass')
    e = request.POST.get('email')
    m = request.POST.get('mob')
    t= request.POST.get('type')
    acc = Account(userid=u, password=p, email=e, mobile=m,type=t)# here we create object of account_teacher class acc and pass value which is given by user
    try:
        acc.save()  # this save()methode save the details in account table in database.
        resp = render(request, 'register.html', {'msg': 'Add User Successfully...'})
        return resp
    except Exception as e:
        resp = render(request, 'register.html', {'msg': 'Something went wrong,please try with different userid'})
        return resp

def auth(request):
    u=request.POST.get('user')
    p=request.POST.get('pass')
    t=request.POST.get('type')

    if(t=='Teacher'):
        qs=Account.objects.filter(userid=u,password=p)
        count=qs.count()
        if(count>0):
            return render(request,'Teacher.html')
        else:
            return render(request,'signup.html',{'msg':'"User Id or Password is Invalid Try Again'})

    elif(t=='Student'):
        qs=student.objects.filter(studentid=u,student_password=p)
        count=qs.count()
        if(count>0):
            qs = student.objects.all()
            return render(request, 'student.html', {'accounts': qs})
        else:
            return render(request,'signup.html',{'msg':'User Id or password is Invalid Try Again'})
    else:
        return render(request,'signup.html',{'msg':'Please Select Type'})


def Teacher(request):
    u=request.POST.get('user')
    n=request.POST.get('name')
    f=request.POST.get('fname')
    p=request.POST.get('pass')
    e=request.POST.get('email')
    m=request.POST.get('mob')
    acc=student(studentid=u,student_password=p,student_email=e,student_mobile=m,student_name=n,student_fname=f)
    try:
        acc.save()  # this save()methode save the details in account table in database.
        resp = render(request, 'Teacher.html', {'msg': 'SingIN Successfully...'})
        return resp
    except Exception as e:
        resp = render(request, 'Teacher.html', {'msg': 'Something went wrong,please try with different userid'})
        return resp

def logout(request):
    return render(request,'logout.html')
def valid(request):
    u=request.POST.get('user')
    p=request.POST.get('pass')
    if(u=='admin'and p=='admin'):
        return render(request,'register.html')
    else:
        return render(request,'newuser.html',{'msg':'Invalid Admin'})
