from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import CommonPasswordValidator, validate_password
from .models import AnalisisCuTFeZn, AnalisisMulti, Muestra, User,AnalisisCuS4FeS4MoS4

class CustomUserCreationForm(UserCreationForm):
   
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'rut', 'username', 'is_administrador', 'is_supervisor', 'is_quimico')
     
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
        fields = ('first_name', 'last_name', 'rut', 'username', 'is_administrador', 'is_supervisor', 'is_quimico')
        
        
class MuestraForm(forms.ModelForm):
    class Meta:
        model = Muestra
        fields = ('__all__')
        
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

        
    

