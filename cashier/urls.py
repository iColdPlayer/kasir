from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeIndex, name='HomeIndex'),
    path('stock/', views.TotalStock, name='TotalStock'),
    path('input/', views.InputStock, name='InputStock'),
    path('cart/', views.Cart, name='Cart'),
    path('struck/<int:pk>/', views.StruckPembelian, name='StruckPembelian'),
    path('purchase/', views.DaftarPembelian, name='DaftarPembelian'),
    path('report/', views.ReportView, name='ReportView'),
]

# handler404 = 'home.views.handler404'
handler500 = 'cashier.views.handler500'