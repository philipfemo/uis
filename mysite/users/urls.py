from django.conf.urls import url, patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
import users

app_name = 'users'
urlpatterns = [
    #ex: /users/
    url(r'^list$', views.IndexView.as_view(), name='user_list'),
    #ex: /users/create
    url(r'^create$', views.CreateUserView.as_view(), name="create_user"),
    url(r'^edit/(?P<pk>\d+)/$', users.views.UpdateUserView.as_view(), name="user_edit"),
    url('^', include('django.contrib.auth.urls')),
    ]
urlpatterns += staticfiles_urlpatterns()
