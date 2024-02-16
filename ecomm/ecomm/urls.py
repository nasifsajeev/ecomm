"""
URL configuration for ecomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home_view'),
    path('user/reg',views.UserRegisterView.as_view(),name='reg_view'),
    path('user/log',views.UserLoginView.as_view(),name='log_view'),
    path('user/logout',views.UserLogoutView.as_view(),name='logout_view'),
    path('product/detail/<int:id>',views.ProductDetailView.as_view(),name='detail_view'),
    path('add/cart/<int:id>',views.AddToCartView.as_view(),name='addcart_view'),
    path('cart/list',views.CartListView.as_view(),name='cartlist_view'),
    path('place/order/<int:cart_id>',views.PlaceOrderView.as_view(),name='placeorder_view'),
    path('cart/delete/<int:id>',views.CartDeleteView.as_view(),name='cartdelete_view')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
