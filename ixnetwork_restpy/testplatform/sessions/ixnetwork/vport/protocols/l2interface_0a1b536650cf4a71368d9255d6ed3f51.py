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


class L2Interface(Base):
    """A single interface on a simulated router to be used in establishing Layer 2 VPNs.
    The L2Interface class encapsulates a list of l2Interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2Interface.find() method.
    The list can be managed by using the L2Interface.add() and L2Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2Interface'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Enabled': 'enabled',
        'GroupId': 'groupId',
        'TrafficGroupId': 'trafficGroupId',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(L2Interface, self).__init__(parent)

    @property
    def L2VcRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vcrange_3eeb152fbba5257d0380b3fb80b06db6.L2VcRange): An instance of the L2VcRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vcrange_3eeb152fbba5257d0380b3fb80b06db6 import L2VcRange
        return L2VcRange(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The number of contiguous values of groupId that will be used in generating FECs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this interface for the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: The group ID associated with all VC FEC elements of this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])
    @GroupId.setter
    def GroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupId'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619): The type of virtual circuit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, Count=None, Enabled=None, GroupId=None, TrafficGroupId=None, Type=None):
        """Updates l2Interface resource on the server.

        Args
        ----
        - Count (number): The number of contiguous values of groupId that will be used in generating FECs.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - GroupId (number): The group ID associated with all VC FEC elements of this interface.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        - Type (str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619)): The type of virtual circuit.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, Enabled=None, GroupId=None, TrafficGroupId=None, Type=None):
        """Adds a new l2Interface resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The number of contiguous values of groupId that will be used in generating FECs.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - GroupId (number): The group ID associated with all VC FEC elements of this interface.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        - Type (str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619)): The type of virtual circuit.

        Returns
        -------
        - self: This instance with all currently retrieved l2Interface resources using find and the newly added l2Interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained l2Interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Enabled=None, GroupId=None, TrafficGroupId=None, Type=None):
        """Finds and retrieves l2Interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2Interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2Interface resources from the server.

        Args
        ----
        - Count (number): The number of contiguous values of groupId that will be used in generating FECs.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - GroupId (number): The group ID associated with all VC FEC elements of this interface.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        - Type (str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619)): The type of virtual circuit.

        Returns
        -------
        - self: This instance with matching l2Interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2Interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2Interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
