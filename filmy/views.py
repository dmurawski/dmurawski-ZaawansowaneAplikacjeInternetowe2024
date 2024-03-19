from django.http import HttpResponse
from django.template import loader
from filmy.models import Film, Ocena, Aktor, ExtraInfo
from django.shortcuts import render, redirect
from filmy.forms import FilmForm
from django.shortcuts import get_object_or_404
from .serializers import FilmModelSerializer, UserSerializer,ExtraInfoSerializer, UserSerializerShort, OcenaModelSerializer, AktorModelSerializer
from rest_framework import generics
from django.contrib.auth.models import User

def wszystkie(request):
    template = loader.get_template("filmy/wszystkie.html")
    wszystkie_filmy = Film.objects.all()
    context = {'wszystkie_filmy':wszystkie_filmy,}
    return HttpResponse(template.render(context, request))

def szczegoly(request,film_id):
    template = loader.get_template("filmy/szczegoly.html")
    film = Film.objects.get(id=film_id)
    context = {'film': film}
    return HttpResponse(template.render(context,request))

def nowy(request):
    nowyform = FilmForm(request.POST or None)
    if nowyform.is_valid():
        nowyform.save()
        return redirect(wszystkie)
    return render(request, 'filmy/c.html', {'nowyform': nowyform})

def edycja(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    form = FilmForm(request.POST or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'filmy/u.html', {'form':form})

def usun(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method=="POST":
        film.delete()
        return redirect(wszystkie)
    return render(request, 'filmy/usun.html', {'film': film})

class FilmList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer

class FilmRetrieve(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer

class FilmCreateList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort


class OcenaList(generics.ListAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaModelSerializer

class OcenaRetrieve(generics.RetrieveAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaModelSerializer

class OcenaCreateList(generics.ListCreateAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaModelSerializer

class AktorList(generics.ListAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorModelSerializer

class AktorRetrieve(generics.RetrieveAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorModelSerializer

class AktorCreateList(generics.ListCreateAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorModelSerializer


class ExtraInfoList(generics.ListAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer

class ExtraInfoRetrieve(generics.RetrieveAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer

class ExtraInfoCreateList(generics.ListCreateAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer