# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=20)),
                ('rate', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service_order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_aceptado', models.FloatField()),
                ('terminado', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service_prop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField()),
                ('fecha', models.DateTimeField()),
                ('rango', django_hstore.fields.DictionaryField()),
                ('empresa', models.ForeignKey(related_name='propuesta_empresa', to='core.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service_req',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Services_tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biografia', models.CharField(max_length=b'200')),
                ('rating', models.FloatField()),
                ('foto_perfil', models.ImageField(default=b'perfil/cliente/avatar.jpg', upload_to=b'perfil/cliente')),
                ('user', models.ForeignKey(related_name='perfil_cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario_empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(related_name='empresa', to='core.Empresa')),
                ('user', models.ForeignKey(related_name='perfil_empresa', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='services_tag',
            name='servicio',
            field=models.ForeignKey(related_name='servicio', to='core.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service_req',
            name='servicio',
            field=models.ForeignKey(related_name='servicio_pedido', to='core.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service_req',
            name='tags',
            field=models.ForeignKey(related_name='etiquetas', to='core.Services_tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service_req',
            name='usuario',
            field=models.ForeignKey(related_name='cliente', to='core.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service_prop',
            name='service_req',
            field=models.ForeignKey(related_name='service_req', to='core.Service_req'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service_order',
            name='service_prop',
            field=models.ForeignKey(related_name='propuesta', to='core.Service_prop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service_order',
            name='service_req',
            field=models.ForeignKey(related_name='pedido', to='core.Service_req'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service_order',
            name='usuario_empresa',
            field=models.ForeignKey(related_name='usuario_empresa', to='core.Usuario_empresa'),
            preserve_default=True,
        ),
    ]
