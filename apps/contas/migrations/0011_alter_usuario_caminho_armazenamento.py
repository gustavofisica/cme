# Generated by Django 3.2.7 on 2021-09-28 20:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0010_alter_usuario_caminho_armazenamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='caminho_armazenamento',
            field=models.UUIDField(default=uuid.UUID('5e2e8003-f14b-495d-8aff-b0fe0d30c4fe'), editable=False),
        ),
    ]
