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


class SummaryIp(Base):
    """
    The SummaryIp class encapsulates a list of summaryIp resources that are managed by the system.
    A list of resources can be retrieved from the server using the SummaryIp.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'summaryIp'
    _SDM_ATT_MAP = {
        'IncrementLinkStateIdBy': 'incrementLinkStateIdBy',
        'Metric': 'metric',
        'NetworkMask': 'networkMask',
        'NumberOfLsa': 'numberOfLsa',
    }

    def __init__(self, parent):
        super(SummaryIp, self).__init__(parent)

    @property
    def IncrementLinkStateIdBy(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementLinkStateIdBy'])
    @IncrementLinkStateIdBy.setter
    def IncrementLinkStateIdBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementLinkStateIdBy'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def NetworkMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkMask'])
    @NetworkMask.setter
    def NetworkMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkMask'], value)

    @property
    def NumberOfLsa(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfLsa'])
    @NumberOfLsa.setter
    def NumberOfLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfLsa'], value)

    def update(self, IncrementLinkStateIdBy=None, Metric=None, NetworkMask=None, NumberOfLsa=None):
        """Updates summaryIp resource on the server.

        Args
        ----
        - IncrementLinkStateIdBy (str): 
        - Metric (number): 
        - NetworkMask (str): 
        - NumberOfLsa (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, IncrementLinkStateIdBy=None, Metric=None, NetworkMask=None, NumberOfLsa=None):
        """Finds and retrieves summaryIp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve summaryIp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all summaryIp resources from the server.

        Args
        ----
        - IncrementLinkStateIdBy (str): 
        - Metric (number): 
        - NetworkMask (str): 
        - NumberOfLsa (number): 

        Returns
        -------
        - self: This instance with matching summaryIp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of summaryIp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the summaryIp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
