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
from typing import List, Any, Union


class OspfSRAlgorithmList(Base):
    """Ospf SR Algorithms
    The OspfSRAlgorithmList class encapsulates a list of ospfSRAlgorithmList resources that are managed by the system.
    A list of resources can be retrieved from the server using the OspfSRAlgorithmList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfSRAlgorithmList'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'OspfSrAlgorithm': 'ospfSrAlgorithm',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(OspfSRAlgorithmList, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OspfSrAlgorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SR Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OspfSrAlgorithm']))

    def update(self, Name=None):
        # type: (str) -> OspfSRAlgorithmList
        """Updates ospfSRAlgorithmList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        # type: (str) -> OspfSRAlgorithmList
        """Adds a new ospfSRAlgorithmList resource on the json, only valid with config assistant

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved ospfSRAlgorithmList resources using find and the newly added ospfSRAlgorithmList resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> OspfSRAlgorithmList
        """Finds and retrieves ospfSRAlgorithmList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfSRAlgorithmList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfSRAlgorithmList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching ospfSRAlgorithmList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfSRAlgorithmList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfSRAlgorithmList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, OspfSrAlgorithm=None):
        """Base class infrastructure that gets a list of ospfSRAlgorithmList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - OspfSrAlgorithm (str): optional regex of ospfSrAlgorithm

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
