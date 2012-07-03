from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gymkhana.views.home', name='home'),
    # url(r'^gymkhana/', include('gymkhana.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'news.views.index'),
    url(r'^newspage$', 'news.views.newspage'),
    url(r'^newsmodal$', 'news.views.newsmodal'),
    url(r'^pintoprofile$', 'news.views.pintoprofile'),
    url(r'^unpinfromprofile$', 'news.views.unpinfromprofile'),

    url(r'^about$', 'users.views.about'),
    url(r'^login$', 'users.views.login'),
    url(r'^logout$', 'users.views.logout'),
    url(r'^profile$', 'users.views.profile'),
)
