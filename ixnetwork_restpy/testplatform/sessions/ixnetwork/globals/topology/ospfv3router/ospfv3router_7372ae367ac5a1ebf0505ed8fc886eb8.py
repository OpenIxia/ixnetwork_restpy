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


class Ospfv3Router(Base):
    """Ospfv3 Port Specific Data
    The Ospfv3Router class encapsulates a required ospfv3Router resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfv3Router'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableDrBdr': 'enableDrBdr',
        'Name': 'name',
        'RowNames': 'rowNames',
        'Srv6CapabilityTlvType': 'srv6CapabilityTlvType',
        'Srv6EndxSubTlvType': 'srv6EndxSubTlvType',
        'Srv6LanEndxSubTlvType': 'srv6LanEndxSubTlvType',
        'Srv6LocatorLSAFuncCode': 'srv6LocatorLSAFuncCode',
        'Srv6SidStructureSubTlvType': 'srv6SidStructureSubTlvType',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv3Router, self).__init__(parent, list_op)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import StartRate
        if self._properties.get('StartRate', None) is not None:
            return self._properties.get('StartRate')
        else:
            return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import StopRate
        if self._properties.get('StopRate', None) is not None:
            return self._properties.get('StopRate')
        else:
            return StopRate(self)._select()

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
    def EnableDrBdr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable DR/BDR
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDrBdr']))

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
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    @property
    def Srv6CapabilityTlvType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This specifies the type of SRv6 Capabilities TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Srv6CapabilityTlvType'])
    @Srv6CapabilityTlvType.setter
    def Srv6CapabilityTlvType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Srv6CapabilityTlvType'], value)

    @property
    def Srv6EndxSubTlvType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This specifies the type of SRv6 End.X SID Sub-TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Srv6EndxSubTlvType'])
    @Srv6EndxSubTlvType.setter
    def Srv6EndxSubTlvType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Srv6EndxSubTlvType'], value)

    @property
    def Srv6LanEndxSubTlvType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This specifies the type Of SRv6 LAN End.X SID Sub-TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Srv6LanEndxSubTlvType'])
    @Srv6LanEndxSubTlvType.setter
    def Srv6LanEndxSubTlvType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Srv6LanEndxSubTlvType'], value)

    @property
    def Srv6LocatorLSAFuncCode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This specifies the Function Code of Locator LSA.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Srv6LocatorLSAFuncCode'])
    @Srv6LocatorLSAFuncCode.setter
    def Srv6LocatorLSAFuncCode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Srv6LocatorLSAFuncCode'], value)

    @property
    def Srv6SidStructureSubTlvType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This specifies the Sub-TLV type of SID Structure Sub-TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Srv6SidStructureSubTlvType'])
    @Srv6SidStructureSubTlvType.setter
    def Srv6SidStructureSubTlvType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Srv6SidStructureSubTlvType'], value)

    def update(self, Name=None, Srv6CapabilityTlvType=None, Srv6EndxSubTlvType=None, Srv6LanEndxSubTlvType=None, Srv6LocatorLSAFuncCode=None, Srv6SidStructureSubTlvType=None):
        # type: (str, int, int, int, int, int) -> Ospfv3Router
        """Updates ospfv3Router resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Srv6CapabilityTlvType (number): This specifies the type of SRv6 Capabilities TLV.
        - Srv6EndxSubTlvType (number): This specifies the type of SRv6 End.X SID Sub-TLV.
        - Srv6LanEndxSubTlvType (number): This specifies the type Of SRv6 LAN End.X SID Sub-TLV.
        - Srv6LocatorLSAFuncCode (number): This specifies the Function Code of Locator LSA.
        - Srv6SidStructureSubTlvType (number): This specifies the Sub-TLV type of SID Structure Sub-TLV.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, EnableDrBdr=None):
        """Base class infrastructure that gets a list of ospfv3Router device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - EnableDrBdr (str): optional regex of enableDrBdr

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
