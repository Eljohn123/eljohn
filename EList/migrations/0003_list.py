# Generated by Django 3.1.6 on 2021-04-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EList', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
