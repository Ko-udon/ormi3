# Generated by Django 4.0.3 on 2023-11-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='이름', max_length=6),
        ),
    ]