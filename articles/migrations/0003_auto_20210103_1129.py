# Generated by Django 3.1.4 on 2021-01-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210103_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('-created_at',), 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]
