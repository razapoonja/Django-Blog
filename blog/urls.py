from django.urls import path
from .views import (post_list, post_detail, post_create, post_update)

urlpatterns = [
    path('', post_list),
    path('create/', post_create),
    path('<str:slug>/', post_detail),
    path('<str:slug>/edit', post_update),
]
