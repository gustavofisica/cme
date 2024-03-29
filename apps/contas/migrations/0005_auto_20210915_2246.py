# Generated by Django 3.2.7 on 2021-09-16 01:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_alter_usuario_caminho_armazenamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='contas.usuario')),
                ('instituicional', models.JSONField(default=dict)),
                ('ramal', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator(message='O ramal deve estar no seguinte formato: 0000', regex='[0-9]{4}')])),
            ],
        ),
        migrations.CreateModel(
            name='Externo',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='contas.usuario')),
                ('tipo_de_instituicao', models.CharField(max_length=40)),
                ('razao_social', models.CharField(max_length=250)),
                ('cnpj', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='O ramal deve estar no seguinte formato: 00.000.000/0000-00', regex='/^\\d{2}\\.\\d{3}\\.\\d{3}\\/\\d{4}\\-\\d{2}$/')])),
                ('cep', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='O ramal deve estar no seguinte formato: 00000-000', regex='[0-9]{5}-[0-9]{3}')])),
                ('uf', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=250)),
                ('bairro', models.CharField(max_length=250)),
                ('rua', models.CharField(max_length=250)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=250)),
                ('telefone_instituicao', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='O telefone de estar no formato de : (xx) xxxxx-xxxx', regex='\\([0-9]{2}\\) [0-9]{4,5}-[0-9]{4}')])),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='caminho_armazenamento',
            field=models.UUIDField(default=uuid.UUID('5bad4559-405d-4f52-b8f3-0d2256edaa12'), editable=False),
        ),
        migrations.CreateModel(
            name='Discente',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='contas.usuario')),
                ('vinculo', models.CharField(blank=True, max_length=25, null=True)),
                ('inicio_vinculo', models.DateField()),
                ('setor', models.CharField(blank=True, max_length=250, null=True)),
                ('departamento', models.CharField(blank=True, max_length=250, null=True)),
                ('periodo_de_permanencia', models.DateField(null=True)),
                ('docente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contas.docente')),
            ],
        ),
    ]
