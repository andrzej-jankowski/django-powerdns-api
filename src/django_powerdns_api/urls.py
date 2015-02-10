# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from django_powerdns_api.routers import router


urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
