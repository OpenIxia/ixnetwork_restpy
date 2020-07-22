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


class LearnedRouteIpv6(Base):
    """NOT DEFINED
    The LearnedRouteIpv6 class encapsulates a list of learnedRouteIpv6 resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedRouteIpv6.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedRouteIpv6'
    _SDM_ATT_MAP = {
        'AsPath': 'asPath',
        'BlockOffset': 'blockOffset',
        'BlockSize': 'blockSize',
        'ControlWordEnabled': 'controlWordEnabled',
        'IpPrefix': 'ipPrefix',
        'LabelBase': 'labelBase',
        'LocalPreference': 'localPreference',
        'MaxLabel': 'maxLabel',
        'MultiExitDiscriminator': 'multiExitDiscriminator',
        'Neighbor': 'neighbor',
        'NextHop': 'nextHop',
        'OriginType': 'originType',
        'PrefixLength': 'prefixLength',
        'RouteDistinguisher': 'routeDistinguisher',
        'SeqDeliveryEnabled': 'seqDeliveryEnabled',
        'SiteId': 'siteId',
    }

    def __init__(self, parent):
        super(LearnedRouteIpv6, self).__init__(parent)

    @property
    def AsPath(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPath'])

    @property
    def BlockOffset(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BlockOffset'])

    @property
    def BlockSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BlockSize'])

    @property
    def ControlWordEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControlWordEnabled'])

    @property
    def IpPrefix(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpPrefix'])

    @property
    def LabelBase(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelBase'])

    @property
    def LocalPreference(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPreference'])

    @property
    def MaxLabel(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxLabel'])

    @property
    def MultiExitDiscriminator(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MultiExitDiscriminator'])

    @property
    def Neighbor(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Neighbor'])

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])

    @property
    def OriginType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginType'])

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])

    @property
    def RouteDistinguisher(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisher'])

    @property
    def SeqDeliveryEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeqDeliveryEnabled'])

    @property
    def SiteId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SiteId'])

    def find(self, AsPath=None, BlockOffset=None, BlockSize=None, ControlWordEnabled=None, IpPrefix=None, LabelBase=None, LocalPreference=None, MaxLabel=None, MultiExitDiscriminator=None, Neighbor=None, NextHop=None, OriginType=None, PrefixLength=None, RouteDistinguisher=None, SeqDeliveryEnabled=None, SiteId=None):
        """Finds and retrieves learnedRouteIpv6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedRouteIpv6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedRouteIpv6 resources from the server.

        Args
        ----
        - AsPath (str): NOT DEFINED
        - BlockOffset (number): NOT DEFINED
        - BlockSize (number): NOT DEFINED
        - ControlWordEnabled (bool): NOT DEFINED
        - IpPrefix (str): NOT DEFINED
        - LabelBase (number): NOT DEFINED
        - LocalPreference (number): NOT DEFINED
        - MaxLabel (number): NOT DEFINED
        - MultiExitDiscriminator (number): NOT DEFINED
        - Neighbor (str): NOT DEFINED
        - NextHop (str): NOT DEFINED
        - OriginType (str): NOT DEFINED
        - PrefixLength (number): NOT DEFINED
        - RouteDistinguisher (str): NOT DEFINED
        - SeqDeliveryEnabled (bool): NOT DEFINED
        - SiteId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching learnedRouteIpv6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedRouteIpv6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedRouteIpv6 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
