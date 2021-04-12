from django.shortcuts import render

from django.views.generic import CreateView

from django.views.generic.edit import FormView

from .forms import UserRegisterForm

from .models import User

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/' #el succes_url lo que hace es redirigir una vez se ejecuta con exito en este caso el registro de un usuario en el template
    
    #funcion para validar los campos del formulario
    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],

        )
        #
        return super(UserRegisterView, self).form_valid(form)