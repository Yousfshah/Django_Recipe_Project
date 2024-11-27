# Generated by Django 5.1.2 on 2024-10-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
