
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('links', views.links, name='links'),
    path('about', views.about, name='about'),
    path('course', views.course, name='course'),
    path('profile', views.profile, name='profile'),
    path('works', views.works, name='works'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('reset', views.reset, name='reset'),
    path('log_out', views.log_out, name='log_out'),
    path('post', views.post, name='post'),
    path('search', views.search, name='search'),
    path('<name_slug>', views.blogpost, name='blogpost'),


]
