# Generated by Django 3.2.5 on 2022-01-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_auto_20220130_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Same',
            field=models.ManyToManyField(default=None, to='commerce.SameProduct'),
        ),
    ]
