from django.shortcuts import get_object_or_404, render
from .models import Workshop

# Create your views here.
def index(request):
    exemplo_de_variavel_no_template = "Essa String do botão veio da função 'index' sustainable/views.py"

    context = {
        "texto_qualquer": exemplo_de_variavel_no_template
    }

    return render(request, 'conteudo/index.html', context)

def pagina(request):
    context = {
        "brendon": "Brendon é um cara legal!"
    }
    return render(request, 'conteudo/pagina.html', context)

def mostra_workshop(request, workshop_slug):
    "Função que retorna o conteudo da página de um workshop a partir de seu slug"
    workshop = get_object_or_404(Workshop, slug=workshop_slug)
    context = {
        'workshop': workshop,
    }
    return render(request, 'conteudo/mostra_workshop.html', context)
