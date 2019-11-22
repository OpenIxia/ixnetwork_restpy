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


class EsmcRange(Base):
    """
    The EsmcRange class encapsulates a list of esmcRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the EsmcRange.find() method.
    The list can be managed by the user by using the EsmcRange.add() and EsmcRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'esmcRange'

    def __init__(self, parent):
        super(EsmcRange, self).__init__(parent)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FlagMode(self):
        """The operation of the SSM header Event flag.

        Returns:
            str
        """
        return self._get_attribute('flagMode')
    @FlagMode.setter
    def FlagMode(self, value):
        self._set_attribute('flagMode', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def Ql(self):
        """The SSM clock quality level(QL) code.

        Returns:
            str
        """
        return self._get_attribute('ql')
    @Ql.setter
    def Ql(self, value):
        self._set_attribute('ql', value)

    @property
    def Rate(self):
        """SSM message transmit rate.

        Returns:
            number
        """
        return self._get_attribute('rate')
    @Rate.setter
    def Rate(self, value):
        self._set_attribute('rate', value)

    @property
    def WaitId(self):
        """This value is true if supplicant is waiting for RequestId from DUT part.

        Returns:
            bool
        """
        return self._get_attribute('waitId')
    @WaitId.setter
    def WaitId(self, value):
        self._set_attribute('waitId', value)

    def update(self, Enabled=None, FlagMode=None, Name=None, Ql=None, Rate=None, WaitId=None):
        """Updates a child instance of esmcRange on the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FlagMode (str): The operation of the SSM header Event flag.
            Name (str): Name of range
            Ql (str): The SSM clock quality level(QL) code.
            Rate (number): SSM message transmit rate.
            WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, FlagMode=None, Name=None, Ql=None, Rate=None, WaitId=None):
        """Adds a new esmcRange node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FlagMode (str): The operation of the SSM header Event flag.
            Name (str): Name of range
            Ql (str): The SSM clock quality level(QL) code.
            Rate (number): SSM message transmit rate.
            WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Returns:
            self: This instance with all currently retrieved esmcRange data using find and the newly added esmcRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the esmcRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, FlagMode=None, Name=None, ObjectId=None, Ql=None, Rate=None, WaitId=None):
        """Finds and retrieves esmcRange data from the server.

        All named parameters support regex and can be used to selectively retrieve esmcRange data from the server.
        By default the find method takes no parameters and will retrieve all esmcRange data from the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FlagMode (str): The operation of the SSM header Event flag.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            Ql (str): The SSM clock quality level(QL) code.
            Rate (number): SSM message transmit rate.
            WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Returns:
            self: This instance with matching esmcRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of esmcRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the esmcRange data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self):
        """Executes the apply operation on the server.

        Apply changes for on the fly configuration support.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('apply', payload=payload, response_object=None)

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

    def ESMCStart(self, *args, **kwargs):
        """Executes the eSMCStart operation on the server.

        Start ESMC

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        eSMCStart()

        eSMCStart(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/esmcRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/vepaEndpoint/range/esmcRange,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/ethernetEndpoint/range/esmcRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('eSMCStart', payload=payload, response_object=None)

    def ESMCStop(self, *args, **kwargs):
        """Executes the eSMCStop operation on the server.

        Stop ESMC

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        eSMCStop()

        eSMCStop(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/esmcRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/esmcRange,/vport/protocolStack/ethernet/ipEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/esmcRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/esmcRange,/vport/protocolStack/ethernet/vepaEndpoint/range/esmcRange,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/ethernetEndpoint/range/esmcRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('eSMCStop', payload=payload, response_object=None)
