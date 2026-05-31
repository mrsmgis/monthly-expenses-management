from . import views
from django.urls import path


urlpatterns = [
    path('', views.view_budget, name="budget_page"),
    path('add/', views.add_budget, name="add_budget"),
]
