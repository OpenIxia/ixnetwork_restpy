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


class Unconnected(Base):
    """Unconnected protocol interfaces that are not connected by any links to the SUT or to other Ixia ports. The unconnected interfaces can be set up to link the Ixia-emulated router to virtual networks "behind" the router, such as emulated OSPF network ranges.
    The Unconnected class encapsulates a required unconnected resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'unconnected'
    _SDM_ATT_MAP = {
        'ConnectedVia': 'connectedVia',
    }

    def __init__(self, parent):
        super(Unconnected, self).__init__(parent)

    @property
    def ConnectedVia(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The name of a specified connected protocol interface on the link that is directly connected to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    def update(self, ConnectedVia=None):
        """Updates unconnected resource on the server.

        Args
        ----
        - ConnectedVia (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The name of a specified connected protocol interface on the link that is directly connected to the DUT.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
