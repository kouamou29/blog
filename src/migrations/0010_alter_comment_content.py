# Generated by Django 5.0 on 2024-01-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=234),
        ),
    ]
