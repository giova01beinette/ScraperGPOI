# Generated by Django 3.0.3 on 2020-05-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect_information', '0002_auto_20200508_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='link_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='links',
            old_name='link_sito',
            new_name='sito',
        ),
        migrations.AddField(
            model_name='links',
            name='link',
            field=models.CharField(default='needed', max_length=150),
        ),
    ]