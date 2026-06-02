from . import views
from django.urls import path


urlpatterns = [
    path('', views.accounts, name="accounts_page"),
    path('add_transaction/', views.add_transaction, name="add_transaction"),
]
