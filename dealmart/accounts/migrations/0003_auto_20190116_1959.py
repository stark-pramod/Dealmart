# Generated by Django 2.1.1 on 2019-01-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190114_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerdetails',
            name='aadhar_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='bank_account_no',
            field=models.BigIntegerField(),
        ),
    ]