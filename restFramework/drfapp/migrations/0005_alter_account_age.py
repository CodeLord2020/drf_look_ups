# Generated by Django 4.1.7 on 2023-06-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0004_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='age',
            field=models.IntegerField(),
        ),
    ]