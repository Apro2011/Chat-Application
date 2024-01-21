from django.urls import path
import views

urlpatterns = [
    path("", views.user_list, name="user_list"),
]
