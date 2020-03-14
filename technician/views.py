# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserUpdateForm,UserPasswordForm,UserSlotForm,AdminForm,StackForm,AdminReportForm
from django.contrib import messages
from .models import technician,notifications,admin_notify,reports
from student.models import problems,stock_details
from django.http import HttpResponseRedirect
from django.urls import reverse
from technician.models import technician
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import re

def my_login_required(function):
    def wrapper(request, *args, **kw): 
        if not request.session.get('username') and request.session.get('id_no'):
            return HttpResponseRedirect('/')
        elif not request.session.get('username'):
            return HttpResponseRedirect('/')    
        else:
            return function(request, *args, **kw)
    return wrapper
@my_login_required
def admin_reports(request):
    if request.method == 'POST':
        form = AdminReportForm(request.POST)
        if form.is_valid():
            no_of_students = form.data.get('no_of_students').lower()
            class_room = form.data.get('class_room').lower()
            dept = form.data.get('dept').lower()
            block = form.data.get('block').lower()
            amplifier = form.data.get('amplifier').lower()
            speakers = form.data.get('speakers').lower()
            audio_port = form.data.get('audio_port').lower()
            audio_cable  = form.data.get('audio_cable').lower()
            projector = form.data.get('projector').lower()
            screen = form.data.get('screen').lower()
            video_cable = form.data.get('video_cable').lower()
            vga_port = form.data.get('vga_port').lower()
            io_port_not_working_positions = form.data.get('io_port_not_working_positions').lower()
            how_many_lan_cables_not_working = form.data.get('how_many_lan_cables_not_working').lower()
            issued_lan_cables = form.data.get('issued_lan_cables').lower()
            class_room_ip = form.data.get('class_room_ip').lower()
            switch = form.data.get('switch').lower()
            rack = form.data.get('rack').lower()
            adapters_not_working = form.data.get('adapters_not_working').lower()
            adapters_working = form.data.get('adapters_working').lower()
            screen_damage = form.data.get('screen_damage').lower()
            d_link_modem = form.data.get('d_link_modem').lower()
            jio_modem = form.data.get('jio_modem').lower()
            bio_metric_essl_not_registered = form.data.get('bio_metric_essl_not_registered').lower()
            bio_metric_aadhar_not_registered = form.data.get('bio_metric_aadhar_not_registered').lower()
            bio_metric_problems_if_any = form.data.get('bio_metric_problems_if_any').lower()
            data2 = reports.objects.all()
            flag=1
            for j in data2:
                if j.class_room==class_room:
                    flag=0
                    break
            if flag==0:
                    messages.warning(request, 'you are alredy add this record ')
                    return redirect('/add_reports')    
            else: 
                pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
                test = pat.match(class_room_ip)
                if test:
                    t = reports.objects.create(no_of_students=no_of_students,class_room=class_room,dept=dept,block=block,amplifier=amplifier,speakers=speakers,audio_port=audio_port,
                    audio_cable=audio_cable,projector=projector,screen=screen,video_cable=video_cable,vga_port=vga_port,io_port_not_working_positions=io_port_not_working_positions
                    ,how_many_lan_cables_not_working=how_many_lan_cables_not_working,issued_lan_cables=issued_lan_cables,class_room_ip=class_room_ip,
                    switch=switch,rack=rack,adapters_not_working=adapters_not_working,adapters_working=adapters_working,screen_damage=screen_damage,
                    d_link_modem=d_link_modem,jio_modem=jio_modem,bio_metric_essl_not_registered=bio_metric_essl_not_registered,
                    bio_metric_aadhar_not_registered=bio_metric_aadhar_not_registered,bio_metric_problems_if_any=bio_metric_problems_if_any
                    )
                    t.save()
                    messages.success(request, 'Your successfully added the report')
                    return redirect('/add_reports')
                else:
                    messages.warning(request, 'invalid ip address')
                    return redirect('/add_reports')    
    else:
        form = AdminReportForm()
    return render(request,"add_reports.html",{'form':form })
            
@login_required
def adminnotify(request,pk):
    if request.method == 'POST':
        site_profile = problems.objects.get(id=pk)
        form1 = AdminForm(request.POST,instance=site_profile)
        if form1.is_valid():
            tech1 = form1.data.get('tech')
            notify = form1.data.get('notify')
            if len(notify)>=15:
                p = problems.objects.filter(id=pk)
                flag=1
                for i in p:
                    if i.id == int(pk):
                        flag=0
                        break
                if flag==1:
                    s = ""
                    for i in p:        
                        s+=i.stu.id_number+" "+i.problem+" "+i.branch+" "+i.class_room
                    notify+=s        
                    data1 = technician.objects.get(id=tech1)
                    p = admin_notify.objects.create(tech=data1,notify=notify)
                    p.save()
                    messages.success(request, 'Your successfully send notification')
                    return redirect('/pendingproblem')
                else:
                    messages.warning(request, 'your already assigned this problem to the technician')
                    return redirect('/pendingproblem')    
            else:
                messages.warning(request, 'please check the notify block')
                return redirect('/pendingproblem')         
    else:
        site_profile = problems.objects.get(id=pk)
        form1 = AdminForm(instance=site_profile)       
    return render(request,'postrequest.html',{'form1':form1})
#def searching(request):
    
    #not_given = problems.objects.all()
    #return render(request,"status_not_given.html",{'not_given':not_given})
@my_login_required
def add_stock(request):
    if request.method == 'POST':
        form = StackForm(request.POST)
        if form.is_valid():
            bill_no = form.data.get('bill_no')
            date = form.data.get('date')
            supplier = form.data.get('supplier')
            items = form.data.get('items')
            no_items = form.data.get('no_items')
            each_item = form.data.get('each_item')
            total_cost = form.data.get('total_cost')
            data2 = stock_details.objects.all()
            flag=1
            for j in data2:
                if j.bill_no==bill_no:
                    flag=0
                    break
            if flag==0:
                    messages.warning(request, 'you are alredy add this stock')
                    return redirect('/stocks')    
            else:    
                p = stock_details.objects.create(bill_no=bill_no,date=date,supplier=supplier,items=items,no_items=no_items,each_item=each_item,total_cost=total_cost)
                p.save()
                messages.success(request, 'Your successfully add the stock details')
                return redirect('/stocks')
    else:
        form = StackForm()
    return render(request,"add_stock.html",{'form':form })    
                        
@my_login_required
def show_notify(request):
    no = admin_notify.objects.all().order_by('-date_posted')
    paginator = Paginator(no,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        note = paginator.page(page)
    except (EmptyPage, InvalidPage):
        note = paginator.page(paginator.num_pages)
    return render(request,"allnotifications.html",{'note':note})       
@my_login_required
def status_given(request):
    give = problems.objects.all().order_by('-date_posted')
    paginator = Paginator(give,10)
    count = 0
    for c in give:
        if c.status == "success" and c.tech_name == request.session["username"]:
            count+=1 
    technician.objects.filter(username = request.session['username']).update(problems_count=count)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        givens = paginator.page(page)
    except (EmptyPage, InvalidPage):
        givens = paginator.page(paginator.num_pages)                  
    return render(request,"status_given.html",{'givens':givens,'count':count})    
        
@my_login_required
def give_status(request,problem_id):
    #p = problems.objects.get(id=problem_id)
    p = problems.objects.all().filter(id=problem_id)
    for c in p:
        if c.status == "reject":
            messages.warning(request, 'you already given the status')
        else:
            p.update(status="success")
            messages.success(request, 'Your successfully given the status')
    #not_given = problems.objects.all()
    #return render(request,"status_not_given.html",{'not_given':not_given})
            return redirect('/status_given')
@my_login_required
def reject_status(request,problem_id):
    #p = problems.objects.get(id=problem_id)
    p = problems.objects.all().filter(id=problem_id)
    #not_given = problems.objects.all()
    #return render(request,"status_not_given.html",{'not_given':not_given})
    for c in p:
        if c.status =="success":
            messages.warning(request, 'you already given the status')
        else:
            p.update(status="reject",tech_name = request.session["username"])
            messages.success(request, 'Your successfully reject the record')
    #not_given = problems.objects.all()
    #return render(request,"status_not_given.html",{'not_given':not_given})
            return redirect('/status_given')        
@my_login_required
def status_not_given(request):
    not_giv = problems.objects.all().order_by('-date_posted')
    paginator = Paginator(not_giv,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        not_given = paginator.page(page)
    except (EmptyPage, InvalidPage):
        not_given = paginator.page(paginator.num_pages)
    idnumber=request.POST.get('search')
    return render(request,"status_not_given.html",{'not_given':not_given,'idnumber':idnumber})    
    
@my_login_required
def slot_not_given(request):
    not_give = problems.objects.all().order_by('-date_posted')
    paginator = Paginator(not_give,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        not_given = paginator.page(page)
    except (EmptyPage, InvalidPage):
        not_given = paginator.page(paginator.num_pages)
    return render(request,"slot_not_given.html",{'not_given':not_given})
@my_login_required
def add_slot_not_given(request,problem_id):
    if request.method == 'POST':
        site_profile = problems.objects.get(id=problem_id)
        form = UserSlotForm(request.POST,instance=site_profile)
        
        if form.is_valid():
            form.save()
            p = problems.objects.get(id=problem_id)
            t = problems.objects.filter(id=problem_id)
            for i in t:
                s = notifications.objects.create(stu1=p,problem_type=i.problem,slot=i.slot)
                s.save()
            messages.success(request, 'Your successfully add the slot and send notification to student')
            return redirect('/not_given')
    else:
        site_profile = problems.objects.get(id=problem_id)
        form = UserSlotForm(instance=site_profile)       
    #add = problems.objects.all(pk=pk)
    return render(request,"add.html",{'form':form})    
@my_login_required
def slot_given(request):
    give = problems.objects.all().order_by('-date_posted')
    paginator = Paginator(give,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        given = paginator.page(page)
    except (EmptyPage, InvalidPage):
        given = paginator.page(paginator.num_pages)
    return render(request,"slot_given.html",{'given':given})  
@my_login_required
def edit_slot_given(request,problem_id):
    if request.method == 'POST':
        site_profile = problems.objects.get(id=problem_id)
        form = UserSlotForm(request.POST,instance=site_profile)
        if form.is_valid():
            form.save()
            #p = notifications.objects.create(stu1=site_profile,problem_type=form.data.get('problem'),slot=form.data.get('slot'))
            p = problems.objects.get(id=problem_id).order_by('-date_posted')
            t = problems.objects.filter(id=problem_id).order_by('-date_posted')
            for i in t:
                notifications.objects.filter(stu1=p).update(problem_type=i.problem,slot=i.slot,data="updated")
            messages.success(request, 'Your successfully Edit the slot and send notification to the given problem')
            return redirect('/given')
    else:
        site_profile = problems.objects.get(id=problem_id)
        form = UserSlotForm(instance=site_profile)       
    #add = problems.objects.all(pk=pk)
    return render(request,"add.html",{'form':form})           
@my_login_required    
def tchangepassword(request):
    if request.method == 'POST':
        form = UserPasswordForm(request.POST)
        if form.is_valid():
            password = form.data.get("password")
            confirm = form.data.get("confirm_password")
            if password == confirm:
                data1 = technician.objects.filter(username=request.session['username']).update(password=password)
                messages.success(request, 'Your successfully change your password')
                return redirect('/')
            else:
                messages.warning(request, 'passwords are mismatch')
                return redirect('/tchange')
                    
    else:
        form = UserPasswordForm()        
    return render(request,'tchangepassword.html',{'form':form }) 
@my_login_required
def profile(request):
    if request.method == 'POST':
        site_profile = technician.objects.get(username=request.session['username'])
        form = UserUpdateForm(request.POST,instance=site_profile)
        if form.is_valid():
            t=any(i.isdigit() for i in form.data.get('name'))
            if not t and len(form.data.get('mobile'))==10:                 
                form.save()
                messages.success(request, 'Your account has been updated!')
                return redirect('/profile')
            else:
                messages.warning(request, 'inavlid name or mobile number')
                return redirect('/profile')    
    else:
        site_profile = technician.objects.get(username=request.session['username'])
        form = UserUpdateForm(instance=site_profile)    
    return render(request,"update_profile.html",{'form': form})

def tlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
             username = form.data.get("username").lower()
             password = form.data.get("password").lower()
             data1 = technician.objects.filter(username=username).values('username','password')
             if data1:
                 for c in data1:
                    if c['username']==username and password==c['password']:
                        request.session['username']=username
                        return HttpResponseRedirect(reverse('home'))
                        #messages.success(request, 'Your successfully login',)
                    else:
                        messages.warning(request,'invalid credentials')
                        return redirect('/tlogin')  
             else:
                messages.warning(request,'invalid username')
                return redirect('/tlogin')
    else:
        form = UserLoginForm()    
    return render(request,"tlogin.html",{'form': form})
def tlogout(request):
    request.session['username']=None
    return redirect('/')     
