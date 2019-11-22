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


class PceUpdateSrv6EroSubObjectList(Base):
    """
    The PceUpdateSrv6EroSubObjectList class encapsulates a list of pceUpdateSrv6EroSubObjectList resources that is managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateSrv6EroSubObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceUpdateSrv6EroSubObjectList'

    def __init__(self, parent):
        super(PceUpdateSrv6EroSubObjectList, self).__init__(parent)

    @property
    def ActiveThisEro(self):
        """Controls whether the ERO sub-object will be sent in the PCInitiate message.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('activeThisEro')

    @property
    def FBit(self):
        """A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('fBit')

    @property
    def Ipv6NodeId(self):
        """IPv6 Node ID is specified as an IPv6 address. This control can be configured if NAI Type is set to IPv6 Node ID and F bit is disabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6NodeId')

    @property
    def LocalIpv6Address(self):
        """This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('localIpv6Address')

    @property
    def LooseHop(self):
        """Indicates if user wants to represent a loose-hop sub object in the LSP

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('looseHop')

    @property
    def RemoteIpv6Address(self):
        """This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('remoteIpv6Address')

    @property
    def Srv6FunctionCode(self):
        """Function Code is is the 16 bit field representing supported functions associated with SRv6 SIDs. This information is optional and included only for maintainability. Following function codes are currently defined - 0: Reserved 1: End Function 2: End.DX6 Function 3: End.DT6 Function 4: End.X Function

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('srv6FunctionCode')

    @property
    def Srv6Identifier(self):
        """SRv6 Identifier is the 128 bit IPv6 addresses representing SRv6 segment.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('srv6Identifier')

    @property
    def Srv6NaiType(self):
        """The SRv6 NAI Type which indicates the interpretation for NAI (Node or Adjacency Identifier).

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('srv6NaiType')

    def find(self):
        """Finds and retrieves pceUpdateSrv6EroSubObjectList data from the server.

        All named parameters support regex and can be used to selectively retrieve pceUpdateSrv6EroSubObjectList data from the server.
        By default the find method takes no parameters and will retrieve all pceUpdateSrv6EroSubObjectList data from the server.

        Returns:
            self: This instance with matching pceUpdateSrv6EroSubObjectList data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of pceUpdateSrv6EroSubObjectList data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the pceUpdateSrv6EroSubObjectList data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveThisEro=None, FBit=None, Ipv6NodeId=None, LocalIpv6Address=None, LooseHop=None, RemoteIpv6Address=None, Srv6FunctionCode=None, Srv6Identifier=None, Srv6NaiType=None):
        """Base class infrastructure that gets a list of pceUpdateSrv6EroSubObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            ActiveThisEro (str): optional regex of activeThisEro
            FBit (str): optional regex of fBit
            Ipv6NodeId (str): optional regex of ipv6NodeId
            LocalIpv6Address (str): optional regex of localIpv6Address
            LooseHop (str): optional regex of looseHop
            RemoteIpv6Address (str): optional regex of remoteIpv6Address
            Srv6FunctionCode (str): optional regex of srv6FunctionCode
            Srv6Identifier (str): optional regex of srv6Identifier
            Srv6NaiType (str): optional regex of srv6NaiType

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
