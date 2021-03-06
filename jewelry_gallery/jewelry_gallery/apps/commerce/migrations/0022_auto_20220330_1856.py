# Generated by Django 3.2.5 on 2022-03-30 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0021_auto_20220330_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Color',
            field=models.ManyToManyField(null=True, to='commerce.Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Same',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='commerce.product'),
        ),
    ]
