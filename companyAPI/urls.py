from django.urls import path
from .views import CarganacionalList, CarganacionalDetalle ,PruebasDptoList ,PruebasMpioList ,PruebassaberEEList, EEList, MunicipiosList 

urlpatterns = [
    path('company/', CarganacionalList.as_view(), name='company_list'),
    path('pruebadpto/', PruebasDptoList.as_view(), name='pruebadpto_list'),
    path('pruebampio/', PruebasMpioList.as_view(), name='pruebampio_list'),
    path('pruebaee/', PruebassaberEEList.as_view(), name='pruebaee_list'),
    path('listaee/',EEList.as_view(), name='ee_list'),
    path('municipios/',MunicipiosList.as_view(), name='municipios_list'),
    path('company/<int:pk>/',CarganacionalDetalle.as_view(), name='companys')
]