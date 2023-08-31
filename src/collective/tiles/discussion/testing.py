from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import zope

import collective.tiles.discussion


class CollectiveTilesDiscussionLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The autoinclude feature is disabled in the Plone fixture base layer.
        # import plone.restapi
        # self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.tiles.discussion)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.tiles.discussion:default')


COLLECTIVE_TILES_DISCUSSION_FIXTURE = CollectiveTilesDiscussionLayer()


COLLECTIVE_TILES_DISCUSSION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_TILES_DISCUSSION_FIXTURE,),
    name='CollectiveTilesDiscussionLayer:IntegrationTesting',
)


COLLECTIVE_TILES_DISCUSSION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_TILES_DISCUSSION_FIXTURE,),
    name='CollectiveTilesDiscussionLayer:FunctionalTesting',
)
