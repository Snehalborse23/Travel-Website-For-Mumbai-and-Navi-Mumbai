from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('locations/', views.locations, name='locations'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('rate/', views.rate, name='stars'),
    path('nerul/', views.nerul, name='nerul'),
    path('mumbai/', views.mumbai, name='mumbai'),
    path('bandra/', views.bandra, name='bandra'),
    path('kharghar/', views.kharghar, name='kharghar'),
    path('westernmumbai/', views.westernmumbai, name='westernmumbai'),
    path('kurla/', views.kurla, name='kurla'),
    path('southmumbai/', views.southmumbai, name='southmumbai'),
    path('uran/', views.uran, name='uran'),
    path('vashi/', views.vashi, name='vashi'),
    path('save_review/<str:location>/<str:review>/<int:rating>/', views.save_review, name='save_review'),
    path('save_review/<str:location>/<str:review>/', views.save_review, name='save_review'),
]
