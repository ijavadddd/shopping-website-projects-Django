# Generated by Django 3.2.5 on 2022-03-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.TextField(default=None),
        ),
    ]
