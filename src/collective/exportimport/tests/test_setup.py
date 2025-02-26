# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.exportimport.testing import COLLECTIVE_EXPORTIMPORT_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.exportimport is properly installed."""

    layer = COLLECTIVE_EXPORTIMPORT_INTEGRATION_TESTING

    def test_restapi_installed(self):
        """Test if restapi is installed, because we need it."""
        if get_installer:
            installer = get_installer(self.layer['portal'], self.layer['request'])
            self.assertTrue(installer.is_product_installed('plone.restapi'))
        else:
            installer = api.portal.get_tool('portal_quickinstaller')
            self.assertTrue(installer.isProductInstalled('plone.restapi'))
