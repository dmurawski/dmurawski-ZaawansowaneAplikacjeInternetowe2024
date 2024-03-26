from django.http import HttpResponse
from django.template import loader
from filmy.models import Film, Ocena, Aktor, ExtraInfo
from django.shortcuts import render, redirect
from filmy.forms import FilmForm
from django.shortcuts import get_object_or_404
from .serializers import FilmModelSerializer, UserSerializerShort, UserSerializer,ExtraInfoSerializer, OcenaSerializer, AktorSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters

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

class FilmCreateList(generics.ListCreateAPIView):
    queryset = Film.objects.all().order_by('-rok','tytul')
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['tytul', 'opis', 'rok']


class FilmRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class OcenaCreateList(generics.ListCreateAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer

class OcenaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class AktorCreateList(generics.ListCreateAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer


class AktorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer


class ExtraInfoCreateList(generics.ListCreateAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class ExtraInfoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer

class UserCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort
    permission_classes = [IsAuthenticated]


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer