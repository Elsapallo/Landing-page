# Generated by Django 3.2.2 on 2021-05-26 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuri', '0002_miembro'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='institucion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
