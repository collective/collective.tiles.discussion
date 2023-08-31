from . import _
from plone import api
from plone import tiles
from plone.app.uuid.utils import uuidToPhysicalPath

import random


class DiscussionTile(tiles.PersistentTile):
    """A tile that show discussion items."""

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return self.data.get("title") or _("Latest comments")

    @property
    def limit(self):
        return self.data.get("number_of_discussions", -1)

    @property
    def query(self):
        """Get the catalog query for discussion search."""
        query = {
            "portal_type": "Discussion Item",
            "sort_on": "created",
            "sort_order": "reverse",
        }
        uuid = self.data.get("discussion_folder")
        if uuid:
            path = uuidToPhysicalPath(uuid)
            query["path"] = path
        # TODO support state?
        # if len(self.data.discussionState) == 1:
        #     query["review_state"] = self.data.discussionState[0]
        if self.limit > 0:
            # Pass on sorting hint to the catalog.
            query["sort_limit"] = self.limit

        return query

    def results(self):
        # The query passes the limit to the catalog, but this is only a hint to
        # speed up sorting.  We may get more results.  So limit it explicitly.
        return api.content.find(**self.query)[:self.limit]
