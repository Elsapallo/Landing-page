# Generated by Django 3.2.2 on 2021-05-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cel', models.CharField(max_length=15)),
            ],
        ),
    ]
