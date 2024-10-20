from django.urls import path
from .views import PizzaListView  # Import your view here

urlpatterns = [
    path('', PizzaListView.as_view(), name='pizza-list'),  # URL for the pizza list
    # You can add more URLs here as needed, for example:
    # path('create/', PizzaCreateView.as_view(), name='pizza-create'),
    # path('<int:pk>/', PizzaDetailView.as_view(), name='pizza-detail'),
]
