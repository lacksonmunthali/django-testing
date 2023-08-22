from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genre/<id>', views.genre, name="genre"),
    path('book/<id>', views.viewBook, name="viewBook"),
    path('greet', views.greet, name='greet'),
]