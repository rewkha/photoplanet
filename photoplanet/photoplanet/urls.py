from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from django.conf import settings

from .views import (
    HomePageListView, AllPhotoListView,
    PhotoDetailView, VotePhotosListView,
    PhotoDayArchiveView)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
print 'autodiscovered'

urlpatterns = patterns('',
    url(r'^$', HomePageListView.as_view(), name='home'),
    url(r'^all/$', AllPhotoListView.as_view(), name='all'),
    url(r'^about/$', TemplateView.as_view(template_name='photoplanet/about.html'), name='about'),
    url(
        r'^photo/(?P<pk>\w+)$',
        PhotoDetailView.as_view(),
        name='detail'
    ),
    url(r'^vote/$', VotePhotosListView.as_view(), name='vote'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        PhotoDayArchiveView.as_view(),
        name="photo-date-view"),
    url(r'^photo_vote/$', 'photoplanet.views.vote', name='photo-vote'),
    url(r'^feedback/', include('feedback.urls')),

    url(r'', include('social_auth.urls')),
    url(r'', include('users.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/'
        }, name='logout'),

    url(
        r'^load_photos/$', 'photoplanet.views.load_photos',
        name='load_photos'
    ),
    url(r'^admin/', include(admin.site.urls)),
)

# add static from Artem repo
urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
