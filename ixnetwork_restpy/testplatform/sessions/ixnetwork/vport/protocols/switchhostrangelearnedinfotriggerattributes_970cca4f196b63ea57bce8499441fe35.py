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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class SwitchHostRangeLearnedInfoTriggerAttributes(Base):
    """NOT DEFINED
    The SwitchHostRangeLearnedInfoTriggerAttributes class encapsulates a required switchHostRangeLearnedInfoTriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "switchHostRangeLearnedInfoTriggerAttributes"
    _SDM_ATT_MAP = {
        "CustomPacket": "customPacket",
        "DestinationCustom": "destinationCustom",
        "DestinationCustomIpv4Address": "destinationCustomIpv4Address",
        "DestinationCustomIpv4AddressStep": "destinationCustomIpv4AddressStep",
        "DestinationCustomMacAddress": "destinationCustomMacAddress",
        "DestinationCustomMacAddressStep": "destinationCustomMacAddressStep",
        "DestinationHostList": "destinationHostList",
        "MeshingType": "meshingType",
        "PacketType": "packetType",
        "PeriodIntervalInMs": "periodIntervalInMs",
        "Periodic": "periodic",
        "PeriodicIterationNumber": "periodicIterationNumber",
        "ResponseTimeout": "responseTimeout",
        "SourceHostList": "sourceHostList",
    }
    _SDM_ENUM_MAP = {
        "meshingType": ["fullyMesh"],
        "packetType": ["arp", "ping", "custom"],
    }

    def __init__(self, parent, list_op=False):
        super(SwitchHostRangeLearnedInfoTriggerAttributes, self).__init__(
            parent, list_op
        )

    @property
    def CustomPacket(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomPacket"])

    @CustomPacket.setter
    def CustomPacket(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomPacket"], value)

    @property
    def DestinationCustom(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationCustom"])

    @DestinationCustom.setter
    def DestinationCustom(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationCustom"], value)

    @property
    def DestinationCustomIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationCustomIpv4Address"])

    @DestinationCustomIpv4Address.setter
    def DestinationCustomIpv4Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationCustomIpv4Address"], value)

    @property
    def DestinationCustomIpv4AddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DestinationCustomIpv4AddressStep"]
        )

    @DestinationCustomIpv4AddressStep.setter
    def DestinationCustomIpv4AddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["DestinationCustomIpv4AddressStep"], value
        )

    @property
    def DestinationCustomMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationCustomMacAddress"])

    @DestinationCustomMacAddress.setter
    def DestinationCustomMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationCustomMacAddress"], value)

    @property
    def DestinationCustomMacAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationCustomMacAddressStep"])

    @DestinationCustomMacAddressStep.setter
    def DestinationCustomMacAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationCustomMacAddressStep"], value)

    @property
    def DestinationHostList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/openFlow/device/interface/switch/switchPorts/switchHostRanges]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationHostList"])

    @DestinationHostList.setter
    def DestinationHostList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationHostList"], value)

    @property
    def MeshingType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fullyMesh): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeshingType"])

    @MeshingType.setter
    def MeshingType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeshingType"], value)

    @property
    def PacketType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(arp | ping | custom): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketType"])

    @PacketType.setter
    def PacketType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketType"], value)

    @property
    def PeriodIntervalInMs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeriodIntervalInMs"])

    @PeriodIntervalInMs.setter
    def PeriodIntervalInMs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeriodIntervalInMs"], value)

    @property
    def Periodic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Periodic"])

    @Periodic.setter
    def Periodic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Periodic"], value)

    @property
    def PeriodicIterationNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeriodicIterationNumber"])

    @PeriodicIterationNumber.setter
    def PeriodicIterationNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeriodicIterationNumber"], value)

    @property
    def ResponseTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResponseTimeout"])

    @ResponseTimeout.setter
    def ResponseTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResponseTimeout"], value)

    @property
    def SourceHostList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/openFlow/device/interface/switch/switchPorts/switchHostRanges]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceHostList"])

    @SourceHostList.setter
    def SourceHostList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceHostList"], value)

    def update(
        self,
        CustomPacket=None,
        DestinationCustom=None,
        DestinationCustomIpv4Address=None,
        DestinationCustomIpv4AddressStep=None,
        DestinationCustomMacAddress=None,
        DestinationCustomMacAddressStep=None,
        DestinationHostList=None,
        MeshingType=None,
        PacketType=None,
        PeriodIntervalInMs=None,
        Periodic=None,
        PeriodicIterationNumber=None,
        ResponseTimeout=None,
        SourceHostList=None,
    ):
        # type: (str, bool, str, str, str, str, List[str], str, str, int, bool, int, int, List[str]) -> SwitchHostRangeLearnedInfoTriggerAttributes
        """Updates switchHostRangeLearnedInfoTriggerAttributes resource on the server.

        Args
        ----
        - CustomPacket (str): NOT DEFINED
        - DestinationCustom (bool): NOT DEFINED
        - DestinationCustomIpv4Address (str): NOT DEFINED
        - DestinationCustomIpv4AddressStep (str): NOT DEFINED
        - DestinationCustomMacAddress (str): NOT DEFINED
        - DestinationCustomMacAddressStep (str): NOT DEFINED
        - DestinationHostList (list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/openFlow/device/interface/switch/switchPorts/switchHostRanges])): NOT DEFINED
        - MeshingType (str(fullyMesh)): NOT DEFINED
        - PacketType (str(arp | ping | custom)): NOT DEFINED
        - PeriodIntervalInMs (number): NOT DEFINED
        - Periodic (bool): NOT DEFINED
        - PeriodicIterationNumber (number): NOT DEFINED
        - ResponseTimeout (number): NOT DEFINED
        - SourceHostList (list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/openFlow/device/interface/switch/switchPorts/switchHostRanges])): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CustomPacket=None,
        DestinationCustom=None,
        DestinationCustomIpv4Address=None,
        DestinationCustomIpv4AddressStep=None,
        DestinationCustomMacAddress=None,
        DestinationCustomMacAddressStep=None,
        DestinationHostList=None,
        MeshingType=None,
        PacketType=None,
        PeriodIntervalInMs=None,
        Periodic=None,
        PeriodicIterationNumber=None,
        ResponseTimeout=None,
        SourceHostList=None,
    ):
        # type: (str, bool, str, str, str, str, List[str], str, str, int, bool, int, int, List[str]) -> SwitchHostRangeLearnedInfoTriggerAttributes
        """Finds and retrieves switchHostRangeLearnedInfoTriggerAttributes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchHostRangeLearnedInfoTriggerAttributes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchHostRangeLearnedInfoTriggerAttributes resources from the server.

        Args
        ----
        - CustomPacket (str): NOT DEFINED
        - DestinationCustom (bool): NOT DEFINED
        - DestinationCustomIpv4Address (str): NOT DEFINED
        - DestinationCustomIpv4AddressStep (str): NOT DEFINED
        - DestinationCustomMacAddress (str): NOT DEFINED
        - DestinationCustomMacAddressStep (str): NOT DEFINED
        - DestinationHostList (list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/openFlow/device/interface/switch/switchPorts/switchHostRanges])): NOT DEFINED
        - MeshingType (str(fullyMesh)): NOT DEFINED
        - PacketType (str(arp | ping | custom)): NOT DEFINED
        - PeriodIntervalInMs (number): NOT DEFINED
        - Periodic (bool): NOT DEFINED
        - PeriodicIterationNumber (number): NOT DEFINED
        - ResponseTimeout (number): NOT DEFINED
        - SourceHostList (list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/openFlow/device/interface/switch/switchPorts/switchHostRanges])): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchHostRangeLearnedInfoTriggerAttributes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchHostRangeLearnedInfoTriggerAttributes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchHostRangeLearnedInfoTriggerAttributes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
