# Generated by Django 5.1.2 on 2024-11-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='group_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
