# Generated by Django 3.1.2 on 2021-05-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20210504_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
