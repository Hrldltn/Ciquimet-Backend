# Generated by Django 5.0.4 on 2024-06-29 00:49

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
            name='Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Muestra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_emision', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=255)),
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
                ('rut', models.CharField(blank=True, max_length=200, null=True)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('is_administrador', models.BooleanField(default=False, verbose_name='Administrador')),
                ('is_supervisor', models.BooleanField(default=False, verbose_name='is_supervisor')),
                ('is_quimico', models.BooleanField(default=False, verbose_name='is_quimico')),
                ('is_cliente', models.BooleanField(default=False, verbose_name='is_cliente')),
                ('is_new_user', models.CharField(blank=True, max_length=200, null=True)),
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
            name='AnalisisMulti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_ppm_ag', models.FloatField(blank=True, null=True, verbose_name='L. ppm Ag')),
                ('l_ppm_ag_bk', models.FloatField(blank=True, null=True, verbose_name='L. ppm Ag-bk')),
                ('ag', models.FloatField(blank=True, null=True, verbose_name='Ag (ppm)')),
                ('l_ppm_as', models.FloatField(blank=True, null=True, verbose_name='L. ppm As')),
                ('l_ppm_as_bk', models.FloatField(blank=True, null=True, verbose_name='L. ppm As-bk')),
                ('analisis_as', models.FloatField(blank=True, null=True, verbose_name='As (%)')),
                ('l_ppm_mo', models.FloatField(blank=True, null=True, verbose_name='L. ppm Mo')),
                ('l_ppm_mo_bk', models.FloatField(blank=True, null=True, verbose_name='L. ppm Mo-bk')),
                ('mo', models.FloatField(blank=True, null=True, verbose_name='Mo (%)')),
                ('l_ppm_pb', models.FloatField(blank=True, null=True, verbose_name='L. ppm Pb')),
                ('l_ppm_pb_bk', models.FloatField(blank=True, null=True, verbose_name='L. ppm Pb-Bk')),
                ('pb', models.FloatField(blank=True, null=True, verbose_name='Pb (%)')),
                ('l_ppm_cu', models.FloatField(blank=True, null=True, verbose_name='L. ppm Cu')),
                ('l_ppm_cu_bk', models.FloatField(blank=True, null=True, verbose_name='L. ppm Cu-bk')),
                ('cu', models.FloatField(blank=True, null=True, verbose_name='Cu (%)')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analisis_multi', to='api.muestra')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuTFeZn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_ppm_fe', models.FloatField(blank=True, null=True, verbose_name='L. ppm Fe')),
                ('l_ppm_bk_fe', models.FloatField(blank=True, null=True, verbose_name='L. ppm-BK Fe')),
                ('fe', models.FloatField(blank=True, null=True, verbose_name='Fe (%)')),
                ('l_ppm_zn', models.FloatField(blank=True, null=True, verbose_name='L. ppm Zn')),
                ('l_ppm_bk_zn', models.FloatField(blank=True, null=True, verbose_name='L. ppm-Bk Zn')),
                ('zn', models.FloatField(blank=True, null=True, verbose_name='Zn (%)')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analisis_cutfezn', to='api.muestra')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuTestConsH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control1_cut_cutest', models.FloatField(blank=True, null=True, verbose_name='Control1 CuT-CuTest')),
                ('cut', models.FloatField(blank=True, null=True, verbose_name='CuT')),
                ('cut_test', models.FloatField(blank=True, null=True, verbose_name='CuTest')),
                ('gaston_ml', models.FloatField(blank=True, null=True, verbose_name='Gaston mL')),
                ('gasto_bk_ml', models.FloatField(blank=True, null=True, verbose_name='Gasto Bk mL')),
                ('n_naco3', models.FloatField(blank=True, null=True, verbose_name='N NaCO3')),
                ('alicuota', models.FloatField(blank=True, null=True, verbose_name='Alicuota')),
                ('consumo_h', models.FloatField(blank=True, null=True, verbose_name='Consumo H+')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analisis_cutestconsh', to='api.muestra')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuSCuSFe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_ppm_cus_fe', models.FloatField(blank=True, null=True, verbose_name='L. ppm CuSFe')),
                ('l_ppm_bk_cus_fe', models.FloatField(blank=True, null=True, verbose_name='L. ppm-Bk CuSFe')),
                ('cus_fe', models.FloatField(blank=True, null=True, verbose_name='CuSFe (%)')),
                ('control2_cut_cus_fe', models.FloatField(blank=True, null=True, verbose_name='Control2 CuT-CuSFe')),
                ('cut', models.FloatField(blank=True, null=True, verbose_name='CuT')),
                ('cus_c', models.FloatField(blank=True, null=True, verbose_name='CuSC')),
                ('cus_fe_2', models.FloatField(blank=True, null=True, verbose_name='CuSFe')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analisis_cuscusfe', to='api.muestra')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuS4FeS4MoS4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control1_cut_cus', models.FloatField(blank=True, null=True, verbose_name='Control1 CuT-CuS')),
                ('l_ppm_cus_fe', models.FloatField(blank=True, null=True, verbose_name='L. ppm CusFe')),
                ('l_ppm_bk_fes4', models.FloatField(blank=True, null=True, verbose_name='L. ppm-BK FeS4')),
                ('fes4', models.FloatField(blank=True, null=True, verbose_name='FeS4 (%)')),
                ('control2_cut_fes4', models.FloatField(blank=True, null=True, verbose_name='Control2 CuT-FeS4')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analisis_cus4fes4mos4', to='api.muestra')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisCuS10FeS10MoS10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_cut_cus', models.FloatField(blank=True, null=True, verbose_name='Control CuT-CuS')),
                ('cut', models.FloatField(blank=True, null=True, verbose_name='CuT')),
                ('cus10', models.FloatField(blank=True, null=True, verbose_name='CuS10')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analisis_cus10fes10mos10', to='api.muestra')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb', models.CharField(max_length=100)),
                ('cu_t', models.FloatField(blank=True, null=True, verbose_name='CuT (%)')),
                ('cu_s4', models.FloatField(blank=True, null=True, verbose_name='CuS4 (%)')),
                ('cu_s10', models.FloatField(blank=True, null=True, verbose_name='CuS10 (%)')),
                ('mo', models.FloatField(blank=True, null=True, verbose_name='Mo (%)')),
                ('cu_s_fe', models.FloatField(blank=True, null=True, verbose_name='CuSFe (%)')),
                ('fe_t', models.FloatField(blank=True, null=True, verbose_name='FeT (%)')),
                ('zn', models.FloatField(blank=True, null=True, verbose_name='Zn (%)')),
                ('ag', models.FloatField(blank=True, null=True, verbose_name='Ag (g/T)')),
                ('resultado_as', models.FloatField(blank=True, null=True, verbose_name='As (%)')),
                ('pb', models.FloatField(blank=True, null=True, verbose_name='Pb (%)')),
                ('cu_test', models.FloatField(blank=True, null=True, verbose_name='CuTest (%)')),
                ('ext', models.CharField(blank=True, max_length=255, null=True, verbose_name='EXT')),
                ('cons_h', models.FloatField(blank=True, null=True, verbose_name='Cons H+ (Kg/Ton)')),
                ('fecha_emision', models.DateField(blank=True, null=True, verbose_name='Fecha de Emisión')),
                ('muestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='api.muestra')),
            ],
        ),
    ]
