from django.urls import include, path

from crud_app.views import BookCrudView

urlpatterns = [
    path("books_dj", BookCrudView.as_view(), name="Book List"), 
]
