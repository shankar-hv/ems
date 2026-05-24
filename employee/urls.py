from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('details/<int:id>',views.details,name='details'),
    path('update/<int:id>/', views.update, name='update'),
    path('create/',views.create,name='create'),
    path('delete/<int:id>/',views.delete, name='delete'),
]