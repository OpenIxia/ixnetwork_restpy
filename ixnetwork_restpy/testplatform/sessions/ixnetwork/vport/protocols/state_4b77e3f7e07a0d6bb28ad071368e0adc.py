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


class State(Base):
    """An object that allows to specify the port state.
    The State class encapsulates a required state resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'state'
    _SDM_ATT_MAP = {
        'Blocked': 'blocked',
        'LinkDown': 'linkDown',
        'LiveForFastFailoverGroup': 'liveForFastFailoverGroup',
        'StpBlock': 'stpBlock',
        'StpForward': 'stpForward',
        'StpLearn': 'stpLearn',
        'StpListen': 'stpListen',
    }

    def __init__(self, parent):
        super(State, self).__init__(parent)

    @property
    def Blocked(self):
        """
        Returns
        -------
        - bool: If true, this state is available for this port. A port is in the blocked state when a switch protocol outside of OpenFlow, such as 802.1D Spanning Tree, prevents the use of that port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Blocked'])
    @Blocked.setter
    def Blocked(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Blocked'], value)

    @property
    def LinkDown(self):
        """
        Returns
        -------
        - bool: If true, there is no physical link present.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkDown'])
    @LinkDown.setter
    def LinkDown(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkDown'], value)

    @property
    def LiveForFastFailoverGroup(self):
        """
        Returns
        -------
        - bool: If true, this state is available for this port. The link is live for the Fast Failover Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LiveForFastFailoverGroup'])
    @LiveForFastFailoverGroup.setter
    def LiveForFastFailoverGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LiveForFastFailoverGroup'], value)

    @property
    def StpBlock(self):
        """
        Returns
        -------
        - bool: If true, this state is available for this port. The Switch Ports goes into a blocking state when a switch receives a BPDU on a port that indicates a better path to the root switch, and if a port is not a root port or a designated port.A port in the blocking state does not participate in frame forwarding and also discards frames received from the attached network segment. During blocking state, the port is only listening to and processing BPDUs on its interfaces. The switch port then changes from the blocking state to the listening state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StpBlock'])
    @StpBlock.setter
    def StpBlock(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StpBlock'], value)

    @property
    def StpForward(self):
        """
        Returns
        -------
        - bool: If true, this state is available for this port. A port in the forwarding state forwards frames across the attached network segment. In a forwarding state, the port processes BPDUs, updates its MAC Address table with frames that it receives, and forwards user traffic through the port. Forwarding State is the normal state. Data and configuration messages are passed through the port, when it is in forwarding state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StpForward'])
    @StpForward.setter
    def StpForward(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StpForward'], value)

    @property
    def StpLearn(self):
        """
        Returns
        -------
        - bool: If true, this state is available for this port. A port changes to learning state after listening state. During the learning state, the port is listening for and processing BPDUs. In the listening state, the port begins to process user frames and starts updating the MAC address table. But the user frames are not forwarded to the destination. The switch port then moves from the learning state to the forwarding state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StpLearn'])
    @StpLearn.setter
    def StpLearn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StpLearn'], value)

    @property
    def StpListen(self):
        """
        Returns
        -------
        - bool: If true, this state is available for this port. After blocking state, a root port or a designated port moves to a listening state. All other ports remains in a blocked state. During the listening state the port discards frames received from the attached network segment and it also discards frames switched from another port for forwarding. At this state, the port receives BPDUs from the network segment and directs them to the switch system module for processing. The switch port then moves from the listening state to the learning state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StpListen'])
    @StpListen.setter
    def StpListen(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StpListen'], value)

    def update(self, Blocked=None, LinkDown=None, LiveForFastFailoverGroup=None, StpBlock=None, StpForward=None, StpLearn=None, StpListen=None):
        """Updates state resource on the server.

        Args
        ----
        - Blocked (bool): If true, this state is available for this port. A port is in the blocked state when a switch protocol outside of OpenFlow, such as 802.1D Spanning Tree, prevents the use of that port.
        - LinkDown (bool): If true, there is no physical link present.
        - LiveForFastFailoverGroup (bool): If true, this state is available for this port. The link is live for the Fast Failover Group.
        - StpBlock (bool): If true, this state is available for this port. The Switch Ports goes into a blocking state when a switch receives a BPDU on a port that indicates a better path to the root switch, and if a port is not a root port or a designated port.A port in the blocking state does not participate in frame forwarding and also discards frames received from the attached network segment. During blocking state, the port is only listening to and processing BPDUs on its interfaces. The switch port then changes from the blocking state to the listening state.
        - StpForward (bool): If true, this state is available for this port. A port in the forwarding state forwards frames across the attached network segment. In a forwarding state, the port processes BPDUs, updates its MAC Address table with frames that it receives, and forwards user traffic through the port. Forwarding State is the normal state. Data and configuration messages are passed through the port, when it is in forwarding state.
        - StpLearn (bool): If true, this state is available for this port. A port changes to learning state after listening state. During the learning state, the port is listening for and processing BPDUs. In the listening state, the port begins to process user frames and starts updating the MAC address table. But the user frames are not forwarded to the destination. The switch port then moves from the learning state to the forwarding state.
        - StpListen (bool): If true, this state is available for this port. After blocking state, a root port or a designated port moves to a listening state. All other ports remains in a blocked state. During the listening state the port discards frames received from the attached network segment and it also discards frames switched from another port for forwarding. At this state, the port receives BPDUs from the network segment and directs them to the switch system module for processing. The switch port then moves from the listening state to the learning state.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
