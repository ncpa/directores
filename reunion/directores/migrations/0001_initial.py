# Generated by Django 2.0 on 2018-10-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('clave', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('apPat', models.CharField(max_length=200, verbose_name='Apellido Paterno')),
                ('apMat', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellido Materno')),
                ('correo', models.CharField(max_length=200, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=25, verbose_name='Teléfono')),
                ('grado', models.TextField(max_length=200, verbose_name='Grado')),
                ('siglas', models.TextField(max_length=10, verbose_name='Siglas de Grado')),
                ('puesto', models.TextField(max_length=200, verbose_name='Puesto')),
                ('status', models.BooleanField(verbose_name='Asistencia')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'director',
                'verbose_name_plural': 'directores',
                'ordering': ['-clave'],
            },
        ),
        migrations.CreateModel(
            name='Ut',
            fields=[
                ('claveUt', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombreUt', models.CharField(max_length=300, verbose_name='Nombre')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Universidad',
                'verbose_name_plural': 'Universidades',
                'ordering': ['-claveUt'],
            },
        ),
        migrations.AddField(
            model_name='director',
            name='claveUt',
            field=models.ManyToManyField(to='directores.Ut', verbose_name='Clave Ut'),
        ),
    ]
