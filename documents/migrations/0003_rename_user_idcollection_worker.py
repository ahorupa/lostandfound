# Generated by Django 3.2.9 on 2021-11-25 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20211122_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idcollection',
            old_name='user',
            new_name='worker',
        ),
    ]
