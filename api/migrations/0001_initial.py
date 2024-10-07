# Generated by Django 5.0.4 on 2024-10-07 07:16

import api.models
import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalisisCuS10FeS10MoS10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_cut_cus', models.FloatField(verbose_name='Control CuT-CuS')),
                ('cut', models.FloatField(verbose_name='CuT')),
                ('cus10', models.FloatField(verbose_name='CuS10')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuS4FeS4MoS4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control1_cut_cus', models.FloatField(verbose_name='Control1 CuT-CuS')),
                ('l_ppm_cus_fe', models.FloatField(verbose_name='L. ppm CusFe')),
                ('l_ppm_bk_fes4', models.FloatField(verbose_name='L. ppm-BK FeS4')),
                ('fes4', models.FloatField(verbose_name='FeS4 (%)')),
                ('control2_cut_fes4', models.FloatField(verbose_name='Control2 CuT-FeS4')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuSCuSFe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_ppm_cus_fe', models.FloatField(verbose_name='L. ppm CuSFe')),
                ('l_ppm_bk_cus_fe', models.FloatField(verbose_name='L. ppm-Bk CuSFe')),
                ('cus_fe', models.FloatField(verbose_name='CuSFe (%)')),
                ('control2_cut_cus_fe', models.FloatField(verbose_name='Control2 CuT-CuSFe')),
                ('cut', models.FloatField(verbose_name='CuT')),
                ('cus_c', models.FloatField(verbose_name='CuSC')),
                ('cus_fe_2', models.FloatField(verbose_name='CuSFe')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuTestConsH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control1_cut_cutest', models.FloatField(verbose_name='Control1 CuT-CuTest')),
                ('cut', models.FloatField(verbose_name='CuT')),
                ('cut_test', models.FloatField(verbose_name='CuTest')),
                ('gaston_ml', models.FloatField(verbose_name='Gaston mL')),
                ('gasto_bk_ml', models.FloatField(verbose_name='Gasto Bk mL')),
                ('n_naco3', models.FloatField(verbose_name='N NaCO3')),
                ('alicuota', models.FloatField(verbose_name='Alicuota')),
                ('consumo_h', models.FloatField(verbose_name='Consumo H+')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuTFeZn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_ppm_fe', models.FloatField(verbose_name='L. ppm Fe')),
                ('l_ppm_bk_fe', models.FloatField(verbose_name='L. ppm-BK Fe')),
                ('fe', models.FloatField(verbose_name='Fe (%)')),
                ('l_ppm_zn', models.FloatField(verbose_name='L. ppm Zn')),
                ('l_ppm_bk_zn', models.FloatField(verbose_name='L. ppm-BK Zn')),
                ('zn', models.FloatField(verbose_name='Zn (%)')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisMulti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_ppm_ag', models.FloatField(verbose_name='L. ppm Ag')),
                ('l_ppm_ag_bk', models.FloatField(verbose_name='L. ppm Ag-bk')),
                ('ag', models.FloatField(verbose_name='Ag (ppm)')),
                ('l_ppm_as', models.FloatField(verbose_name='L. ppm As')),
                ('l_ppm_as_bk', models.FloatField(verbose_name='L. ppm As-bk')),
                ('analisis_as', models.FloatField(verbose_name='As (%)')),
                ('l_ppm_mo', models.FloatField(verbose_name='L. ppm Mo')),
                ('l_ppm_mo_bk', models.FloatField(verbose_name='L. ppm Mo-bk')),
                ('mo', models.FloatField(verbose_name='Mo (%)')),
                ('l_ppm_pb', models.FloatField(verbose_name='L. ppm Pb')),
                ('l_ppm_pb_bk', models.FloatField(verbose_name='L. ppm Pb-Bk')),
                ('pb', models.FloatField(verbose_name='Pb (%)')),
                ('l_ppm_cu', models.FloatField(verbose_name='L. ppm Cu')),
                ('l_ppm_cu_bk', models.FloatField(verbose_name='L. ppm Cu-bk')),
                ('cu', models.FloatField(verbose_name='Cu (%)')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ElementoMetodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('gramos', models.FloatField()),
                ('miligramos', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Elementos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('tipo', models.CharField(max_length=200)),
                ('simbolo', models.CharField(blank=True, max_length=5, null=True)),
                ('numero_atomico', models.IntegerField(blank=True, null=True)),
                ('masa_atomica', models.FloatField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Activo')),
                ('descripcion', models.TextField(blank=True, max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb', models.CharField(max_length=100)),
                ('cu_t', models.FloatField(verbose_name='CuT (%)')),
                ('cu_s4', models.FloatField(verbose_name='CuS4 (%)')),
                ('cu_s10', models.FloatField(verbose_name='CuS10 (%)')),
                ('mo', models.FloatField(verbose_name='Mo (%)')),
                ('cu_s_fe', models.FloatField(verbose_name='CuSFe (%)')),
                ('fe_t', models.FloatField(verbose_name='FeT (%)')),
                ('zn', models.FloatField(verbose_name='Zn (%)')),
                ('ag', models.FloatField(verbose_name='Ag (g/T)')),
                ('resultado_as', models.FloatField(verbose_name='As (%)')),
                ('pb', models.FloatField(verbose_name='Pb (%)')),
                ('cu_test', models.FloatField(verbose_name='CuTest (%)')),
                ('ext', models.CharField(max_length=255, verbose_name='EXT')),
                ('cons_h', models.FloatField(verbose_name='Cons H+ (Kg/Ton)')),
                ('fecha_emision', models.DateField(verbose_name='Fecha de Emisión')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('username', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('rut', models.CharField(max_length=200, unique=True)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('rolname', models.CharField(choices=[('Supervisor', 'Supervisor'), ('Administrador', 'Administrador'), ('Quimico', 'Químico')], max_length=200)),
                ('turno', models.CharField(choices=[('Dia', 'Dia'), ('Noche', 'Noche')], max_length=200)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ingreso')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Analisis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Analisis_metodo', models.CharField(max_length=200, verbose_name='Método de análisis')),
                ('Nro_Analisis', models.CharField(max_length=200, null=True, unique=True, verbose_name='Código de análisis')),
                ('descripcion', models.CharField(max_length=255)),
                ('Formula', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Activo')),
                ('Elementos', models.ManyToManyField(blank=True, to='api.elementos', verbose_name='Elementos')),
            ],
        ),
        migrations.CreateModel(
            name='MetodoAnalisis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('metodologia', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to='api.cliente')),
                ('elementos', models.ManyToManyField(related_name='metodos_analisis', to='api.elementometodo')),
            ],
        ),
        migrations.CreateModel(
            name='ODT',
            fields=[
                ('Fec_Recep', models.DateField()),
                ('Fec_Finalizacion', models.DateField()),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Número de OT')),
                ('Prefijo', models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[api.models.validate_length], verbose_name='Muestra inicial')),
                ('Responsable', models.CharField(blank=True, max_length=200, null=True, verbose_name='Responsable envío')),
                ('Prioridad', models.CharField(blank=True, choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=200, verbose_name='Prioridad')),
                ('TipoMuestra', models.CharField(blank=True, choices=[('Sondaje', 'Sondaje'), ('Subterranea', 'Subterranea'), ('Tronadura', 'Tronadura')], max_length=200, verbose_name='Tipo de Muestra')),
                ('Referencia', models.PositiveIntegerField(blank=True, null=True, verbose_name='Batch')),
                ('Cant_Muestra', models.PositiveIntegerField(blank=True, null=True, verbose_name='Cantidad de Muestras')),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='MuestraMasificada',
            fields=[
                ('Prefijo', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('tipoMuestra', models.CharField(default='M', max_length=200)),
                ('odt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masificaciones', to='api.odt')),
            ],
        ),
        migrations.CreateModel(
            name='OT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_muestra', models.CharField(max_length=50, unique=True, verbose_name='ID Muestra')),
                ('peso_muestra', models.FloatField(verbose_name='Peso Muestra')),
                ('volumen', models.FloatField(verbose_name='Volumen')),
                ('dilucion', models.FloatField(verbose_name='Dilución')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('odt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ots', to='api.odt')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_emision', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='odt',
            name='Proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proyecto'),
        ),
        migrations.CreateModel(
            name='Muestra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_emision', models.DateField()),
                ('elemento', models.CharField(max_length=100)),
                ('nbo', models.CharField(max_length=100)),
                ('ident', models.CharField(max_length=100)),
                ('t', models.CharField(max_length=100)),
                ('peso_m', models.FloatField(verbose_name='PesoM. (g)')),
                ('v_ml', models.FloatField(verbose_name='V. mL')),
                ('l_ppm', models.FloatField(verbose_name='L. ppm')),
                ('l_ppm_bk', models.FloatField(verbose_name='L. ppm-BK')),
                ('porcentaje', models.FloatField(verbose_name='Porcentaje (%)')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proyecto')),
            ],
        ),
    ]
