# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserPasswordForm,UserProblemsForm,AdminPasswordForm,AdminUpdateForm,AdminPostImage,UserLoginForm
#PostrequestForm
from django.contrib import messages
from .models import problems,admin_update,galley,stock_details,register
#Postrequest
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.utils import timezone
from technician.models import notifications,reports
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from technician.models import technician
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.hashers import make_password,check_password
from django.db import connection

def my_login_required(function):
    def wrapper(request, *args, **kw): 
        if not request.session.get('id_no') and request.session.get('username'):
            return HttpResponseRedirect('/')
        elif not request.session.get('id_no'):
            return HttpResponseRedirect('/')    
        else:
            return function(request, *args, **kw)
    return wrapper
def ithome(request):
    updates = admin_update.objects.all().order_by('-date_posted')
    return render(request,"ithome.html",{'updates':updates})    
def about(request):
    return render(request, "about.html",{'title':'About'})
def contact(request):
    return render(request,"contact.html")
def ourteam(request):
    return render(request,"ourteam.html")
def reset_password(request):
    mail = request.POST.get("email")
    m = register.objects.all().filter(email=mail)
    if m:
        for l in m:
            import smtplib
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("sureshcheeti84@gmail.com", "ilovemother")
            message = "your password is "+l.password
            s.sendmail("sureshcheeti84@gmail.com", m, message) 
            s.quit()
            messages.success(request, 'you password is sent your mail please check it once.')    
    return render(request,"password_reset.html")
        
@login_required     
def enter_reports(request):
    repo = reports.objects.all()
    paginator = Paginator(repo,15)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        Reports = paginator.page(page)
    except (EmptyPage, InvalidPage):
        Reports = paginator.page(paginator.num_pages)
    return render(request,"allreports.html",{'Reports':Reports})    
@login_required     
def enter_stock(request):
    noti = stock_details.objects.all()
    paginator = Paginator(noti,15)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        stocks = paginator.page(page)
    except (EmptyPage, InvalidPage):
        stocks = paginator.page(paginator.num_pages)
    return render(request,"allstocks.html",{'stocks':stocks})           
def gally(request):
    post_img = galley.objects.all().order_by('-date_posted')
    return render(request,"gallery.html",{'post_img':post_img})
@login_required     
def post_img(request):
    if request.method == 'POST':
        form = AdminPostImage(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your successfully post the problem')
            return redirect('/galle')
    else:
        form = AdminPostImage()    
    return render(request,"post_image.html",{'form':form })       
#@my_login_required
#def post_request(request):
#      if request.method == 'POST':
#        form = PostrequestForm(request.POST)
#        if form.is_valid():
#            content = form.data.get('content')
#            if len(content)>=15:
#                data1 = student.objects.get(id_number=request.session['id_number'])
#                p = Postrequest.objects.create(idnumber=data1,content=content)
#                p.save()
#                messages.success(request, 'Your successfully post the request')
#                return redirect('/request')
#            else:
#                messages.warning(request, 'please enter the correct description minimum 15 characters')
#                return redirect('/request')         
#      else:
#        form = PostrequestForm()        
#      return render(request,'postrequest.html',{'form':form})        
    
@my_login_required
def post_problem(request):
    if request.method == 'POST':
        form = UserProblemsForm(request.POST)
        if form.is_valid():
            problem_type=form.data.get('problem_type').lower()
            description = form.data.get('description').lower()
            branch = form.data.get('branch').lower()
            class_room = form.data.get('class_room').lower()
            if (problem_type!="select" or branch!="select") and (problem_type!="select" and branch!="select"):
                if len(description)>=14 and (class_room[:3]=="ab2" or class_room[:3]=="ab1"):
                        data1 = register.objects.get(id_no=request.session['id_no'])
                        lk = problems.objects.filter(stu_id=data1)
                        data2 = register.objects.filter(id_no=request.session['id_no'])
                        if not lk:
                            p = problems.objects.create(stu=data1,problem=problem_type,description=description,branch=branch,class_room=class_room,slot=None,status="pending") 
                            p.save()
                            messages.success(request, 'Your successfully post the problem')
                            return redirect('/post')
                        else:
                            list1=[]
                            for item in lk:
                                list1.append(item)
                            flag=0    
                            #for i in range(len(list1)):
                            flag=1
                            for j in list1:  
                               if j.status=="success" and j.problem==problem_type:
                                    p = problems.objects.create(stu=data1,problem=problem_type,description=description,branch=branch,class_room=class_room,slot=None,status="pending") 
                                    p.save()
                                    messages.success(request, 'Your successfully post the problem')
                                    return redirect('/post')
                                    flag=0
                                    break
                               elif j.problem == problem_type and j.status!="success":
                                    messages.warning(request, 'You already post this problem')
                                    return redirect('/post')
                                    flag=0
                                    break
                               else:
                                    flag=1     
                            
                            if flag==1:
                                p = problems.objects.create(stu=data1,problem=problem_type,description=description,branch=branch,class_room=class_room,slot=None,status="pending") 
                                p.save()
                                messages.success(request, 'Your successfully post the problem')
                                return redirect('/post')                 
                else:
                    messages.warning(request, 'please enter the correct description or class room')
                    return redirect('/post')        
            else:
                messages.warning(request, 'please select the fields')
                return redirect('/post')
                
    else:
        form = UserProblemsForm()        
    return render(request,'problems.html',{'form':form})
@my_login_required
def notification(request):
        noti = notifications.objects.all().order_by('-date_posted')
        paginator = Paginator(noti,15)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            notify = paginator.page(page)
        except (EmptyPage, InvalidPage):
            notify = paginator.page(paginator.num_pages)
        return render(request,"notifications.html",{'notify':notify})
@login_required
def all_students(request):
    stu1 = register.objects.all()
    paginator = Paginator(stu1,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        students = paginator.page(page)
    except (EmptyPage, InvalidPage):
        students = paginator.page(paginator.num_pages)
    return render(request,"allstudents.html",{'students':students})

@login_required
def delete_student(request,pk):
    stu1 = register.objects.get(id=pk)
    stu1.delete()
    messages.success(request, 'Your successfully deleted the user.')
    return redirect('/allstudents')
@login_required
def all_views(request,problem_id):
    stu1 = problems.objects.all()
    suc = request.POST.get('success')
    print(suc)
    approve=0
    reject=0
    pending=0
    for c in stu1:
        if c.stu_id == int(problem_id):
            if c.status == "success":
                approve+=1
            elif c.status == "reject":
                reject+=1
            elif c.status == "pending":
                pending+=1                  
    return render(request,"view_all.html",{'stu1':stu1,'approve':approve,'reject':reject,'pending':pending,'all':approve+pending+reject})                            
@my_login_required    
def histroy(request):
    prob = problems.objects.all().order_by('-date_posted')
    paginator = Paginator(prob,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        problem = paginator.page(page)
    except (EmptyPage, InvalidPage):
        problem = paginator.page(paginator.num_pages)
    return render(request,"history.html",{'problem':problem})    
@my_login_required    
def changepassword(request):
    if request.method == 'POST':
        form = UserPasswordForm(request.POST)
        if form.is_valid():
            password = form.data.get("password").lower()
            confirm = form.data.get("confirm_password").lower()
            if password == confirm:
                data1 = register.objects.filter(id_no=request.session['id_no']).update(password=make_password(password))
                messages.success(request, 'Your successfully change your password')
            else:
                messages.warning(request, 'passwords are mismatch')
                return redirect('/change')
                    
    else:
        form = UserPasswordForm()        
    return render(request,'changepassword.html',{'form':form }) 
      
def slogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
             id_no = form.data.get("id_no").lower()
             password = form.data.get("password")
             data1 = register.objects.filter(id_no=id_no).values('id_no','password')
             if data1:
                 for c in data1:
                        #print course['id_number'],course['password'
                    if c['id_no']==id_no and check_password(password,c['password']):
                        request.session['id_no']=id_no
                        return HttpResponseRedirect(reverse('home'))
                    elif c['id_no']==id_no and password==c['password']:
                        request.session['id_no']=id_no
                        return HttpResponseRedirect(reverse('home'))    
                        #messages.success(request, 'Your successfully login',)
                    else:
                        messages.warning(request,'invalid credentials')
                        return redirect('/slogin')  
             else:
                messages.warning(request,'please complete your registration')
                return redirect('/reg')
    else:
        form = UserLoginForm()    
    return render(request,"slogin.html",{'form': form})     
def slogout(request):
    request.session['id_no']=None
    return redirect('/')
def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            id_no = form.data.get("id_no").lower()
            email = form.data.get("email").lower()
            mobile = form.data.get("mobile")
            password = form.data.get("password").lower()
            hashed_pwd=make_password(password)
            data2 = register.objects.all()
            flag=1
            for j in data2:
                if j.id_no==id_no or j.email==email:
                    flag=0
                    break
            if flag==0:
                    messages.warning(request, 'id number or email already exists')
                    return redirect('/reg')    
            else:       
                if len(id_no)==7 and (id_no[0]=='r' or id_no[0]=='b') and len(mobile)==10:
                    t = register.objects.create(id_no=id_no,email=email,mobile=mobile,password=hashed_pwd)
                    t.save()
                    messages.success(request, 'Your successfully registered')
                    return redirect('/reg')
                else:
                    messages.warning(request, 'invalid mobile or id number')
                    return redirect('/reg')    
            
    else:
        form = UserRegisterForm()
    return render(request,"student_register.html",{'form':form})             
@login_required
def adminchangepassword(request):
    if request.method == 'POST':
        form = AdminPasswordForm(request.POST)
        if form.is_valid():
            password = form.data.get("password")
            confirm = form.data.get("confirm_password")
            if password == confirm:
                data1 = User.objects.get(username='admin123')
                data1.set_password(password)
                data1.save()
                messages.success(request, 'Your successfully change your password')
            else:
                messages.warning(request, 'passwords are mismatch')
                return redirect('/adminchange')
                    
    else:
        form = AdminPasswordForm()        
    return render(request,'changepassword.html',{'form':form })
@login_required
def tech_status(request):
    tech1 = technician.objects.all()
    return render(request,"techstatus.html",{'tech1':tech1 })
@login_required
def search(request):
    problem = problems.objects.all().order_by('-date_posted') 
    if request.method == 'POST':
        value = request.POST['search'].strip().lower()
        if value == "":
            problem = problems.objects.all().order_by('-date_posted')
        elif value == "ab1":
            problem = problems.objects.filter(class_room__startswith="ab1")
        elif value == "ab2":
            problem = problems.objects.filter(class_room__startswith="ab2")
        elif value == "r14":
            problem = problems.objects.filter(stu__id_no__startswith="r14")
        elif value == "r15":
            problem = problems.objects.filter(stu__id_no__startswith="r15")
        elif value == "r16":
            problem = problems.objects.filter(stu__id_no__startswith="r16")
        elif value == "r17":
            problem = problems.objects.filter(stu__id_no__startswith="r17")
        elif value == "r18":
            problem = problems.objects.filter(problem__startswith="r18")
        elif value == "e4":
            problem = problems.objects.filter(branch__startswith="e4")
        elif value == "e3":
            problem = problems.objects.filter(branch__startswith="e3")
        elif value == "e2":
            problem = problems.objects.filter(branch__startswith="e2")
        elif value == "e1":
            problem = problems.objects.filter(branch__startswith="e1")
        elif value == "puc1":
            problem = problems.objects.filter(branch__startswith="puc1")
        elif value == "puc2":
            problem = problems.objects.filter(branch__startswith="puc2")                        
        elif value == "lan":
            problem = problems.objects.filter(problem__startswith="lan")
        elif value == "os":
            problem = problems.objects.filter(problem__startswith="os")
        elif value == "adapter":
            problem = problems.objects.filter(problem__startswith="adapter")
        elif value == "screen":
            problem = problems.objects.filter(problem__startswith="screen")                
        else:
             return render(request,"allproblems.html",{'message':"No Results Found"})                            
        return render(request,"allproblems.html",{'problem':problem,'message':"No Results Found"})    
    else:        
        return render(request,"allproblems.html",{'problem':problem})        
            
#@login_required
#def show_requests(request):
#     req = Postrequest.objects.all()
#     return render(request,"showrequests.html",{'req':req})   
@login_required
def adminupdate(request):
     if request.method == 'POST':
        form = AdminUpdateForm(request.POST)
        if form.is_valid():
            problem_type = form.data.get("problem_type")
            content = form.data.get("content")
            data1 = admin_update.objects.create(problem_type=problem_type,content=content)
            data1.save()
            messages.success(request, 'Your successfully submit the update')
            return redirect('/adminup')
                    
     else:
        form = AdminUpdateForm()        
     return render(request,'adminupdate.html',{'form':form }) 
                
@login_required
def pendingproblem(request):
    problem = problems.objects.all().order_by('-date_posted')
    if request.method == 'POST':
        value = request.POST['search'].strip().lower()
        if value == "":
            problem = problems.objects.all().order_by('-date_posted')
        elif value == "ab1":
            problem = problems.objects.filter(class_room__startswith="ab1")
        elif value == "ab2":
            problem = problems.objects.filter(class_room__startswith="ab2")
        elif value == "r14":
            problem = problems.objects.filter(stu__id_no__startswith="r14")
        elif value == "r15":
            problem = problems.objects.filter(stu__id_no__startswith="r15")
        elif value == "r16":
            problem = problems.objects.filter(stu__id_no__startswith="r16")
        elif value == "r17":
            problem = problems.objects.filter(stu__id_no__startswith="r17")
        elif value == "r18":
            problem = problems.objects.filter(problem__startswith="r18")
        elif value == "e4":
            problem = problems.objects.filter(branch__startswith="e4")
        elif value == "e3":
            problem = problems.objects.filter(branch__startswith="e3")
        elif value == "e2":
            problem = problems.objects.filter(branch__startswith="e2")
        elif value == "e1":
            problem = problems.objects.filter(branch__startswith="e1")
        elif value == "puc1":
            problem = problems.objects.filter(branch__startswith="puc1")
        elif value == "puc2":
            problem = problems.objects.filter(branch__startswith="puc2")                        
        elif value == "lan":
            problem = problems.objects.filter(problem__startswith="lan")
        elif value == "os":
            problem = problems.objects.filter(problem__startswith="os")
        elif value == "adapter":
            problem = problems.objects.filter(problem__startswith="adapter")
        elif value == "screen":
            problem = problems.objects.filter(problem__startswith="screen")                
        else:
             return render(request,"pendingproblem.html",{'message':"No Results Found"})                       
        return render(request,"pendingproblem.html",{'problem':problem,'message':"No Results Found"})    
    else:        
        return render(request,"pendingproblem.html",{'problem':problem})
