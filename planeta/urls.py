from django.urls import path

from planeta.views import (ListPlanetasView, CreatePlanetaView, PlanetaDetailView,
                           PlanetaDeleteView, UpdatePlanetaView)

urlpatterns = [
    path('', ListPlanetasView.as_view(), name='planeta-home'),
    path('create/', CreatePlanetaView.as_view(), name='planeta-create'),
    path('planeta/<uuid:pk>/', PlanetaDetailView.as_view(), name='planeta-detail'),
    path('planeta/<uuid:pk>/delete', PlanetaDeleteView.as_view(), name='planeta-delete'),
    path('planeta/<uuid:pk>/update', UpdatePlanetaView.as_view(), name='planeta-update'),
]
