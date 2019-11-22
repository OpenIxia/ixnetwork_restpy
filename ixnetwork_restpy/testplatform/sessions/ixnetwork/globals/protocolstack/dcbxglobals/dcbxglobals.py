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


class DcbxGlobals(Base):
    """Global settings for DCBX protocol
    The DcbxGlobals class encapsulates a list of dcbxGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the DcbxGlobals.find() method.
    The list can be managed by the user by using the DcbxGlobals.add() and DcbxGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxGlobals'

    def __init__(self, parent):
        super(DcbxGlobals, self).__init__(parent)

    @property
    def AllowMultipleSessions(self):
        """Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.

        Returns:
            bool
        """
        return self._get_attribute('allowMultipleSessions')
    @AllowMultipleSessions.setter
    def AllowMultipleSessions(self, value):
        self._set_attribute('allowMultipleSessions', value)

    @property
    def FailOnMismatch(self):
        """If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.

        Returns:
            bool
        """
        return self._get_attribute('failOnMismatch')
    @FailOnMismatch.setter
    def FailOnMismatch(self, value):
        self._set_attribute('failOnMismatch', value)

    @property
    def FlapLinkOnStart(self):
        """Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.

        Returns:
            bool
        """
        return self._get_attribute('flapLinkOnStart')
    @FlapLinkOnStart.setter
    def FlapLinkOnStart(self, value):
        self._set_attribute('flapLinkOnStart', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def update(self, AllowMultipleSessions=None, FailOnMismatch=None, FlapLinkOnStart=None):
        """Updates a child instance of dcbxGlobals on the server.

        Args:
            AllowMultipleSessions (bool): Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.
            FailOnMismatch (bool): If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.
            FlapLinkOnStart (bool): Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AllowMultipleSessions=None, FailOnMismatch=None, FlapLinkOnStart=None):
        """Adds a new dcbxGlobals node on the server and retrieves it in this instance.

        Args:
            AllowMultipleSessions (bool): Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.
            FailOnMismatch (bool): If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.
            FlapLinkOnStart (bool): Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.

        Returns:
            self: This instance with all currently retrieved dcbxGlobals data using find and the newly added dcbxGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dcbxGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AllowMultipleSessions=None, FailOnMismatch=None, FlapLinkOnStart=None, ObjectId=None):
        """Finds and retrieves dcbxGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve dcbxGlobals data from the server.
        By default the find method takes no parameters and will retrieve all dcbxGlobals data from the server.

        Args:
            AllowMultipleSessions (bool): Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.
            FailOnMismatch (bool): If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.
            FlapLinkOnStart (bool): Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching dcbxGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dcbxGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dcbxGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
