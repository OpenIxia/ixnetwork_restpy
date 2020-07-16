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


class PacketInMaskMaster(Base):
    """When packets are received by the datapath and sent to the Controller, it may get no response from the Controller based on what the asynchronous message contains
    The PacketInMaskMaster class encapsulates a required packetInMaskMaster resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'packetInMaskMaster'
    _SDM_ATT_MAP = {
        'Action': 'action',
        'InvalidTtl': 'invalidTtl',
        'NoMatch': 'noMatch',
    }

    def __init__(self, parent):
        super(PacketInMaskMaster, self).__init__(parent)

    @property
    def Action(self):
        """
        Returns
        -------
        - bool: Action explicitly output to controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Action'])
    @Action.setter
    def Action(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Action'], value)

    @property
    def InvalidTtl(self):
        """
        Returns
        -------
        - bool: This indicates that a packet with an invalid IP TTL or MPLS TTL was rejected by the OpenFlow pipeline and passed to the controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidTtl'])
    @InvalidTtl.setter
    def InvalidTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InvalidTtl'], value)

    @property
    def NoMatch(self):
        """
        Returns
        -------
        - bool: This indicates that a packet with no matching flow (table-miss flow entry) is passed to the controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoMatch'])
    @NoMatch.setter
    def NoMatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoMatch'], value)

    def update(self, Action=None, InvalidTtl=None, NoMatch=None):
        """Updates packetInMaskMaster resource on the server.

        Args
        ----
        - Action (bool): Action explicitly output to controller.
        - InvalidTtl (bool): This indicates that a packet with an invalid IP TTL or MPLS TTL was rejected by the OpenFlow pipeline and passed to the controller.
        - NoMatch (bool): This indicates that a packet with no matching flow (table-miss flow entry) is passed to the controller.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
