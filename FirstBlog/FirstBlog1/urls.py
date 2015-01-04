from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FirstBlog1.blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/', 'FirstBlog1.blog.views.form', name = 'form'),
    url(r'^newform/', 'FirstBlog1.blog.views.newform', name = 'newform'),

    url(r'^submitform/', 'FirstBlog1.blog.views.submit_form', name = 'submit_form'),
    url(r'^thanks/', 'FirstBlog1.blog.views.submit_form', name = 'thanks'),

    url(r'^newformv2/', 'FirstBlog1.blog.views.newformv2', name = 'newformv2'),
)