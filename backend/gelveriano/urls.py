from django.urls import path

from .views import DemandaAlimentosListtView, DemandaAlimentoView, ApiOverview, add_items, update_items, delete_items

app_name="blog"

urlpatterns = [
    path('demandas/', DemandaAlimentosListtView.as_view()),
    path('demanda/create/', add_items, name='addDemandas'),
    path('demanda/<id>/', DemandaAlimentoView.as_view()), 
    path('', ApiOverview, name='home'),
    path('demanda/<int:pk>/update/', update_items, name='update-items'),
    path('demanda/<int:pk>/delete/', delete_items, name='delete-items'),
]