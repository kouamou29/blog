# Generated by Django 5.0 on 2024-01-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_blog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
