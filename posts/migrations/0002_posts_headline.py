# Generated by Django 3.2 on 2022-06-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='headline',
            field=models.TextField(default=0, verbose_name='Headline'),
            preserve_default=False,
        ),
    ]
