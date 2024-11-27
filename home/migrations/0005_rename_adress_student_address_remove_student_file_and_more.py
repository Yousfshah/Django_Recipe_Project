# Generated by Django 5.1.2 on 2024-10-28 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_student_age_alter_student_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='adress',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(default=310),
            preserve_default=False,
        ),
    ]
