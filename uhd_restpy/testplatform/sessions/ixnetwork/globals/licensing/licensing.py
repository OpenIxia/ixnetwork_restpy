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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Licensing(Base):
    """Container for licensing options
    The Licensing class encapsulates a required licensing resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'licensing'
    _SDM_ATT_MAP = {
        'LicensingServers': 'licensingServers',
        'Mode': 'mode',
        'Tier': 'tier',
    }
    _SDM_ENUM_MAP = {
        'mode': ['aggregation', 'mixed', 'perpetual', 'subscription'],
    }

    def __init__(self, parent, list_op=False):
        super(Licensing, self).__init__(parent, list_op)

    @property
    def LicensingServers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of license servers to use
        """
        return self._get_attribute(self._SDM_ATT_MAP['LicensingServers'])
    @LicensingServers.setter
    def LicensingServers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['LicensingServers'], value)

    @property
    def Mode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(aggregation | mixed | perpetual | subscription): Set license mode to either of perpetual,subscription,mixed or aggregation
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mode'])
    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Mode'], value)

    @property
    def Tier(self):
        # type: () -> str
        """
        Returns
        -------
        - str: set or get the tier level, using the tier ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tier'])
    @Tier.setter
    def Tier(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Tier'], value)

    def update(self, LicensingServers=None, Mode=None, Tier=None):
        # type: (List[str], str, str) -> Licensing
        """Updates licensing resource on the server.

        Args
        ----
        - LicensingServers (list(str)): List of license servers to use
        - Mode (str(aggregation | mixed | perpetual | subscription)): Set license mode to either of perpetual,subscription,mixed or aggregation
        - Tier (str): set or get the tier level, using the tier ID.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, LicensingServers=None, Mode=None, Tier=None):
        # type: (List[str], str, str) -> Licensing
        """Finds and retrieves licensing resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve licensing resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all licensing resources from the server.

        Args
        ----
        - LicensingServers (list(str)): List of license servers to use
        - Mode (str(aggregation | mixed | perpetual | subscription)): Set license mode to either of perpetual,subscription,mixed or aggregation
        - Tier (str): set or get the tier level, using the tier ID.

        Returns
        -------
        - self: This instance with matching licensing resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of licensing data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the licensing resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
