# Generated by Django 3.2.10 on 2024-10-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='object_id',
            field=models.CharField(max_length=255),
        ),
    ]
