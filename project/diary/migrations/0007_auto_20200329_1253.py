# Generated by Django 3.0.3 on 2020-03-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_auto_20200329_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dep',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='person',
            name='re_area',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='univ',
            field=models.CharField(max_length=80),
        ),
    ]
