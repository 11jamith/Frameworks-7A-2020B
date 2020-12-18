from django.urls import path

from.import views

urlpatterns=[
    path('',views.index, name='index'),
    path('/listar_categorias/',views.listar_categorias, name='listar_categorias'),
    path('/listar_productos/',views.listar_productos, name='listar_productos'),

]