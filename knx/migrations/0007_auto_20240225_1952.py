# Generated by Django 3.0 on 2024-02-25 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knx', '0006_scraperdetail'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profiledata',
            unique_together={('company_name', 'phone_number')},
        ),
    ]
