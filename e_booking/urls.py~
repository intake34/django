from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'e_booking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    url(r'^hotels/', include('hotels.urls')),
    url(r'^reservation/', include('reservation.urls')),
    url(r'^feedbacks/', include('feedbacks.urls'))
)
