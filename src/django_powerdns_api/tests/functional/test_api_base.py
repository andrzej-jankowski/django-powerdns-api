# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient


REQUIRED_API_ENTRY_POINTS = (
    'domains', 'crypto-keys', 'records', 'domains-metadata',
    'super-masters',
)


class TestEntryPoints(TestCase):

    def test_entry_points_availability(self):
        client = APIClient()
        response = client.get('/', format='json')
        self.assertEqual(response.status_code, 200)
        for entry_point in REQUIRED_API_ENTRY_POINTS:
            self.assertTrue(entry_point in response.data)
