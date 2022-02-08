from django.urls import path

from .views import DemandaAlimentosListtView, DemandaAlimentoView

app_name="blog"

urlpatterns = [
    path('demandas/', DemandaAlimentosListtView.as_view()),
    path('demanda/<id>/', DemandaAlimentoView.as_view()),
]