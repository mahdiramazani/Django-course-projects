# Generated by Django 4.1.7 on 2023-03-29 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile_app', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUSer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
