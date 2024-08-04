from django.urls import path
from . import views


urlpatterns = [
    path("",views.home, name="home"),
    path("login",views.login_view,name="login"),
    path("register",views.register_view,name="register"),
    path("profile",views.profile_view,name="profile"),
    path("profileupdate",views.profile_update,name="profileform"),
    path("logout",views.logout_view,name="logout"),
    path("delete",views.delete_view,name="delete"),

]