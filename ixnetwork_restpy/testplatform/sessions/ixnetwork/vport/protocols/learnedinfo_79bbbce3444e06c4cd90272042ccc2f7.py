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


class LearnedInfo(Base):
    """Learned information associated with an interface on an stpBridge object.
    The LearnedInfo class encapsulates a required learnedInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInfo'
    _SDM_ATT_MAP = {
        'DesignatedCost': 'designatedCost',
        'DesignatedMac': 'designatedMac',
        'DesignatedPortId': 'designatedPortId',
        'DesignatedPriority': 'designatedPriority',
        'InterfaceDesc': 'interfaceDesc',
        'InterfaceRole': 'interfaceRole',
        'InterfaceState': 'interfaceState',
        'RootMac': 'rootMac',
        'RootPriority': 'rootPriority',
    }

    def __init__(self, parent):
        super(LearnedInfo, self).__init__(parent)

    @property
    def DesignatedCost(self):
        """
        Returns
        -------
        - number: Root Path Cost. The administrative cost for the shortest path from this bridge to the Root bridge. A 4-byte unsigned integer. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesignatedCost'])

    @property
    def DesignatedMac(self):
        """
        Returns
        -------
        - str: (Read-only) The 6-byte MAC address of the designated bridge on the LAN segment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesignatedMac'])

    @property
    def DesignatedPortId(self):
        """
        Returns
        -------
        - number: (Read-only) The port ID of the designated bridge's designated port on the LAN segment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesignatedPortId'])

    @property
    def DesignatedPriority(self):
        """
        Returns
        -------
        - number: (Read-only) The priority of the designated bridge on the LAN segment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesignatedPriority'])

    @property
    def InterfaceDesc(self):
        """
        Returns
        -------
        - str: (Read-only) The descriptive identifier of the protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceDesc'])

    @property
    def InterfaceRole(self):
        """
        Returns
        -------
        - str: (Read-only) The role of the Interface. One of the following options: Disabled, Root, Designated, Alternate, or Backup.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceRole'])

    @property
    def InterfaceState(self):
        """
        Returns
        -------
        - str: Read-only) The state of the interface. One of the following options: Discarding, learning, or forwarding.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceState'])

    @property
    def RootMac(self):
        """
        Returns
        -------
        - str: (Read-only) The 6-byte MAC address of the root bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootMac'])

    @property
    def RootPriority(self):
        """
        Returns
        -------
        - number: (Read-only) The priority of the root bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootPriority'])
