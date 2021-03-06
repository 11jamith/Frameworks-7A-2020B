# Generated by Django 3.1.2 on 2020-10-30 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paises',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('abreviatura', models.CharField(max_length=4)),
                ('estado', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ciudades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('abreviatura', models.CharField(max_length=4)),
                ('estado', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('id_pais', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Modulo2.paises')),
            ],
        ),
        migrations.CreateModel(
            name='afiliados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellidos', models.TextField()),
                ('numero_movil', models.IntegerField()),
                ('direccion', models.TextField()),
                ('email', models.TextField()),
                ('estado', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('id_ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Modulo2.ciudades')),
            ],
        ),
    ]
