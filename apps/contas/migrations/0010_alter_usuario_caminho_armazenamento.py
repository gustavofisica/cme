# Generated by Django 3.2.7 on 2021-09-28 19:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0009_alter_usuario_caminho_armazenamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='caminho_armazenamento',
            field=models.UUIDField(default=uuid.UUID('63374526-3b0e-4842-a666-8532571f5239'), editable=False),
        ),
    ]
