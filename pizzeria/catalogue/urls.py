from django.urls import path
from .views import PizzaMenuListView

urlpatterns = [
    path('all/', PizzaMenuListView.as_view(), name='pizza-menu-list'),
]
