from django.shortcuts import render

# Create your views here.
def criar_documento (request):
    return render(request, "documentos.html")