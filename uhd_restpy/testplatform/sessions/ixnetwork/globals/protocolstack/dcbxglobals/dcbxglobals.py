# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class DcbxGlobals(Base):
    """Global settings for DCBX protocol
    The DcbxGlobals class encapsulates a list of dcbxGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the DcbxGlobals.find() method.
    The list can be managed by using the DcbxGlobals.add() and DcbxGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxGlobals'
    _SDM_ATT_MAP = {
        'AllowMultipleSessions': 'allowMultipleSessions',
        'FailOnMismatch': 'failOnMismatch',
        'FlapLinkOnStart': 'flapLinkOnStart',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(DcbxGlobals, self).__init__(parent)

    @property
    def AllowMultipleSessions(self):
        """
        Returns
        -------
        - bool: Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowMultipleSessions'])
    @AllowMultipleSessions.setter
    def AllowMultipleSessions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllowMultipleSessions'], value)

    @property
    def FailOnMismatch(self):
        """
        Returns
        -------
        - bool: If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FailOnMismatch'])
    @FailOnMismatch.setter
    def FailOnMismatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FailOnMismatch'], value)

    @property
    def FlapLinkOnStart(self):
        """
        Returns
        -------
        - bool: Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlapLinkOnStart'])
    @FlapLinkOnStart.setter
    def FlapLinkOnStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlapLinkOnStart'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, AllowMultipleSessions=None, FailOnMismatch=None, FlapLinkOnStart=None):
        """Updates dcbxGlobals resource on the server.

        Args
        ----
        - AllowMultipleSessions (bool): Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.
        - FailOnMismatch (bool): If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.
        - FlapLinkOnStart (bool): Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AllowMultipleSessions=None, FailOnMismatch=None, FlapLinkOnStart=None):
        """Adds a new dcbxGlobals resource on the server and adds it to the container.

        Args
        ----
        - AllowMultipleSessions (bool): Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.
        - FailOnMismatch (bool): If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.
        - FlapLinkOnStart (bool): Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.

        Returns
        -------
        - self: This instance with all currently retrieved dcbxGlobals resources using find and the newly added dcbxGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dcbxGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AllowMultipleSessions=None, FailOnMismatch=None, FlapLinkOnStart=None, ObjectId=None):
        """Finds and retrieves dcbxGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxGlobals resources from the server.

        Args
        ----
        - AllowMultipleSessions (bool): Allows multiple LLDP / DCBX sessions on a single port. The sessions are identified by inserting a VLAN header before the upper layer protocol headers. This VLAN ID uniquely identifying the session is configured in Ethernet VLAN area.
        - FailOnMismatch (bool): If true, DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the advertised parameters do not match.
        - FlapLinkOnStart (bool): Change the link status (link down, then link up) to notify the LLDP / DCBX peer that the negotiation is about to be restarted. Simulates a Converged Network Adapter (CNA) power-on or reconfiguration.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching dcbxGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
