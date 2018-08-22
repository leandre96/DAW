from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Usuario

#----------------libs for email------------------------
from django.core.mail import send_mail
from django.conf import settings
#------------------------------------------------------


#-------------to set apirest view-------------------
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response
 
from .serializers import UsuarioSerializer


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#--------------------------------------------------
 

def index(request):        
    return render(request, 'cooking/index.html')

def testFiltrar(request):        
    return render(request, 'cooking/testFiltrar.html')

#must set in the path even if it doesn't have a view
#action of the form to send the email
def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us ' + request.GET['mensaje']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sss.leandre96@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect(render(request, 'cooking/testEmail.html'))

def testEmail(request):        
    return render(request, 'cooking/testEmail.html')


def filtrar(request):	
    #use Usuario.objects.get() when the object is unique
    usuarios_list=Usuario.objects.filter(servicio=request.GET['servicio'], fecha=request.GET['fecha'])	   
    context = {'usuarios_list':usuarios_list}    
    return render(request, 'cooking/filtrar.html', context)


#the view for apirest

#this seems to be to render the result
@api_view(['GET', 'POST'])
def usuario_list(request):
    if request.method == 'GET': 
        usuarios = Usuario.objects.all() 
        serializer = UsuarioSerializer(usuarios, many=True) 
        return Response(serializer.data) 

    elif request.method == 'POST': 
        serializer = UsuarioSerializer(data=request.data)        
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def usuario_detail(request, pk):
    """
    Retrieve, update or delete a user
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        usuario.fecha=request.data['fecha']
        usuario.save()
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
        """   
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
				"""

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
  
"""
def filtrar(request):
   return HttpResponse("hey")

"""
"""
from .models import Usuario
def index(request):
    lista_usuarios=Usuario.objects.all()
    output= ''
    for u in lista_usuarios:
        output+=str(u)
        output+='<br>'	
    return HttpResponse(output)
"""
