from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^delivery/', views.delivery, name='delivery')
]