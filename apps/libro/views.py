from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
from django.views.generic import TemplateView, ListView


# Create your views here.

# Templateview me permite renderizar templates. Es una vista basada en clase
class Inicio(TemplateView):
    template_name = 'index.html'


def crearautor(request):
    if request.method == 'POST':
        print(request.POST)
        nom = request.POST.get('nombre')
        ape = request.POST.get('apellidos')
        nacio = request.POST.get('nacionalidad')
        desc = request.POST.get('descripcion')
        autor = Autor(nombre=nom, apellidos=ape, nacionalidad=nacio, descripcion=desc)
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/crear_autor.html')


# List view me permite listar contenido de modelos. Es una vista basada en clases.
class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'  # en el html cuando hago el if pongo este nombre "if autores" hace x cosa
    queryset = Autor.objects.filter(estado=True).order_by('id')


def editarautor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})


def eliminarautor(request, id):
    autor = Autor.objects.get(id=id)
    autor.estado = False
    autor.save()
    return redirect('libro:listar_autor')
