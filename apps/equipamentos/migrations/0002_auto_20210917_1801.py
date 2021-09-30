# Generated by Django 3.2.7 on 2021-09-17 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='fabricante',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='microscopio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='modelo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='numero_patrimonio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='pre_microscopia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='sala',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='tecnicas',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='tipo_de_equipamento',
            field=models.CharField(blank=True, choices=[('SEM', 'Microscópio Eletrônico de Varredura'), ('TEM', 'Microscópio Eletrônico de Transmissão'), ('Raman', 'Microscópio Confocal Raman'), ('AFM', 'Microscópio de Força Atômica')], max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='AcessorioEquipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_acessorio', models.CharField(max_length=255)),
                ('fabricante', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('numero_patrimonio', models.IntegerField()),
                ('equipamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipamentos.equipamento')),
            ],
        ),
    ]
