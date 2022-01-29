# Generated by Django 3.2.5 on 2022-01-29 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0007_alter_sameproduct_mainimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Productd',
        ),
        migrations.AddField(
            model_name='product',
            name='Same',
            field=models.ManyToManyField(blank=True, null=True, to='commerce.SameProduct'),
        ),
        migrations.AddField(
            model_name='sameproduct',
            name='ProductId',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
