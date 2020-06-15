from django.urls import path

from . import views


app_name = 'project'

urlpatterns = [
    path('upload', views.product_upload, name='upload'),
    path('products', views.display_products, name='display_products')
    

    
]