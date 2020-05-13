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
    The LearnedInfoUpdate class encapsulates a list of learnedInfoUpdate resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInfoUpdate.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInfoUpdate'

    def __init__(self, parent):
        super(LearnedInfoUpdate, self).__init__(parent)

    @property
    def PceBasicRsvpSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams_9128fdd3b6df6b06508a030315b5dcd4.PceBasicRsvpSyncLspUpdateParams): An instance of the PceBasicRsvpSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams_9128fdd3b6df6b06508a030315b5dcd4 import PceBasicRsvpSyncLspUpdateParams
        return PceBasicRsvpSyncLspUpdateParams(self)

    @property
    def PceBasicSrSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams_7f7870dcde005a31b7941f9a341ab07e.PceBasicSrSyncLspUpdateParams): An instance of the PceBasicSrSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams_7f7870dcde005a31b7941f9a341ab07e import PceBasicSrSyncLspUpdateParams
        return PceBasicSrSyncLspUpdateParams(self)

    @property
    def PceBasicSrv6SyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrv6synclspupdateparams_3f1e9c656acf3c1c4ab0113ca6ccd0cc.PceBasicSrv6SyncLspUpdateParams): An instance of the PceBasicSrv6SyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrv6synclspupdateparams_3f1e9c656acf3c1c4ab0113ca6ccd0cc import PceBasicSrv6SyncLspUpdateParams
        return PceBasicSrv6SyncLspUpdateParams(self)

    @property
    def PceDetailedRsvpSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams_7bab256bb68c4a58bb9c6fca1d6e8177.PceDetailedRsvpSyncLspUpdateParams): An instance of the PceDetailedRsvpSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams_7bab256bb68c4a58bb9c6fca1d6e8177 import PceDetailedRsvpSyncLspUpdateParams
        return PceDetailedRsvpSyncLspUpdateParams(self)

    @property
    def PceDetailedSrSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams_c30ed74890a7f9e1b6469b93b3e61538.PceDetailedSrSyncLspUpdateParams): An instance of the PceDetailedSrSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams_c30ed74890a7f9e1b6469b93b3e61538 import PceDetailedSrSyncLspUpdateParams
        return PceDetailedSrSyncLspUpdateParams(self)

    @property
    def PceDetailedSrv6SyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrv6synclspupdateparams_b6b67983090c12f28171a9790bcc0d11.PceDetailedSrv6SyncLspUpdateParams): An instance of the PceDetailedSrv6SyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrv6synclspupdateparams_b6b67983090c12f28171a9790bcc0d11 import PceDetailedSrv6SyncLspUpdateParams
        return PceDetailedSrv6SyncLspUpdateParams(self)

    def find(self):
        """Finds and retrieves learnedInfoUpdate resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInfoUpdate resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInfoUpdate resources from the server.

        Returns
        -------
        - self: This instance with matching learnedInfoUpdate resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInfoUpdate data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInfoUpdate resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
