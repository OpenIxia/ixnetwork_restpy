# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LearnedInfoUpdate(Base):
    """The learned information trigger node that contains trigger tables of learned information.
    The LearnedInfoUpdate class encapsulates a list of learnedInfoUpdate resources that is managed by the system.
    A list of resources can be retrieved from the server using the LearnedInfoUpdate.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInfoUpdate'

    def __init__(self, parent):
        super(LearnedInfoUpdate, self).__init__(parent)

    @property
    def PceBasicRsvpSyncLspUpdateParams(self):
        """An instance of the PceBasicRsvpSyncLspUpdateParams class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams.PceBasicRsvpSyncLspUpdateParams)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams import PceBasicRsvpSyncLspUpdateParams
        return PceBasicRsvpSyncLspUpdateParams(self)

    @property
    def PceBasicSrSyncLspUpdateParams(self):
        """An instance of the PceBasicSrSyncLspUpdateParams class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams.PceBasicSrSyncLspUpdateParams)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams import PceBasicSrSyncLspUpdateParams
        return PceBasicSrSyncLspUpdateParams(self)

    @property
    def PceBasicSrv6SyncLspUpdateParams(self):
        """An instance of the PceBasicSrv6SyncLspUpdateParams class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrv6synclspupdateparams.PceBasicSrv6SyncLspUpdateParams)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrv6synclspupdateparams import PceBasicSrv6SyncLspUpdateParams
        return PceBasicSrv6SyncLspUpdateParams(self)

    @property
    def PceDetailedRsvpSyncLspUpdateParams(self):
        """An instance of the PceDetailedRsvpSyncLspUpdateParams class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams.PceDetailedRsvpSyncLspUpdateParams)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams import PceDetailedRsvpSyncLspUpdateParams
        return PceDetailedRsvpSyncLspUpdateParams(self)

    @property
    def PceDetailedSrSyncLspUpdateParams(self):
        """An instance of the PceDetailedSrSyncLspUpdateParams class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams.PceDetailedSrSyncLspUpdateParams)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams import PceDetailedSrSyncLspUpdateParams
        return PceDetailedSrSyncLspUpdateParams(self)

    @property
    def PceDetailedSrv6SyncLspUpdateParams(self):
        """An instance of the PceDetailedSrv6SyncLspUpdateParams class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrv6synclspupdateparams.PceDetailedSrv6SyncLspUpdateParams)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrv6synclspupdateparams import PceDetailedSrv6SyncLspUpdateParams
        return PceDetailedSrv6SyncLspUpdateParams(self)

    def find(self):
        """Finds and retrieves learnedInfoUpdate data from the server.

        All named parameters support regex and can be used to selectively retrieve learnedInfoUpdate data from the server.
        By default the find method takes no parameters and will retrieve all learnedInfoUpdate data from the server.

        Returns:
            self: This instance with matching learnedInfoUpdate data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of learnedInfoUpdate data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the learnedInfoUpdate data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
