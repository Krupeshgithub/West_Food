# Generated by Django 4.0.3 on 2022-03-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_ngo_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='logo',
            field=models.FileField(default='media/tiger.jpg', upload_to='media/images/'),
        ),
    ]