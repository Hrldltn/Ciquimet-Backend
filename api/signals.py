from django.db import IntegrityError
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from .models import ODT, MuestraMasificada



@receiver(post_save, sender=ODT)
def crear_muestras_masificadas(sender, instance, created, **kwargs):
    if created and instance.Cant_Muestra and instance.Prefijo:
        base_prefix = str(instance.Prefijo)[:7]
        start_suffix = int(str(instance.Prefijo)[7:])
        
        # Crear las muestras masificadas
        for i in range(instance.Cant_Muestra):
            unique_suffix = start_suffix + i
            try:
                muestra = MuestraMasificada.objects.create(
                    odt=instance,
                    Prefijo=f'{base_prefix}{unique_suffix}',
                )
                print(f"Creada MuestraMasificada con Prefijo: {muestra.Prefijo}")
            except IntegrityError as e:
                print(f"Error al crear MuestraMasificada con Prefijo {base_prefix}{unique_suffix}: {str(e)}")
            except Exception as e:
                print(f"Error inesperado al crear MuestraMasificada: {str(e)}")
                
                

@receiver(pre_save, sender=ODT)
def set_odt_id(sender, instance, **kwargs):
    if not instance.id:
        # Obtener el último `Nro_OT` y generar el nuevo valor
        last_odt = ODT.objects.order_by('-id').first()
        if last_odt:
            try:
                last_number = int(last_odt.id[3:])
                new_number = last_number + 1
            except ValueError:
                new_number = 1
        else:
            new_number = 1
        instance.id = f'WSS{new_number:06d}' 