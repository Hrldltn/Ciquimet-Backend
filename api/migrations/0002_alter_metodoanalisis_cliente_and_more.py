# Generated by Django 5.0.4 on 2024-10-07 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodoanalisis',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metodos_analisis', to='api.cliente'),
        ),
        migrations.AlterUniqueTogether(
            name='metodoanalisis',
            unique_together={('cliente', 'nombre')},
        ),
        migrations.AddConstraint(
            model_name='metodoanalisis',
            constraint=models.UniqueConstraint(fields=('cliente', 'nombre'), name='unique_metodo_por_cliente'),
        ),
    ]
