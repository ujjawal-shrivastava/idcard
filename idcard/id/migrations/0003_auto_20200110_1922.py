# Generated by Django 3.0.2 on 2020-01-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0002_auto_20200110_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(choices=[(1, '1st'), (2, '2nd'), (3, '3rd')], default=1),
        ),
    ]