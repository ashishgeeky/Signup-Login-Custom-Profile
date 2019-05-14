from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('wall', views.post_list, name='post_list'),
    path('', views.home, name='home'),
    path('show', views.show, name='show'),
    path('market', views.mybusiness, name='mybusiness'),
    path('sports', views.mysport, name='mysport'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="blog/try.html"), name="login"),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name="blog/login.html"), name="logout"),


]