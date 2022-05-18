# Generated by Django 4.0.4 on 2022-05-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_escola'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('categoria', models.CharField(choices=[('moderno', 'Moderno'), ('tradicional', 'Tradicional'), ('shuaijiao', 'ShuaiJiao'), ('sanda', 'Sanda'), ('outros', 'Outros')], max_length=50)),
                ('regiao', models.CharField(choices=[('sul', 'Sul'), ('norte', 'Norte'), ('leste', 'Leste'), ('oeste', 'Oeste'), ('outros', 'Outros')], max_length=50)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'estilos',
            },
        ),
    ]