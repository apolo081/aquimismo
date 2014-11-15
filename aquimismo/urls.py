from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from comments.views import CommentViewSet

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aquimismo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
