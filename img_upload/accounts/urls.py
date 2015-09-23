from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from . import views

urlpatterns = patterns('',
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'accounts/login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
    url(
        r'^password_change$',
        'django.contrib.auth.views.password_change',
        name='password_change',
        kwargs={
               'template_name': 'accounts/password_change_form.html',
               'post_change_redirect':'accounts:password_change_done',
               }
    ),
    url(
        r'^password_change_done$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done',
        kwargs={'template_name': 'accounts/password_change_done.html'}
    ),

)
