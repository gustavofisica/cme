# Generated by Django 3.2.7 on 2021-09-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0004_auto_20210928_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='apelido',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]