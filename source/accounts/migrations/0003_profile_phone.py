# Generated by Django 4.0.5 on 2022-06-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_create_profile_for_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Номер'),
        ),
    ]