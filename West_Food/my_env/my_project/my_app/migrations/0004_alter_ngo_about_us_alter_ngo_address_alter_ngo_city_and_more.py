# Generated by Django 4.0.3 on 2022-03-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='about_us',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='address',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='contact_person_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='contact_person_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='locations',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='no_member',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='registration_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='role',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='working_hourse',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
