from django.urls import path
from .views import home, book_room_page,book_room
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home-page"),
    path("book-room/", book_room_page, name="book-room-page"),
    path("book-room/book/",book_room,name="bookroom"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', auth_views.LoginView.as_view(), name='signup'),
       
]