# Generated by Django 3.2.7 on 2021-09-27 22:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0008_alter_usuario_caminho_armazenamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='caminho_armazenamento',
            field=models.UUIDField(default=uuid.UUID('a448766f-9d12-4a9a-843a-420c9d065577'), editable=False),
        ),
    ]
