# Generated by Django 3.2.7 on 2021-09-28 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0006_alter_acessorioequipamento_equipamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessorioequipamento',
            name='equipamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acessorios', to='equipamentos.equipamento'),
        ),
    ]
