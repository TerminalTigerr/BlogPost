# Generated by Django 4.2.1 on 2023-05-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('bio', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pic')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]