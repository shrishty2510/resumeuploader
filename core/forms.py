from django import forms
from. models import Resume

gender_choice = [
    ('Male','Male'),
    ('Female','Female')
]
job_choices = [
    ('Delhi ','Delhi '),
    ('Indore ','Indore '),
    ('Mumbai ','Mumbai '),
    ('Bangalore ','Bangalore '),
    ('Pune ','Pune '),
    ('Hyderabad ','Hyderabad '),
]

class Resumeform(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations',choices=job_choices,widget=forms.CheckboxSelectMultiple)
    class Meta :
        model = Resume
        fields=['name','dob','gender','email','mobile','locality','city','state','pin','job_city','profile_image','my_file']
        labels = {'name':'Full Name','dob':'Date of Birth','pin':'Pin Code' ,'mobile':'Mobile No.','profile_image':'Profile Image','my_file':'Document','email':'Email Id'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control '}),
            'dob':forms.DateInput(attrs={'class':'form-control ','type':'date'}),
            'city':forms.TextInput(attrs={'class':'form-control '}),
            'state':forms.Select(attrs={'class':'form-control '}),
            'pin':forms.NumberInput(attrs={'class':'form-control '}),
            'email':forms.EmailInput(attrs={'class':'form-control '}),
            'locality':forms.TextInput(attrs={'class':'form-control '}),
            'mobile':forms.NumberInput(attrs={'class':'form-control '}),
        }