from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import Pacientes, Tarefas, Consultas, Visualizacoes
from django.contrib.messages import constants

def pacientes(request):
    if request.method == "GET":
        pacientes_list = Pacientes.objects.all()
        return render(request, 'pacientes.html', {'queixas': Pacientes.queixa_choices, 'pacientes': pacientes_list})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'O campo nome e foto são obrigatórios')
            return redirect('pacientes')

        paciente = Pacientes(
            nome=nome,
            email=email,
            telefone=telefone,
            queixa=queixa,
            foto=foto
        )
        paciente.save()

        messages.add_message(request, constants.SUCCESS, 'Paciente adicionado com sucesso')
        return redirect('pacientes')
    
def paciente_view(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if request.method == "GET":
        tarefas = Tarefas.objects.all()
        consultas = Consultas.objects.filter(paciente=paciente)
        total_consultas = consultas.count()

        tuple_grafico = ([str(i.data) for i in consultas], [str(i.humor) for i in consultas])

        # Cria e salva a instância de Visualizacoes
        for consulta in consultas:
            visualizacao = Visualizacoes(consulta=consulta, ip=request.META.get('REMOTE_ADDR'))
            visualizacao.save()

        return render(request, 'paciente.html', {
            'paciente': paciente, 
            'tarefas': tarefas, 
            'consultas': consultas, 
            'tuple_grafico': tuple_grafico, 
            'total_consultas': total_consultas, 
            'faltas': paciente.faltas
        })
    
    elif request.method == "POST":
        tarefas = request.POST.getlist('tarefas')
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video', None)
        falta = request.POST.get('falta')

        if falta == 'sim':
            paciente.faltas += 1
            paciente.save()
            messages.add_message(request, constants.SUCCESS, 'Falta registrada')
            return redirect(f'/pacientes/{id}')
        else:
            if not video:
                messages.add_message(request, constants.ERROR, 'O campo de vídeo é obrigatório.')
                return redirect(f'/pacientes/{id}')
            
            consulta = Consultas(
                humor=int(humor),
                registro_geral=registro_geral,
                video=video,
                paciente=paciente
            )
            consulta.save()

            for i in tarefas:
                tarefa = Tarefas.objects.get(id=i)
                consulta.tarefas.add(tarefa)

            consulta.save()

            messages.add_message(request, constants.SUCCESS, 'Consulta adicionada com sucesso')
        
        return redirect(f'/pacientes/{id}')
    
def atualizar_paciente(request, id):
    paciente = Pacientes.objects.get(id=id)
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    status = True if pagamento_em_dia == 'ativo' else False
    paciente.pagamento_em_dia = status
    paciente.save()
    return redirect(f'/pacientes/{id}')

def excluir_consulta(request, id):
    consulta = Consultas.objects.get(id=id)
    consulta.delete()
    return redirect(f'/pacientes/{consulta.paciente.id}')

def consulta_publica(request, id):
    consulta = Consultas.objects.get(id=id)
    if not consulta.paciente.pagamento_em_dia:
        raise Http404()

    return render(request, 'consulta_publica.html', {'consulta': consulta})

def views(self):
    views = Visualizacoes.objects.filter(consulta=self)
    totais = views.count()
    unicas = views.values('ip').distinct().count()
    return f'{totais} - {unicas}'