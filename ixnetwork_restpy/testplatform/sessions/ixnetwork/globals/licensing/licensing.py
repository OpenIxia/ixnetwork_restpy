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


class Licensing(Base):
    """Container for licensing options
    The Licensing class encapsulates a required licensing resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "licensing"
    _SDM_ATT_MAP = {
        "AvailableTierOptions": "availableTierOptions",
        "HwMode": "hwMode",
        "HwTier": "hwTier",
        "LicensingServers": "licensingServers",
        "Mode": "mode",
        "Tier": "tier",
        "VmMode": "vmMode",
        "VmTier": "vmTier",
    }
    _SDM_ENUM_MAP = {
        "hwMode": ["perpetual", "subscription"],
        "mode": ["aggregation", "mixed", "perpetual", "subscription"],
        "vmMode": ["aggregation", "perpetual", "subscription"],
    }

    def __init__(self, parent, list_op=False):
        super(Licensing, self).__init__(parent, list_op)

    @property
    def AvailableTierOptions(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:list[str])): Gets list of available tier options for applicable license modes
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableTierOptions"])

    @property
    def HwMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(perpetual | subscription): Set license mode to either perpetual mode or subscription mode. This setting is applicable for hardware ports only.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HwMode"])

    @HwMode.setter
    def HwMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["HwMode"], value)

    @property
    def HwTier(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set or get the tier level, by using the tier ID. This setting is applicable for hardware ports only.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HwTier"])

    @HwTier.setter
    def HwTier(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["HwTier"], value)

    @property
    def LicensingServers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of license servers to use
        """
        return self._get_attribute(self._SDM_ATT_MAP["LicensingServers"])

    @LicensingServers.setter
    def LicensingServers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["LicensingServers"], value)

    @property
    def Mode(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(aggregation | mixed | perpetual | subscription): Set license mode to either of perpetual,subscription,mixed or aggregation
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mode"])

    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mode"], value)

    @property
    def Tier(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: set or get the tier level, using the tier ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tier"])

    @Tier.setter
    def Tier(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tier"], value)

    @property
    def VmMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(aggregation | perpetual | subscription): Set license mode to either perpetual mode, subscription mode or aggregation mode. This setting is applicable for virtual ports only.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VmMode"])

    @VmMode.setter
    def VmMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VmMode"], value)

    @property
    def VmTier(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set or get the tier level, by using the tier ID. This setting is applicable for virtual ports only.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VmTier"])

    @VmTier.setter
    def VmTier(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VmTier"], value)

    def update(
        self,
        HwMode=None,
        HwTier=None,
        LicensingServers=None,
        Mode=None,
        Tier=None,
        VmMode=None,
        VmTier=None,
    ):
        # type: (str, str, List[str], str, str, str, str) -> Licensing
        """Updates licensing resource on the server.

        Args
        ----
        - HwMode (str(perpetual | subscription)): Set license mode to either perpetual mode or subscription mode. This setting is applicable for hardware ports only.
        - HwTier (str): Set or get the tier level, by using the tier ID. This setting is applicable for hardware ports only.
        - LicensingServers (list(str)): List of license servers to use
        - Mode (str(aggregation | mixed | perpetual | subscription)): Set license mode to either of perpetual,subscription,mixed or aggregation
        - Tier (str): set or get the tier level, using the tier ID.
        - VmMode (str(aggregation | perpetual | subscription)): Set license mode to either perpetual mode, subscription mode or aggregation mode. This setting is applicable for virtual ports only.
        - VmTier (str): Set or get the tier level, by using the tier ID. This setting is applicable for virtual ports only.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvailableTierOptions=None,
        HwMode=None,
        HwTier=None,
        LicensingServers=None,
        Mode=None,
        Tier=None,
        VmMode=None,
        VmTier=None,
    ):
        """Finds and retrieves licensing resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve licensing resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all licensing resources from the server.

        Args
        ----
        - AvailableTierOptions (list(dict(arg1:str,arg2:list[str]))): Gets list of available tier options for applicable license modes
        - HwMode (str(perpetual | subscription)): Set license mode to either perpetual mode or subscription mode. This setting is applicable for hardware ports only.
        - HwTier (str): Set or get the tier level, by using the tier ID. This setting is applicable for hardware ports only.
        - LicensingServers (list(str)): List of license servers to use
        - Mode (str(aggregation | mixed | perpetual | subscription)): Set license mode to either of perpetual,subscription,mixed or aggregation
        - Tier (str): set or get the tier level, using the tier ID.
        - VmMode (str(aggregation | perpetual | subscription)): Set license mode to either perpetual mode, subscription mode or aggregation mode. This setting is applicable for virtual ports only.
        - VmTier (str): Set or get the tier level, by using the tier ID. This setting is applicable for virtual ports only.

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
