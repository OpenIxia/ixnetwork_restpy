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


class PcRequestMatchCriteria(Base):
    """PCRequest Match Criteria
    The PcRequestMatchCriteria class encapsulates a required pcRequestMatchCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pcRequestMatchCriteria'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestIpv4Address': 'destIpv4Address',
        'DestIpv6Address': 'destIpv6Address',
        'IpVersion': 'ipVersion',
        'IroType': 'iroType',
        'MatchEndPoints': 'matchEndPoints',
        'Name': 'name',
        'SrcIpv4Address': 'srcIpv4Address',
        'SrcIpv6Address': 'srcIpv6Address',
    }

    def __init__(self, parent):
        super(PcRequestMatchCriteria, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

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
    def DestIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestIpv4Address']))

    @property
    def DestIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination IPv6 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestIpv6Address']))

    @property
    def IpVersion(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IP Version
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpVersion']))

    @property
    def IroType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Match IRO Option
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IroType']))

    @property
    def MatchEndPoints(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates Whether response parameters will be matched based on endpoints in the PCReq messaged received from PCC.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MatchEndPoints']))

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
    def SrcIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrcIpv4Address']))

    @property
    def SrcIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv6 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrcIpv6Address']))

    def update(self, Name=None):
        """Updates pcRequestMatchCriteria resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, DestIpv4Address=None, DestIpv6Address=None, IpVersion=None, IroType=None, MatchEndPoints=None, SrcIpv4Address=None, SrcIpv6Address=None):
        """Base class infrastructure that gets a list of pcRequestMatchCriteria device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - DestIpv4Address (str): optional regex of destIpv4Address
        - DestIpv6Address (str): optional regex of destIpv6Address
        - IpVersion (str): optional regex of ipVersion
        - IroType (str): optional regex of iroType
        - MatchEndPoints (str): optional regex of matchEndPoints
        - SrcIpv4Address (str): optional regex of srcIpv4Address
        - SrcIpv6Address (str): optional regex of srcIpv6Address

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
