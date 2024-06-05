from django.shortcuts import render

# Create your views here.
def criar_convenio(request):
    return render(request, "convenio.html")


