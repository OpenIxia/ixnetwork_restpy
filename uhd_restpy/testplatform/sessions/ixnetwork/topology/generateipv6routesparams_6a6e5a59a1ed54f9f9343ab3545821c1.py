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


class GenerateIpv6RoutesParams(Base):
    """Generate Primary and Duplicate Routes with advanced prefix length distribution options.
    The GenerateIpv6RoutesParams class encapsulates a required generateIpv6RoutesParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'generateIpv6RoutesParams'
    _SDM_ATT_MAP = {
        'AddressRangesToSkip': 'addressRangesToSkip',
        'CustomDistributionFile': 'customDistributionFile',
        'DuplicateRoutesAsPathSuffix': 'duplicateRoutesAsPathSuffix',
        'DuplicateRoutesPerDevicePercent': 'duplicateRoutesPerDevicePercent',
        'NetworkAddressStart': 'networkAddressStart',
        'NetworkAddressStep': 'networkAddressStep',
        'PrefixLengthDistributionScope': 'prefixLengthDistributionScope',
        'PrefixLengthDistributionType': 'prefixLengthDistributionType',
        'PrefixLengthEnd': 'prefixLengthEnd',
        'PrefixLengthStart': 'prefixLengthStart',
        'PrimaryRoutesAsPathSuffix': 'primaryRoutesAsPathSuffix',
        'PrimaryRoutesPerDevice': 'primaryRoutesPerDevice',
        'PrimaryRoutesPerRange': 'primaryRoutesPerRange',
        'SkipLoopback': 'skipLoopback',
        'SkipMcast': 'skipMcast',
    }
    _SDM_ENUM_MAP = {
        'prefixLengthDistributionScope': ['perTopology', 'perDevice', 'perPort'],
        'prefixLengthDistributionType': ['fixed', 'random', 'even', 'exponential', 'internet', 'custom'],
    }

    def __init__(self, parent, list_op=False):
        super(GenerateIpv6RoutesParams, self).__init__(parent, list_op)

    @property
    def AddressRangesToSkip(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: aa:0:1:b: - bb:0:2:c:, aa00: - bb00:1
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressRangesToSkip'])
    @AddressRangesToSkip.setter
    def AddressRangesToSkip(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AddressRangesToSkip'], value)

    @property
    def CustomDistributionFile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.files.Files): Source file having custom distribution information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomDistributionFile'])
    @CustomDistributionFile.setter
    def CustomDistributionFile(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomDistributionFile'], value)

    @property
    def DuplicateRoutesAsPathSuffix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: AS Path Suffix for Duplicate Routes
        """
        return self._get_attribute(self._SDM_ATT_MAP['DuplicateRoutesAsPathSuffix'])
    @DuplicateRoutesAsPathSuffix.setter
    def DuplicateRoutesAsPathSuffix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DuplicateRoutesAsPathSuffix'], value)

    @property
    def DuplicateRoutesPerDevicePercent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Percentage to Duplicate Primary Routes per Device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DuplicateRoutesPerDevicePercent'])
    @DuplicateRoutesPerDevicePercent.setter
    def DuplicateRoutesPerDevicePercent(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DuplicateRoutesPerDevicePercent'], value)

    @property
    def NetworkAddressStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Start Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkAddressStart'])
    @NetworkAddressStart.setter
    def NetworkAddressStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NetworkAddressStart'], value)

    @property
    def NetworkAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkAddressStep'])
    @NetworkAddressStep.setter
    def NetworkAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NetworkAddressStep'], value)

    @property
    def PrefixLengthDistributionScope(self):
        # type: () -> str
        """
        Returns
        -------
        - str(perTopology | perDevice | perPort): Prefix Length Distribution Scope.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLengthDistributionScope'])
    @PrefixLengthDistributionScope.setter
    def PrefixLengthDistributionScope(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PrefixLengthDistributionScope'], value)

    @property
    def PrefixLengthDistributionType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixed | random | even | exponential | internet | custom): Prefix Length Distribution Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLengthDistributionType'])
    @PrefixLengthDistributionType.setter
    def PrefixLengthDistributionType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PrefixLengthDistributionType'], value)

    @property
    def PrefixLengthEnd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Prefix Length End Value. Applicable only for Even and Exponential distribution type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLengthEnd'])
    @PrefixLengthEnd.setter
    def PrefixLengthEnd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PrefixLengthEnd'], value)

    @property
    def PrefixLengthStart(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Prefix Length Start Value. Applicable only for Fixed, Even and Exponential distribution type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLengthStart'])
    @PrefixLengthStart.setter
    def PrefixLengthStart(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PrefixLengthStart'], value)

    @property
    def PrimaryRoutesAsPathSuffix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: AS Path Suffix for Primary Routes
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrimaryRoutesAsPathSuffix'])
    @PrimaryRoutesAsPathSuffix.setter
    def PrimaryRoutesAsPathSuffix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PrimaryRoutesAsPathSuffix'], value)

    @property
    def PrimaryRoutesPerDevice(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Primary Routes per Device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrimaryRoutesPerDevice'])
    @PrimaryRoutesPerDevice.setter
    def PrimaryRoutesPerDevice(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PrimaryRoutesPerDevice'], value)

    @property
    def PrimaryRoutesPerRange(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Routes per Route Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrimaryRoutesPerRange'])
    @PrimaryRoutesPerRange.setter
    def PrimaryRoutesPerRange(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PrimaryRoutesPerRange'], value)

    @property
    def SkipLoopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Do not include Loopback Address in the generated Address Range
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipLoopback'])
    @SkipLoopback.setter
    def SkipLoopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SkipLoopback'], value)

    @property
    def SkipMcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Do not include Multicast Address in the generated Address Range
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipMcast'])
    @SkipMcast.setter
    def SkipMcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SkipMcast'], value)

    def update(self, AddressRangesToSkip=None, CustomDistributionFile=None, DuplicateRoutesAsPathSuffix=None, DuplicateRoutesPerDevicePercent=None, NetworkAddressStart=None, NetworkAddressStep=None, PrefixLengthDistributionScope=None, PrefixLengthDistributionType=None, PrefixLengthEnd=None, PrefixLengthStart=None, PrimaryRoutesAsPathSuffix=None, PrimaryRoutesPerDevice=None, PrimaryRoutesPerRange=None, SkipLoopback=None, SkipMcast=None):
        """Updates generateIpv6RoutesParams resource on the server.

        Args
        ----
        - AddressRangesToSkip (str): Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: aa:0:1:b: - bb:0:2:c:, aa00: - bb00:1
        - CustomDistributionFile (obj(uhd_restpy.files.Files)): Source file having custom distribution information.
        - DuplicateRoutesAsPathSuffix (str): AS Path Suffix for Duplicate Routes
        - DuplicateRoutesPerDevicePercent (number): Percentage to Duplicate Primary Routes per Device.
        - NetworkAddressStart (str): Network Address Start Value.
        - NetworkAddressStep (str): Network Address Step Value.
        - PrefixLengthDistributionScope (str(perTopology | perDevice | perPort)): Prefix Length Distribution Scope.
        - PrefixLengthDistributionType (str(fixed | random | even | exponential | internet | custom)): Prefix Length Distribution Type.
        - PrefixLengthEnd (number): Prefix Length End Value. Applicable only for Even and Exponential distribution type.
        - PrefixLengthStart (number): Prefix Length Start Value. Applicable only for Fixed, Even and Exponential distribution type.
        - PrimaryRoutesAsPathSuffix (str): AS Path Suffix for Primary Routes
        - PrimaryRoutesPerDevice (number): Number of Primary Routes per Device.
        - PrimaryRoutesPerRange (number): Number of Routes per Route Range.
        - SkipLoopback (bool): Do not include Loopback Address in the generated Address Range
        - SkipMcast (bool): Do not include Multicast Address in the generated Address Range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def GenerateIpv6Routes(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the generateIpv6Routes operation on the server.

        Generate Primary and Duplicate Routes with advanced prefix length distribution options.

        generateIpv6Routes(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateIpv6Routes', payload=payload, response_object=None)
