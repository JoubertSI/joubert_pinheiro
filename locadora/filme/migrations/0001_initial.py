# Generated by Django 4.2 on 2023-04-07 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100, verbose_name='Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.CharField(max_length=100, verbose_name='Nome')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preco')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filme.generos')),
            ],
        ),
    ]
