# Generated by Django 3.1.7 on 2021-03-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210226_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]