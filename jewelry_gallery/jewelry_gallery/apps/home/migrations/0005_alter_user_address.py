# Generated by Django 3.2.5 on 2022-03-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
