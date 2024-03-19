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
from filmy.views import wszystkie, szczegoly, nowy, edycja, UserList,usun, FilmList, FilmRetrieve, FilmCreateList, OcenaList, OcenaRetrieve, OcenaCreateList, AktorList, AktorRetrieve, AktorCreateList , ExtraInfoCreateList, ExtraInfoList, ExtraInfoRetrieve


urlpatterns = [
    path('wszystkie/', wszystkie,name='wszystkie'),
    path('szczegoly/<int:film_id>/', szczegoly,name='szczegoly'),
    path('nowy/', nowy),
    path('edycja/<int:film_id>/', edycja),
    path('usun/<int:film_id>/', usun),

    path('filmlist/', FilmList.as_view(), name='FilmList'),
    path('filmretrieve/<int:pk>/',FilmRetrieve.as_view(), name='FilmRetrieve' ),
    path('filmcreatelist/', FilmCreateList.as_view(), name='FilmCreateList'),

    path('userlist/', UserList.as_view(), name='UserList'),

    path('ocenalist/', OcenaList.as_view(), name='OcenaList'),
    path('ocenaretrieve/<int:pk>/', OcenaRetrieve.as_view(), name='OcenaRetrieve'),
    path('ocenacreatelist/', OcenaCreateList.as_view(), name='OcenaCreateList'),

    path('aktorlist/', AktorList.as_view(), name='AktorList'),
    path('aktorretrieve/<int:pk>/', AktorRetrieve.as_view(), name='AktorRetrieve'),
    path('aktorcreatelist/', AktorCreateList.as_view(), name='AktorCreateList'),

    path('extraInfolist/', ExtraInfoList.as_view(), name='ExtraInfoList'),
    path('extraInforetrieve/<int:pk>/', ExtraInfoRetrieve.as_view(), name='ExtraInfoRetrieve'),
    path('extraInfocreatelist/', ExtraInfoCreateList.as_view(), name='ExtraInfoCreateList'),
]
