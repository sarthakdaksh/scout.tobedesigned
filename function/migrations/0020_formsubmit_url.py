# Generated by Django 4.0.4 on 2022-05-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0019_remove_formsubmit_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmit',
            name='url',
            field=models.CharField(default=0, max_length=100),
        ),
    ]