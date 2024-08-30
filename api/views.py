from asyncio.log import logger
from django.conf import settings
from django.core import signing
from datetime import datetime, timedelta
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate, login
from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import AnalisisCuS4FeS4MoS4, Muestra, User , AnalisisCuTFeZn
from .forms import AnalisisCuS4FeS4MoS4Form, AnalisisCuTFeZnForm, CustomUserCreationForm, MuestraForm
from django.views.decorators.csrf import csrf_exempt
from .decorators import is_administrador, is_supervisor, is_quimico

@api_view(['GET'])
def users_list(request):
    try:
        users = User.objects.all()
        users_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_active': user.is_active,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'is_administrador': user.is_administrador,
                'is_supervisor': user.is_supervisor,
                'is_quimico': user.is_quimico,
                'is_new_user': user.is_new_user,
                'date_joined': user.date_joined,
            }
            users_list.append(user_dict)
        return JsonResponse({'users': users_list})
    except Exception as e:
        logger.error("Error fetching user list: %s", e)
        return JsonResponse({'message': 'Error al obtener usuarios'}, status=500)

@api_view(['POST'])
def login_user(request):
    try:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is None:
                return JsonResponse({'error': 'El usuario o la contraseña ingresada son incorrectas'}, status=400)
            login(request, user)
            token=generar_token(user.id)
            user.token=token
            user.save()
            first_name = user.first_name
            last_name = user.last_name
            token = user.token
            message=last_name
             
            return JsonResponse({'tipo':'success','message':message, 'first_name': first_name,'token':token})
        else:
            message='El usuario o la contraseña ingresada son incorrectas'
            return JsonResponse({'tipo':'error','message':message }, status=400)
    except Exception as e:
        message="Error al loguear usuario:"
        return JsonResponse({'tipo':'error','message':message}, status=500)
   
def generar_token(user_id):
    expiracion = datetime.utcnow() + timedelta(days=1)
    token_data = {
        'user_id': user_id,
        'exp': expiracion.timestamp()
    }
    token = signing.dumps(token_data, key=settings.SECRET_KEY)
    return token


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try: 
                user = form.save()
                first_name = user.first_name
                date_joined = user.date_joined.date()  
                current_date = datetime.now().date()
                if (current_date - date_joined).days < 30:
                    is_new_user=user.is_new_user = True
                    user.save()
                else:
                    is_new_user=user.is_new_user = False
                    user.save()
                message = f"Usuario creado correctamente: {first_name}"
                return JsonResponse({'message': message, 'tipo': 'success', 'is_new_user': is_new_user})
            except ValidationError  as e:
                message = f"Error al crear usuario: {str(e)}"
                return JsonResponse({'message': message, 'tipo': 'error'})
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f": {error}")
            return JsonResponse({'tipo': 'error', 'message': 'Error al crear usuario', 'errors': errors})
    else:
        return JsonResponse({'tipo': 'error', 'message': 'Método no permitido. Utiliza el método POST.'})
    
def laboratorio(request):
    return render(request, 'hola')

@api_view(['GET'])
def muestras(request):
        muestras = Muestra.objects.all()
        muestra_list = []
        try:
            for muestra in muestras:
                muestra_dict = {
                    'id': muestra.id,
                    'nombre': muestra.nombre,
                    'fecha_emision': muestra.fecha_emision,
                    'elemento': muestra.elemento,
                    'nbo': muestra.nbo,
                    'ident': muestra.ident,
                    't': muestra.t,
                    'peso_m': muestra.peso_m,
                    'v_ml': muestra.v_ml,
                    'l_ppm': muestra.l_ppm,
                    'l_ppm_bk': muestra.l_ppm_bk,
                    'porcentaje': muestra.porcentaje,
                    
                }
                muestra_list.append(muestra_dict)
            return JsonResponse({'muestras': muestra_list})
        except Exception as e:
            logger.error("Error fetching user list: %s", e)
            return JsonResponse({'message': 'Error al obtener muestras'}, status=500)

@api_view(['POST'])
def register_muestra(request):
    if request.method == 'POST':
        form = MuestraForm(request.POST)
        if form.is_valid():
            try: 
                muestra = form.save()
                muestra.save()
                nombre=muestra.nombre
                message = f"Muestra creada correctamente: {nombre}"
                return JsonResponse({'message': message, 'tipo': 'success'})
            except ValidationError  as e:
                message = f"Error al crear la muestra: {str(e)}"
                return JsonResponse({'message': message, 'tipo': 'error'})
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f": {error}")
            return JsonResponse({'tipo': 'error', 'message': 'Error al crear la muestra', 'errors': errors})
    else:
        return JsonResponse({'tipo': 'error', 'message': 'Método no permitido. Utiliza el método POST.'})

@api_view(['POST'])
def register_CutFeZn(request):
    if request.method == 'POST':
        data = request.POST
        form = AnalisisCuTFeZnForm(data)
     
        if form.is_valid():
            try:
                # Verificar si se está enviando un ID para actualizar el registro existente
                if 'id' in data and data['id']:
                    # Obtener el registro existente para actualizarlo
                    analisis = AnalisisCuTFeZn.objects.get(pk=data['id'])
                    form = AnalisisCuTFeZnForm(data, instance=analisis)
                    form.save()
                    message = f"Validador actualizado correctamente: Cut-Fe-Zn"
                else:
                    # Crear un nuevo registro
                    analisis = form.save()
                    message = f"Validador creado correctamente: Cut-Fe-Zn"

                return JsonResponse({'message': message, 'tipo': 'success'})

            except ValidationError as e:
                message = f"Error al procesar la muestra: {str(e)}"
                return JsonResponse({'message': message, 'tipo': 'error'})

            except AnalisisCuTFeZn.DoesNotExist:
                return JsonResponse({'message': 'El registro no existe.', 'tipo': 'error'})

        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")
            return JsonResponse({'tipo': 'error', 'message': 'Error al procesar el validador', 'errors': errors})

    return JsonResponse({'tipo': 'error', 'message': 'Método no permitido. Utiliza el método POST.'})

@api_view(['POST'])
def register_CuS4FeS4MoS4(request):
    if request.method == 'POST':
        data = request.POST
        form = AnalisisCuS4FeS4MoS4Form(data)
     
        if form.is_valid():
            try:
                # Verificar si se está enviando un ID para actualizar el registro existente
                if 'id' in data and data['id']:
                    # Obtener el registro existente para actualizarlo
                    analisis = AnalisisCuS4FeS4MoS4.objects.get(pk=data['id'])
                    form = AnalisisCuS4FeS4MoS4Form(data, instance=analisis)
                    form.save()
                    message = f"Validador actualizado correctamente: CuS4-FeS4-MoS4"
                else:
                    # Crear un nuevo registro
                    analisis = form.save()
                    message = f"Validador creado correctamente: CuS4-FeS4-MoS4"

                return JsonResponse({'message': message, 'tipo': 'success'})

            except ValidationError as e:
                message = f"Error al procesar la muestra: {str(e)}"
                return JsonResponse({'message': message, 'tipo': 'error'})

            except AnalisisCuTFeZn.DoesNotExist:
                return JsonResponse({'message': 'El registro no existe.', 'tipo': 'error'})

        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")
            return JsonResponse({'tipo': 'error', 'message': 'Error al procesar el validador', 'errors': errors})

    return JsonResponse({'tipo': 'error', 'message': 'Método no permitido. Utiliza el método POST.'})

@api_view(['GET'])
def CutFeZn(request):
        cutfezn = AnalisisCuTFeZn.objects.all()
        cutfezn_list = []
        try:
            for Cutfezn in cutfezn:
                cutfezn_dict = {
                    'id': Cutfezn.id,
                    'l_ppm_fe': Cutfezn.l_ppm_fe,
                    'l_ppm_bk_fe': Cutfezn.l_ppm_bk_fe,
                    'fe': Cutfezn.fe,
                    'l_ppm_zn': Cutfezn.l_ppm_zn,
                    'l_ppm_bk_zn': Cutfezn.l_ppm_bk_zn,
                    'zn': Cutfezn.zn
                }
                cutfezn_list.append(cutfezn_dict)
            return JsonResponse({'validacion': cutfezn_list})
        except Exception as e:
            logger.error("Error fetching validation list: %s", e)
            return JsonResponse({'message': 'Error al obtener la validación'}, status=500)

@api_view(['GET'])
def CuS4FeS4MoS4(request):
        CuS4FeS4MoS4 = AnalisisCuS4FeS4MoS4.objects.all()
        CuS4FeS4MoS4_list = []
        try:
            for cuS4FeS4MoS4 in CuS4FeS4MoS4:
                CuS4FeS4MoS4_dict = {
                    'id': cuS4FeS4MoS4.id,
                    'control1_cut_cus': cuS4FeS4MoS4.control1_cut_cus,
                    'l_ppm_cus_fe': cuS4FeS4MoS4.l_ppm_cus_fe,
                    'l_ppm_bk_fes4': cuS4FeS4MoS4.l_ppm_bk_fes4,
                    'fes4': cuS4FeS4MoS4.fes4,
                    'control2_cut_fes4': cuS4FeS4MoS4.control2_cut_fes4,
                }
                CuS4FeS4MoS4_list.append(CuS4FeS4MoS4_dict)
            return JsonResponse({'validacion': CuS4FeS4MoS4_list})
        except Exception as e:
            logger.error("Error fetching validation list: %s", e)
            return JsonResponse({'message': 'Error al obtener la validación'}, status=500)
        
        