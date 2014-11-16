#coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login,logout, authenticate
from core.mixins import IsAuthenticatedMixin

from core.serializers import UserSerializer


class Autenticacion(APIView):

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.DATA['username'],
                     password=request.DATA['password'])
        if user:
            login(request,user)
            dic = {
                'done': request.user.is_authenticated(),
                'user': request.user.username,
                'redirect': reverse('index')
            }
            return Response(dic)
        else:
            return Response({'done':False, 'message':'Usuario/Contraseña invalidos'})

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})

authentication = Autenticacion.as_view()

class Index(APIView,IsAuthenticatedMixin):

    def dispatch(self, request, *args, **kwargs):
        redirect = self.is_authenticated(request)
        return redirect if redirect != None else super(Index,self).dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return HttpResponse(request.user)

index = Index.as_view()

def ajax(request):
    print request.method
    print request.is_ajax()