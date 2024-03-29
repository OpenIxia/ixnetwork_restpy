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


class L2MacVlanRange(Base):
    """This object holds a list of MAC/VLAN address ranges.
    The L2MacVlanRange class encapsulates a required l2MacVlanRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "l2MacVlanRange"
    _SDM_ATT_MAP = {
        "Count": "count",
        "EnableRepeatMac": "enableRepeatMac",
        "EnableSameVlan": "enableSameVlan",
        "EnableVlan": "enableVlan",
        "Enabled": "enabled",
        "FirstVlanId": "firstVlanId",
        "IncrementVlanMode": "incrementVlanMode",
        "IncremetVlanMode": "incremetVlanMode",
        "SkipVlanIdZero": "skipVlanIdZero",
        "StartMac": "startMac",
        "Tpid": "tpid",
        "VlanCount": "vlanCount",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {
        "incrementVlanMode": [
            "noIncrement",
            "parallelIncrement",
            "innerFirst",
            "outerFirst",
        ],
        "incremetVlanMode": [
            "noIncrement",
            "parallelIncrement",
            "innerFirst",
            "outerFirst",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(L2MacVlanRange, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Enable VLAN is enabled, this it the number of MAC address/VLAN combinations that will be created. If Enabled VLAN is not enabled, this is the number of MAC addresses that will be created.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def EnableRepeatMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, and the count is greater than 1, the same address value will be repeated for all MAC addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRepeatMac"])

    @EnableRepeatMac.setter
    def EnableRepeatMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRepeatMac"], value)

    @property
    def EnableSameVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, all MAC addresses in the range will be associated with the same VLAN ID. If enabled, all MAC addresses in the range will be associated with different VLAN IDs, where the VLAN IDs will be automatically incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSameVlan"])

    @EnableSameVlan.setter
    def EnableSameVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSameVlan"], value)

    @property
    def EnableVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the MAC/VLAN range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVlan"])

    @EnableVlan.setter
    def EnableVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVlan"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the Layer 2 MAC/VLAN address range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FirstVlanId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The VLAN ID for the first VLAN in the MAC/VLAN range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstVlanId"])

    @FirstVlanId.setter
    def FirstVlanId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstVlanId"], value)

    @property
    def IncrementVlanMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): If true, each additional VLAN in the range is incremented to create unique VLAN IDs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementVlanMode"])

    @IncrementVlanMode.setter
    def IncrementVlanMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementVlanMode"], value)

    @property
    def IncremetVlanMode(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): If true, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncremetVlanMode"])

    @IncremetVlanMode.setter
    def IncremetVlanMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncremetVlanMode"], value)

    @property
    def SkipVlanIdZero(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Skip the value of vlad id, if the vlan id value is equal to zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SkipVlanIdZero"])

    @SkipVlanIdZero.setter
    def SkipVlanIdZero(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SkipVlanIdZero"], value)

    @property
    def StartMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first MAC address in the MAC range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartMac"])

    @StartMac.setter
    def StartMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartMac"], value)

    @property
    def Tpid(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tpid"])

    @Tpid.setter
    def Tpid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tpid"], value)

    @property
    def VlanCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of VLANs created.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanCount"])

    @VlanCount.setter
    def VlanCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanCount"], value)

    @property
    def VlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The identifier for the first VLAN in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        Count=None,
        EnableRepeatMac=None,
        EnableSameVlan=None,
        EnableVlan=None,
        Enabled=None,
        FirstVlanId=None,
        IncrementVlanMode=None,
        IncremetVlanMode=None,
        SkipVlanIdZero=None,
        StartMac=None,
        Tpid=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (int, bool, bool, bool, bool, int, str, str, bool, str, str, int, str, str) -> L2MacVlanRange
        """Updates l2MacVlanRange resource on the server.

        Args
        ----
        - Count (number): If Enable VLAN is enabled, this it the number of MAC address/VLAN combinations that will be created. If Enabled VLAN is not enabled, this is the number of MAC addresses that will be created.
        - EnableRepeatMac (bool): If enabled, and the count is greater than 1, the same address value will be repeated for all MAC addresses.
        - EnableSameVlan (bool): If enabled, all MAC addresses in the range will be associated with the same VLAN ID. If enabled, all MAC addresses in the range will be associated with different VLAN IDs, where the VLAN IDs will be automatically incremented.
        - EnableVlan (bool): Enables the MAC/VLAN range.
        - Enabled (bool): Enables the Layer 2 MAC/VLAN address range.
        - FirstVlanId (number): The VLAN ID for the first VLAN in the MAC/VLAN range.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, each additional VLAN in the range is incremented to create unique VLAN IDs.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1.
        - SkipVlanIdZero (bool): Skip the value of vlad id, if the vlan id value is equal to zero.
        - StartMac (str): The first MAC address in the MAC range.
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The identifier for the first VLAN in the range.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        EnableRepeatMac=None,
        EnableSameVlan=None,
        EnableVlan=None,
        Enabled=None,
        FirstVlanId=None,
        IncrementVlanMode=None,
        IncremetVlanMode=None,
        SkipVlanIdZero=None,
        StartMac=None,
        Tpid=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (int, bool, bool, bool, bool, int, str, str, bool, str, str, int, str, str) -> L2MacVlanRange
        """Finds and retrieves l2MacVlanRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2MacVlanRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2MacVlanRange resources from the server.

        Args
        ----
        - Count (number): If Enable VLAN is enabled, this it the number of MAC address/VLAN combinations that will be created. If Enabled VLAN is not enabled, this is the number of MAC addresses that will be created.
        - EnableRepeatMac (bool): If enabled, and the count is greater than 1, the same address value will be repeated for all MAC addresses.
        - EnableSameVlan (bool): If enabled, all MAC addresses in the range will be associated with the same VLAN ID. If enabled, all MAC addresses in the range will be associated with different VLAN IDs, where the VLAN IDs will be automatically incremented.
        - EnableVlan (bool): Enables the MAC/VLAN range.
        - Enabled (bool): Enables the Layer 2 MAC/VLAN address range.
        - FirstVlanId (number): The VLAN ID for the first VLAN in the MAC/VLAN range.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, each additional VLAN in the range is incremented to create unique VLAN IDs.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1.
        - SkipVlanIdZero (bool): Skip the value of vlad id, if the vlan id value is equal to zero.
        - StartMac (str): The first MAC address in the MAC range.
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The identifier for the first VLAN in the range.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Returns
        -------
        - self: This instance with matching l2MacVlanRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2MacVlanRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2MacVlanRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
