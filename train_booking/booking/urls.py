from django.urls import path
from . import views

urlpatterns = [
    path('', views.seating_plan, name='seating_plan'),

    path('book/<int:seat_id>/', views.book_seat, name='book_seat'),
]