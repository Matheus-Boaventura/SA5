from django.shortcuts import render, redirect, get_object_or_404
from .models import Dado
from datetime import datetime

def home(request):
    data = {}

    if request.method == 'POST':
        # Operação Create (Salvar)
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento_str = request.POST.get('data_nascimento')
        pais = request.POST.get('pais')

        # Convertendo a string da data para um objeto date
        data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date() if data_nascimento_str else None

        Dado.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            pais=pais
        )
        return redirect('home')  # Redirecionar para evitar envios duplicados após o refresh

    # Operação Read (Listar)
    data['dados'] = Dado.objects.all()

    return render(request, 'app_aula5/home.html', context=data)

def update_dado(request, dado_id):
    dado = get_object_or_404(Dado, pk=dado_id)

    if request.method == 'POST':
        # Operação Update (Atualizar)
        dado.nome = request.POST.get('nome')
        dado.email = request.POST.get('email')
        dado.telefone = request.POST.get('telefone')
        data_nascimento_str = request.POST.get('data_nascimento')
        pais = request.POST.get('pais')

        # Convertendo a string da data para um objeto date
        dado.data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date() if data_nascimento_str else None

        dado.save()
        return redirect('home')

    return render(request, 'app_aula5/update.html', {'dado': dado})

def remove_dado(request, dado_id):
    dado = get_object_or_404(Dado, pk=dado_id)

    if request.method == 'POST':
        # Operação Remove (Excluir)
        dado.delete()
        return redirect('home')

    return render(request, 'app_aula5/remove.html', {'dado': dado})