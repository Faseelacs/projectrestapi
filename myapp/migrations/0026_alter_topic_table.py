# Generated by Django 3.2.11 on 2022-01-14 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_delete_topicandcomment'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='topic',
            table='Topic',
        ),
    ]