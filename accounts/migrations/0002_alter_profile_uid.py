# Generated by Django 4.0.6 on 2022-08-08 18:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('fdf2927b-62c8-4733-9dc2-8ee37d75af6b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
