from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from api.views import *

urlpatterns = [
    path('login/', obtain_jwt_token),



    path('shipping/', shipping_list),
    path('shipping/<int:pk>/', shipping_detail),

    path('images/', image_list),
    path('images/<int:pk>/', image_detail),

    path('comments/', comment_list),
    path('comments/<int:pk>/', comment_detail),


    path('categories/', CategoryListAPIView1.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('products/', ProductListAPIView1.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),


]
