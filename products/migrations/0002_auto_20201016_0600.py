# Generated by Django 3.1.2 on 2020-10-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discountPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
    ]
