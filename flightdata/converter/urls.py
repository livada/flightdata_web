from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'converter.views.converter', name='converter'),
)
