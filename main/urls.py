from django.urls import path
from . import views

urlpatterns = [
    path('', views.sakums, name='sakums'),
    path('par-mums/', views.par_mums, name='par_mums'),
    path('pakalpojumi/', views.pakalpojumi, name='pakalpojumi'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('raksti-mums/', views.raksti_mums, name='raksti_mums'),
    path('atsauksmes/', views.atsauksmes, name='atsauksmes'),
]