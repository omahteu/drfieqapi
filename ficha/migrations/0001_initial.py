# Generated by Django 4.1.4 on 2022-12-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50)),
                ('sobrenome', models.CharField(blank=True, max_length=50)),
                ('telefone', models.CharField(blank=True, max_length=11)),
                ('nascimento', models.CharField(blank=True, max_length=10)),
                ('membro', models.CharField(blank=True, max_length=7)),
                ('endereco', models.TextField()),
            ],
        ),
    ]