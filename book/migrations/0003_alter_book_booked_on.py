# Generated by Django 4.1.5 on 2023-04-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_delete_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='booked_on',
            field=models.DateField(auto_now=True),
        ),
    ]
