# Generated by Django 3.1.5 on 2021-02-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
    ]
