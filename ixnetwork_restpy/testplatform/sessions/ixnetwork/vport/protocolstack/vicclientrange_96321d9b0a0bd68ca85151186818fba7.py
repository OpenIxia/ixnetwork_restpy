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


class VicClientRange(Base):
    """Range settings for VIC protocol
    The VicClientRange class encapsulates a list of vicClientRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the VicClientRange.find() method.
    The list can be managed by the user by using the VicClientRange.add() and VicClientRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vicClientRange'

    def __init__(self, parent):
        super(VicClientRange, self).__init__(parent)

    @property
    def ChannelIdIncrement(self):
        """The increment step for channel ID.

        Returns:
            number
        """
        return self._get_attribute('channelIdIncrement')
    @ChannelIdIncrement.setter
    def ChannelIdIncrement(self, value):
        self._set_attribute('channelIdIncrement', value)

    @property
    def ChannelIdStart(self):
        """The channel ID within VIC session.

        Returns:
            number
        """
        return self._get_attribute('channelIdStart')
    @ChannelIdStart.setter
    def ChannelIdStart(self, value):
        self._set_attribute('channelIdStart', value)

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
    def MacsPerVif(self):
        """Number of MAC interfaces managed by a single VIF object.

        Returns:
            number
        """
        return self._get_attribute('macsPerVif')
    @MacsPerVif.setter
    def MacsPerVif(self, value):
        self._set_attribute('macsPerVif', value)

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
    def ProvInfoOui(self):
        """IEEE OUI owning the provisioning information type space.

        Returns:
            str
        """
        return self._get_attribute('provInfoOui')
    @ProvInfoOui.setter
    def ProvInfoOui(self, value):
        self._set_attribute('provInfoOui', value)

    @property
    def ProvInfoTlvs(self):
        """The provisioning TLVs associated with this range.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=vicOptionSet)
        """
        return self._get_attribute('provInfoTlvs')
    @ProvInfoTlvs.setter
    def ProvInfoTlvs(self, value):
        self._set_attribute('provInfoTlvs', value)

    @property
    def ProvInfoType(self):
        """The type of the provisioning information (defined in each namespace).

        Returns:
            number
        """
        return self._get_attribute('provInfoType')
    @ProvInfoType.setter
    def ProvInfoType(self, value):
        self._set_attribute('provInfoType', value)

    @property
    def TlvOffset(self):
        """The number of TLV increments to apply before using the TLV values for this range.

        Returns:
            number
        """
        return self._get_attribute('tlvOffset')
    @TlvOffset.setter
    def TlvOffset(self, value):
        self._set_attribute('tlvOffset', value)

    @property
    def VifActive(self):
        """The initial state of this interface set: true for Active, false for Standby.

        Returns:
            bool
        """
        return self._get_attribute('vifActive')
    @VifActive.setter
    def VifActive(self, value):
        self._set_attribute('vifActive', value)

    def update(self, ChannelIdIncrement=None, ChannelIdStart=None, Enabled=None, MacsPerVif=None, Name=None, ProvInfoOui=None, ProvInfoTlvs=None, ProvInfoType=None, TlvOffset=None, VifActive=None):
        """Updates a child instance of vicClientRange on the server.

        Args:
            ChannelIdIncrement (number): The increment step for channel ID.
            ChannelIdStart (number): The channel ID within VIC session.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            MacsPerVif (number): Number of MAC interfaces managed by a single VIF object.
            Name (str): Name of range
            ProvInfoOui (str): IEEE OUI owning the provisioning information type space.
            ProvInfoTlvs (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=vicOptionSet)): The provisioning TLVs associated with this range.
            ProvInfoType (number): The type of the provisioning information (defined in each namespace).
            TlvOffset (number): The number of TLV increments to apply before using the TLV values for this range.
            VifActive (bool): The initial state of this interface set: true for Active, false for Standby.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ChannelIdIncrement=None, ChannelIdStart=None, Enabled=None, MacsPerVif=None, Name=None, ProvInfoOui=None, ProvInfoTlvs=None, ProvInfoType=None, TlvOffset=None, VifActive=None):
        """Adds a new vicClientRange node on the server and retrieves it in this instance.

        Args:
            ChannelIdIncrement (number): The increment step for channel ID.
            ChannelIdStart (number): The channel ID within VIC session.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            MacsPerVif (number): Number of MAC interfaces managed by a single VIF object.
            Name (str): Name of range
            ProvInfoOui (str): IEEE OUI owning the provisioning information type space.
            ProvInfoTlvs (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=vicOptionSet)): The provisioning TLVs associated with this range.
            ProvInfoType (number): The type of the provisioning information (defined in each namespace).
            TlvOffset (number): The number of TLV increments to apply before using the TLV values for this range.
            VifActive (bool): The initial state of this interface set: true for Active, false for Standby.

        Returns:
            self: This instance with all currently retrieved vicClientRange data using find and the newly added vicClientRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vicClientRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ChannelIdIncrement=None, ChannelIdStart=None, Enabled=None, MacsPerVif=None, Name=None, ObjectId=None, ProvInfoOui=None, ProvInfoTlvs=None, ProvInfoType=None, TlvOffset=None, VifActive=None):
        """Finds and retrieves vicClientRange data from the server.

        All named parameters support regex and can be used to selectively retrieve vicClientRange data from the server.
        By default the find method takes no parameters and will retrieve all vicClientRange data from the server.

        Args:
            ChannelIdIncrement (number): The increment step for channel ID.
            ChannelIdStart (number): The channel ID within VIC session.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            MacsPerVif (number): Number of MAC interfaces managed by a single VIF object.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            ProvInfoOui (str): IEEE OUI owning the provisioning information type space.
            ProvInfoTlvs (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=vicOptionSet)): The provisioning TLVs associated with this range.
            ProvInfoType (number): The type of the provisioning information (defined in each namespace).
            TlvOffset (number): The number of TLV increments to apply before using the TLV values for this range.
            VifActive (bool): The initial state of this interface set: true for Active, false for Standby.

        Returns:
            self: This instance with matching vicClientRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vicClientRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vicClientRange data from the server available through an iterator or index

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

    def VicClientActivate(self):
        """Executes the vicClientActivate operation on the server.

        Send VIF-ACTIVATE for selected ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientActivate', payload=payload, response_object=None)

    def VicClientCreate(self):
        """Executes the vicClientCreate operation on the server.

        Send VIF-CREATE for selected ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientCreate', payload=payload, response_object=None)

    def VicClientDeactivate(self):
        """Executes the vicClientDeactivate operation on the server.

        Send VIF-DEACTIVATE for selected ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientDeactivate', payload=payload, response_object=None)

    def VicClientDelete(self):
        """Executes the vicClientDelete operation on the server.

        Send VIF-DELETE for selected ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientDelete', payload=payload, response_object=None)

    def VicClientDisable(self):
        """Executes the vicClientDisable operation on the server.

        Send VIF-DISABLE for selected ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientDisable', payload=payload, response_object=None)

    def VicClientEnable(self):
        """Executes the vicClientEnable operation on the server.

        Send VIF-ENABLE for selected ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientEnable', payload=payload, response_object=None)

    def VicClientStart(self, *args, **kwargs):
        """Executes the vicClientStart operation on the server.

        Negotiate VIC sessions for selected ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        vicClientStart()

        vicClientStart(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vepaEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vicClient,/vport/protocolStack/ethernetEndpoint/range/vicClientRange,/vport/protocolStack/ethernetEndpoint/vicClient]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('vicClientStart', payload=payload, response_object=None)

    def VicClientStop(self, *args, **kwargs):
        """Executes the vicClientStop operation on the server.

        Teardown VIC sessions for selected ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        vicClientStop()

        vicClientStop(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/ipEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vepaEndpoint/range/vicClientRange,/vport/protocolStack/ethernet/vicClient,/vport/protocolStack/ethernetEndpoint/range/vicClientRange,/vport/protocolStack/ethernetEndpoint/vicClient]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('vicClientStop', payload=payload, response_object=None)
