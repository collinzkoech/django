
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('',views.images),
    path('about/',views.about),
    path('contacts/',views.contacts),
    path('collection/',views.collection),
]
