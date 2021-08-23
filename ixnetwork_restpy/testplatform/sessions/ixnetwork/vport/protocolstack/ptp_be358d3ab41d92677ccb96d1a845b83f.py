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


class Ptp(Base):
    """Network stack element plugin that manages dynamic PTP clocks
    as a list of address blocks or 'ranges'.
    The Ptp class encapsulates a list of ptp resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ptp.find() method.
    The list can be managed by using the Ptp.add() and Ptp.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ptp'
    _SDM_ATT_MAP = {
        'Name': 'name',
        'ObjectId': 'objectId',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Ptp, self).__init__(parent, list_op)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, Name=None):
        # type: (str) -> Ptp
        """Updates ptp resource on the server.

        Args
        ----
        - Name (str): Name of range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        # type: (str) -> Ptp
        """Adds a new ptp resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of range

        Returns
        -------
        - self: This instance with all currently retrieved ptp resources using find and the newly added ptp resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ptp resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Name=None, ObjectId=None):
        # type: (str, str) -> Ptp
        """Finds and retrieves ptp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ptp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ptp resources from the server.

        Args
        ----
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching ptp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ptp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ptp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
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
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
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

    def PtpChangeDropSignalParams(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpChangeDropSignalParams operation on the server.

        Change Drop Signal Parameters

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpChangeDropSignalParams(Arg2=bool, Arg3=bool, Arg4=bool, async_operation=bool)
        --------------------------------------------------------------------------------
        - Arg2 (bool): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (bool): Drop any Signal Request received on a master side that contains one Announce TLV.
        - Arg4 (bool): Drop any Signal Request received on a master side that contains one Sync TLV.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ptpChangeDropSignalParams(Arg2=bool, Arg3=bool, Arg4=bool, Arg5=enum, async_operation=bool)
        -------------------------------------------------------------------------------------------
        - Arg2 (bool): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (bool): Drop any Signal Request received on a master side that contains one Announce TLV.
        - Arg4 (bool): Drop any Signal Request received on a master side that contains one Sync TLV.
        - Arg5 (str(async | sync)): Drop any Signal Request received on a master side that contains one DelayResp TLV.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeDropSignalParams', payload=payload, response_object=None)

    def PtpChangeMiscParams(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpChangeMiscParams operation on the server.

        Change Misc Parameters

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpChangeMiscParams(Arg2=number, Arg3=number, async_operation=bool)
        -------------------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): PTP Domain.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ptpChangeMiscParams(Arg2=number, Arg3=number, Arg4=enum, async_operation=bool)
        ------------------------------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): PTP Domain.
        - Arg4 (str(async | sync)): The number of announceInterval that has to pass without receipt of an Announce message.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeMiscParams', payload=payload, response_object=None)

    def PtpChangeNegativeTesting(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpChangeNegativeTesting operation on the server.

        Change Negative Testing Parameters

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpChangeNegativeTesting(Arg2=number, Arg3=number, Arg4=number, Arg5=number, Arg6=number, Arg7=number, Arg8=number, Arg9=number, Arg10=number, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds).
        - Arg4 (number): Percentage rate of the Follow_Up messages in which the delay is introduced.
        - Arg5 (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        - Arg6 (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
        - Arg7 (number): Percentage rate of the dropped Announce messages.
        - Arg8 (number): Percentage rate of the dropped Sync messages.
        - Arg9 (number): Percentage rate of the dropped Follow_Up messages.
        - Arg10 (number): Percentage rate of the dropped Delay_Resp messages.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ptpChangeNegativeTesting(Arg2=number, Arg3=number, Arg4=number, Arg5=number, Arg6=number, Arg7=number, Arg8=number, Arg9=number, Arg10=number, Arg11=enum, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds).
        - Arg4 (number): Percentage rate of the Follow_Up messages in which the delay is introduced.
        - Arg5 (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        - Arg6 (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
        - Arg7 (number): Percentage rate of the dropped Announce messages.
        - Arg8 (number): Percentage rate of the dropped Sync messages.
        - Arg9 (number): Percentage rate of the dropped Follow_Up messages.
        - Arg10 (number): Percentage rate of the dropped Delay_Resp messages.
        - Arg11 (str(async | sync)): Percentage rate of the bad crc Follow_Up messages.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeNegativeTesting', payload=payload, response_object=None)

    def PtpClearStats(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpClearStats operation on the server.

        Clear PTP statistics for selected plugins

        ptpClearStats(async_operation=bool)
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpClearStats', payload=payload, response_object=None)

    def PtpConfigure(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpConfigure operation on the server.

        Configure PTP protocol on selected ranges.

        ptpConfigure(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpConfigure', payload=payload, response_object=None)

    def PtpPause(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpPause operation on the server.

        Pause negotiation of PTP for selected plugins and ranges

        ptpPause(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpPause', payload=payload, response_object=None)

    def PtpResume(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpResume operation on the server.

        Resume previously paused negotiation of PTP for selected plugins and ranges

        ptpResume(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpResume', payload=payload, response_object=None)

    def PtpStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpStart operation on the server.

        Negotiate PTP for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpStart(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ptpStart(Arg2=enum, async_operation=bool)
        -----------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpStart', payload=payload, response_object=None)

    def PtpStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ptpStop operation on the server.

        Release PTP for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpStop(async_operation=bool)
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ptpStop(Arg2=enum, async_operation=bool)
        ----------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpStop', payload=payload, response_object=None)
