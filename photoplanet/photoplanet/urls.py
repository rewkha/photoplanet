from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from django.conf import settings
from .views import HomePageListView, AllPhotoListView, PhotoDetailView

urlpatterns = patterns('',
    url(r'^$', HomePageListView.as_view(), name='home'),
    url(r'^all/$', AllPhotoListView.as_view(), name='all'),
    url(r'^about/', 'photoplanet.views.about', name='about'),
    url(r'^day/', 'photoplanet.views.day', name='day'),

        url(
        r'^photo/(?P<pk>\w+)$',
        PhotoDetailView.as_view(),
        name='detail'
    ),

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
)

# add static from Artem repo
urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
