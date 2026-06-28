from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('plants/', views.plant_list, name='plants'),
    path("about/", views.about, name="about_us"),
    path("contact/", views.contact, name="contact_us"),
    path("register/", views.register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="core/login.html") ,name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)