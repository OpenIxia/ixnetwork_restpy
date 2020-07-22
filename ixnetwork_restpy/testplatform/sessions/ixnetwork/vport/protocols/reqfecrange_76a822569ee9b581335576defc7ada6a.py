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


class ReqFecRange(Base):
    """This object enables a request for a set of FEC ranges.
    The ReqFecRange class encapsulates a list of reqFecRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the ReqFecRange.find() method.
    The list can be managed by using the ReqFecRange.add() and ReqFecRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'reqFecRange'
    _SDM_ATT_MAP = {
        'EnableHopCount': 'enableHopCount',
        'EnableStateTimer': 'enableStateTimer',
        'Enabled': 'enabled',
        'FirstNetwork': 'firstNetwork',
        'HopCount': 'hopCount',
        'MaskWidth': 'maskWidth',
        'NextHopPeer': 'nextHopPeer',
        'NumberOfRoutes': 'numberOfRoutes',
        'StaleReqTime': 'staleReqTime',
    }

    def __init__(self, parent):
        super(ReqFecRange, self).__init__(parent)

    @property
    def EnableHopCount(self):
        """
        Returns
        -------
        - bool: Enables the hops along the path of the LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHopCount'])
    @EnableHopCount.setter
    def EnableHopCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHopCount'], value)

    @property
    def EnableStateTimer(self):
        """
        Returns
        -------
        - bool: Enable the Stale Request Timer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStateTimer'])
    @EnableStateTimer.setter
    def EnableStateTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStateTimer'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this request FEC range for the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FirstNetwork(self):
        """
        Returns
        -------
        - str: The first FEC network address in the range (in IP address format).
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstNetwork'])
    @FirstNetwork.setter
    def FirstNetwork(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstNetwork'], value)

    @property
    def HopCount(self):
        """
        Returns
        -------
        - number: The number of hops along the path of the LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HopCount'])
    @HopCount.setter
    def HopCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HopCount'], value)

    @property
    def MaskWidth(self):
        """
        Returns
        -------
        - number: The number of bits in the FEC mask applied to the FEC network address. The masked bits in the first network address form the FEC address prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaskWidth'])
    @MaskWidth.setter
    def MaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaskWidth'], value)

    @property
    def NextHopPeer(self):
        """
        Returns
        -------
        - str: The IPv4 address of the LDP Peer that is the next hop router on this path. (0.0.0.0 indicates that requests will be sent to all of this router's peers that are in Downstream on Demand mode.)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopPeer'])
    @NextHopPeer.setter
    def NextHopPeer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopPeer'], value)

    @property
    def NumberOfRoutes(self):
        """
        Returns
        -------
        - number: The number of routes configured for this LDP requesting FEC range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRoutes'])
    @NumberOfRoutes.setter
    def NumberOfRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRoutes'], value)

    @property
    def StaleReqTime(self):
        """
        Returns
        -------
        - number: The Stale Request Time value. Value range is 1 to 65.535 seconds. (default = 300)
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaleReqTime'])
    @StaleReqTime.setter
    def StaleReqTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StaleReqTime'], value)

    def update(self, EnableHopCount=None, EnableStateTimer=None, Enabled=None, FirstNetwork=None, HopCount=None, MaskWidth=None, NextHopPeer=None, NumberOfRoutes=None, StaleReqTime=None):
        """Updates reqFecRange resource on the server.

        Args
        ----
        - EnableHopCount (bool): Enables the hops along the path of the LSP.
        - EnableStateTimer (bool): Enable the Stale Request Timer.
        - Enabled (bool): Enables the use of this request FEC range for the simulated router.
        - FirstNetwork (str): The first FEC network address in the range (in IP address format).
        - HopCount (number): The number of hops along the path of the LSP.
        - MaskWidth (number): The number of bits in the FEC mask applied to the FEC network address. The masked bits in the first network address form the FEC address prefix.
        - NextHopPeer (str): The IPv4 address of the LDP Peer that is the next hop router on this path. (0.0.0.0 indicates that requests will be sent to all of this router's peers that are in Downstream on Demand mode.)
        - NumberOfRoutes (number): The number of routes configured for this LDP requesting FEC range.
        - StaleReqTime (number): The Stale Request Time value. Value range is 1 to 65.535 seconds. (default = 300)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableHopCount=None, EnableStateTimer=None, Enabled=None, FirstNetwork=None, HopCount=None, MaskWidth=None, NextHopPeer=None, NumberOfRoutes=None, StaleReqTime=None):
        """Adds a new reqFecRange resource on the server and adds it to the container.

        Args
        ----
        - EnableHopCount (bool): Enables the hops along the path of the LSP.
        - EnableStateTimer (bool): Enable the Stale Request Timer.
        - Enabled (bool): Enables the use of this request FEC range for the simulated router.
        - FirstNetwork (str): The first FEC network address in the range (in IP address format).
        - HopCount (number): The number of hops along the path of the LSP.
        - MaskWidth (number): The number of bits in the FEC mask applied to the FEC network address. The masked bits in the first network address form the FEC address prefix.
        - NextHopPeer (str): The IPv4 address of the LDP Peer that is the next hop router on this path. (0.0.0.0 indicates that requests will be sent to all of this router's peers that are in Downstream on Demand mode.)
        - NumberOfRoutes (number): The number of routes configured for this LDP requesting FEC range.
        - StaleReqTime (number): The Stale Request Time value. Value range is 1 to 65.535 seconds. (default = 300)

        Returns
        -------
        - self: This instance with all currently retrieved reqFecRange resources using find and the newly added reqFecRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained reqFecRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableHopCount=None, EnableStateTimer=None, Enabled=None, FirstNetwork=None, HopCount=None, MaskWidth=None, NextHopPeer=None, NumberOfRoutes=None, StaleReqTime=None):
        """Finds and retrieves reqFecRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve reqFecRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all reqFecRange resources from the server.

        Args
        ----
        - EnableHopCount (bool): Enables the hops along the path of the LSP.
        - EnableStateTimer (bool): Enable the Stale Request Timer.
        - Enabled (bool): Enables the use of this request FEC range for the simulated router.
        - FirstNetwork (str): The first FEC network address in the range (in IP address format).
        - HopCount (number): The number of hops along the path of the LSP.
        - MaskWidth (number): The number of bits in the FEC mask applied to the FEC network address. The masked bits in the first network address form the FEC address prefix.
        - NextHopPeer (str): The IPv4 address of the LDP Peer that is the next hop router on this path. (0.0.0.0 indicates that requests will be sent to all of this router's peers that are in Downstream on Demand mode.)
        - NumberOfRoutes (number): The number of routes configured for this LDP requesting FEC range.
        - StaleReqTime (number): The Stale Request Time value. Value range is 1 to 65.535 seconds. (default = 300)

        Returns
        -------
        - self: This instance with matching reqFecRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of reqFecRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the reqFecRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
