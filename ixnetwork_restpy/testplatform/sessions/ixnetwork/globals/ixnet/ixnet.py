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
from typing import List, Any, Union


class Ixnet(Base):
    """Tracks remote clients connected using the ixNet API Service over websockets.
    The Ixnet class encapsulates a required ixnet resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ixnet'
    _SDM_ATT_MAP = {
        'ConnectedClients': 'connectedClients',
        'IsActive': 'isActive',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Ixnet, self).__init__(parent, list_op)

    @property
    def ConnectedClients(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Returns the remote address and remote port for each of the currently connected ixNet clients.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedClients'])

    @property
    def IsActive(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Returns true if any remote clients are connected, false if no remote clients are connected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsActive'])
