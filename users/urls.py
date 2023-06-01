from django.urls import path
from .views import list_users, create_user, delete_user, edit_user


urlpatterns = [
    path('', list_users),
    path('new/', create_user),
    path('delete/<int:id>/', delete_user, name='delete_user'),
    path('edit/<int:id>/', edit_user, name='edit_user'),
]
