# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.ClamAV


class CollectiveClamavLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.ClamAV)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.ClamAV:default')


COLLECTIVE_CLAMAV_FIXTURE = CollectiveClamavLayer()


COLLECTIVE_CLAMAV_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_CLAMAV_FIXTURE,),
    name='CollectiveClamavLayer:IntegrationTesting'
)


COLLECTIVE_CLAMAV_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CLAMAV_FIXTURE,),
    name='CollectiveClamavLayer:FunctionalTesting'
)


COLLECTIVE_CLAMAV_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_CLAMAV_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveClamavLayer:AcceptanceTesting'
)
