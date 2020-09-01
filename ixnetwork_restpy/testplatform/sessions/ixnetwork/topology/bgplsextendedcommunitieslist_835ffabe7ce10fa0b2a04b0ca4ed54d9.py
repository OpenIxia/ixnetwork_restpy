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


class BgpLsExtendedCommunitiesList(Base):
    """Bgp Non VPN RR External Communities
    The BgpLsExtendedCommunitiesList class encapsulates a list of bgpLsExtendedCommunitiesList resources that are managed by the system.
    A list of resources can be retrieved from the server using the BgpLsExtendedCommunitiesList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpLsExtendedCommunitiesList'
    _SDM_ATT_MAP = {
        'AsNumber2Bytes': 'asNumber2Bytes',
        'AsNumber4Bytes': 'asNumber4Bytes',
        'AssignedNumber2Bytes': 'assignedNumber2Bytes',
        'AssignedNumber4Bytes': 'assignedNumber4Bytes',
        'ColorCOBits': 'colorCOBits',
        'ColorReservedBits': 'colorReservedBits',
        'ColorValue': 'colorValue',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Ip': 'ip',
        'LinkBandwidth': 'linkBandwidth',
        'Name': 'name',
        'OpaqueData': 'opaqueData',
        'SubType': 'subType',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(BgpLsExtendedCommunitiesList, self).__init__(parent)

    @property
    def AsNumber2Bytes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS 2-Bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumber2Bytes']))

    @property
    def AsNumber4Bytes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS 4-Bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumber4Bytes']))

    @property
    def AssignedNumber2Bytes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Assigned Number(2 Octets)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumber2Bytes']))

    @property
    def AssignedNumber4Bytes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Assigned Number(4 Octets)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumber4Bytes']))

    @property
    def ColorCOBits(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color CO Bits
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ColorCOBits']))

    @property
    def ColorReservedBits(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color Reserved Bits
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ColorReservedBits']))

    @property
    def ColorValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ColorValue']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Ip(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ip']))

    @property
    def LinkBandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Bandwidth
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkBandwidth']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OpaqueData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Opaque Data
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OpaqueData']))

    @property
    def SubType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SubType
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubType']))

    @property
    def Type(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    def update(self, Name=None):
        """Updates bgpLsExtendedCommunitiesList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        """Finds and retrieves bgpLsExtendedCommunitiesList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpLsExtendedCommunitiesList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpLsExtendedCommunitiesList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching bgpLsExtendedCommunitiesList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpLsExtendedCommunitiesList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpLsExtendedCommunitiesList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, AsNumber2Bytes=None, AsNumber4Bytes=None, AssignedNumber2Bytes=None, AssignedNumber4Bytes=None, ColorCOBits=None, ColorReservedBits=None, ColorValue=None, Ip=None, LinkBandwidth=None, OpaqueData=None, SubType=None, Type=None):
        """Base class infrastructure that gets a list of bgpLsExtendedCommunitiesList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AsNumber2Bytes (str): optional regex of asNumber2Bytes
        - AsNumber4Bytes (str): optional regex of asNumber4Bytes
        - AssignedNumber2Bytes (str): optional regex of assignedNumber2Bytes
        - AssignedNumber4Bytes (str): optional regex of assignedNumber4Bytes
        - ColorCOBits (str): optional regex of colorCOBits
        - ColorReservedBits (str): optional regex of colorReservedBits
        - ColorValue (str): optional regex of colorValue
        - Ip (str): optional regex of ip
        - LinkBandwidth (str): optional regex of linkBandwidth
        - OpaqueData (str): optional regex of opaqueData
        - SubType (str): optional regex of subType
        - Type (str): optional regex of type

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
