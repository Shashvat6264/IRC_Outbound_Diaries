# Generated by Django 3.0.3 on 2020-03-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20200326_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
