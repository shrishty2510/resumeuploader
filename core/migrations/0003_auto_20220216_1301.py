# Generated by Django 3.2.7 on 2022-02-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_resume_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='pin',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh (AR)', 'Arunachal Pradesh (AR)'), ('Assam (AS)', 'Assam (AS)'), ('Bihar (BR)', 'Bihar (BR)'), ('Chhattisgarh (CG)', 'Chhattisgarh (CG)'), ('Goa (GA)', 'Goa (GA)'), ('Gujarat (GJ)', 'Gujarat (GJ)'), ('Haryana (HR)', 'Haryana (HR)'), ('Himachal Pradesh (HP)', 'Himachal Pradesh (HP)'), ('Jammu and Kashmir (JK)', 'Jammu and Kashmir (JK)'), ('Jharkhand (JH)', 'Jharkhand (JH)'), ('Karnataka (KA)', 'Karnataka (KA)'), ('Kerala (KL)', 'Kerala (KL)'), ('Madhya Pradesh (MP)', 'Madhya Pradesh (MP)'), ('Maharashtra (MH)', 'Maharashtra (MH)'), ('Manipur (MN)', 'Manipur (MN)'), ('Meghalaya (ML)', 'Meghalaya (ML)'), ('Mizoram (MZ)', 'Mizoram (MZ)'), ('Nagaland (NL)', 'Nagaland (NL)'), ('Odisha(OR)', 'Odisha(OR)'), ('Punjab (PB)', 'Punjab (PB)'), ('Rajasthan (RJ)', 'Rajasthan (RJ)'), ('Sikkim (SK)', 'Sikkim (SK)'), ('Tamil Nadu (TN)', 'Tamil Nadu (TN)'), ('Telangana (TS)', 'Telangana (TS)'), ('Tripura (TR)', 'Tripura (TR)'), ('Uttar Pradesh (UP)', 'Uttar Pradesh (UP)'), ('Uttarakhand (UK)', 'Uttarakhand (UK)'), ('West Bengal (WB)', 'West Bengal (WB)')], max_length=30),
        ),
    ]
