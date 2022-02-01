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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class OFSwitchLearnedInfoConfig(Base):
    """Openflow Switch Learned Info Configuration
    The OFSwitchLearnedInfoConfig class encapsulates a required oFSwitchLearnedInfoConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'oFSwitchLearnedInfoConfig'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'FlowStatOutGroupMode': 'flowStatOutGroupMode',
        'FlowStatOutGroupValue': 'flowStatOutGroupValue',
        'FlowStatOutPortMode': 'flowStatOutPortMode',
        'FlowStatOutPortValue': 'flowStatOutPortValue',
        'FlowStatTableIdMode': 'flowStatTableIdMode',
        'FlowStatTableIdValue': 'flowStatTableIdValue',
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
        'flowStatOutGroupMode': ['oFPGALL', 'oFPGANY', 'outGroupCustom'],
        'flowStatOutPortMode': ['oFPP_IN_PORT', 'oFPP_NORMAL', 'oFPP_FLOOD', 'oFPP_ALL', 'oFPP_CONTROLLER', 'oFPP_LOCAL', 'oFPP_ANY', 'outPortCustom'],
        'flowStatTableIdMode': ['tableIdAllTables', 'tableIdCustom'],
    }

    def __init__(self, parent, list_op=False):
        super(OFSwitchLearnedInfoConfig, self).__init__(parent, list_op)

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
    def FlowStatOutGroupMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPGALL | oFPGANY | outGroupCustom): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutGroupMode'])
    @FlowStatOutGroupMode.setter
    def FlowStatOutGroupMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutGroupMode'], value)

    @property
    def FlowStatOutGroupValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Out Group is Custom/Manual, type the output group value in the box provided
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutGroupValue'])
    @FlowStatOutGroupValue.setter
    def FlowStatOutGroupValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutGroupValue'], value)

    @property
    def FlowStatOutPortMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutPortMode'])
    @FlowStatOutPortMode.setter
    def FlowStatOutPortMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutPortMode'], value)

    @property
    def FlowStatOutPortValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Out Port is Custom/Manual, type the output port value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutPortValue'])
    @FlowStatOutPortValue.setter
    def FlowStatOutPortValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutPortValue'], value)

    @property
    def FlowStatTableIdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tableIdAllTables | tableIdCustom): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatTableIdMode'])
    @FlowStatTableIdMode.setter
    def FlowStatTableIdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowStatTableIdMode'], value)

    @property
    def FlowStatTableIdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Table ID is Custom/ Manual, type the Table ID Number
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatTableIdValue'])
    @FlowStatTableIdValue.setter
    def FlowStatTableIdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowStatTableIdValue'], value)

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

    def update(self, FlowStatOutGroupMode=None, FlowStatOutGroupValue=None, FlowStatOutPortMode=None, FlowStatOutPortValue=None, FlowStatTableIdMode=None, FlowStatTableIdValue=None, Name=None):
        # type: (str, int, str, int, str, int, str) -> OFSwitchLearnedInfoConfig
        """Updates oFSwitchLearnedInfoConfig resource on the server.

        Args
        ----
        - FlowStatOutGroupMode (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowStatOutPortMode (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value.
        - FlowStatTableIdMode (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual.
        - FlowStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, FlowStatOutGroupMode=None, FlowStatOutGroupValue=None, FlowStatOutPortMode=None, FlowStatOutPortValue=None, FlowStatTableIdMode=None, FlowStatTableIdValue=None, Name=None):
        # type: (int, str, str, int, str, int, str, int, str) -> OFSwitchLearnedInfoConfig
        """Finds and retrieves oFSwitchLearnedInfoConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve oFSwitchLearnedInfoConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all oFSwitchLearnedInfoConfig resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - FlowStatOutGroupMode (str(oFPGALL | oFPGANY | outGroupCustom)): Specify the Output Group Type. The options are: 1) All Groups 2) Any Group 3) Custom/Manual
        - FlowStatOutGroupValue (number): If Out Group is Custom/Manual, type the output group value in the box provided
        - FlowStatOutPortMode (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | oFPP_ANY | outPortCustom)): Specify the Output Port Type. The options are: 1) OFPP_IN_PORT 2) OFPP_NORMAL 3) OFPP_FLOOD 4) OFPP_ALL 5) OFPP_CONTROLLER 6) OFPP_LOCAL 7) OFPP_ANY 8) Custom/Manual
        - FlowStatOutPortValue (number): If Out Port is Custom/Manual, type the output port value.
        - FlowStatTableIdMode (str(tableIdAllTables | tableIdCustom)): The identifier of the table. The options are: 1) All Tables 2) Custom/Manual.
        - FlowStatTableIdValue (number): If Table ID is Custom/ Manual, type the Table ID Number
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching oFSwitchLearnedInfoConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of oFSwitchLearnedInfoConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the oFSwitchLearnedInfoConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
