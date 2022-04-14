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


class AncpVlanRange(Base):
    """
    The AncpVlanRange class encapsulates a required ancpVlanRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ancpVlanRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "FirstId": "firstId",
        "IdIncrMode": "idIncrMode",
        "Increment": "increment",
        "IncrementStep": "incrementStep",
        "InnerEnable": "innerEnable",
        "InnerFirstId": "innerFirstId",
        "InnerIncrement": "innerIncrement",
        "InnerIncrementStep": "innerIncrementStep",
        "InnerPriority": "innerPriority",
        "InnerTpid": "innerTpid",
        "InnerUniqueCount": "innerUniqueCount",
        "Name": "name",
        "ObjectId": "objectId",
        "Priority": "priority",
        "Tpid": "tpid",
        "UniqueCount": "uniqueCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AncpVlanRange, self).__init__(parent, list_op)

    @property
    def VlanIdInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_7bba7c9e8069c103a6c866a7a3284b08.VlanIdInfo): An instance of the VlanIdInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_7bba7c9e8069c103a6c866a7a3284b08 import (
            VlanIdInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VlanIdInfo", None) is not None:
                return self._properties.get("VlanIdInfo")
        return VlanIdInfo(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FirstId(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The first ID to be used for the first VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstId"])

    @FirstId.setter
    def FirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstId"], value)

    @property
    def IdIncrMode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Method used to increment VLAN IDs. May take the following values: 0 (First VLAN first), 1 (Last VLAN first), 2 (All).
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdIncrMode"])

    @IdIncrMode.setter
    def IdIncrMode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IdIncrMode"], value)

    @property
    def Increment(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Amount of increment per increment step for first VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        """
        return self._get_attribute(self._SDM_ATT_MAP["Increment"])

    @Increment.setter
    def Increment(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Increment"], value)

    @property
    def IncrementStep(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Frequency of first VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementStep"])

    @IncrementStep.setter
    def IncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementStep"], value)

    @property
    def InnerEnable(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Enable the inner VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerEnable"])

    @InnerEnable.setter
    def InnerEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerEnable"], value)

    @property
    def InnerFirstId(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The first ID to be used for the inner VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerFirstId"])

    @InnerFirstId.setter
    def InnerFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerFirstId"], value)

    @property
    def InnerIncrement(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Amount of increment per increment step for Inner VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerIncrement"])

    @InnerIncrement.setter
    def InnerIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerIncrement"], value)

    @property
    def InnerIncrementStep(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Frequency of inner VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerIncrementStep"])

    @InnerIncrementStep.setter
    def InnerIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerIncrementStep"], value)

    @property
    def InnerPriority(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The 802.1Q priority to be used for the inner VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerPriority"])

    @InnerPriority.setter
    def InnerPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerPriority"], value)

    @property
    def InnerTpid(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: The TPID value in the inner VLAN Tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerTpid"])

    @InnerTpid.setter
    def InnerTpid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerTpid"], value)

    @property
    def InnerUniqueCount(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Number of unique inner VLAN IDs to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerUniqueCount"])

    @InnerUniqueCount.setter
    def InnerUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerUniqueCount"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def Priority(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The 802.1Q priority to be used for the outer VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Priority"])

    @Priority.setter
    def Priority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Priority"], value)

    @property
    def Tpid(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: The TPID value in the outer VLAN Tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tpid"])

    @Tpid.setter
    def Tpid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tpid"], value)

    @property
    def UniqueCount(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Number of unique first VLAN IDs to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UniqueCount"])

    @UniqueCount.setter
    def UniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UniqueCount"], value)

    def update(
        self,
        Enabled=None,
        FirstId=None,
        IdIncrMode=None,
        Increment=None,
        IncrementStep=None,
        InnerEnable=None,
        InnerFirstId=None,
        InnerIncrement=None,
        InnerIncrementStep=None,
        InnerPriority=None,
        InnerTpid=None,
        InnerUniqueCount=None,
        Name=None,
        Priority=None,
        Tpid=None,
        UniqueCount=None,
    ):
        # type: (bool, int, int, int, int, bool, int, int, int, int, str, int, str, int, str, int) -> AncpVlanRange
        """Updates ancpVlanRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FirstId (number): The first ID to be used for the first VLAN tag.
        - IdIncrMode (number): Method used to increment VLAN IDs. May take the following values: 0 (First VLAN first), 1 (Last VLAN first), 2 (All).
        - Increment (number): Amount of increment per increment step for first VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        - IncrementStep (number): Frequency of first VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        - InnerEnable (bool): Enable the inner VLAN.
        - InnerFirstId (number): The first ID to be used for the inner VLAN tag.
        - InnerIncrement (number): Amount of increment per increment step for Inner VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        - InnerIncrementStep (number): Frequency of inner VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        - InnerPriority (number): The 802.1Q priority to be used for the inner VLAN tag.
        - InnerTpid (str): The TPID value in the inner VLAN Tag.
        - InnerUniqueCount (number): Number of unique inner VLAN IDs to use.
        - Name (str): Name of range
        - Priority (number): The 802.1Q priority to be used for the outer VLAN tag.
        - Tpid (str): The TPID value in the outer VLAN Tag.
        - UniqueCount (number): Number of unique first VLAN IDs to use.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Enabled=None,
        FirstId=None,
        IdIncrMode=None,
        Increment=None,
        IncrementStep=None,
        InnerEnable=None,
        InnerFirstId=None,
        InnerIncrement=None,
        InnerIncrementStep=None,
        InnerPriority=None,
        InnerTpid=None,
        InnerUniqueCount=None,
        Name=None,
        ObjectId=None,
        Priority=None,
        Tpid=None,
        UniqueCount=None,
    ):
        # type: (bool, int, int, int, int, bool, int, int, int, int, str, int, str, str, int, str, int) -> AncpVlanRange
        """Finds and retrieves ancpVlanRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ancpVlanRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ancpVlanRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FirstId (number): The first ID to be used for the first VLAN tag.
        - IdIncrMode (number): Method used to increment VLAN IDs. May take the following values: 0 (First VLAN first), 1 (Last VLAN first), 2 (All).
        - Increment (number): Amount of increment per increment step for first VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        - IncrementStep (number): Frequency of first VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        - InnerEnable (bool): Enable the inner VLAN.
        - InnerFirstId (number): The first ID to be used for the inner VLAN tag.
        - InnerIncrement (number): Amount of increment per increment step for Inner VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        - InnerIncrementStep (number): Frequency of inner VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        - InnerPriority (number): The 802.1Q priority to be used for the inner VLAN tag.
        - InnerTpid (str): The TPID value in the inner VLAN Tag.
        - InnerUniqueCount (number): Number of unique inner VLAN IDs to use.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - Priority (number): The 802.1Q priority to be used for the outer VLAN tag.
        - Tpid (str): The TPID value in the outer VLAN Tag.
        - UniqueCount (number): Number of unique first VLAN IDs to use.

        Returns
        -------
        - self: This instance with matching ancpVlanRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ancpVlanRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ancpVlanRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )
