# Generated by Django 3.1.4 on 2021-02-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210222_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.CharField(max_length=200, null=True),
        ),
    ]