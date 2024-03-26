"""
URL configuration for filmweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from filmy.views import wszystkie, szczegoly, nowy, edycja, usun,\
    FilmCreateList, FilmRetrieveUpdateDestroy,  ExtraInfoCreateList, ExtraInfoRetrieveUpdateDestroy,\
    OcenaCreateList, OcenaRetrieveUpdateDestroy, AktorCreateList, AktorRetrieveUpdateDestroy, \
    UserCreateList, UserRetrieveUpdateDestroy


urlpatterns = [
    path('wszystkie/', wszystkie,name='wszystkie'),
    path('szczegoly/<int:film_id>/', szczegoly,name='szczegoly'),
    path('nowy/', nowy),
    path('edycja/<int:film_id>/', edycja),
    path('usun/<int:film_id>/', usun),

    path('filmy/', FilmCreateList.as_view(), name='FilmCreateList'),

    path('filmy/<int:pk>/', FilmRetrieveUpdateDestroy.as_view(), name='FilmRetrieveUpdateDestroy'),
    path('extrainfo/', ExtraInfoCreateList.as_view(), name='ExtraInfoCreateList'),
    path('extrainfo/<int:pk>/', ExtraInfoRetrieveUpdateDestroy.as_view(), name='ExtraInfoRetrieveUpdateDestroy'),

    path('ocena/', OcenaCreateList.as_view(), name='OcenaCreateList'),
    path('ocena/<int:pk>/', OcenaRetrieveUpdateDestroy.as_view(), name='OcenaRetrieveUpdateDestroy'),

    path('aktor/', AktorCreateList.as_view(), name='AktorCreateList'),
    path('aktor/<int:pk>/', AktorRetrieveUpdateDestroy.as_view(), name='AktorRetrieveUpdateDestroy'),

    path('user/', UserCreateList.as_view(), name='UserCreateList'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='UserRetrieveUpdateDestroy')
]
