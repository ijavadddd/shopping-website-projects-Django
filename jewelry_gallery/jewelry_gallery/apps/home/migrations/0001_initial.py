# Generated by Django 3.2.5 on 2022-03-16 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=35)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=35)),
                ('LastName', models.CharField(default='None', max_length=35)),
                ('Password', models.CharField(max_length=35)),
                ('PhoneNumber', models.CharField(max_length=20)),
                ('Email', models.EmailField(default=None, max_length=45)),
                ('Address', models.TextField(default=None)),
                ('Status', models.BooleanField(default=True)),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.role')),
            ],
        ),
    ]
