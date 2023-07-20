from . import views
from django.urls import path

urlpatterns = [
    path('<str:username>/add', views.add_note),
    path('<str:username>/all', views.list_view),
    path('update/<int:note_id>', views.update_view),
    path('delete/<int:note_id>', views.delete_view),

]