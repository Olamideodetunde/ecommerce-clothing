from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home-page' ),
    path('about/',views.about, name='about-page' ),
    path('contact/',views.contact, name='contact-page' ),
    path('shop/',views.shop, name='shop-page' ),
    path('blog/',views.blog, name='blog-page' ),
    path('cart/',views.cart, name='cart-page' ),
    path('checkout/',views.checkout, name='checkout-page' ),
    path('login/',views.login_view, name='login-page' ),
    path('signup/',views.signup_view, name='signup-page' ),
]
