# Generated by Django 3.1.1 on 2021-05-19 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210505_0254'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]