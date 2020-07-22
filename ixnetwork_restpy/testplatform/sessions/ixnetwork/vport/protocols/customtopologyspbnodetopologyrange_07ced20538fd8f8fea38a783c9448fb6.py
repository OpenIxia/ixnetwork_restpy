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


class CustomTopologySpbNodeTopologyRange(Base):
    """NOT DEFINED
    The CustomTopologySpbNodeTopologyRange class encapsulates a list of customTopologySpbNodeTopologyRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologySpbNodeTopologyRange.find() method.
    The list can be managed by using the CustomTopologySpbNodeTopologyRange.add() and CustomTopologySpbNodeTopologyRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologySpbNodeTopologyRange'
    _SDM_ATT_MAP = {
        'CistExternalRootCost': 'cistExternalRootCost',
        'CistRootIdentifier': 'cistRootIdentifier',
        'EnableVbit': 'enableVbit',
        'NoOfPorts': 'noOfPorts',
        'PortIdentifier': 'portIdentifier',
    }

    def __init__(self, parent):
        super(CustomTopologySpbNodeTopologyRange, self).__init__(parent)

    @property
    def CustomTopologySpbNodeBaseVidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodebasevidrange_a1c545f3676d26c300d952f561521cf4.CustomTopologySpbNodeBaseVidRange): An instance of the CustomTopologySpbNodeBaseVidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodebasevidrange_a1c545f3676d26c300d952f561521cf4 import CustomTopologySpbNodeBaseVidRange
        return CustomTopologySpbNodeBaseVidRange(self)

    @property
    def CistExternalRootCost(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistExternalRootCost'])
    @CistExternalRootCost.setter
    def CistExternalRootCost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistExternalRootCost'], value)

    @property
    def CistRootIdentifier(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistRootIdentifier'])
    @CistRootIdentifier.setter
    def CistRootIdentifier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistRootIdentifier'], value)

    @property
    def EnableVbit(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVbit'])
    @EnableVbit.setter
    def EnableVbit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVbit'], value)

    @property
    def NoOfPorts(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfPorts'])
    @NoOfPorts.setter
    def NoOfPorts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfPorts'], value)

    @property
    def PortIdentifier(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortIdentifier'])
    @PortIdentifier.setter
    def PortIdentifier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortIdentifier'], value)

    def update(self, CistExternalRootCost=None, CistRootIdentifier=None, EnableVbit=None, NoOfPorts=None, PortIdentifier=None):
        """Updates customTopologySpbNodeTopologyRange resource on the server.

        Args
        ----
        - CistExternalRootCost (number): NOT DEFINED
        - CistRootIdentifier (str): NOT DEFINED
        - EnableVbit (bool): NOT DEFINED
        - NoOfPorts (number): NOT DEFINED
        - PortIdentifier (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CistExternalRootCost=None, CistRootIdentifier=None, EnableVbit=None, NoOfPorts=None, PortIdentifier=None):
        """Adds a new customTopologySpbNodeTopologyRange resource on the server and adds it to the container.

        Args
        ----
        - CistExternalRootCost (number): NOT DEFINED
        - CistRootIdentifier (str): NOT DEFINED
        - EnableVbit (bool): NOT DEFINED
        - NoOfPorts (number): NOT DEFINED
        - PortIdentifier (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologySpbNodeTopologyRange resources using find and the newly added customTopologySpbNodeTopologyRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologySpbNodeTopologyRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CistExternalRootCost=None, CistRootIdentifier=None, EnableVbit=None, NoOfPorts=None, PortIdentifier=None):
        """Finds and retrieves customTopologySpbNodeTopologyRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologySpbNodeTopologyRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologySpbNodeTopologyRange resources from the server.

        Args
        ----
        - CistExternalRootCost (number): NOT DEFINED
        - CistRootIdentifier (str): NOT DEFINED
        - EnableVbit (bool): NOT DEFINED
        - NoOfPorts (number): NOT DEFINED
        - PortIdentifier (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologySpbNodeTopologyRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologySpbNodeTopologyRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologySpbNodeTopologyRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
