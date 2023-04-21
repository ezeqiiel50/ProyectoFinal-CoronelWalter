from django.shortcuts import render
from AppShortStories.models import Genero, ShortStories, Profile, Mensaje
from AppShortStories.forms import (UserReistrationForm, BuscarGeneroform, BuscarStoriesform, BuscarMensajeform,
                                    GeneroForm,ShortForm,LoginForm,ProfileForm, MensajeForm, MensajeUpdateForm)
from django.views.generic import ListView ,CreateView,DetailView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def Inicio(request):
    context ={
        "cuentos":ShortStories.objects.all().order_by('-id')
    }
    return render(request,"AppShortStories/inicio.html",context)

##import pdb; pdb.set_trace() 
    ## linea par debug l para ver donde se quedo , n para sergir la linea , c para continuar

class BuscarGenero(LoginRequiredMixin, ListView):
    model = Genero
    context_object_name = "generos"

    def get_queryset(self):
        f = BuscarGeneroform(self.request.GET)
        user_id = self.request.user.id
        if f.is_valid():
           return Genero.objects.filter(descripcion__icontains =f.data["criterio_descripcion"],creador = user_id ).all()
        return Genero.objects.filter(creador = user_id)

class GeneroCreate(LoginRequiredMixin, CreateView):
    model = Genero
    form_class = GeneroForm
    success_url = reverse_lazy("genero-list")

    def form_valid(self,form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class GeneroDetail(LoginRequiredMixin,UserPassesTestMixin, DetailView):
    model = Genero

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Genero.objects.filter(creador=user_id, id = post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class GeneroUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Genero
    form_class = GeneroForm
    success_url = reverse_lazy("genero-list")

    def form_valid(self,form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_id = self.request.user.id
        posteo_id = self.kwargs.get('pk')
        return Genero.objects.filter(creador=user_id, id = posteo_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class GeneroDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Genero
    success_url = reverse_lazy("genero-list")

    def test_func(self):
        user_id = self.request.user.id
        posteo_id = self.kwargs.get('pk')
        return Genero.objects.filter(creador=user_id, id = posteo_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class BuscarShortStories(LoginRequiredMixin, ListView):
    model = ShortStories
    context_object_name = "cuentos"

    def get_queryset(self):
        f = BuscarStoriesform(self.request.GET)
        user_id = self.request.user.id
        if f.is_valid():
           return ShortStories.objects.filter(titulo__icontains =f.data["criterio_titulo"]).all()
        return ShortStories.objects.filter(publisher = user_id)

class ShortStoriesCreate(LoginRequiredMixin, CreateView):
    model = ShortStories
    form_class = ShortForm
    success_url = reverse_lazy("cuento-list")

    def form_valid(self,form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class ShortStoriesDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ShortStories

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return ShortStories.objects.filter(publisher=user_id, id = post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class ShortStoriesUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ShortStories
    form_class = ShortForm
    success_url = reverse_lazy("cuento-list")

    def form_valid(self,form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return ShortStories.objects.filter(publisher=user_id, id = post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class ShortStoriesDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ShortStories
    success_url = reverse_lazy("cuento-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return ShortStories.objects.filter(publisher=user_id, id = post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class SignUp(CreateView):
    form_class = UserReistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("login")
    success_message = "Usuario registrado satisfactoriamente"

class Login(LoginView):
    form_class = LoginForm
    next_page = reverse_lazy("inicio")

class Logout(LogoutView):
    template_name = "registration/logout.html"
    

class ProfileDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
     model = Profile
     fields = '__all__'

     def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id = profile_id).exists()
    
     def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("inicio")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("inicio")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id = profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")

class MensajeCreate(CreateView):
    model = Mensaje
    form_class = MensajeForm
    success_url = reverse_lazy("inicio")

    def form_valid(self,form):
        user_admin = User.objects.filter(id = 1).first()
        form.instance.destinatario = user_admin
        return super().form_valid(form)

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        f = BuscarMensajeform(self.request.GET)
        mi_profile = Profile.objects.filter(user = self.request.user).first()
        if self.request.user.id == int(1):
            if f.is_valid():
                return Mensaje.objects.filter(mensaje__icontains =f.data["criterio_mensaje"]).all().order_by('-id')
            return Mensaje.objects.all().order_by('-id')
        else :
            if mi_profile:
                if f.is_valid():
                    return Mensaje.objects.filter(email = mi_profile.email, mensaje__icontains =f.data["criterio_mensaje"]).order_by('-id')
                return Mensaje.objects.filter(email = mi_profile.email).order_by('-id')
            return Mensaje.objects.filter(destinatario = self.request.user).order_by('-id')

class MensajeUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Mensaje
    form_class = MensajeUpdateForm
    success_url = reverse_lazy("mensaje-list")

    def form_valid(self,form):
        user_admin = User.objects.filter(id = 1).first()
        form.instance.destinatario = user_admin
        return super().form_valid(form)

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id, id = mensaje_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"AppShortStories/not_found.html")
