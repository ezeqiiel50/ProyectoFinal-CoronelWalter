from django import forms
from AppShortStories.models import Genero, ShortStories, Profile, Mensaje
from django.contrib.auth.forms import UserCreationForm, User,AuthenticationForm

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['descripcion','estado']
        labels = {
            'descripcion' : 'Descripcion del Genero',
            'estado' : 'Activo',
        }
        widgets = {
            'descripcion' : forms.TextInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un genero',
                    'autocomplete': 'off'
                }),
            'estado' : forms.CheckboxInput(
                attrs={
                    'class' : 'form-check-input'
                })
        }

class ShortForm(forms.ModelForm):
     def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['titulo'].widget.attrs['autofocus'] = True
        self.fields['genero'].queryset = Genero.objects.filter( estado = True)

     class Meta:
        model = ShortStories
        fields = ['titulo','genero','estado','texto','imagen']
        labels = {
            'titulo' : 'Titulo',
            'genero' : 'Genero',
            'estado' : 'Privado',
            'texto' : 'Cuento',
            'imagen' : 'Selecione una imagen representativa',
        }
        widgets = {
            'titulo' : forms.TextInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un Titulo',
                    'autocomplete' : 'off'
                }),
            'genero' : forms.Select(
                attrs ={
                    'class' : 'form-select',
                }),
            'estado' : forms.CheckboxInput(
                attrs={
                    'class' : 'form-check-input'
                }),
            'texto' : forms.Textarea(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un Cuento corto',
                })
        }

class BuscarGeneroform(forms.Form):
    criterio_descripcion = forms.CharField(max_length=50)

class BuscarStoriesform(forms.Form):
    criterio_titulo = forms.CharField(max_length=50)

class UserReistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['username','password1','password2' ]
        widgets = {
            'username' : forms.TextInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un usuario',
                    'autocomplete' : 'off'
                })
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Ingrese su usuario', 'autocomplete' : 'off'}))
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingrese su contraseña', 'autocomplete' : 'off'}))

class ProfileForm(forms.ModelForm):
     def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True

     class Meta:
        model = Profile
        fields = ['nombre','apellido','email','telefono','imagen']
        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'email' : 'Email',
            'telefono' : 'Tel',
            'imagen' : 'Selecione una imagen representativa',
        }
        widgets = {
            'nombre' : forms.TextInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su Nombre'
                }),
            'apellido' : forms.TextInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su Apellido'
                }),
            'telefono' : forms.NumberInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un Telefono',
                    'min':'0',
                    'max':'9999999999',
                    'pattern':'[0-9.]+'
                }),
            'email' : forms.EmailInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un email'
                }),
        }
class BuscarMensajeform(forms.Form):
    criterio_mensaje = forms.CharField(max_length=50)

class MensajeForm(forms.ModelForm):
     def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['email'].widget.attrs['autofocus'] = True

     class Meta:
        model = Mensaje
        fields = ['email','motivo','mensaje']
        labels = {
            'email' : 'Email',
            'mensaje' : 'Mensaje'
        }
        widgets = {
            'email' : forms.EmailInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su email para ser contactado'
                }),
            'motivo' : forms.Select(
                attrs ={
                    'class' : 'form-select',
                }),
            'mensaje' : forms.Textarea(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su consulta'
                }),
        }

class MensajeUpdateForm(forms.ModelForm):
     def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

     class Meta:
        model = Mensaje
        fields = ['email','motivo','estado','mensaje']
        labels = {
            'email' : 'Email',
            'mensaje' : 'Mensaje',
            'motivo' : 'Selecione el motivo de su mensaje'
        }
        widgets = {
            'email' : forms.EmailInput(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su email para ser contactado',
                    'readonly' : 'readonly'
                }),
            'motivo' : forms.Select(
                attrs ={
                    'class' : 'form-select',
                    'disabled' : 'True',
                }),
            'estado' : forms.Select(
                attrs ={
                    'class' : 'form-select',
                }),
            'mensaje' : forms.Textarea(
                attrs ={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su consulta',
                    'required ' :'False',
                    'readonly' : 'readonly'
                }),
        }