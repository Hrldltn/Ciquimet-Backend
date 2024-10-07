from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext as _

# Modelo para almacenar los usuarios
class User(AbstractUser):
    class Role(models.TextChoices):
            SUPERVISOR = 'Supervisor', _('Supervisor')
            ADMINISTRADOR = 'Administrador', _('Administrador')
            QUIMICO = 'Quimico', _('Químico')
    
    class Turno(models.TextChoices):
        DIA = 'Dia', _('Dia')
        NOCHE = 'Noche', _('Noche')
            
    username = models.EmailField(_('Correo'), unique=True, null=False, blank=False)
    rut = models.CharField(max_length=200, unique=True, null=False, blank=False)
    token = models.CharField(max_length=200, null=True, blank=True)  # Único campo opcional
    rolname = models.CharField(max_length=200, choices=Role.choices)
    turno = models.CharField(max_length=200, choices=Turno.choices)
    date_joined = models.DateTimeField(_('Fecha de ingreso'), auto_now_add=True)
    
    def _str_(self):
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



def validate_length(value):
    if len(str(value)) != 9:
        raise ValidationError('El número debe tener exactamente 9 dígitos.')


class ODT(models.Model):
    class T_MUESTRA(models.TextChoices):
        SONDAJE = 'Sondaje', _('Sondaje')
        SUBTERRANEA = 'Subterranea', _('Subterranea')
        TRONADURA = 'Tronadura', _('Tronadura')

    class PrioridadChoice(models.TextChoices):
        ALTA = 'Alta', _('Alta')
        MEDIA = 'Media', _('Media')
        BAJA = 'Baja', _('Baja')

    Fec_Recep = models.DateField()
    Fec_Finalizacion = models.DateField()
    id = models.CharField(_("Número de OT"), max_length=200, unique=True, primary_key=True)
    Prefijo = models.PositiveIntegerField(_("Muestra inicial"), blank=True, null=True)
    Cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=False, blank=False)
    Proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, null=False, blank=False)
    Responsable = models.CharField(_("Responsable envío"), max_length=200, blank=True, null=True)
    Prioridad = models.CharField(_("Prioridad"), max_length=200, choices=PrioridadChoice.choices, blank=True)
    TipoMuestra = models.CharField(_("Tipo de Muestra"), max_length=200, choices=T_MUESTRA.choices, blank=True)
    Referencia = models.PositiveIntegerField(_("Batch"), blank=True, null=True)
    Comentarios = models.CharField(max_length=255, blank=True)
    Cant_Muestra = models.PositiveIntegerField(_("Cantidad de Muestras"), blank=True, null=True)

    def save(self, *args, **kwargs):
        # Solo generar un nuevo ID si la instancia no tiene un ID asignado (es un nuevo registro)
        if self._state.adding and not self.id:
            last_odt = ODT.objects.order_by('-id').first()
            if last_odt:
                try:
                    last_number = int(last_odt.id[3:])
                    new_number = last_number + 1
                except ValueError:
                    new_number = 1
            else:
                new_number = 1
            self.id = f'WSS{new_number:06d}'
        
        super().save(*args, **kwargs)
    
class MuestraMasificada(models.Model):
    odt = models.ForeignKey(ODT, on_delete=models.CASCADE, related_name='masificaciones')
    Prefijo = models.CharField(max_length=200, unique=True, primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tipoMuestra = models.CharField(max_length=200 ,default='M')

    def __str__(self):
        return f'Muestra {self.Prefijo} para ODT {self.odt.Nro_OT}'
    


class ElementoMetodo(models.Model):
    nombre = models.CharField(max_length=200)
    gramos = models.FloatField()
    miligramos = models.FloatField()

    def __str__(self):
        return f"{self.nombre} ({self.gramos}g / {self.miligramos}ml)"

class MetodoAnalisis(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name="metodos_analisis")
    nombre = models.CharField(max_length=200)
    metodologia = models.TextField()
    elementos = models.ManyToManyField(ElementoMetodo, related_name="metodos_analisis")

    class Meta:
        unique_together = ('cliente', 'nombre')
    
    def __str__(self):
        return f"Metodo {self.nombre}"


class Analisis(models.Model):
    id = models.AutoField(primary_key=True)
    Analisis_metodo = models.CharField(_("Método de análisis"), max_length=200)
    Nro_Analisis = models.CharField(_("Código de análisis"), max_length=200, unique=True, null=True)
    descripcion = models.CharField(max_length=255)
    Formula = models.CharField(max_length=255)
    Elementos = models.ManyToManyField('Elementos', verbose_name=_("Elementos"), blank=True)  # Relación con Elementos
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última modificación
    enabled = models.BooleanField(_("Activo"), default=True)

    def __str__(self):
        return self.Analisis_metodo


class Elementos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(_("Nombre"), max_length=200)
    tipo = models.CharField(max_length=200)
    simbolo = models.CharField(max_length=5, blank=True, null=True)
    numero_atomico = models.IntegerField(blank=True, null=True) 
    masa_atomica = models.FloatField(blank=True, null=True)
    enabled = models.BooleanField(_("Activo"), default=True)
    descripcion = models.TextField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última modificación

    def __str__(self):
        return self.nombre

class OT(models.Model):
    id = models.AutoField(primary_key=True)
    id_muestra = models.CharField(_("ID Muestra"), max_length=50, unique=True)
    peso_muestra = models.FloatField(_("Peso Muestra"))
    volumen = models.FloatField(_("Volumen"))
    dilucion = models.FloatField(_("Dilución"))
    odt = models.ForeignKey(ODT, on_delete=models.CASCADE, related_name="ots")
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última modificación

    def __str__(self):
        return self.id_muestra

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
