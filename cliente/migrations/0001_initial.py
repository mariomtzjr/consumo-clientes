# Generated by Django 2.2 on 2020-04-21 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('slug', models.SlugField(blank=True, default=None, max_length=150, null=True)),
            ],
        ),
    ]
