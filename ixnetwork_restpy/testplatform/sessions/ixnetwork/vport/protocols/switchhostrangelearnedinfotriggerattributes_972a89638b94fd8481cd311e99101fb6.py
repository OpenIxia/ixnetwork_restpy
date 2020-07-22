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


class SwitchHostRangeLearnedInfoTriggerAttributes(Base):
    """NOT DEFINED
    The SwitchHostRangeLearnedInfoTriggerAttributes class encapsulates a required switchHostRangeLearnedInfoTriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'switchHostRangeLearnedInfoTriggerAttributes'
    _SDM_ATT_MAP = {
        'CustomPacket': 'customPacket',
        'DestinationCustom': 'destinationCustom',
        'DestinationCustomIpv4Address': 'destinationCustomIpv4Address',
        'DestinationCustomIpv4AddressStep': 'destinationCustomIpv4AddressStep',
        'DestinationCustomMacAddress': 'destinationCustomMacAddress',
        'DestinationCustomMacAddressStep': 'destinationCustomMacAddressStep',
        'DestinationHostList': 'destinationHostList',
        'MeshingType': 'meshingType',
        'PacketType': 'packetType',
        'PeriodIntervalInMs': 'periodIntervalInMs',
        'Periodic': 'periodic',
        'PeriodicIterationNumber': 'periodicIterationNumber',
        'ResponseTimeout': 'responseTimeout',
        'SourceHostList': 'sourceHostList',
    }

    def __init__(self, parent):
        super(SwitchHostRangeLearnedInfoTriggerAttributes, self).__init__(parent)

    @property
    def CustomPacket(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomPacket'])
    @CustomPacket.setter
    def CustomPacket(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomPacket'], value)

    @property
    def DestinationCustom(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationCustom'])
    @DestinationCustom.setter
    def DestinationCustom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationCustom'], value)

    @property
    def DestinationCustomIpv4Address(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationCustomIpv4Address'])
    @DestinationCustomIpv4Address.setter
    def DestinationCustomIpv4Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationCustomIpv4Address'], value)

    @property
    def DestinationCustomIpv4AddressStep(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationCustomIpv4AddressStep'])
    @DestinationCustomIpv4AddressStep.setter
    def DestinationCustomIpv4AddressStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationCustomIpv4AddressStep'], value)

    @property
    def DestinationCustomMacAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationCustomMacAddress'])
    @DestinationCustomMacAddress.setter
    def DestinationCustomMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationCustomMacAddress'], value)

    @property
    def DestinationCustomMacAddressStep(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationCustomMacAddressStep'])
    @DestinationCustomMacAddressStep.setter
    def DestinationCustomMacAddressStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationCustomMacAddressStep'], value)

    @property
    def DestinationHostList(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../switchHostRanges]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationHostList'])
    @DestinationHostList.setter
    def DestinationHostList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationHostList'], value)

    @property
    def MeshingType(self):
        """
        Returns
        -------
        - str(fullyMesh): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeshingType'])
    @MeshingType.setter
    def MeshingType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeshingType'], value)

    @property
    def PacketType(self):
        """
        Returns
        -------
        - str(arp | ping | custom): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketType'])
    @PacketType.setter
    def PacketType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketType'], value)

    @property
    def PeriodIntervalInMs(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeriodIntervalInMs'])
    @PeriodIntervalInMs.setter
    def PeriodIntervalInMs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeriodIntervalInMs'], value)

    @property
    def Periodic(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Periodic'])
    @Periodic.setter
    def Periodic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Periodic'], value)

    @property
    def PeriodicIterationNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeriodicIterationNumber'])
    @PeriodicIterationNumber.setter
    def PeriodicIterationNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeriodicIterationNumber'], value)

    @property
    def ResponseTimeout(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResponseTimeout'])
    @ResponseTimeout.setter
    def ResponseTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResponseTimeout'], value)

    @property
    def SourceHostList(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../switchHostRanges]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceHostList'])
    @SourceHostList.setter
    def SourceHostList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceHostList'], value)

    def update(self, CustomPacket=None, DestinationCustom=None, DestinationCustomIpv4Address=None, DestinationCustomIpv4AddressStep=None, DestinationCustomMacAddress=None, DestinationCustomMacAddressStep=None, DestinationHostList=None, MeshingType=None, PacketType=None, PeriodIntervalInMs=None, Periodic=None, PeriodicIterationNumber=None, ResponseTimeout=None, SourceHostList=None):
        """Updates switchHostRangeLearnedInfoTriggerAttributes resource on the server.

        Args
        ----
        - CustomPacket (str): NOT DEFINED
        - DestinationCustom (bool): NOT DEFINED
        - DestinationCustomIpv4Address (str): NOT DEFINED
        - DestinationCustomIpv4AddressStep (str): NOT DEFINED
        - DestinationCustomMacAddress (str): NOT DEFINED
        - DestinationCustomMacAddressStep (str): NOT DEFINED
        - DestinationHostList (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../switchHostRanges])): NOT DEFINED
        - MeshingType (str(fullyMesh)): NOT DEFINED
        - PacketType (str(arp | ping | custom)): NOT DEFINED
        - PeriodIntervalInMs (number): NOT DEFINED
        - Periodic (bool): NOT DEFINED
        - PeriodicIterationNumber (number): NOT DEFINED
        - ResponseTimeout (number): NOT DEFINED
        - SourceHostList (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../switchHostRanges])): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
