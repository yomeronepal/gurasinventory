# Generated by Django 3.1.5 on 2021-01-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_vendordetail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendordetail',
            name='pan_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
