from django.http import HttpResponse


def wszystkie(request):
    return HttpResponse("<h1>Tu będzie wyświetlana lista spektakli z bazy danych.</h1>")

def szczegoly(request):
    return HttpResponse("<h1>Tu będą wyświetlane szczególy wybranego spektaklu.</h1>")