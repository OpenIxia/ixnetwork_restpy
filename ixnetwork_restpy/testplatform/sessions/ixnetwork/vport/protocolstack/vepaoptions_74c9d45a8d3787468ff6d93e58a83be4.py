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


class VepaOptions(Base):
    """
    The VepaOptions class encapsulates a list of vepaOptions resources that is be managed by the user.
    A list of resources can be retrieved from the server using the VepaOptions.find() method.
    The list can be managed by the user by using the VepaOptions.add() and VepaOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vepaOptions'

    def __init__(self, parent):
        super(VepaOptions, self).__init__(parent)

    @property
    def EcpDestinationMac(self):
        """Destination MAC address for ECP packets.

        Returns:
            str
        """
        return self._get_attribute('ecpDestinationMac')
    @EcpDestinationMac.setter
    def EcpDestinationMac(self, value):
        self._set_attribute('ecpDestinationMac', value)

    @property
    def EcpEthertype(self):
        """2 byte value used for encapsulating ethertype field in MAC header for ECP packets.

        Returns:
            str
        """
        return self._get_attribute('ecpEthertype')
    @EcpEthertype.setter
    def EcpEthertype(self, value):
        self._set_attribute('ecpEthertype', value)

    @property
    def LldpCdcpDestinationMac(self):
        """Destination MAC address for LLDP-CDCP packets.

        Returns:
            str
        """
        return self._get_attribute('lldpCdcpDestinationMac')
    @LldpCdcpDestinationMac.setter
    def LldpCdcpDestinationMac(self, value):
        self._set_attribute('lldpCdcpDestinationMac', value)

    @property
    def LldpEvbDestinationMac(self):
        """Destination MAC address for LLDP-EVB packets.

        Returns:
            str
        """
        return self._get_attribute('lldpEvbDestinationMac')
    @LldpEvbDestinationMac.setter
    def LldpEvbDestinationMac(self, value):
        self._set_attribute('lldpEvbDestinationMac', value)

    @property
    def MaxVdpCommands(self):
        """Max Outstanding VDP Commands.

        Returns:
            number
        """
        return self._get_attribute('maxVdpCommands')
    @MaxVdpCommands.setter
    def MaxVdpCommands(self, value):
        self._set_attribute('maxVdpCommands', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def OverrideGlobalVsiRateControl(self):
        """If true then all the VSI Rate settings defined at Session level will be overriden by VSI Rate settings defined on this PortGroup.

        Returns:
            bool
        """
        return self._get_attribute('overrideGlobalVsiRateControl')
    @OverrideGlobalVsiRateControl.setter
    def OverrideGlobalVsiRateControl(self, value):
        self._set_attribute('overrideGlobalVsiRateControl', value)

    @property
    def SetupRate(self):
        """Setup rate is the number of VSIs to start in each second.

        Returns:
            number
        """
        return self._get_attribute('setupRate')
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute('setupRate', value)

    @property
    def TeardownRate(self):
        """Teardown rate is the number of VSIs to stop in each second.

        Returns:
            number
        """
        return self._get_attribute('teardownRate')
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute('teardownRate', value)

    def update(self, EcpDestinationMac=None, EcpEthertype=None, LldpCdcpDestinationMac=None, LldpEvbDestinationMac=None, MaxVdpCommands=None, OverrideGlobalVsiRateControl=None, SetupRate=None, TeardownRate=None):
        """Updates a child instance of vepaOptions on the server.

        Args:
            EcpDestinationMac (str): Destination MAC address for ECP packets.
            EcpEthertype (str): 2 byte value used for encapsulating ethertype field in MAC header for ECP packets.
            LldpCdcpDestinationMac (str): Destination MAC address for LLDP-CDCP packets.
            LldpEvbDestinationMac (str): Destination MAC address for LLDP-EVB packets.
            MaxVdpCommands (number): Max Outstanding VDP Commands.
            OverrideGlobalVsiRateControl (bool): If true then all the VSI Rate settings defined at Session level will be overriden by VSI Rate settings defined on this PortGroup.
            SetupRate (number): Setup rate is the number of VSIs to start in each second.
            TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, EcpDestinationMac=None, EcpEthertype=None, LldpCdcpDestinationMac=None, LldpEvbDestinationMac=None, MaxVdpCommands=None, OverrideGlobalVsiRateControl=None, SetupRate=None, TeardownRate=None):
        """Adds a new vepaOptions node on the server and retrieves it in this instance.

        Args:
            EcpDestinationMac (str): Destination MAC address for ECP packets.
            EcpEthertype (str): 2 byte value used for encapsulating ethertype field in MAC header for ECP packets.
            LldpCdcpDestinationMac (str): Destination MAC address for LLDP-CDCP packets.
            LldpEvbDestinationMac (str): Destination MAC address for LLDP-EVB packets.
            MaxVdpCommands (number): Max Outstanding VDP Commands.
            OverrideGlobalVsiRateControl (bool): If true then all the VSI Rate settings defined at Session level will be overriden by VSI Rate settings defined on this PortGroup.
            SetupRate (number): Setup rate is the number of VSIs to start in each second.
            TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Returns:
            self: This instance with all currently retrieved vepaOptions data using find and the newly added vepaOptions data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vepaOptions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EcpDestinationMac=None, EcpEthertype=None, LldpCdcpDestinationMac=None, LldpEvbDestinationMac=None, MaxVdpCommands=None, ObjectId=None, OverrideGlobalVsiRateControl=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves vepaOptions data from the server.

        All named parameters support regex and can be used to selectively retrieve vepaOptions data from the server.
        By default the find method takes no parameters and will retrieve all vepaOptions data from the server.

        Args:
            EcpDestinationMac (str): Destination MAC address for ECP packets.
            EcpEthertype (str): 2 byte value used for encapsulating ethertype field in MAC header for ECP packets.
            LldpCdcpDestinationMac (str): Destination MAC address for LLDP-CDCP packets.
            LldpEvbDestinationMac (str): Destination MAC address for LLDP-EVB packets.
            MaxVdpCommands (number): Max Outstanding VDP Commands.
            ObjectId (str): Unique identifier for this object
            OverrideGlobalVsiRateControl (bool): If true then all the VSI Rate settings defined at Session level will be overriden by VSI Rate settings defined on this PortGroup.
            SetupRate (number): Setup rate is the number of VSIs to start in each second.
            TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Returns:
            self: This instance with matching vepaOptions data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vepaOptions data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vepaOptions data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
