# Generated by Django 3.0.2 on 2020-01-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0003_auto_20200110_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year')], default=1, max_length=3),
        ),
    ]