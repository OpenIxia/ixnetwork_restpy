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


class Iptv(Base):
    """
    The Iptv class encapsulates a list of iptv resources that are managed by the user.
    A list of resources can be retrieved from the server using the Iptv.find() method.
    The list can be managed by using the Iptv.add() and Iptv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'iptv'
    _SDM_ATT_MAP = {
        'CsvLogFileName': 'csvLogFileName',
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(Iptv, self).__init__(parent)

    @property
    def CsvLogFileName(self):
        """
        Returns
        -------
        - str: Defines the new name of the csv log file name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvLogFileName'])
    @CsvLogFileName.setter
    def CsvLogFileName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CsvLogFileName'], value)

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

    def update(self, CsvLogFileName=None, Name=None):
        """Updates iptv resource on the server.

        Args
        ----
        - CsvLogFileName (str): Defines the new name of the csv log file name.
        - Name (str): Name of range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CsvLogFileName=None, Name=None):
        """Adds a new iptv resource on the server and adds it to the container.

        Args
        ----
        - CsvLogFileName (str): Defines the new name of the csv log file name.
        - Name (str): Name of range

        Returns
        -------
        - self: This instance with all currently retrieved iptv resources using find and the newly added iptv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained iptv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CsvLogFileName=None, Name=None, ObjectId=None):
        """Finds and retrieves iptv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve iptv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all iptv resources from the server.

        Args
        ----
        - CsvLogFileName (str): Defines the new name of the csv log file name.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching iptv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of iptv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the iptv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def IptvStart(self, *args, **kwargs):
        """Executes the iptvStart operation on the server.

        Start IPTV on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        iptvStart(Arg2=enum)
        --------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/iptv,/vport/protocolStack/atm/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/iptv,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/iptv,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ipEndpoint/iptv,/vport/protocolStack/atm/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/iptv,/vport/protocolStack/atm/pppoxEndpoint/iptv,/vport/protocolStack/atm/pppoxEndpoint/range/iptvRange,/vport/protocolStack/ethernet/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/iptv,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/iptv,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ipEndpoint/iptv,/vport/protocolStack/ethernet/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/range/iptvRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('iptvStart', payload=payload, response_object=None)

    def IptvStop(self, *args, **kwargs):
        """Executes the iptvStop operation on the server.

        Stop IPTV on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        iptvStop(Arg2=enum)
        -------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/iptv,/vport/protocolStack/atm/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/iptv,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/iptv,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ipEndpoint/iptv,/vport/protocolStack/atm/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/iptv,/vport/protocolStack/atm/pppoxEndpoint/iptv,/vport/protocolStack/atm/pppoxEndpoint/range/iptvRange,/vport/protocolStack/ethernet/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/iptv,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/iptv,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ipEndpoint/iptv,/vport/protocolStack/ethernet/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/range/iptvRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('iptvStop', payload=payload, response_object=None)
