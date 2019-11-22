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


class VicClient(Base):
    """Settings for vNIC Interface Control protocol
    The VicClient class encapsulates a list of vicClient resources that is be managed by the user.
    A list of resources can be retrieved from the server using the VicClient.find() method.
    The list can be managed by the user by using the VicClient.add() and VicClient.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vicClient'

    def __init__(self, parent):
        super(VicClient, self).__init__(parent)

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

    def update(self, Name=None):
        """Updates a child instance of vicClient on the server.

        Args:
            Name (str): Name of range

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Name=None):
        """Adds a new vicClient node on the server and retrieves it in this instance.

        Args:
            Name (str): Name of range

        Returns:
            self: This instance with all currently retrieved vicClient data using find and the newly added vicClient data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vicClient data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Name=None, ObjectId=None):
        """Finds and retrieves vicClient data from the server.

        All named parameters support regex and can be used to selectively retrieve vicClient data from the server.
        By default the find method takes no parameters and will retrieve all vicClient data from the server.

        Args:
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching vicClient data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vicClient data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vicClient data from the server available through an iterator or index

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

    def VicClientClearStats(self):
        """Executes the vicClientClearStats operation on the server.

        Clear VIC statistics for selected plugins

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientClearStats', payload=payload, response_object=None)

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

    def VicClientFastDeconfigure(self, *args, **kwargs):
        """Executes the vicClientFastDeconfigure operation on the server.

        Fast deconfigure VIC sessions for selected plugins

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        vicClientFastDeconfigure()

        vicClientFastDeconfigure(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/ethernet/vicClient,/vport/protocolStack/ethernetEndpoint/vicClient]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('vicClientFastDeconfigure', payload=payload, response_object=None)

    def VicClientOpen(self):
        """Executes the vicClientOpen operation on the server.

        Send VIC-OPEN for selected plugins

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('vicClientOpen', payload=payload, response_object=None)

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
