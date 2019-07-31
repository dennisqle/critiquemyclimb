from django.urls import path
from . import views

urlpatterns = [
    path('', views.climbs_list, name='climbs_list'),
    path('new',views.climbs_new, name='climbs_new'),
    path('<int:pk>', views.climbs_detail, name='climbs_detail'),
    path('<int:pk>/edit', views.climbs_edit, name='climbs_edit'),
]