import email
from django.db import models
State_choice = (
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh (AR)','Arunachal Pradesh (AR)'),
('Assam (AS)','Assam (AS)'),
('Bihar (BR)','Bihar (BR)'),
('Chhattisgarh (CG)','Chhattisgarh (CG)'),
('Goa (GA)','Goa (GA)'),
('Gujarat (GJ)','Gujarat (GJ)'),
('Haryana (HR)','Haryana (HR)'),
('Himachal Pradesh (HP)','Himachal Pradesh (HP)'),
('Jammu and Kashmir (JK)','Jammu and Kashmir (JK)'),
('Jharkhand (JH)','Jharkhand (JH)'),
('Karnataka (KA)','Karnataka (KA)'),
('Kerala (KL)','Kerala (KL)'),
('Madhya Pradesh (MP)','Madhya Pradesh (MP)'),
('Maharashtra (MH)','Maharashtra (MH)'),
('Manipur (MN)','Manipur (MN)'),
('Meghalaya (ML)','Meghalaya (ML)'),
('Mizoram (MZ)','Mizoram (MZ)'),
('Nagaland (NL)','Nagaland (NL)'),
('Odisha(OR)','Odisha(OR)'),
('Punjab (PB)','Punjab (PB)'),
('Rajasthan (RJ)','Rajasthan (RJ)'),
('Sikkim (SK)','Sikkim (SK)'),
('Tamil Nadu (TN)','Tamil Nadu (TN)'),
('Telangana (TS)','Telangana (TS)'),
('Tripura (TR)','Tripura (TR)'),
('Uttar Pradesh (UP)','Uttar Pradesh (UP)'),
('Uttarakhand (UK)','Uttarakhand (UK)'),
('West Bengal (WB)','West Bengal (WB)'),
)

class Resume(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=7)
    locality = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30,choices= State_choice)
    pin = models.CharField(  max_length=30)
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField( upload_to='doc',  blank=True)

    

# Create your models here.
