from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='main/', permanent=False)),
    path('main/', views.main, name='main'),
    path('demand/', views.demand, name='demand'),
    path('latest/', views.latest, name='latest'),
    path('skills/', views.skills, name='skills'),
    path('geography/', views.geography, name='geography'),
]
