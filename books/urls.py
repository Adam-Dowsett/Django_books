from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="books-index"),
    path("<int:book_id>/", views.show, name="books-show"),
    path("new/", views.new, name="books-new")
]

handler404 = "books.views.not_found_404"