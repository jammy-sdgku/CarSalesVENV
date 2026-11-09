from django.urls import path
from . import views
urlpatterns = [
    path('', views.carslist, name = 'carslist'),
    path('addcar', views.addcar, name = 'addcar'),
    path('updatecar/<int:id>', views.updatecar, name = 'updatecar'),
    path('deletecar/<int:id>', views.deletecar, name = 'deletecar')
]