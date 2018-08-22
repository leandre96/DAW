from django.shortcuts import render
from .models import Registro

# Create your views here.
def index(request):
    r=Registro.objects.all()
    conjunto=set()
    for elem in r:
        conjunto.add(elem.servicio)
    lis=list(conjunto)
    return render(request,'ind4.html',{'registros':r,'unicos':lis})
def filtrar(request):
    ul=Registro.objects.filter(servicio=request.GET['servicio'],fecha=request.GET['fecha'])
    cn={'us':ul}
    return render(request,'filtrar.html',cn)
