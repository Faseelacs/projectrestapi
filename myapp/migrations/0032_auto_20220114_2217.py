# Generated by Django 3.2.11 on 2022-01-14 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_topicandcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicandcomment',
            name='topic_id',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Topicandcomment',
        ),
    ]
