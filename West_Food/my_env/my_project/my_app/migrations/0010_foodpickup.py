# Generated by Django 4.0.3 on 2022-04-05 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPickup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_quality', models.CharField(blank=True, max_length=30, null=True)),
                ('food_category', models.CharField(blank=True, max_length=50, null=True)),
                ('food_description', models.TextField()),
                ('pick_up_location', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('food_donor_purpose', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('pick_up_address', models.TextField()),
                ('pick_up_time', models.IntegerField()),
                ('food_status', models.CharField(blank=True, max_length=50, null=True)),
                ('picture', models.FileField(default='media/food-defualt.jpg', upload_to='media/images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
    ]