from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.info, name='trade_point')
]