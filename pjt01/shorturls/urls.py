from django.urls import path
from . import views

appname = 'shorturls'

urlpatterns = [
    path('<url>/<original>/', views.change_url),
    path('<url>/', views.url_redirect),
    path('shorten/history/show/', views.get_history),
]