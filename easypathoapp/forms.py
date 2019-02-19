from django import forms

class cpr(forms.Form):
    Name= forms.CharField(max_length=20,
                         widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': 'Enter Your Full Name', 'aria-label':'Name'}))
    CompanyName= forms.CharField(max_length=20,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'Enter Your Company Name ','aria-label':'cn' }))
    EmployeeStrength= forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your Employee Strength ','aria-label' : 'es' }))
    phone=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your Phone Number ','aria-label' : 'p'}))
    Email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your Email id ', 'aria-label' : 'em'}))
    city=forms.CharField(max_length=20,
                         widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': 'Enter Your City Name ','aria-label' : 'city'}))

