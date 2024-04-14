from django import forms  
from Employee.models import Employee  

class EmployeeForm(forms.ModelForm):  
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:  
        model = Employee  
        fields = ['name', 'contact', 'email', 'gender', 'address', 'department'] 
        widgets = { 
            'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
        }
