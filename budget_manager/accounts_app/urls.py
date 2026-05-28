from . import views
from django.urls import path


urlpatterns = [
    path('', views.accounts, name="accounts_page"),
]
