# Generated by Django 4.1.5 on 2023-03-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_phone', models.CharField(max_length=100)),
                ('p_email', models.EmailField(max_length=254)),
                ('doc_name', models.CharField(max_length=100)),
            ],
        ),
    ]