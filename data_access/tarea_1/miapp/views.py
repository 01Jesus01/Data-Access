from django.shortcuts import render
from django.http import HttpResponse
from miapp.models import WebHeros

# Create your views here.
def index(request):
    # uno = {'Primer_interes': 'Armar cubos rubik'}
    # dos = {'Segundo_interes': 'Música'}
    # tres = {'Tercer_interes': 'Los videojuegos de PC'}
    access_webheros = WebHeros.objects.order_by('correo')
    context = {
        'Primer_interes': 'Armar cubos rubik',
        'Segundo_interes': 'Música',
        'Tercer_interes': 'Los videojuegos de PC',
        'access_webheros': access_webheros,
    }
    return render(request, "mi_app/index.html", context=context)

    #return HttpResponse("Mi primera chamba")

