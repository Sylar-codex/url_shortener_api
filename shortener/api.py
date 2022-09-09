from .serializer import ShortenerSerializer
from .models import Shortener
from rest_framework import viewsets
from django.shortcuts import redirect
from django.views import View
from django.conf import settings

class ShortenerViewset(viewsets.ModelViewSet) :
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer


class Redirect(View) :
    def get(self,request,hash,*args,**kwargs):
        hash = settings.HOST_URL+'/'+self.kwargs['hash']
        redirect_link = Shortener.objects.filter(hash = hash).first().original_url
        return redirect(redirect_link)
