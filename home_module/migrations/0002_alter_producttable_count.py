# Generated by Django 5.0.4 on 2024-04-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttable',
            name='count',
            field=models.IntegerField(verbose_name='تعداد محصول'),
        ),
    ]
