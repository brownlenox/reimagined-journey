# Generated by Django 4.2.7 on 2023-11-08 13:06

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_employee_created_at_employee_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile',
            field=models.ImageField(default='employees/employee.png', null=True, upload_to=mainapp.models.unique_img_name),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
