# Generated by Django 3.2.2 on 2021-05-30 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuri', '0003_alter_miembro_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='photo',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]
