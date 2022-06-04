# Generated by Django 4.0.3 on 2022-04-07 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_alter_foodpickup_pick_up_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='POST_NGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('likes', models.IntegerField()),
                ('views', models.IntegerField()),
                ('picture', models.FileField(blank=True, default='media/food-defualt.jpg', null=True, upload_to='media/images/')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='')),
                ('audiofile', models.FileField(null=True, upload_to='media/musics/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Ngo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.ngo')),
            ],
        ),
    ]