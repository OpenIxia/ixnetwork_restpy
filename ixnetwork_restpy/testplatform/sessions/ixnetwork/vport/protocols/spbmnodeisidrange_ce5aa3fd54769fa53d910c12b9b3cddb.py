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


class SpbmNodeIsIdRange(Base):
    """The SPBM Node ISIS ID Range.
    The SpbmNodeIsIdRange class encapsulates a list of spbmNodeIsIdRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbmNodeIsIdRange.find() method.
    The list can be managed by using the SpbmNodeIsIdRange.add() and SpbmNodeIsIdRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "spbmNodeIsIdRange"
    _SDM_ATT_MAP = {
        "CMacAddressCount": "cMacAddressCount",
        "CMacAddressStep": "cMacAddressStep",
        "ITagEthernetType": "iTagEthernetType",
        "InterNodeCmacAddress": "interNodeCmacAddress",
        "InterNodeCvlan": "interNodeCvlan",
        "InterNodeIsIdIncrement": "interNodeIsIdIncrement",
        "InterNodeSvlan": "interNodeSvlan",
        "IsId": "isId",
        "RBit": "rBit",
        "StartCmacAddress": "startCmacAddress",
        "StartCvlan": "startCvlan",
        "StartSvlan": "startSvlan",
        "TBit": "tBit",
        "TrafficDestMacAddress": "trafficDestMacAddress",
        "TransmissionType": "transmissionType",
        "VlanType": "vlanType",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SpbmNodeIsIdRange, self).__init__(parent, list_op)

    @property
    def CMacAddressCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of C-MAC addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CMacAddressCount"])

    @CMacAddressCount.setter
    def CMacAddressCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CMacAddressCount"], value)

    @property
    def CMacAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The incremental value of C-MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CMacAddressStep"])

    @CMacAddressStep.setter
    def CMacAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CMacAddressStep"], value)

    @property
    def ITagEthernetType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The I-Tag Ethernet type. An I-Tag is a multiplexing tag for service instance scaling in Provider Bridged Networks.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ITagEthernetType"])

    @property
    def InterNodeCmacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The incremental value of the Inter Node C-MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterNodeCmacAddress"])

    @InterNodeCmacAddress.setter
    def InterNodeCmacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterNodeCmacAddress"], value)

    @property
    def InterNodeCvlan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Inter Node Stacked VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterNodeCvlan"])

    @InterNodeCvlan.setter
    def InterNodeCvlan(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterNodeCvlan"], value)

    @property
    def InterNodeIsIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The incremental value of Inter Node service identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterNodeIsIdIncrement"])

    @InterNodeIsIdIncrement.setter
    def InterNodeIsIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterNodeIsIdIncrement"], value)

    @property
    def InterNodeSvlan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Inter Node Single VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterNodeSvlan"])

    @InterNodeSvlan.setter
    def InterNodeSvlan(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterNodeSvlan"], value)

    @property
    def IsId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsId"])

    @IsId.setter
    def IsId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsId"], value)

    @property
    def RBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The Restart State bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RBit"])

    @RBit.setter
    def RBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RBit"], value)

    @property
    def StartCmacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The starting C-MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartCmacAddress"])

    @StartCmacAddress.setter
    def StartCmacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartCmacAddress"], value)

    @property
    def StartCvlan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The starting value of Stacked VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartCvlan"])

    @StartCvlan.setter
    def StartCvlan(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartCvlan"], value)

    @property
    def StartSvlan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The starting value of Single VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartSvlan"])

    @StartSvlan.setter
    def StartSvlan(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartSvlan"], value)

    @property
    def TBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The external route tag bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TBit"])

    @TBit.setter
    def TBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TBit"], value)

    @property
    def TrafficDestMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The traffic-destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficDestMacAddress"])

    @TrafficDestMacAddress.setter
    def TrafficDestMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficDestMacAddress"], value)

    @property
    def TransmissionType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Select the type of packet transmission. Options include Unicast and Multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmissionType"])

    @TransmissionType.setter
    def TransmissionType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmissionType"], value)

    @property
    def VlanType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanType"])

    @VlanType.setter
    def VlanType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanType"], value)

    def update(
        self,
        CMacAddressCount=None,
        CMacAddressStep=None,
        InterNodeCmacAddress=None,
        InterNodeCvlan=None,
        InterNodeIsIdIncrement=None,
        InterNodeSvlan=None,
        IsId=None,
        RBit=None,
        StartCmacAddress=None,
        StartCvlan=None,
        StartSvlan=None,
        TBit=None,
        TrafficDestMacAddress=None,
        TransmissionType=None,
        VlanType=None,
    ):
        # type: (int, str, str, int, int, int, int, bool, str, int, int, bool, str, int, int) -> SpbmNodeIsIdRange
        """Updates spbmNodeIsIdRange resource on the server.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC addresses.
        - CMacAddressStep (str): The incremental value of C-MAC address.
        - InterNodeCmacAddress (str): The incremental value of the Inter Node C-MAC address.
        - InterNodeCvlan (number): The Inter Node Stacked VLAN.
        - InterNodeIsIdIncrement (number): The incremental value of Inter Node service identifier.
        - InterNodeSvlan (number): The Inter Node Single VLAN.
        - IsId (number): The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - StartCmacAddress (str): The starting C-MAC address.
        - StartCvlan (number): The starting value of Stacked VLAN.
        - StartSvlan (number): The starting value of Single VLAN.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): The type of VLAN.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        CMacAddressCount=None,
        CMacAddressStep=None,
        InterNodeCmacAddress=None,
        InterNodeCvlan=None,
        InterNodeIsIdIncrement=None,
        InterNodeSvlan=None,
        IsId=None,
        RBit=None,
        StartCmacAddress=None,
        StartCvlan=None,
        StartSvlan=None,
        TBit=None,
        TrafficDestMacAddress=None,
        TransmissionType=None,
        VlanType=None,
    ):
        # type: (int, str, str, int, int, int, int, bool, str, int, int, bool, str, int, int) -> SpbmNodeIsIdRange
        """Adds a new spbmNodeIsIdRange resource on the server and adds it to the container.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC addresses.
        - CMacAddressStep (str): The incremental value of C-MAC address.
        - InterNodeCmacAddress (str): The incremental value of the Inter Node C-MAC address.
        - InterNodeCvlan (number): The Inter Node Stacked VLAN.
        - InterNodeIsIdIncrement (number): The incremental value of Inter Node service identifier.
        - InterNodeSvlan (number): The Inter Node Single VLAN.
        - IsId (number): The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - StartCmacAddress (str): The starting C-MAC address.
        - StartCvlan (number): The starting value of Stacked VLAN.
        - StartSvlan (number): The starting value of Single VLAN.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): The type of VLAN.

        Returns
        -------
        - self: This instance with all currently retrieved spbmNodeIsIdRange resources using find and the newly added spbmNodeIsIdRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained spbmNodeIsIdRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        CMacAddressCount=None,
        CMacAddressStep=None,
        ITagEthernetType=None,
        InterNodeCmacAddress=None,
        InterNodeCvlan=None,
        InterNodeIsIdIncrement=None,
        InterNodeSvlan=None,
        IsId=None,
        RBit=None,
        StartCmacAddress=None,
        StartCvlan=None,
        StartSvlan=None,
        TBit=None,
        TrafficDestMacAddress=None,
        TransmissionType=None,
        VlanType=None,
    ):
        # type: (int, str, int, str, int, int, int, int, bool, str, int, int, bool, str, int, int) -> SpbmNodeIsIdRange
        """Finds and retrieves spbmNodeIsIdRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbmNodeIsIdRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbmNodeIsIdRange resources from the server.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC addresses.
        - CMacAddressStep (str): The incremental value of C-MAC address.
        - ITagEthernetType (number): The I-Tag Ethernet type. An I-Tag is a multiplexing tag for service instance scaling in Provider Bridged Networks.
        - InterNodeCmacAddress (str): The incremental value of the Inter Node C-MAC address.
        - InterNodeCvlan (number): The Inter Node Stacked VLAN.
        - InterNodeIsIdIncrement (number): The incremental value of Inter Node service identifier.
        - InterNodeSvlan (number): The Inter Node Single VLAN.
        - IsId (number): The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - StartCmacAddress (str): The starting C-MAC address.
        - StartCvlan (number): The starting value of Stacked VLAN.
        - StartSvlan (number): The starting value of Single VLAN.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): The type of VLAN.

        Returns
        -------
        - self: This instance with matching spbmNodeIsIdRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbmNodeIsIdRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbmNodeIsIdRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
