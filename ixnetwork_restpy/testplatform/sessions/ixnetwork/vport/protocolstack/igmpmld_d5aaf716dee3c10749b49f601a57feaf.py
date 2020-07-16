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


class IgmpMld(Base):
    """
    The IgmpMld class encapsulates a list of igmpMld resources that are managed by the user.
    A list of resources can be retrieved from the server using the IgmpMld.find() method.
    The list can be managed by using the IgmpMld.add() and IgmpMld.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpMld'
    _SDM_ATT_MAP = {
        'IsStandAlone': 'isStandAlone',
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(IgmpMld, self).__init__(parent)

    @property
    def IsStandAlone(self):
        """
        Returns
        -------
        - bool: When an Iptv extension is added, this property is marked as false
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsStandAlone'])
    @IsStandAlone.setter
    def IsStandAlone(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsStandAlone'], value)

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

    def update(self, IsStandAlone=None, Name=None):
        """Updates igmpMld resource on the server.

        Args
        ----
        - IsStandAlone (bool): When an Iptv extension is added, this property is marked as false
        - Name (str): Name of range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IsStandAlone=None, Name=None):
        """Adds a new igmpMld resource on the server and adds it to the container.

        Args
        ----
        - IsStandAlone (bool): When an Iptv extension is added, this property is marked as false
        - Name (str): Name of range

        Returns
        -------
        - self: This instance with all currently retrieved igmpMld resources using find and the newly added igmpMld resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained igmpMld resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IsStandAlone=None, Name=None, ObjectId=None):
        """Finds and retrieves igmpMld resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpMld resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpMld resources from the server.

        Args
        ----
        - IsStandAlone (bool): When an Iptv extension is added, this property is marked as false
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching igmpMld resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpMld data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpMld resources from the server available through an iterator or index

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

    def IgmpMldJoin(self, *args, **kwargs):
        """Executes the igmpMldJoin operation on the server.

        Join IGMP/MLD multicast group ranges on the fly

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldJoin(Arg2=enum)
        ----------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldJoin', payload=payload, response_object=None)

    def IgmpMldLeave(self, *args, **kwargs):
        """Executes the igmpMldLeave operation on the server.

        Leave IGMP/MLD multicast group ranges on the fly

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldLeave(Arg2=enum)
        -----------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldLeave', payload=payload, response_object=None)

    def IgmpMldStart(self, *args, **kwargs):
        """Executes the igmpMldStart operation on the server.

        Start IGMP/MLD on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldStart(Arg2=enum)
        -----------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldStart', payload=payload, response_object=None)

    def IgmpMldStop(self, *args, **kwargs):
        """Executes the igmpMldStop operation on the server.

        Stop IGMP/MLD on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldStop(Arg2=enum)
        ----------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldStop', payload=payload, response_object=None)
