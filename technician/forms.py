from django import forms
from .models import technician,admin_notify,reports
from django.core.validators import RegexValidator
from student.models import problems,stock_details
class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    class Meta:
        model = technician
        fields = ['username']
class AdminForm(forms.ModelForm):  
    notify = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter notification\nMinimum 15 characters','rows':7,'cols':10}))
    class Meta:
        model = admin_notify
        fields = ['tech','notify']
class StackForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    bill_no = forms.CharField(widget=forms.TextInput(attrs={'rows':3,'cols':10,'placeholder':'Enter the bill number','type':'number'}))
    supplier = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':10,'placeholder':'Enter the name of the supplier'}))
    items = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':10,'placeholder':'Enter the name of the items'}))
    no_items = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':10,'placeholder':'Enter the no of  items'}))
    each_item = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':10,'placeholder':'Enter the each item'}))
    total_cost = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':10,'placeholder':'Enter the total_cost'}))
    class Meta:
        model = stock_details
        fields = '__all__'             
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = technician
        fields = ['name','username','email','mobile']
class UserPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your confirm password'}))
    
    class Meta:
        model = technician
        fields = ['password']  

class AdminReportForm(forms.ModelForm):
    no_of_students = forms.CharField(widget=forms.TextInput(attrs={'type':'number','placeholder': 'Enter no of students'}))
    class_room = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter class room number Ex:s008'}))
    dept = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter department name Ex:cse'}))
    block = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter block name Ex:AB1 '}))
    amplifier = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter amplifier status Ex: yes,working'}))
    speakers = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter speakers status Ex: yes,working'}))
    audio_port = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter audio port status Ex: yes,working'}))
    audio_cable = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter audio cable status Ex: yes,working'}))
    projector = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter projector status Ex: yes,working'}))
    screen = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter screen status Ex: yes,working'}))
    video_cable = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter video cable status Ex: yes,working'}))
    vga_port = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter vga port status Ex: yes,working'}))
    io_port_not_working_positions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    how_many_lan_cables_not_working = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    issued_lan_cables = forms.CharField(widget=forms.TextInput(attrs={'type':'number','placeholder': 'Enter no of lan cables issued'}))
    class_room_ip = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter class room ip Ex: 10.30.44.100'}))
    switch = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter switch status Ex: yes,working'}))
    rack = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter rack status Ex: yes,working'}))
    adapters_not_working = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    adapters_working = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    screen_damage = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    d_link_modem = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter d link modem status Ex: yes,working'}))
    jio_modem = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter jio modem status Ex: yes,working'}))
    bio_metric_essl_not_registered = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    bio_metric_aadhar_not_registered = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    bio_metric_problems_if_any = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter seating positions if Ex: A0,A1,B0 otherwise put "NO"'}))
    class Meta:
        model = reports
        fields = '__all__'

class UserSlotForm(forms.ModelForm):
    slot = forms.DateField(widget = forms.SelectDateWidget)
    problem = forms.CharField(widget=forms.TextInput, disabled=True)
    branch = forms.CharField(widget=forms.TextInput, disabled=True)
    class_room = forms.CharField(widget=forms.TextInput, disabled=True)
    date_posted = forms.DateField(widget=forms.SelectDateWidget, disabled=True)
    class Meta:
        model = problems
        fields = ['problem','branch','class_room','date_posted','slot']                      
