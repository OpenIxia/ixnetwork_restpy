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


class DhcpoPppClientEndpoint(Base):
    """Plugin that manages DHCPoPPP on port.
    The DhcpoPppClientEndpoint class encapsulates a list of dhcpoPppClientEndpoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the DhcpoPppClientEndpoint.find() method.
    The list can be managed by using the DhcpoPppClientEndpoint.add() and DhcpoPppClientEndpoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpoPppClientEndpoint'
    _SDM_ATT_MAP = {
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(DhcpoPppClientEndpoint, self).__init__(parent)

    @property
    def Range(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.range_df989eb48817c7440dc6576fa44a3b35.Range): An instance of the Range class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.range_df989eb48817c7440dc6576fa44a3b35 import Range
        return Range(self)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, Name=None):
        """Updates dhcpoPppClientEndpoint resource on the server.

        Args
        ----
        - Name (str): Name of range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        """Adds a new dhcpoPppClientEndpoint resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of range

        Returns
        -------
        - self: This instance with all currently retrieved dhcpoPppClientEndpoint resources using find and the newly added dhcpoPppClientEndpoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpoPppClientEndpoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Name=None, ObjectId=None):
        """Finds and retrieves dhcpoPppClientEndpoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpoPppClientEndpoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpoPppClientEndpoint resources from the server.

        Args
        ----
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching dhcpoPppClientEndpoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpoPppClientEndpoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpoPppClientEndpoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort protocols on all selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(Arg2=enum)
        ----------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/amt,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/amt,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/amt,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/amt,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/amt,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/amt,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/amt,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/amt,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/amt,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/amt,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/amt,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/amt,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcFportFwdEndpoint]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DhcpHostsClearStats(self):
        """Executes the dhcpHostsClearStats operation on the server.

        Clear DHCPHosts statistics for selected plugins

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('dhcpHostsClearStats', payload=payload, response_object=None)

    def DhcpHostsPause(self):
        """Executes the dhcpHostsPause operation on the server.

        Pause negotiation of DHCPHosts for selected plugins and ranges

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('dhcpHostsPause', payload=payload, response_object=None)

    def DhcpHostsResume(self):
        """Executes the dhcpHostsResume operation on the server.

        Resume previously paused negotiation of DHCPHosts for selected plugins and ranges

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('dhcpHostsResume', payload=payload, response_object=None)

    def DhcpHostsStart(self, *args, **kwargs):
        """Executes the dhcpHostsStart operation on the server.

        Negotiate DHCPHosts for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dhcpHostsStart(Arg2=enum)
        -------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dhcpHostsStart', payload=payload, response_object=None)

    def DhcpHostsStop(self, *args, **kwargs):
        """Executes the dhcpHostsStop operation on the server.

        Release DHCPHosts for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dhcpHostsStop(Arg2=enum)
        ------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dhcpHostsStop', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Negotiate sessions for all protocols on all ranges belonging to selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(Arg2=enum)
        ----------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Teardown sessions for all protocols on all ranges belonging to selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(Arg2=enum)
        ---------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
