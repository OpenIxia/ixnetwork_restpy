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


class DataMdt(Base):
    """A set of Data MDT Ranges to be included in this PIM-SM interface.
    The DataMdt class encapsulates a list of dataMdt resources that are managed by the user.
    A list of resources can be retrieved from the server using the DataMdt.find() method.
    The list can be managed by using the DataMdt.add() and DataMdt.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "dataMdt"
    _SDM_ATT_MAP = {
        "ActivationInterval": "activationInterval",
        "CeGroupAddress": "ceGroupAddress",
        "CeGroupCount": "ceGroupCount",
        "CeSourceAddress": "ceSourceAddress",
        "CeSourceCount": "ceSourceCount",
        "DataMdtGroupAddress": "dataMdtGroupAddress",
        "DataMdtGroupAddressCount": "dataMdtGroupAddressCount",
        "DiscardLearnedState": "discardLearnedState",
        "Enabled": "enabled",
        "PackTlv": "packTlv",
        "RangeType": "rangeType",
    }
    _SDM_ENUM_MAP = {
        "rangeType": ["fullyMeshed", "oneToOne"],
    }

    def __init__(self, parent, list_op=False):
        super(DataMdt, self).__init__(parent, list_op)

    @property
    def LearnedMdtState(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmdtstate_dde8b4051ae44ed52084e863309783f6.LearnedMdtState): An instance of the LearnedMdtState class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmdtstate_dde8b4051ae44ed52084e863309783f6 import (
            LearnedMdtState,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedMdtState", None) is not None:
                return self._properties.get("LearnedMdtState")
        return LearnedMdtState(self)

    @property
    def ActivationInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time period after which packets will be sent (to support the switchover from the default MDT to the data MDT). The default is 60 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActivationInterval"])

    @ActivationInterval.setter
    def ActivationInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActivationInterval"], value)

    @property
    def CeGroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A multicast IPv4 address for the first CE destination group in the range.The default is 225.0.0.0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CeGroupAddress"])

    @CeGroupAddress.setter
    def CeGroupAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CeGroupAddress"], value)

    @property
    def CeGroupCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of CE group addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CeGroupCount"])

    @CeGroupCount.setter
    def CeGroupCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CeGroupCount"], value)

    @property
    def CeSourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A unicast IPv4 address for the first CE source.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CeSourceAddress"])

    @CeSourceAddress.setter
    def CeSourceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CeSourceAddress"], value)

    @property
    def CeSourceCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of CE Source Addresses in the range. Used with fully-meshed range type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CeSourceCount"])

    @CeSourceCount.setter
    def CeSourceCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CeSourceCount"], value)

    @property
    def DataMdtGroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first multicast group address in the data MDT range. The default is 230.0.0.0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataMdtGroupAddress"])

    @DataMdtGroupAddress.setter
    def DataMdtGroupAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataMdtGroupAddress"], value)

    @property
    def DataMdtGroupAddressCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of group addresses in the data MDT range. The default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataMdtGroupAddressCount"])

    @DataMdtGroupAddressCount.setter
    def DataMdtGroupAddressCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataMdtGroupAddressCount"], value)

    @property
    def DiscardLearnedState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, learned states associated with this data MDT range will be discarded.The default is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscardLearnedState"])

    @DiscardLearnedState.setter
    def DiscardLearnedState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DiscardLearnedState"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the switchover from the default MDT to the data MDT will triggered. The default is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def PackTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables packing of the data MDT type-length-values (TLVs). Multiple TLVs can be transmitted in one message.The default is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PackTlv"])

    @PackTlv.setter
    def PackTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PackTlv"], value)

    @property
    def RangeType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne): The type of data MDT range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeType"])

    @RangeType.setter
    def RangeType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeType"], value)

    def update(
        self,
        ActivationInterval=None,
        CeGroupAddress=None,
        CeGroupCount=None,
        CeSourceAddress=None,
        CeSourceCount=None,
        DataMdtGroupAddress=None,
        DataMdtGroupAddressCount=None,
        DiscardLearnedState=None,
        Enabled=None,
        PackTlv=None,
        RangeType=None,
    ):
        # type: (int, str, int, str, int, str, int, bool, bool, bool, str) -> DataMdt
        """Updates dataMdt resource on the server.

        Args
        ----
        - ActivationInterval (number): The time period after which packets will be sent (to support the switchover from the default MDT to the data MDT). The default is 60 seconds.
        - CeGroupAddress (str): A multicast IPv4 address for the first CE destination group in the range.The default is 225.0.0.0.
        - CeGroupCount (number): The number of CE group addresses in the range.
        - CeSourceAddress (str): A unicast IPv4 address for the first CE source.
        - CeSourceCount (number): The number of CE Source Addresses in the range. Used with fully-meshed range type.
        - DataMdtGroupAddress (str): The first multicast group address in the data MDT range. The default is 230.0.0.0.
        - DataMdtGroupAddressCount (number): The number of group addresses in the data MDT range. The default is 1.
        - DiscardLearnedState (bool): If enabled, learned states associated with this data MDT range will be discarded.The default is enabled.
        - Enabled (bool): If enabled, the switchover from the default MDT to the data MDT will triggered. The default is disabled.
        - PackTlv (bool): Enables packing of the data MDT type-length-values (TLVs). Multiple TLVs can be transmitted in one message.The default is enabled.
        - RangeType (str(fullyMeshed | oneToOne)): The type of data MDT range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ActivationInterval=None,
        CeGroupAddress=None,
        CeGroupCount=None,
        CeSourceAddress=None,
        CeSourceCount=None,
        DataMdtGroupAddress=None,
        DataMdtGroupAddressCount=None,
        DiscardLearnedState=None,
        Enabled=None,
        PackTlv=None,
        RangeType=None,
    ):
        # type: (int, str, int, str, int, str, int, bool, bool, bool, str) -> DataMdt
        """Adds a new dataMdt resource on the server and adds it to the container.

        Args
        ----
        - ActivationInterval (number): The time period after which packets will be sent (to support the switchover from the default MDT to the data MDT). The default is 60 seconds.
        - CeGroupAddress (str): A multicast IPv4 address for the first CE destination group in the range.The default is 225.0.0.0.
        - CeGroupCount (number): The number of CE group addresses in the range.
        - CeSourceAddress (str): A unicast IPv4 address for the first CE source.
        - CeSourceCount (number): The number of CE Source Addresses in the range. Used with fully-meshed range type.
        - DataMdtGroupAddress (str): The first multicast group address in the data MDT range. The default is 230.0.0.0.
        - DataMdtGroupAddressCount (number): The number of group addresses in the data MDT range. The default is 1.
        - DiscardLearnedState (bool): If enabled, learned states associated with this data MDT range will be discarded.The default is enabled.
        - Enabled (bool): If enabled, the switchover from the default MDT to the data MDT will triggered. The default is disabled.
        - PackTlv (bool): Enables packing of the data MDT type-length-values (TLVs). Multiple TLVs can be transmitted in one message.The default is enabled.
        - RangeType (str(fullyMeshed | oneToOne)): The type of data MDT range.

        Returns
        -------
        - self: This instance with all currently retrieved dataMdt resources using find and the newly added dataMdt resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dataMdt resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ActivationInterval=None,
        CeGroupAddress=None,
        CeGroupCount=None,
        CeSourceAddress=None,
        CeSourceCount=None,
        DataMdtGroupAddress=None,
        DataMdtGroupAddressCount=None,
        DiscardLearnedState=None,
        Enabled=None,
        PackTlv=None,
        RangeType=None,
    ):
        # type: (int, str, int, str, int, str, int, bool, bool, bool, str) -> DataMdt
        """Finds and retrieves dataMdt resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dataMdt resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dataMdt resources from the server.

        Args
        ----
        - ActivationInterval (number): The time period after which packets will be sent (to support the switchover from the default MDT to the data MDT). The default is 60 seconds.
        - CeGroupAddress (str): A multicast IPv4 address for the first CE destination group in the range.The default is 225.0.0.0.
        - CeGroupCount (number): The number of CE group addresses in the range.
        - CeSourceAddress (str): A unicast IPv4 address for the first CE source.
        - CeSourceCount (number): The number of CE Source Addresses in the range. Used with fully-meshed range type.
        - DataMdtGroupAddress (str): The first multicast group address in the data MDT range. The default is 230.0.0.0.
        - DataMdtGroupAddressCount (number): The number of group addresses in the data MDT range. The default is 1.
        - DiscardLearnedState (bool): If enabled, learned states associated with this data MDT range will be discarded.The default is enabled.
        - Enabled (bool): If enabled, the switchover from the default MDT to the data MDT will triggered. The default is disabled.
        - PackTlv (bool): Enables packing of the data MDT type-length-values (TLVs). Multiple TLVs can be transmitted in one message.The default is enabled.
        - RangeType (str(fullyMeshed | oneToOne)): The type of data MDT range.

        Returns
        -------
        - self: This instance with matching dataMdt resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dataMdt data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dataMdt resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
