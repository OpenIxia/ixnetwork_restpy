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


class PceUpdateXroSubObjectList(Base):
    """
    The PceUpdateXroSubObjectList class encapsulates a list of pceUpdateXroSubObjectList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateXroSubObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceUpdateXroSubObjectList'
    _SDM_ATT_MAP = {
        'ActiveXRO': 'activeXRO',
        'AsNumber': 'asNumber',
        'Attribute': 'attribute',
        'InterfaceId': 'interfaceId',
        'Ipv4Address': 'ipv4Address',
        'Ipv6Address': 'ipv6Address',
        'PFlagXro': 'pFlagXro',
        'PceId128': 'pceId128',
        'PceId32': 'pceId32',
        'PrefixLength': 'prefixLength',
        'RouterId': 'routerId',
        'SrlgId': 'srlgId',
        'SubObjectType': 'subObjectType',
        'XBit': 'xBit',
    }

    def __init__(self, parent):
        super(PceUpdateXroSubObjectList, self).__init__(parent)

    @property
    def ActiveXRO(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Controls whether the XRO sub-object will be sent in the PCRequest message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveXRO']))

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
    def Attribute(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates how the exclusion subobject is to be indicated
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Attribute']))

    @property
    def InterfaceId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interface ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterfaceId']))

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4Address']))

    @property
    def Ipv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Address']))

    @property
    def PFlagXro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): XRO P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagXro']))

    @property
    def PceId128(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 128 bit PKS ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PceId128']))

    @property
    def PceId32(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 32 bit PKS ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PceId32']))

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
    def RouterId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Router ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterId']))

    @property
    def SrlgId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRLG ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrlgId']))

    @property
    def SubObjectType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Using the Sub Object Type control user can configure which sub object needs to be included from the following options: IPv4 Prefix IPv6 Prefix Unnumbered Interface ID AS Number. SRLG
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubObjectType']))

    @property
    def XBit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether the exclusion is mandatory or desired.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['XBit']))

    def find(self):
        """Finds and retrieves pceUpdateXroSubObjectList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceUpdateXroSubObjectList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceUpdateXroSubObjectList resources from the server.

        Returns
        -------
        - self: This instance with matching pceUpdateXroSubObjectList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceUpdateXroSubObjectList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceUpdateXroSubObjectList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveXRO=None, AsNumber=None, Attribute=None, InterfaceId=None, Ipv4Address=None, Ipv6Address=None, PFlagXro=None, PceId128=None, PceId32=None, PrefixLength=None, RouterId=None, SrlgId=None, SubObjectType=None, XBit=None):
        """Base class infrastructure that gets a list of pceUpdateXroSubObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveXRO (str): optional regex of activeXRO
        - AsNumber (str): optional regex of asNumber
        - Attribute (str): optional regex of attribute
        - InterfaceId (str): optional regex of interfaceId
        - Ipv4Address (str): optional regex of ipv4Address
        - Ipv6Address (str): optional regex of ipv6Address
        - PFlagXro (str): optional regex of pFlagXro
        - PceId128 (str): optional regex of pceId128
        - PceId32 (str): optional regex of pceId32
        - PrefixLength (str): optional regex of prefixLength
        - RouterId (str): optional regex of routerId
        - SrlgId (str): optional regex of srlgId
        - SubObjectType (str): optional regex of subObjectType
        - XBit (str): optional regex of xBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
