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


class Vlan(Base):
    """Controls the general VLAN interface properties.
    The Vlan class encapsulates a required vlan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "vlan"
    _SDM_ATT_MAP = {
        "Tpid": "tpid",
        "VlanCount": "vlanCount",
        "VlanEnable": "vlanEnable",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Vlan, self).__init__(parent, list_op)

    @property
    def Tpid(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag). (Active only if VLAN has been enabled.)
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
        - number: The number of VLANs configured for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanCount"])

    @VlanCount.setter
    def VlanCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanCount"], value)

    @property
    def VlanEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, a VLAN can be assigned for each of the interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanEnable"])

    @VlanEnable.setter
    def VlanEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanEnable"], value)

    @property
    def VlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If the VLAN option is enabled for the current interface, a VLAN ID may be added to the packet, to identify the VLAN that the packet belongs to. The default is 1. If the VLAN Count is greater than 1 (for stacked VLANs), corresponding multiple entries will appear in the VLAN ID field.
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
        - str: The user priority of the VLAN tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.The default is 5.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self, Tpid=None, VlanCount=None, VlanEnable=None, VlanId=None, VlanPriority=None
    ):
        # type: (str, int, bool, str, str) -> Vlan
        """Updates vlan resource on the server.

        Args
        ----
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag). (Active only if VLAN has been enabled.)
        - VlanCount (number): The number of VLANs configured for this interface.
        - VlanEnable (bool): If enabled, a VLAN can be assigned for each of the interfaces.
        - VlanId (str): If the VLAN option is enabled for the current interface, a VLAN ID may be added to the packet, to identify the VLAN that the packet belongs to. The default is 1. If the VLAN Count is greater than 1 (for stacked VLANs), corresponding multiple entries will appear in the VLAN ID field.
        - VlanPriority (str): The user priority of the VLAN tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.The default is 5.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self, Tpid=None, VlanCount=None, VlanEnable=None, VlanId=None, VlanPriority=None
    ):
        # type: (str, int, bool, str, str) -> Vlan
        """Finds and retrieves vlan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vlan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vlan resources from the server.

        Args
        ----
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag). (Active only if VLAN has been enabled.)
        - VlanCount (number): The number of VLANs configured for this interface.
        - VlanEnable (bool): If enabled, a VLAN can be assigned for each of the interfaces.
        - VlanId (str): If the VLAN option is enabled for the current interface, a VLAN ID may be added to the packet, to identify the VLAN that the packet belongs to. The default is 1. If the VLAN Count is greater than 1 (for stacked VLANs), corresponding multiple entries will appear in the VLAN ID field.
        - VlanPriority (str): The user priority of the VLAN tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.The default is 5.

        Returns
        -------
        - self: This instance with matching vlan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vlan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vlan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
