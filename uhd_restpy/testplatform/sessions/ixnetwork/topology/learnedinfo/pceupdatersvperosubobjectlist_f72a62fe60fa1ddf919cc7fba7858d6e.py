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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class PceUpdateRsvpEroSubObjectList(Base):
    """
    The PceUpdateRsvpEroSubObjectList class encapsulates a list of pceUpdateRsvpEroSubObjectList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateRsvpEroSubObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceUpdateRsvpEroSubObjectList'
    _SDM_ATT_MAP = {
        'ActiveThisEro': 'activeThisEro',
        'AsNumber': 'asNumber',
        'Ipv4Prefix': 'ipv4Prefix',
        'Ipv6Prefix': 'ipv6Prefix',
        'LooseHop': 'looseHop',
        'PrefixLength': 'prefixLength',
        'SubObjectType': 'subObjectType',
    }

    def __init__(self, parent):
        super(PceUpdateRsvpEroSubObjectList, self).__init__(parent)

    @property
    def ActiveThisEro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Controls whether the ERO sub-object will be sent in the PCInitiate message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveThisEro']))

    @property
    def AsNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumber']))

    @property
    def Ipv4Prefix(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Prefix is specified as an IPv4 address.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4Prefix']))

    @property
    def Ipv6Prefix(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Prefix is specified as an IPv6 address.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Prefix']))

    @property
    def LooseHop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates if user wants to represent a loose-hop sub object in the LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LooseHop']))

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Prefix Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixLength']))

    @property
    def SubObjectType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Using the Sub Object Type control user can configure which sub object needs to be included from the following options: Not Applicable IPv4 Prefix IPv6 Prefix AS Number.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubObjectType']))

    def find(self):
        """Finds and retrieves pceUpdateRsvpEroSubObjectList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceUpdateRsvpEroSubObjectList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceUpdateRsvpEroSubObjectList resources from the server.

        Returns
        -------
        - self: This instance with matching pceUpdateRsvpEroSubObjectList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceUpdateRsvpEroSubObjectList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceUpdateRsvpEroSubObjectList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveThisEro=None, AsNumber=None, Ipv4Prefix=None, Ipv6Prefix=None, LooseHop=None, PrefixLength=None, SubObjectType=None):
        """Base class infrastructure that gets a list of pceUpdateRsvpEroSubObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveThisEro (str): optional regex of activeThisEro
        - AsNumber (str): optional regex of asNumber
        - Ipv4Prefix (str): optional regex of ipv4Prefix
        - Ipv6Prefix (str): optional regex of ipv6Prefix
        - LooseHop (str): optional regex of looseHop
        - PrefixLength (str): optional regex of prefixLength
        - SubObjectType (str): optional regex of subObjectType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
