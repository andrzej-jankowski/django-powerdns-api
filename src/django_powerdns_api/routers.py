# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from django_powerdns_api.views import (
    CryptoKeyViewSet,
    DomainMetadataViewSet,
    DomainViewSet,
    RecordViewSet,
    SuperMasterViewSet,
)


router = DefaultRouter()
router.register(r'domains', DomainViewSet)
router.register(r'records', RecordViewSet)
router.register(r'crypto-keys', CryptoKeyViewSet)
router.register(r'domains-metadata', DomainMetadataViewSet)
router.register(r'super-masters', SuperMasterViewSet)


__all__ = [
    'router',
]
