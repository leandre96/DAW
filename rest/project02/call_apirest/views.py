from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse

import requests

# Create your views here.
url='http://127.0.0.1:8000/cooking/usuarios/'

#index will show users
def index(request):    
    response = requests.get(url)
    #usuarios retrieved from api rest
    usuarios=response.json()
    context={'usuarios':usuarios}  
    return render(request, 'index.html',context)

def delete(request,u_id):
    #url='http://127.0.0.1:8000/cooking/usuarios/'
    #u_id='2'
    #finalURL='http://127.0.0.1:8000/cooking/usuarios/2'
    finalURL=url + str(u_id)
    response = requests.delete(finalURL)	 
    return HttpResponseRedirect(reverse('index'))

def add(request):
		Data={
			'nombre':request.POST['nombre'],
			'servicio':request.POST['servicio'],
			'ciudad':request.POST['ciudad'],
			'fecha':request.POST['fecha']
		}
		response=requests.post(url,data=Data)
		return HttpResponseRedirect(reverse('index'))

def update(request,u_id):
		#it seems in put you must set that final slash
		finalURL=url + str(u_id) +'/'
		print(finalURL)
		Data={'fecha':request.POST['fecha']}
		response=requests.put(finalURL,data=Data)
		return HttpResponseRedirect(reverse('index'))
		
		
		
    
