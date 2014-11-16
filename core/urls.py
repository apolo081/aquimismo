from django.conf.urls import patterns, include, url


urlpatterns = patterns('core.views',
    # Examples:
    # url(r'^$', 'aquimismo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$','authentication',name='authentication'),
    url(r'index/$','index',name='index')
)