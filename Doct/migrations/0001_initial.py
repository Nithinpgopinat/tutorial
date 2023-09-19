# Generated by Django 4.1.5 on 2023-03-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.CharField(max_length=255)),
                ('dep_name', models.CharField(max_length=255)),
                ('doc_image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]