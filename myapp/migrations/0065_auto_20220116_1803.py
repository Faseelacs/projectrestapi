# Generated by Django 3.2.11 on 2022-01-16 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0064_topicandcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
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