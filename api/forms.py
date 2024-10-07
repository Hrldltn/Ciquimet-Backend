from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import CommonPasswordValidator, validate_password
from .models import AnalisisCuTFeZn, AnalisisMulti, Cliente, MetodoAnalisis, Muestra, Proyecto, User,AnalisisCuS4FeS4MoS4,ODT,ElementoMetodo

class CustomUserCreationForm(UserCreationForm):
   
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'rut', 'username', 'rolname','turno')
     
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(('Este correo electrónico ya está en uso.'))
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            try:
                validate_password(password1, self.instance)
            except forms.ValidationError as error:
                raise forms.ValidationError(error)
            common_validator = CommonPasswordValidator()
            try:
                common_validator.validate(password1)
            except forms.ValidationError:
                raise forms.ValidationError(("La contraseña es demasiado común."))
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(("Las contraseñas no coinciden."))
        return password2
    
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'rut', 'username', 'rolname','turno')
        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('__all__')
        
class MuestraForm(forms.ModelForm):
    class Meta:
        model = Muestra
        fields = ['nombre', 'proyecto', 'fecha_emision', 'elemento', 'nbo', 'ident', 't', 'peso_m', 'v_ml', 'l_ppm', 'l_ppm_bk', 'porcentaje']

        
class AnalisisCuTFeZnForm(forms.ModelForm):
    class Meta:
        model = AnalisisCuTFeZn
        fields = ('__all__')
        
class AnalisisCuS4FeS4MoS4Form(forms.ModelForm):
    class Meta:
        model = AnalisisCuS4FeS4MoS4
        fields = ('__all__')
        
class AnalisisMultiForm(forms.ModelForm):
    class Meta:
        model = AnalisisMulti
        fields = ('__all__')
        
class ODTForm(forms.ModelForm):
    class Meta:
        model = ODT
        fields='__all__'
        exclude = ['id']  # Excluir Nro_OT del formulario, ya que se genera automáticamente

   
class ElementoMetodoForm(forms.ModelForm):
    class Meta:
        model = ElementoMetodo
        fields = ('__all__')
        
class MetodoAnalisisForm(forms.ModelForm):
    class Meta:
        model = MetodoAnalisis
        fields = ('__all__')