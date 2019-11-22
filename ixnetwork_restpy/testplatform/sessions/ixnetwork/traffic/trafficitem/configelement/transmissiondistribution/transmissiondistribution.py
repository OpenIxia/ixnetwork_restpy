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


class TransmissionDistribution(Base):
    """This object provides the options for packet transmission distribution.
    The TransmissionDistribution class encapsulates a list of transmissionDistribution resources that is managed by the system.
    A list of resources can be retrieved from the server using the TransmissionDistribution.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'transmissionDistribution'

    def __init__(self, parent):
        super(TransmissionDistribution, self).__init__(parent)

    @property
    def AvailableDistributions(self):
        """Indicates the available transmission distributions for the traffic streams.

        Returns:
            list(str)
        """
        return self._get_attribute('availableDistributions')

    @property
    def AvailableDistributionsSet(self):
        """Returns user friendly list of distribution fields

        Returns:
            list(dict(arg1:str,arg2:str))
        """
        return self._get_attribute('availableDistributionsSet')

    @property
    def Distributions(self):
        """Indicates the predefined size distribution based on size and weight.

        Returns:
            list(str)
        """
        return self._get_attribute('distributions')
    @Distributions.setter
    def Distributions(self, value):
        self._set_attribute('distributions', value)

    @property
    def DistributionsDisplayNames(self):
        """Returns user friendly list of distribution fields

        Returns:
            list(str)
        """
        return self._get_attribute('distributionsDisplayNames')

    def update(self, Distributions=None):
        """Updates a child instance of transmissionDistribution on the server.

        Args:
            Distributions (list(str)): Indicates the predefined size distribution based on size and weight.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, AvailableDistributions=None, AvailableDistributionsSet=None, Distributions=None, DistributionsDisplayNames=None):
        """Finds and retrieves transmissionDistribution data from the server.

        All named parameters support regex and can be used to selectively retrieve transmissionDistribution data from the server.
        By default the find method takes no parameters and will retrieve all transmissionDistribution data from the server.

        Args:
            AvailableDistributions (list(str)): Indicates the available transmission distributions for the traffic streams.
            AvailableDistributionsSet (list(dict(arg1:str,arg2:str))): Returns user friendly list of distribution fields
            Distributions (list(str)): Indicates the predefined size distribution based on size and weight.
            DistributionsDisplayNames (list(str)): Returns user friendly list of distribution fields

        Returns:
            self: This instance with matching transmissionDistribution data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of transmissionDistribution data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the transmissionDistribution data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
