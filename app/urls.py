from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('account', views.account, name='account'),
    path('api/create', views.LinkCreate.as_view(), name='link_create'),
    path('api/retrieve', views.LinkRetrieve.as_view(), name='link_retrieve'),
    path('api/update/<str:pk>', views.LinkUpdate.as_view(), name='link_update'),
    path('api/delete/<str:pk>', views.LinkDelete.as_view(), name='link_delete'),
]
