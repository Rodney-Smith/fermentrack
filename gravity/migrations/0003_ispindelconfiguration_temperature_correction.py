# Generated by Django 3.0.11 on 2020-11-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gravity', '0002_brewfather_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='ispindelconfiguration',
            name='temperature_correction',
            field=models.FloatField(default=0.0, help_text='Value to correct iSpindel temperature value with '),
        ),
    ]