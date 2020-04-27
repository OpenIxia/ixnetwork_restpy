# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class GenerateRoutesParams(Base):
    """Generate Primary and Duplicate Routes with advanced prefix length distribution options.
    The GenerateRoutesParams class encapsulates a required generateRoutesParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'generateRoutesParams'

    def __init__(self, parent):
        super(GenerateRoutesParams, self).__init__(parent)

    @property
    def AddressRangesToSkip(self):
        """
        Returns
        -------
        - str: Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: 192.0.0.0 - 192.255.255.255
        """
        return self._get_attribute('addressRangesToSkip')
    @AddressRangesToSkip.setter
    def AddressRangesToSkip(self, value):
        self._set_attribute('addressRangesToSkip', value)

    @property
    def CustomDistributionFile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.files.Files): Source file having custom distribution information.
        """
        return self._get_attribute('customDistributionFile')
    @CustomDistributionFile.setter
    def CustomDistributionFile(self, value):
        self._set_attribute('customDistributionFile', value)

    @property
    def DuplicateRoutesAsPathSuffix(self):
        """
        Returns
        -------
        - str: AS Path Suffix for Duplicate Routes
        """
        return self._get_attribute('duplicateRoutesAsPathSuffix')
    @DuplicateRoutesAsPathSuffix.setter
    def DuplicateRoutesAsPathSuffix(self, value):
        self._set_attribute('duplicateRoutesAsPathSuffix', value)

    @property
    def DuplicateRoutesPerDevicePercent(self):
        """
        Returns
        -------
        - number: Percentage to Duplicate Primary Routes per Device.
        """
        return self._get_attribute('duplicateRoutesPerDevicePercent')
    @DuplicateRoutesPerDevicePercent.setter
    def DuplicateRoutesPerDevicePercent(self, value):
        self._set_attribute('duplicateRoutesPerDevicePercent', value)

    @property
    def NetworkAddressStart(self):
        """
        Returns
        -------
        - str: Network Address Start Value.
        """
        return self._get_attribute('networkAddressStart')
    @NetworkAddressStart.setter
    def NetworkAddressStart(self, value):
        self._set_attribute('networkAddressStart', value)

    @property
    def NetworkAddressStep(self):
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute('networkAddressStep')
    @NetworkAddressStep.setter
    def NetworkAddressStep(self, value):
        self._set_attribute('networkAddressStep', value)

    @property
    def PrefixLengthDistributionScope(self):
        """
        Returns
        -------
        - str(perTopology | perDevice | perPort): Prefix Length Distribution Scope.
        """
        return self._get_attribute('prefixLengthDistributionScope')
    @PrefixLengthDistributionScope.setter
    def PrefixLengthDistributionScope(self, value):
        self._set_attribute('prefixLengthDistributionScope', value)

    @property
    def PrefixLengthDistributionType(self):
        """
        Returns
        -------
        - str(fixed | random | even | exponential | internet | custom): Prefix Length Distribution Type.
        """
        return self._get_attribute('prefixLengthDistributionType')
    @PrefixLengthDistributionType.setter
    def PrefixLengthDistributionType(self, value):
        self._set_attribute('prefixLengthDistributionType', value)

    @property
    def PrefixLengthEnd(self):
        """
        Returns
        -------
        - number: Prefix Length End Value. Applicable only for Even and Exponential distribution type.
        """
        return self._get_attribute('prefixLengthEnd')
    @PrefixLengthEnd.setter
    def PrefixLengthEnd(self, value):
        self._set_attribute('prefixLengthEnd', value)

    @property
    def PrefixLengthStart(self):
        """
        Returns
        -------
        - number: Prefix Length Start Value. Applicable only for Fixed, Even and Exponential distribution type.
        """
        return self._get_attribute('prefixLengthStart')
    @PrefixLengthStart.setter
    def PrefixLengthStart(self, value):
        self._set_attribute('prefixLengthStart', value)

    @property
    def PrimaryRoutesAsPathSuffix(self):
        """
        Returns
        -------
        - str: AS Path Suffix for Primary Routes
        """
        return self._get_attribute('primaryRoutesAsPathSuffix')
    @PrimaryRoutesAsPathSuffix.setter
    def PrimaryRoutesAsPathSuffix(self, value):
        self._set_attribute('primaryRoutesAsPathSuffix', value)

    @property
    def PrimaryRoutesPerDevice(self):
        """
        Returns
        -------
        - number: Number of Primary Routes per Device.
        """
        return self._get_attribute('primaryRoutesPerDevice')
    @PrimaryRoutesPerDevice.setter
    def PrimaryRoutesPerDevice(self, value):
        self._set_attribute('primaryRoutesPerDevice', value)

    @property
    def PrimaryRoutesPerRange(self):
        """
        Returns
        -------
        - number: Number of Routes per Route Range.
        """
        return self._get_attribute('primaryRoutesPerRange')
    @PrimaryRoutesPerRange.setter
    def PrimaryRoutesPerRange(self, value):
        self._set_attribute('primaryRoutesPerRange', value)

    @property
    def SkipLoopback(self):
        """
        Returns
        -------
        - bool: Do not include Loopback Address in the generated Address Range
        """
        return self._get_attribute('skipLoopback')
    @SkipLoopback.setter
    def SkipLoopback(self, value):
        self._set_attribute('skipLoopback', value)

    @property
    def SkipMcast(self):
        """
        Returns
        -------
        - bool: Do not include Multicast Address in the generated Address Range
        """
        return self._get_attribute('skipMcast')
    @SkipMcast.setter
    def SkipMcast(self, value):
        self._set_attribute('skipMcast', value)

    def update(self, AddressRangesToSkip=None, CustomDistributionFile=None, DuplicateRoutesAsPathSuffix=None, DuplicateRoutesPerDevicePercent=None, NetworkAddressStart=None, NetworkAddressStep=None, PrefixLengthDistributionScope=None, PrefixLengthDistributionType=None, PrefixLengthEnd=None, PrefixLengthStart=None, PrimaryRoutesAsPathSuffix=None, PrimaryRoutesPerDevice=None, PrimaryRoutesPerRange=None, SkipLoopback=None, SkipMcast=None):
        """Updates generateRoutesParams resource on the server.

        Args
        ----
        - AddressRangesToSkip (str): Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: 192.0.0.0 - 192.255.255.255
        - CustomDistributionFile (obj(ixnetwork_restpy.files.Files)): Source file having custom distribution information.
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
        return self._update(locals())

    def GenerateRoutes(self):
        """Executes the generateRoutes operation on the server.

        Generate Primary and Duplicate Routes with advanced prefix length distribution options.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateRoutes', payload=payload, response_object=None)
