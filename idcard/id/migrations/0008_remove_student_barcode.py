# Generated by Django 3.0.2 on 2020-01-11 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0007_student_barcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='barcode',
        ),
    ]
