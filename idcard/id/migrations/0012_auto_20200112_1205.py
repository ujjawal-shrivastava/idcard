# Generated by Django 2.1 on 2020-01-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0011_auto_20200112_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
