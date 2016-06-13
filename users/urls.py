from django.conf.urls import url
from django.contrib.auth.views import login
from .views import logout_view, register


context = {'template_name': 'users/login.html'}

urlpatterns = [
    # Login page
    url(r'^login/$', login, context, name='login'),
    # Log out page
    url(r'^logout/$', logout_view, name='logout'),
    # Register page
    url(r'^register/$', register, name='register')
]
