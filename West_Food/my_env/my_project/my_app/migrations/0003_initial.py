# Generated by Django 4.0.3 on 2022-03-27 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_app', '0002_delete_ngo_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('is_activate', models.BooleanField(default=True)),
                ('is_verify', models.BooleanField(default=True)),
                ('role', models.CharField(max_length=40)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(max_length=40)),
                ('contact_person_number', models.CharField(max_length=15)),
                ('contact_person_name', models.CharField(max_length=40)),
                ('registration_no', models.CharField(max_length=50)),
                ('no_member', models.IntegerField(max_length=40)),
                ('working_hourse', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('locations', models.CharField(max_length=40)),
                ('address', models.TextField(max_length=300)),
                ('about_us', models.TextField(max_length=600)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
    ]
