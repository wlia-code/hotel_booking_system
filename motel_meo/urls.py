from django.urls import path
from .views import home, book_room_page,book_room

urlpatterns = [
    path("", home, name="home-page"),
    path("book-room/", book_room_page, name="book-room-page"),
    path("book-room/book/",book_room,name="bookroom"),   
]