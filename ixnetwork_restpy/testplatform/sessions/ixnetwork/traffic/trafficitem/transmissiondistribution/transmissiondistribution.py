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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class TransmissionDistribution(Base):
    """This object provides the options for packet transmission distribution.
    The TransmissionDistribution class encapsulates a list of transmissionDistribution resources that are managed by the system.
    A list of resources can be retrieved from the server using the TransmissionDistribution.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "transmissionDistribution"
    _SDM_ATT_MAP = {
        "AvailableDistributions": "availableDistributions",
        "AvailableDistributionsSet": "availableDistributionsSet",
        "Distributions": "distributions",
        "DistributionsDisplayNames": "distributionsDisplayNames",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TransmissionDistribution, self).__init__(parent, list_op)

    @property
    def AvailableDistributions(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Indicates the available transmission distributions for the traffic streams.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableDistributions"])

    @property
    def AvailableDistributionsSet(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str)): Returns user friendly list of distribution fields
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableDistributionsSet"])

    @property
    def Distributions(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Indicates the predefined size distribution based on size and weight.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Distributions"])

    @Distributions.setter
    def Distributions(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["Distributions"], value)

    @property
    def DistributionsDisplayNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Returns user friendly list of distribution fields
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistributionsDisplayNames"])

    def update(self, Distributions=None):
        # type: (List[str]) -> TransmissionDistribution
        """Updates transmissionDistribution resource on the server.

        Args
        ----
        - Distributions (list(str)): Indicates the predefined size distribution based on size and weight.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Distributions=None):
        # type: (List[str]) -> TransmissionDistribution
        """Adds a new transmissionDistribution resource on the json, only valid with batch add utility

        Args
        ----
        - Distributions (list(str)): Indicates the predefined size distribution based on size and weight.

        Returns
        -------
        - self: This instance with all currently retrieved transmissionDistribution resources using find and the newly added transmissionDistribution resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvailableDistributions=None,
        AvailableDistributionsSet=None,
        Distributions=None,
        DistributionsDisplayNames=None,
    ):
        """Finds and retrieves transmissionDistribution resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve transmissionDistribution resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all transmissionDistribution resources from the server.

        Args
        ----
        - AvailableDistributions (list(str)): Indicates the available transmission distributions for the traffic streams.
        - AvailableDistributionsSet (list(dict(arg1:str,arg2:str))): Returns user friendly list of distribution fields
        - Distributions (list(str)): Indicates the predefined size distribution based on size and weight.
        - DistributionsDisplayNames (list(str)): Returns user friendly list of distribution fields

        Returns
        -------
        - self: This instance with matching transmissionDistribution resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of transmissionDistribution data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the transmissionDistribution resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
