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


class CustomTopologySpbNodeBaseVidRange(Base):
    """NOT DEFINED
    The CustomTopologySpbNodeBaseVidRange class encapsulates a list of customTopologySpbNodeBaseVidRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologySpbNodeBaseVidRange.find() method.
    The list can be managed by using the CustomTopologySpbNodeBaseVidRange.add() and CustomTopologySpbNodeBaseVidRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologySpbNodeBaseVidRange'
    _SDM_ATT_MAP = {
        'BVlanPriority': 'bVlanPriority',
        'BVlanTpId': 'bVlanTpId',
        'BaseVid': 'baseVid',
        'EctAlgorithm': 'ectAlgorithm',
        'UseFlag': 'useFlag',
    }

    def __init__(self, parent):
        super(CustomTopologySpbNodeBaseVidRange, self).__init__(parent)

    @property
    def CustomTopologySpbNodeIsidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodeisidrange_78a032435bf02443f6052691120cbbe1.CustomTopologySpbNodeIsidRange): An instance of the CustomTopologySpbNodeIsidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodeisidrange_78a032435bf02443f6052691120cbbe1 import CustomTopologySpbNodeIsidRange
        return CustomTopologySpbNodeIsidRange(self)

    @property
    def BVlanPriority(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BVlanPriority'])
    @BVlanPriority.setter
    def BVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BVlanPriority'], value)

    @property
    def BVlanTpId(self):
        """
        Returns
        -------
        - str(33024 | 37120 | 37376 | 34987): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BVlanTpId'])
    @BVlanTpId.setter
    def BVlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BVlanTpId'], value)

    @property
    def BaseVid(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BaseVid'])
    @BaseVid.setter
    def BaseVid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BaseVid'], value)

    @property
    def EctAlgorithm(self):
        """
        Returns
        -------
        - str(00-80-C2-01 | 00-80-C2-02 | 00-80-C2-03 | 00-80-C2-04 | 00-80-C2-05 | 00-80-C2-06 | 00-80-C2-07 | 00-80-C2-08 | 00-80-C2-09 | 00-80-C2-0A | 00-80-C2-0B | 00-80-C2-0C | 00-80-C2-0D | 00-80-C2-0E | 00-80-C2-0F | 00-80-C2-10): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EctAlgorithm'])
    @EctAlgorithm.setter
    def EctAlgorithm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EctAlgorithm'], value)

    @property
    def UseFlag(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseFlag'])
    @UseFlag.setter
    def UseFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseFlag'], value)

    def update(self, BVlanPriority=None, BVlanTpId=None, BaseVid=None, EctAlgorithm=None, UseFlag=None):
        """Updates customTopologySpbNodeBaseVidRange resource on the server.

        Args
        ----
        - BVlanPriority (number): NOT DEFINED
        - BVlanTpId (str(33024 | 37120 | 37376 | 34987)): NOT DEFINED
        - BaseVid (number): NOT DEFINED
        - EctAlgorithm (str(00-80-C2-01 | 00-80-C2-02 | 00-80-C2-03 | 00-80-C2-04 | 00-80-C2-05 | 00-80-C2-06 | 00-80-C2-07 | 00-80-C2-08 | 00-80-C2-09 | 00-80-C2-0A | 00-80-C2-0B | 00-80-C2-0C | 00-80-C2-0D | 00-80-C2-0E | 00-80-C2-0F | 00-80-C2-10)): NOT DEFINED
        - UseFlag (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BVlanPriority=None, BVlanTpId=None, BaseVid=None, EctAlgorithm=None, UseFlag=None):
        """Adds a new customTopologySpbNodeBaseVidRange resource on the server and adds it to the container.

        Args
        ----
        - BVlanPriority (number): NOT DEFINED
        - BVlanTpId (str(33024 | 37120 | 37376 | 34987)): NOT DEFINED
        - BaseVid (number): NOT DEFINED
        - EctAlgorithm (str(00-80-C2-01 | 00-80-C2-02 | 00-80-C2-03 | 00-80-C2-04 | 00-80-C2-05 | 00-80-C2-06 | 00-80-C2-07 | 00-80-C2-08 | 00-80-C2-09 | 00-80-C2-0A | 00-80-C2-0B | 00-80-C2-0C | 00-80-C2-0D | 00-80-C2-0E | 00-80-C2-0F | 00-80-C2-10)): NOT DEFINED
        - UseFlag (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologySpbNodeBaseVidRange resources using find and the newly added customTopologySpbNodeBaseVidRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologySpbNodeBaseVidRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BVlanPriority=None, BVlanTpId=None, BaseVid=None, EctAlgorithm=None, UseFlag=None):
        """Finds and retrieves customTopologySpbNodeBaseVidRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologySpbNodeBaseVidRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologySpbNodeBaseVidRange resources from the server.

        Args
        ----
        - BVlanPriority (number): NOT DEFINED
        - BVlanTpId (str(33024 | 37120 | 37376 | 34987)): NOT DEFINED
        - BaseVid (number): NOT DEFINED
        - EctAlgorithm (str(00-80-C2-01 | 00-80-C2-02 | 00-80-C2-03 | 00-80-C2-04 | 00-80-C2-05 | 00-80-C2-06 | 00-80-C2-07 | 00-80-C2-08 | 00-80-C2-09 | 00-80-C2-0A | 00-80-C2-0B | 00-80-C2-0C | 00-80-C2-0D | 00-80-C2-0E | 00-80-C2-0F | 00-80-C2-10)): NOT DEFINED
        - UseFlag (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologySpbNodeBaseVidRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologySpbNodeBaseVidRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologySpbNodeBaseVidRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
