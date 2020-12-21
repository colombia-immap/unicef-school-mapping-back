from django.views import View
from .models import Carganacional1, PruebasaberDptos, PruebasaberMpios, PruebasaberEE, Municipios, EE
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.

class CarganacionalList(View):
    def get(self, request):
        clist = Carganacional1.objects.all()
        return JsonResponse(list(clist.values()),safe=False)

class PruebasDptoList(View):
    def get(self, request):
        cliste = PruebasaberDptos.objects.all()
        return JsonResponse(list(cliste.values()),safe=False)

class PruebasMpioList(View):
    def get(self, request):
        prueba = PruebasaberMpios.objects.all()
        return JsonResponse(list(prueba.values()),safe=False)

class PruebassaberEEList(View):
    def get(self, request):
        pruebas = PruebasaberEE.objects.all()
        return JsonResponse(list(pruebas.values()),safe=False)

class EEList(View):
    def get(self, request):
        eelista = EE.objects.all()
        return JsonResponse(list(eelista.values()),safe=False)

class MunicipiosList(View):
    def get(self, request):
        municipioslista = Municipios.objects.all()
        return JsonResponse(list(municipioslista.values()),safe=False)

class CarganacionalDetalle(View):
    def get(self, request):
        company = Carganacional1.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company))
