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


class SpbBaseVidRange(Base):
    """The Base VLAN ID of the SPB Topology Range.
    The SpbBaseVidRange class encapsulates a list of spbBaseVidRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbBaseVidRange.find() method.
    The list can be managed by using the SpbBaseVidRange.add() and SpbBaseVidRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "spbBaseVidRange"
    _SDM_ATT_MAP = {
        "BMacAddress": "bMacAddress",
        "BVlanPriority": "bVlanPriority",
        "BVlanTpId": "bVlanTpId",
        "BaseVid": "baseVid",
        "EctAlgorithmType": "ectAlgorithmType",
        "EnableAutoBmacEnabled": "enableAutoBmacEnabled",
        "EnableUseFlagBit": "enableUseFlagBit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SpbBaseVidRange, self).__init__(parent, list_op)

    @property
    def SpbIsIdRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbisidrange_31c007fedf45d93a5e16f9377610bf83.SpbIsIdRange): An instance of the SpbIsIdRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbisidrange_31c007fedf45d93a5e16f9377610bf83 import (
            SpbIsIdRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SpbIsIdRange", None) is not None:
                return self._properties.get("SpbIsIdRange")
        return SpbIsIdRange(self)

    @property
    def BMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The B-MAC address. The default value is the System ID of the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BMacAddress"])

    @BMacAddress.setter
    def BMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BMacAddress"], value)

    @property
    def BVlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The user priority of the Base VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BVlanPriority"])

    @BVlanPriority.setter
    def BVlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BVlanPriority"], value)

    @property
    def BVlanTpId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The tag priority identifier for base VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BVlanTpId"])

    @BVlanTpId.setter
    def BVlanTpId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BVlanTpId"], value)

    @property
    def BaseVid(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BaseVid"])

    @BaseVid.setter
    def BaseVid(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BaseVid"], value)

    @property
    def EctAlgorithmType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of SPB Equal Cost Tree (ECT) algorithm. The default value is 01-80-C2-01.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EctAlgorithmType"])

    @EctAlgorithmType.setter
    def EctAlgorithmType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EctAlgorithmType"], value)

    @property
    def EnableAutoBmacEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables auto base MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoBmacEnabled"])

    @EnableAutoBmacEnabled.setter
    def EnableAutoBmacEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoBmacEnabled"], value)

    @property
    def EnableUseFlagBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If set to true, allows to use flag bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableUseFlagBit"])

    @EnableUseFlagBit.setter
    def EnableUseFlagBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableUseFlagBit"], value)

    def update(
        self,
        BMacAddress=None,
        BVlanPriority=None,
        BVlanTpId=None,
        BaseVid=None,
        EctAlgorithmType=None,
        EnableAutoBmacEnabled=None,
        EnableUseFlagBit=None,
    ):
        # type: (str, int, int, int, int, bool, bool) -> SpbBaseVidRange
        """Updates spbBaseVidRange resource on the server.

        Args
        ----
        - BMacAddress (str): The B-MAC address. The default value is the System ID of the router.
        - BVlanPriority (number): The user priority of the Base VLAN tag.
        - BVlanTpId (number): The tag priority identifier for base VLAN.
        - BaseVid (number): The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        - EctAlgorithmType (number): The type of SPB Equal Cost Tree (ECT) algorithm. The default value is 01-80-C2-01.
        - EnableAutoBmacEnabled (bool): If true, enables auto base MAC address.
        - EnableUseFlagBit (bool): If set to true, allows to use flag bit.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        BMacAddress=None,
        BVlanPriority=None,
        BVlanTpId=None,
        BaseVid=None,
        EctAlgorithmType=None,
        EnableAutoBmacEnabled=None,
        EnableUseFlagBit=None,
    ):
        # type: (str, int, int, int, int, bool, bool) -> SpbBaseVidRange
        """Adds a new spbBaseVidRange resource on the server and adds it to the container.

        Args
        ----
        - BMacAddress (str): The B-MAC address. The default value is the System ID of the router.
        - BVlanPriority (number): The user priority of the Base VLAN tag.
        - BVlanTpId (number): The tag priority identifier for base VLAN.
        - BaseVid (number): The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        - EctAlgorithmType (number): The type of SPB Equal Cost Tree (ECT) algorithm. The default value is 01-80-C2-01.
        - EnableAutoBmacEnabled (bool): If true, enables auto base MAC address.
        - EnableUseFlagBit (bool): If set to true, allows to use flag bit.

        Returns
        -------
        - self: This instance with all currently retrieved spbBaseVidRange resources using find and the newly added spbBaseVidRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained spbBaseVidRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        BMacAddress=None,
        BVlanPriority=None,
        BVlanTpId=None,
        BaseVid=None,
        EctAlgorithmType=None,
        EnableAutoBmacEnabled=None,
        EnableUseFlagBit=None,
    ):
        # type: (str, int, int, int, int, bool, bool) -> SpbBaseVidRange
        """Finds and retrieves spbBaseVidRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbBaseVidRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbBaseVidRange resources from the server.

        Args
        ----
        - BMacAddress (str): The B-MAC address. The default value is the System ID of the router.
        - BVlanPriority (number): The user priority of the Base VLAN tag.
        - BVlanTpId (number): The tag priority identifier for base VLAN.
        - BaseVid (number): The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        - EctAlgorithmType (number): The type of SPB Equal Cost Tree (ECT) algorithm. The default value is 01-80-C2-01.
        - EnableAutoBmacEnabled (bool): If true, enables auto base MAC address.
        - EnableUseFlagBit (bool): If set to true, allows to use flag bit.

        Returns
        -------
        - self: This instance with matching spbBaseVidRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbBaseVidRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbBaseVidRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
