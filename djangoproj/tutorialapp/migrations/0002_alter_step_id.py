# Generated by Django 3.2.7 on 2022-01-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
