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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LearnedInterface(Base):
    """Learned information associated with a CIST for an interface on an (MSTP) stpBridge.
    The LearnedInterface class encapsulates a list of learnedInterface resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInterface'
    _SDM_ATT_MAP = {
        'DesignatedMac': 'designatedMac',
        'DesignatedPortId': 'designatedPortId',
        'DesignatedPriority': 'designatedPriority',
        'InterfaceDesc': 'interfaceDesc',
        'InterfaceRole': 'interfaceRole',
        'InterfaceState': 'interfaceState',
    }

    def __init__(self, parent):
        super(LearnedInterface, self).__init__(parent)

    @property
    def DesignatedMac(self):
        """
        Returns
        -------
        - str: (Read-only) The 6-byte MAC Address of the advertised designated MSTP bridge on the LAN segment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesignatedMac'])

    @property
    def DesignatedPortId(self):
        """
        Returns
        -------
        - number: (Read-only) The port ID of the advertised eesignated MSTP bridge's port on the LAN segment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesignatedPortId'])

    @property
    def DesignatedPriority(self):
        """
        Returns
        -------
        - number: (Read-only) The priority of the advertised designated MSTP bridge on the LAN segment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesignatedPriority'])

    @property
    def InterfaceDesc(self):
        """
        Returns
        -------
        - str: (Read-only) The descriptive identifier of this advertised protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceDesc'])

    @property
    def InterfaceRole(self):
        """
        Returns
        -------
        - str: (Read-only) The role of the advertised interface. One of the following options: Disabled, Root, Designated, Alternate, or Backup.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceRole'])

    @property
    def InterfaceState(self):
        """
        Returns
        -------
        - str: (Read-only) The state of the advertised interface. One of the following options: Discarding (discarding MAC), Learning (MAC frame learning), or Forwarding (forwarding MAC frames).
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceState'])

    def find(self, DesignatedMac=None, DesignatedPortId=None, DesignatedPriority=None, InterfaceDesc=None, InterfaceRole=None, InterfaceState=None):
        """Finds and retrieves learnedInterface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInterface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInterface resources from the server.

        Args
        ----
        - DesignatedMac (str): (Read-only) The 6-byte MAC Address of the advertised designated MSTP bridge on the LAN segment.
        - DesignatedPortId (number): (Read-only) The port ID of the advertised eesignated MSTP bridge's port on the LAN segment.
        - DesignatedPriority (number): (Read-only) The priority of the advertised designated MSTP bridge on the LAN segment.
        - InterfaceDesc (str): (Read-only) The descriptive identifier of this advertised protocol interface.
        - InterfaceRole (str): (Read-only) The role of the advertised interface. One of the following options: Disabled, Root, Designated, Alternate, or Backup.
        - InterfaceState (str): (Read-only) The state of the advertised interface. One of the following options: Discarding (discarding MAC), Learning (MAC frame learning), or Forwarding (forwarding MAC frames).

        Returns
        -------
        - self: This instance with matching learnedInterface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInterface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInterface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
