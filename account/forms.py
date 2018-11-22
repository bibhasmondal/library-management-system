from django.contrib.auth.models import User
from django import forms
from django.apps import apps
from .models import Student
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','max_length': 100,'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','max_length':100,'class':'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder': 'Usename','max_length': 100,'class':'form-control'}))
    first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={'placeholder': 'First name','max_length': 100,'class':'form-control'}))
    last_name = forms.CharField(label='Last name',widget=forms.TextInput(attrs={'placeholder': 'Last name','max_length': 100,'class':'form-control'}))
    email = forms.EmailField(label='Email address',widget=forms.EmailInput(attrs={'placeholder': 'Email address','max_length': 100,'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password','max_length': 100,'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password','max_length': 100,'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class StudentRegistrationForm(forms.ModelForm):
    DEPT_CHOICES = (('ME', 'Mechanical Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics and Communications'),
        ('MCA', 'Master of Computer Application'),
        ('MME', 'MTech: Mechanical'),
        ('MCSE', 'MTech: Computer Science'),
        ('MIT', 'MTech: Information Technology'),
        ('MEE', 'MTech: Electrical Engineering'),
        ('MECE', 'MTech: Electronics and Communication'),
        )
    Year_Of_Passing = forms.IntegerField(label='Year of passing',widget=forms.TextInput(attrs={'placeholder':'Year of passing','class':'form-control','max_length': 16}))
    Department = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control','max_length': 16}),choices=DEPT_CHOICES)
    Address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'placeholder': 'Address', 'class': 'form-control', 'style': 'height:60px'}))
    Mobile_No = forms.DecimalField(label='Mobile No.', widget=forms.TextInput(attrs={'placeholder': 'Mobile No.', 'class': 'form-control'}))
    class Meta:
        model = Student
        fields = ('Department','Year_Of_Passing','Address','Mobile_No')

class ChangePassword(forms.Form):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'placeholder': 'Old Password','max_length': 100,'class':'form-control'}))
    new_password = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'placeholder': 'New Password','max_length': 100,'class':'form-control'}))
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','max_length': 100,'class':'form-control'}))
    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['new_password'] != cd['confirm_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['confirm_password']

class ForgotPassword(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder': 'Usename','max_length': 100,'class':'form-control'}))
    email = forms.EmailField(label='Email address',widget=forms.EmailInput(attrs={'placeholder': 'Email address','max_length': 100,'class':'form-control'}))

class Edit_Details(forms.Form):
    dp=forms.ImageField(label="DP", widget=forms.FileInput())
