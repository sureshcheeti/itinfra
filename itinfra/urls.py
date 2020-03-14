"""itinfra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from student import views
from technician import views as tech_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.ithome, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^slogin/$', views.slogin, name='student-login'),
    url(r'^slogout/$', views.slogout, name='student-logout'),
    url(r'^post/$', views.post_problem, name='student-post'),
    url(r'^change/$', views.changepassword, name='student-change'),
    url(r'^histroy/$', views.histroy, name='student-histroy'),
    url(r'^notify/$', views.notification, name='student-notify'),
    url(r'^tlogin/$',tech_views.tlogin, name='tech-login'),
    url(r'^tlogout/$',tech_views.tlogout, name='tech-logout'),
    url(r'^profile/$',tech_views.profile, name='tech-profile'),
    url(r'^tchange/$',tech_views.tchangepassword, name='tech-change'),
    url(r'^not_given/$',tech_views.slot_not_given, name='slot-not-given'),
    url(r'^add_slot/(?P<problem_id>\d+)/$',tech_views.add_slot_not_given, name='add-slot-not-given'),
    url(r'^given/$',tech_views.slot_given, name='slot-given'),
    url(r'^status_given/$',tech_views.status_given, name='status-given'),
    url(r'^edit_slot/(?P<problem_id>\d+)/$',tech_views.edit_slot_given, name='edit-slot-given'),
    url(r'^not_status/$',tech_views.status_not_given, name='status-not-given'),
    url(r'^status/(?P<problem_id>\d+)/$',tech_views.give_status, name='give-status'),
    url(r'^alogin/$', auth_views.LoginView.as_view(template_name='alogin.html'), name='login'),
    url(r'^alogout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^adminchange/$',views.adminchangepassword, name='admin-change'),
    #url(r'^adminproblem/$',views.allproblem, name='admin-problem'),
    url(r'^pendingproblem/$',views.pendingproblem, name='pending-problem'),
    url(r'^adminup/$',views.adminupdate, name='admin-update'),
    url(r'^ourteam/$',views.ourteam, name='team'),
    url(r'^techstatus/$',views.tech_status, name='tech-status'), 
    url(r'^admin_notify/(?P<pk>\d+)/$',tech_views.adminnotify, name='admin-notify'),
    url(r'^allnotify/$',tech_views.show_notify, name='show-notify'),
    url(r'^gall/$',views.gally,name="gallery"),
    url(r'^galle/$',views.post_img,name="post-image"),
    url(r'^stoc/$',views.enter_stock,name="enter-stock"),
    url(r'^stocks/$',tech_views.add_stock,name="add-stock"),
    url(r'^reg/$',views.registration,name="student-register"),
    url(r'^add_reports/$',tech_views.admin_reports,name='admin-reports'),
    url(r'^enter_reports/$',views.enter_reports,name='enter-reports'),
    url(r'^forget/$',views.reset_password,name='reset-password'),
    url(r'^allstudents/$',views.all_students,name='all-students'),
    url(r'^studentdelete/(?P<pk>\d+)/$',views.delete_student,name='delete-student'),
    url(r'^rstatus/(?P<problem_id>\d+)/$',tech_views.reject_status, name='reject-status'),
    url(r'^all_view/(?P<problem_id>\d+)/$',views.all_views,name='all-view'),
    url(r'^valuesearch/$',views.search,name='search'),  

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)                       
