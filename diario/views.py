from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoas, diario
from datetime import datetime, timedelta

def home(request):
    textos = Diario.objects.all().order_by('create_at')[:3]
    pessoas = Pessoas.objects.all()
    nomes = [pessoas.nome for pessoas in pessoas]
    qtds = []
    for pessoas in pessoas:
        qtd = Diario.objects.filter(pessoas=pessoas).count()
    qtd.append(qtd)
    #pessoas_com_contagem = Pessoas.objects.annotate(qtd_diarios=Count('diarios'))
    #nomes = [pessoas.nome for pessoas in pessoas_com_contagem]
    #qtds = [pessoas.qtd_diarios for pessoasn in pessoas_com_contagem]
    return render(request, 'home.html', {'textos': textos, 'nomes': nomes, 'qtds': qtds })

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoas.objects.all()
       
        return render(request, 'escrever.html', {'pessoas': pessoas}) 
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')
        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            #TODO: Adicionar mensagens de erro 
            return redirect('escrever')

        diario= Diario(
            titulo=titulo,
            texto=texto
        )    
        diario.set_tags(tags)
        diario.save()
        for i in pessoas:
            pessoas = Pessoas.objects.get(id=i)
            diario.pessoas.add(pessoas)

        diario.save()
        
        #TODO: Adicionar mensagens de sucesso
        return HttpResponse(f'{titulo} - {tags} - {pessoas} - {texto}')

def cadastrar_pessoas(request):
    if request.method == 'GET':
        return render(request, 'pessoas.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        
        pessoas = Pessoas(
            nome=nome,
            foto=foto

       ) 
        pessoas.save()
        return redirect('escrever')

def dia(request) :
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    diarios = Diarios.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=data_formatada+timedelta(days=1))

    return render(request, 'dia.html', {'diarios' : diarios, 'total': diarios.count(), 'data': data}) 

def excluir_dia(request): 
    dia = datetime.strptime(request.GET.get('data'),'%Y-%m-%d')
    diarios = Diarios.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=data_formatada+timedelta(days=1))
    
    #diarios.delete()
    print(diarios) #para mostrar
    return HttpResponse('test')
   


