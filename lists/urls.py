__author__ = 'nwilliams1'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:

                       url(r'^new$', 'lists.views.new_list', name='new_list'),
                       url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),

                       # url(r'^blog/', include('blog.urls')),

)
