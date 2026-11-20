from django.shortcuts import render

from django.http import JsonResponse

def resumo(request):
    dados = {"mensagem": "API de gastos no ar", "total": "0.00"}
    return JsonResponse(dados)
