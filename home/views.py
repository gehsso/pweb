from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import time
from django.db.models import Q
from django.http import JsonResponse

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

from django.http import HttpResponse
from .models import Produto
from home.forms import ProdutoForm

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def perfil(request,usuario):
    print(usuario)
    #return HttpResponse('<h1> Bem vindo '+usuario+' </h1>')
    return render(request, 'perfil.html', {'usuario':usuario})

def teste(request, codigo, nome):
    contexto = {
        'id': codigo,
        'nome': nome,
    }
    return render(request, 'teste.html', contexto)


def produto(request):
    contexto = {
        'titulo':'Listagem de Produtos 2',
    }

    return render(request, 'produto/lista.html', contexto)


@login_required
def form_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            mensagens = []
            for campo, msg_erro in form.errors.items():
                mensagens.extend(msg_erro)
            return JsonResponse({'success': False, 'erros': mensagens})
    else:
        form = ProdutoForm()

    context = {
        'form': form,
    }
    return render(request, 'produto/form.html', context)


@login_required
def editar_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    form = ProdutoForm(instance=produto)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto')

    context = {
            'form':form,
        }
    return render(request, 'produto/form.html',context)

@login_required
def remover_produtoBKP(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'GET':
            produto.delete()
    return redirect('produto')


@login_required
def remover_produto(request, pk):
    mensagem = ''
    if request.method == 'GET':
        try:
            produto = Produto.objects.get(pk=pk)
            produto.delete()
            mensagem = 'Registro Removido com sucesso'
            return JsonResponse({'success': True, 'msg': mensagem})
        except Produto.DoesNotExist:
            mensagem = 'O produto não foi encontrado.'
        except Exception as e:
            mensagem = str(e)
        return JsonResponse({'success': False, 'msg': mensagem})


@login_required
def detalhes_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    return render(request, 'produto/detalhes.html', {'produto': produto})


def listagem_produto(request):
    descricao = request.POST.get('descricao', None)
    idProduto = request.POST.get('idProduto', None)

    # Crie um objeto consulta do Tipo Q vazio para construir condições de filtro dinamicamente
    consulta = Q()

    if descricao:
        consulta &= Q(nome__icontains=descricao)

    if idProduto:
        consulta &= Q(id=idProduto)

    # Verifica se algum filtro foi aplicado
    if consulta:
        # Se algum filtro foi aplicado, liste pelos filtros
        lista = Produto.objects.filter(consulta)
    else:
        # Se nenhum filtro foi aplicado, liste todos os produtos
        lista =  Produto.objects.all()

    contexto = {
        'lista': lista,
    }
    return render(request, 'produto/listagem.html', contexto)


def qtde_produto(request):
    quantidade = Produto.objects.count()
    data = {'quantidade': quantidade}
    return JsonResponse(data)

def relatorio_produto(request):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    cabecalho_y = 740
   # pdf.drawImage('e:\ifpi.png',10,cabecalho_y+20,80,68)
    pdf.drawString(10, cabecalho_y, "Código")
    pdf.drawString(90, cabecalho_y, "Nome")
    pdf.drawString(480, cabecalho_y, "Valor(R$)")
    pdf.line(10,cabecalho_y-10,540,cabecalho_y-10)
    dados_y = cabecalho_y-25
    lista = Produto.objects.all()
    for item in lista:
        pdf.drawString(10, dados_y, str(item.id))
        pdf.drawString(90, dados_y, item.nome)
        pdf.drawString(480, dados_y, str(item.preco))
        dados_y = dados_y - 15
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer,filename="relatorio.pdf")















def relatorio_produtoxxx(request):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(10, 800, "Relatório de Produtos, parte 01.")
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer,filename="relatorio.pdf")
    #return FileResponse(buffer, as_attachment=True, filename="hello.pdf")


"""
    cabecalho_y = 800
    pdf.drawString(20, cabecalho_y, 'Código')
    pdf.drawString(90, cabecalho_y, 'Nome')
    pdf.drawString(380, cabecalho_y, 'Valor (R$) ')
    pdf.line(00, cabecalho_y-10, 580, cabecalho_y-10)

    dados_y = cabecalho_y-30
    lista = Produto.objects.all()
    for item in lista:
        pdf.drawString(20, dados_y, str(item.id))
        pdf.drawString(90, dados_y, item.nome)
        pdf.drawString(380, dados_y, str(item.preco))
        dados_y = dados_y - 15
"""