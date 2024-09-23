from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

# Modelo para almacenar los usuarios
class User(AbstractUser):
    username = models.EmailField(_('Correo'), unique=True, null=False, blank=False)
    rut = models.CharField(max_length=200, unique=True, null=False, blank=False)
    token = models.CharField(max_length=200, null=True, blank=True)  # Único campo opcional
    is_administrador = models.BooleanField('Administrador', default=False)
    is_supervisor = models.BooleanField('Supervisor', default=False)
    is_quimico = models.BooleanField('Químico', default=False)
    is_new_user = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(_('Fecha de ingreso'), auto_now_add=True)
    
    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name

# Modelo para almacenar los clientes y proyectos
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=False, blank=False)
    fecha_emision = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return self.cliente.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    rut = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self):
        return self.nombre

# Modelo general para almacenar asociadas a una muestra de análisis
class Muestra(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=False, blank=False)
    fecha_emision = models.DateField(null=False, blank=False)
    elemento = models.CharField(max_length=100, null=False, blank=False)
    nbo = models.CharField(max_length=100, null=False, blank=False)
    ident = models.CharField(max_length=100, null=False, blank=False)
    t = models.CharField(max_length=100, null=False, blank=False)
    peso_m = models.FloatField(verbose_name="PesoM. (g)", null=False, blank=False)
    v_ml = models.FloatField(verbose_name="V. mL", null=False, blank=False)
    l_ppm = models.FloatField(verbose_name="L. ppm", null=False, blank=False)
    l_ppm_bk = models.FloatField(verbose_name="L. ppm-BK", null=False, blank=False)
    porcentaje = models.FloatField(verbose_name="Porcentaje (%)", null=False, blank=False)
    
    def __str__(self):
        return f"Muestra {self.nombre} de {self.elemento}"

# Modelos específicos para los diferentes tipos de análisis
class AnalisisCuTFeZn(models.Model):
    l_ppm_fe = models.FloatField(verbose_name="L. ppm Fe", null=False, blank=False)
    l_ppm_bk_fe = models.FloatField(verbose_name="L. ppm-BK Fe", null=False, blank=False)
    fe = models.FloatField(verbose_name="Fe (%)", null=False, blank=False)
    l_ppm_zn = models.FloatField(verbose_name="L. ppm Zn", null=False, blank=False)
    l_ppm_bk_zn = models.FloatField(verbose_name="L. ppm-BK Zn", null=False, blank=False)
    zn = models.FloatField(verbose_name="Zn (%)", null=False, blank=False)
    
    def __str__(self):
        return f"Análisis CuT-Fe-Zn"

class AnalisisCuS4FeS4MoS4(models.Model):
    control1_cut_cus = models.FloatField(verbose_name="Control1 CuT-CuS", null=False, blank=False)
    l_ppm_cus_fe = models.FloatField(verbose_name="L. ppm CusFe", null=False, blank=False)
    l_ppm_bk_fes4 = models.FloatField(verbose_name="L. ppm-BK FeS4", null=False, blank=False)
    fes4 = models.FloatField(verbose_name="FeS4 (%)", null=False, blank=False)
    control2_cut_fes4 = models.FloatField(verbose_name="Control2 CuT-FeS4", null=False, blank=False)
    
    def __str__(self):
        return f"Análisis CuS4-FeS4-MoS4"

class AnalisisMulti(models.Model):
    l_ppm_ag = models.FloatField(verbose_name="L. ppm Ag", null=False, blank=False)
    l_ppm_ag_bk = models.FloatField(verbose_name="L. ppm Ag-bk", null=False, blank=False)
    ag = models.FloatField(verbose_name="Ag (ppm)", null=False, blank=False)
    l_ppm_as = models.FloatField(verbose_name="L. ppm As", null=False, blank=False)
    l_ppm_as_bk = models.FloatField(verbose_name="L. ppm As-bk", null=False, blank=False)
    analisis_as = models.FloatField(verbose_name="As (%)", null=False, blank=False)
    l_ppm_mo = models.FloatField(verbose_name="L. ppm Mo", null=False, blank=False)
    l_ppm_mo_bk = models.FloatField(verbose_name="L. ppm Mo-bk", null=False, blank=False)
    mo = models.FloatField(verbose_name="Mo (%)", null=False, blank=False)
    l_ppm_pb = models.FloatField(verbose_name="L. ppm Pb", null=False, blank=False)
    l_ppm_pb_bk = models.FloatField(verbose_name="L. ppm Pb-Bk", null=False, blank=False)
    pb = models.FloatField(verbose_name="Pb (%)", null=False, blank=False)
    l_ppm_cu = models.FloatField(verbose_name="L. ppm Cu", null=False, blank=False)
    l_ppm_cu_bk = models.FloatField(verbose_name="L. ppm Cu-bk", null=False, blank=False)
    cu = models.FloatField(verbose_name="Cu (%)", null=False, blank=False)
    
    def __str__(self):
        return f"Análisis Multi"

class AnalisisCuS10FeS10MoS10(models.Model):
    control_cut_cus = models.FloatField(verbose_name="Control CuT-CuS", null=False, blank=False)
    cut = models.FloatField(verbose_name="CuT", null=False, blank=False)
    cus10 = models.FloatField(verbose_name="CuS10", null=False, blank=False)
    
    def __str__(self):
        return f"Análisis CuS10-FeS10-MoS10"

class AnalisisCuSCuSFe(models.Model):
    l_ppm_cus_fe = models.FloatField(verbose_name="L. ppm CuSFe", null=False, blank=False)
    l_ppm_bk_cus_fe = models.FloatField(verbose_name="L. ppm-Bk CuSFe", null=False, blank=False)
    cus_fe = models.FloatField(verbose_name="CuSFe (%)", null=False, blank=False)
    control2_cut_cus_fe = models.FloatField(verbose_name="Control2 CuT-CuSFe", null=False, blank=False)
    cut = models.FloatField(verbose_name="CuT", null=False, blank=False)
    cus_c = models.FloatField(verbose_name="CuSC", null=False, blank=False)
    cus_fe_2 = models.FloatField(verbose_name="CuSFe", null=False, blank=False)
    
    def __str__(self):
        return f"Análisis CuS3-CuSFe"

class AnalisisCuTestConsH(models.Model):
    control1_cut_cutest = models.FloatField(verbose_name="Control1 CuT-CuTest", null=False, blank=False)
    cut = models.FloatField(verbose_name="CuT", null=False, blank=False)
    cut_test = models.FloatField(verbose_name="CuTest", null=False, blank=False)
    gaston_ml = models.FloatField(verbose_name="Gaston mL", null=False, blank=False)
    gasto_bk_ml = models.FloatField(verbose_name="Gasto Bk mL", null=False, blank=False)
    n_naco3 = models.FloatField(verbose_name="N NaCO3", null=False, blank=False)
    alicuota = models.FloatField(verbose_name="Alicuota", null=False, blank=False)
    consumo_h = models.FloatField(verbose_name="Consumo H+", null=False, blank=False)
    
    def __str__(self):
        return f"Análisis CuTest-ConsH"

# Modelo para almacenar los resultados

class Resultado(models.Model):
    nb = models.CharField(max_length=100, null=False, blank=False)
    cu_t = models.FloatField(verbose_name="CuT (%)", null=False, blank=False)
    cu_s4 = models.FloatField(verbose_name="CuS4 (%)", null=False, blank=False)
    cu_s10 = models.FloatField(verbose_name="CuS10 (%)", null=False, blank=False)
    mo = models.FloatField(verbose_name="Mo (%)", null=False, blank=False)
    cu_s_fe = models.FloatField(verbose_name="CuSFe (%)", null=False, blank=False)
    fe_t = models.FloatField(verbose_name="FeT (%)", null=False, blank=False)
    zn = models.FloatField(verbose_name="Zn (%)", null=False, blank=False)
    ag = models.FloatField(verbose_name="Ag (g/T)", null=False, blank=False)
    resultado_as = models.FloatField(verbose_name="As (%)", null=False, blank=False)
    pb = models.FloatField(verbose_name="Pb (%)", null=False, blank=False)
    cu_test = models.FloatField(verbose_name="CuTest (%)", null=False, blank=False)
    ext = models.CharField(max_length=255, verbose_name="EXT", null=False, blank=False)
    cons_h = models.FloatField(verbose_name="Cons H+ (Kg/Ton)", null=False, blank=False)
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión", null=False, blank=False)



# import uuid
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext as _

# # Modelo para almacenar los usuarios
# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     username = models.EmailField(_('Correo'), unique=True, null=False, blank=False)
#     rut = models.CharField(max_length=200, unique=True, null=False, blank=False)
#     token = models.CharField(max_length=200, null=True, blank=True)
#     is_administrador = models.BooleanField('Administrador', default=False)
#     is_supervisor = models.BooleanField('Supervisor', default=False)
#     is_quimico = models.BooleanField('Químico', default=False)
#     is_new_user = models.CharField(max_length=200, null=False, blank=False)
#     date_joined = models.DateTimeField(_('Fecha de ingreso'), auto_now_add=True)
    
#     def __str__(self):
#         name = self.first_name + ' ' + self.last_name
#         return name

# # Modelo para almacenar los clientes y proyectos
# class Proyecto(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nombre = models.CharField(max_length=100, null=False, blank=False)
#     cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=False, blank=False)
#     fecha_emision = models.DateField(null=False, blank=False)
    
#     def __str__(self):
#         return self.cliente.nombre

# class Cliente(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nombre = models.CharField(max_length=100, null=False, blank=False)
#     rut = models.CharField(max_length=100, null=False, blank=False)
#     direccion = models.CharField(max_length=100, null=False, blank=False)
#     telefono = models.CharField(max_length=100, null=False, blank=False)
#     email = models.EmailField(null=False, blank=False)
    
#     def __str__(self):
#         return self.nombre

# # Modelo general para almacenar asociadas a una muestra de análisis
# class Muestra(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nombre = models.CharField(max_length=100, null=False, blank=False)
#     proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=False, blank=False)
#     fecha_emision = models.DateField(null=False, blank=False)
#     elemento = models.CharField(max_length=100, null=False, blank=False)
#     nbo = models.CharField(max_length=100, null=False, blank=False)
#     ident = models.CharField(max_length=100, null=False, blank=False)
#     t = models.CharField(max_length=100, null=False, blank=False)
#     peso_m = models.FloatField(verbose_name="PesoM. (g)", null=False, blank=False)
#     v_ml = models.FloatField(verbose_name="V. mL", null=False, blank=False)
#     l_ppm = models.FloatField(verbose_name="L. ppm", null=False, blank=False)
#     l_ppm_bk = models.FloatField(verbose_name="L. ppm-BK", null=False, blank=False)
#     porcentaje = models.FloatField(verbose_name="Porcentaje (%)", null=False, blank=False)
    
#     def __str__(self):
#         return f"Muestra {self.nombre} de {self.elemento}"

# # Modelos específicos para los diferentes tipos de análisis
# class AnalisisCuTFeZn(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     l_ppm_fe = models.FloatField(verbose_name="L. ppm Fe", null=False, blank=False)
#     l_ppm_bk_fe = models.FloatField(verbose_name="L. ppm-BK Fe", null=False, blank=False)
#     fe = models.FloatField(verbose_name="Fe (%)", null=False, blank=False)
#     l_ppm_zn = models.FloatField(verbose_name="L. ppm Zn", null=False, blank=False)
#     l_ppm_bk_zn = models.FloatField(verbose_name="L. ppm-BK Zn", null=False, blank=False)
#     zn = models.FloatField(verbose_name="Zn (%)", null=False, blank=False)
    
#     def __str__(self):
#         return f"Análisis CuT-Fe-Zn"

# class AnalisisCuS4FeS4MoS4(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     control1_cut_cus = models.FloatField(verbose_name="Control1 CuT-CuS", null=False, blank=False)
#     l_ppm_cus_fe = models.FloatField(verbose_name="L. ppm CusFe", null=False, blank=False)
#     l_ppm_bk_fes4 = models.FloatField(verbose_name="L. ppm-BK FeS4", null=False, blank=False)
#     fes4 = models.FloatField(verbose_name="FeS4 (%)", null=False, blank=False)
#     control2_cut_fes4 = models.FloatField(verbose_name="Control2 CuT-FeS4", null=False, blank=False)
    
#     def __str__(self):
#         return f"Análisis CuS4-FeS4-MoS4"

# class AnalisisMulti(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     l_ppm_ag = models.FloatField(verbose_name="L. ppm Ag", null=False, blank=False)
#     l_ppm_ag_bk = models.FloatField(verbose_name="L. ppm Ag-bk", null=False, blank=False)
#     ag = models.FloatField(verbose_name="Ag (ppm)", null=False, blank=False)
#     l_ppm_as = models.FloatField(verbose_name="L. ppm As", null=False, blank=False)
#     l_ppm_as_bk = models.FloatField(verbose_name="L. ppm As-bk", null=False, blank=False)
#     analisis_as = models.FloatField(verbose_name="As (%)", null=False, blank=False)
#     l_ppm_mo = models.FloatField(verbose_name="L. ppm Mo", null=False, blank=False)
#     l_ppm_mo_bk = models.FloatField(verbose_name="L. ppm Mo-bk", null=False, blank=False)
#     mo = models.FloatField(verbose_name="Mo (%)", null=False, blank=False)
#     l_ppm_pb = models.FloatField(verbose_name="L. ppm Pb", null=False, blank=False)
#     l_ppm_pb_bk = models.FloatField(verbose_name="L. ppm Pb-Bk", null=False, blank=False)
#     pb = models.FloatField(verbose_name="Pb (%)", null=False, blank=False)
#     l_ppm_cu = models.FloatField(verbose_name="L. ppm Cu", null=False, blank=False)
#     l_ppm_cu_bk = models.FloatField(verbose_name="L. ppm Cu-bk", null=False, blank=False)
#     cu = models.FloatField(verbose_name="Cu (%)", null=False, blank=False)
    
#     def __str__(self):
#         return f"Análisis Multi"

# class AnalisisCuS10FeS10MoS10(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     control_cut_cus = models.FloatField(verbose_name="Control CuT-CuS", null=False, blank=False)
#     cut = models.FloatField(verbose_name="CuT", null=False, blank=False)
#     cus10 = models.FloatField(verbose_name="CuS10", null=False, blank=False)
    
#     def __str__(self):
#         return f"Análisis CuS10-FeS10-MoS10"

# class AnalisisCuSCuSFe(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     l_ppm_cus_fe = models.FloatField(verbose_name="L. ppm CuSFe", null=False, blank=False)
#     l_ppm_bk_cus_fe = models.FloatField(verbose_name="L. ppm-Bk CuSFe", null=False, blank=False)
#     cus_fe = models.FloatField(verbose_name="CuSFe (%)", null=False, blank=False)
#     control2_cut_cus_fe = models.FloatField(verbose_name="Control2 CuT-CuSFe", null=False, blank=False)
#     cut = models.FloatField(verbose_name="CuT", null=False, blank=False)
#     cus_c = models.FloatField(verbose_name="CuSC", null=False, blank=False)
#     cus_fe_2 = models.FloatField(verbose_name="CuSFe", null=False, blank=False)
    
#     def __str__(self):
#         return f"Análisis CuS3-CuSFe"

# class AnalisisCuTestConsH(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     control1_cut_cutest = models.FloatField(verbose_name="Control1 CuT-CuTest", null=False, blank=False)
#     cut = models.FloatField(verbose_name="CuT", null=False, blank=False)
#     cut_test = models.FloatField(verbose_name="CuTest", null=False, blank=False)
#     gaston_ml = models.FloatField(verbose_name="Gaston mL", null=False, blank=False)
#     gasto_bk_ml = models.FloatField(verbose_name="Gasto Bk mL", null=False, blank=False)
#     n_naco3 = models.FloatField(verbose_name="N NaCO3", null=False, blank=False)
#     alicuota = models.FloatField(verbose_name="Alicuota", null=False, blank=False)
#     consumo_h = models.FloatField(verbose_name="Consumo H+", null=False, blank=False)
    
#     def __str__(self):
#         return f"Análisis CuTest-ConsH"

# # Modelo para almacenar los resultados
# class Resultado(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nb = models.CharField(max_length=100, null=False, blank=False)
#     cu_t = models.FloatField(verbose_name="CuT (%)", null=False, blank=False)
#     cu_s4 = models.FloatField(verbose_name="CuS4 (%)", null=False, blank=False)
#     cu_s10 = models.FloatField(verbose_name="CuS10 (%)", null=False, blank=False)
#     mo = models.FloatField(verbose_name="Mo (%)", null=False, blank=False)
#     cu_s_fe = models.FloatField(verbose_name="CuSFe (%)", null=False, blank=False)
#     fe_t = models.FloatField(verbose_name="FeT (%)", null=False, blank=False)
#     zn = models.FloatField(verbose_name="Zn (%)", null=False, blank=False)
#     ag = models.FloatField(verbose_name="Ag (g/T)", null=False, blank=False)
#     resultado_as = models.FloatField(verbose_name="As (%)", null=False, blank=False)
#     pb = models.FloatField(verbose_name="Pb (%)", null=False, blank=False)
#     cu_test = models.FloatField(verbose_name="CuTest (%)", null=False, blank=False)
#     ext = models.CharField(max_length=255, verbose_name="EXT", null=False, blank=False)
#     cons_h = models.FloatField(verbose_name="Cons H+ (Kg/Ton)", null=False, blank=False)
#     fecha_emision = models.DateField(verbose_name="Fecha de Emisión", null=False, blank=False)
    
#     def __str__(self):
#         return f"Resultado {self.nb}"

# # Modelo para almacenar los parámetros
# class Parametro(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nombre = models.CharField(max_length=100, null=False, blank=False)
#     valor = models.CharField(max_length=255, null=False, blank=False)
    
#     def __str__(self):
#         return self.nombre
