# Generated by Django 4.2.7 on 2023-11-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
