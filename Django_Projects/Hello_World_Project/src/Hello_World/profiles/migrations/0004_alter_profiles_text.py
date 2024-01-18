# Generated by Django 4.1 on 2023-08-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profiles_text_alter_profiles_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='text',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], default='', max_length=60),
        ),
    ]
