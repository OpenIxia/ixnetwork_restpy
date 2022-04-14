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


class VsiFiltersInfo(Base):
    """
    The VsiFiltersInfo class encapsulates a list of vsiFiltersInfo resources that are managed by the user.
    A list of resources can be retrieved from the server using the VsiFiltersInfo.find() method.
    The list can be managed by using the VsiFiltersInfo.add() and VsiFiltersInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "vsiFiltersInfo"
    _SDM_ATT_MAP = {
        "CvlanFirstId": "cvlanFirstId",
        "CvlanIncrement": "cvlanIncrement",
        "CvlanIncrementStep": "cvlanIncrementStep",
        "CvlanUniqueCount": "cvlanUniqueCount",
        "Enabled": "enabled",
        "GroupFirstId": "groupFirstId",
        "GroupIncrement": "groupIncrement",
        "GroupIncrementStep": "groupIncrementStep",
        "GroupUniqueCount": "groupUniqueCount",
        "Mac": "mac",
        "MacIncrementBy": "macIncrementBy",
        "ObjectId": "objectId",
        "PcpFirstId": "pcpFirstId",
        "PcpIncrement": "pcpIncrement",
        "PcpIncrementStep": "pcpIncrementStep",
        "PcpUniqueCount": "pcpUniqueCount",
        "Ps": "ps",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(VsiFiltersInfo, self).__init__(parent, list_op)

    @property
    def CvlanFirstId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The first ID to be used for the C-VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CvlanFirstId"])

    @CvlanFirstId.setter
    def CvlanFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CvlanFirstId"], value)

    @property
    def CvlanIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CvlanIncrement"])

    @CvlanIncrement.setter
    def CvlanIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CvlanIncrement"], value)

    @property
    def CvlanIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CvlanIncrementStep"])

    @CvlanIncrementStep.setter
    def CvlanIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CvlanIncrementStep"], value)

    @property
    def CvlanUniqueCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of unique C-VLAN IDs to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CvlanUniqueCount"])

    @CvlanUniqueCount.setter
    def CvlanUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CvlanUniqueCount"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def GroupFirstId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The first Group ID to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupFirstId"])

    @GroupFirstId.setter
    def GroupFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupFirstId"], value)

    @property
    def GroupIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Amount of increment per increment step for Group ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupIncrement"])

    @GroupIncrement.setter
    def GroupIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupIncrement"], value)

    @property
    def GroupIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Frequency of Group ID increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupIncrementStep"])

    @GroupIncrementStep.setter
    def GroupIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupIncrementStep"], value)

    @property
    def GroupUniqueCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of unique Group IDs to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupUniqueCount"])

    @GroupUniqueCount.setter
    def GroupUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupUniqueCount"], value)

    @property
    def Mac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The start MAC address for the interface. It is always available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mac"])

    @Mac.setter
    def Mac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mac"], value)

    @property
    def MacIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacIncrementBy"])

    @MacIncrementBy.setter
    def MacIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacIncrementBy"], value)

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
    def PcpFirstId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The first ID to be used for the PCP tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcpFirstId"])

    @PcpFirstId.setter
    def PcpFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcpFirstId"], value)

    @property
    def PcpIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Amount of increment per increment step for PCP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcpIncrement"])

    @PcpIncrement.setter
    def PcpIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcpIncrement"], value)

    @property
    def PcpIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Frequency of PCP ID increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcpIncrementStep"])

    @PcpIncrementStep.setter
    def PcpIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcpIncrementStep"], value)

    @property
    def PcpUniqueCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of unique PCP IDs to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcpUniqueCount"])

    @PcpUniqueCount.setter
    def PcpUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcpUniqueCount"], value)

    @property
    def Ps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/disable priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ps"])

    @Ps.setter
    def Ps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ps"], value)

    def update(
        self,
        CvlanFirstId=None,
        CvlanIncrement=None,
        CvlanIncrementStep=None,
        CvlanUniqueCount=None,
        Enabled=None,
        GroupFirstId=None,
        GroupIncrement=None,
        GroupIncrementStep=None,
        GroupUniqueCount=None,
        Mac=None,
        MacIncrementBy=None,
        PcpFirstId=None,
        PcpIncrement=None,
        PcpIncrementStep=None,
        PcpUniqueCount=None,
        Ps=None,
    ):
        # type: (int, int, int, int, bool, int, int, int, int, str, str, int, int, int, int, bool) -> VsiFiltersInfo
        """Updates vsiFiltersInfo resource on the server.

        Args
        ----
        - CvlanFirstId (number): The first ID to be used for the C-VLAN tag.
        - CvlanIncrement (number): Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        - CvlanIncrementStep (number): Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        - CvlanUniqueCount (number): Number of unique C-VLAN IDs to use.
        - Enabled (bool):
        - GroupFirstId (number): The first Group ID to be used.
        - GroupIncrement (number): Amount of increment per increment step for Group ID.
        - GroupIncrementStep (number): Frequency of Group ID increment.
        - GroupUniqueCount (number): Number of unique Group IDs to use.
        - Mac (str): The start MAC address for the interface. It is always available.
        - MacIncrementBy (str): The increment MAC address.
        - PcpFirstId (number): The first ID to be used for the PCP tag.
        - PcpIncrement (number): Amount of increment per increment step for PCP.
        - PcpIncrementStep (number): Frequency of PCP ID increment.
        - PcpUniqueCount (number): Number of unique PCP IDs to use.
        - Ps (bool): Enable/disable priority.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        CvlanFirstId=None,
        CvlanIncrement=None,
        CvlanIncrementStep=None,
        CvlanUniqueCount=None,
        Enabled=None,
        GroupFirstId=None,
        GroupIncrement=None,
        GroupIncrementStep=None,
        GroupUniqueCount=None,
        Mac=None,
        MacIncrementBy=None,
        PcpFirstId=None,
        PcpIncrement=None,
        PcpIncrementStep=None,
        PcpUniqueCount=None,
        Ps=None,
    ):
        # type: (int, int, int, int, bool, int, int, int, int, str, str, int, int, int, int, bool) -> VsiFiltersInfo
        """Adds a new vsiFiltersInfo resource on the server and adds it to the container.

        Args
        ----
        - CvlanFirstId (number): The first ID to be used for the C-VLAN tag.
        - CvlanIncrement (number): Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        - CvlanIncrementStep (number): Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        - CvlanUniqueCount (number): Number of unique C-VLAN IDs to use.
        - Enabled (bool):
        - GroupFirstId (number): The first Group ID to be used.
        - GroupIncrement (number): Amount of increment per increment step for Group ID.
        - GroupIncrementStep (number): Frequency of Group ID increment.
        - GroupUniqueCount (number): Number of unique Group IDs to use.
        - Mac (str): The start MAC address for the interface. It is always available.
        - MacIncrementBy (str): The increment MAC address.
        - PcpFirstId (number): The first ID to be used for the PCP tag.
        - PcpIncrement (number): Amount of increment per increment step for PCP.
        - PcpIncrementStep (number): Frequency of PCP ID increment.
        - PcpUniqueCount (number): Number of unique PCP IDs to use.
        - Ps (bool): Enable/disable priority.

        Returns
        -------
        - self: This instance with all currently retrieved vsiFiltersInfo resources using find and the newly added vsiFiltersInfo resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vsiFiltersInfo resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        CvlanFirstId=None,
        CvlanIncrement=None,
        CvlanIncrementStep=None,
        CvlanUniqueCount=None,
        Enabled=None,
        GroupFirstId=None,
        GroupIncrement=None,
        GroupIncrementStep=None,
        GroupUniqueCount=None,
        Mac=None,
        MacIncrementBy=None,
        ObjectId=None,
        PcpFirstId=None,
        PcpIncrement=None,
        PcpIncrementStep=None,
        PcpUniqueCount=None,
        Ps=None,
    ):
        # type: (int, int, int, int, bool, int, int, int, int, str, str, str, int, int, int, int, bool) -> VsiFiltersInfo
        """Finds and retrieves vsiFiltersInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vsiFiltersInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vsiFiltersInfo resources from the server.

        Args
        ----
        - CvlanFirstId (number): The first ID to be used for the C-VLAN tag.
        - CvlanIncrement (number): Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        - CvlanIncrementStep (number): Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        - CvlanUniqueCount (number): Number of unique C-VLAN IDs to use.
        - Enabled (bool):
        - GroupFirstId (number): The first Group ID to be used.
        - GroupIncrement (number): Amount of increment per increment step for Group ID.
        - GroupIncrementStep (number): Frequency of Group ID increment.
        - GroupUniqueCount (number): Number of unique Group IDs to use.
        - Mac (str): The start MAC address for the interface. It is always available.
        - MacIncrementBy (str): The increment MAC address.
        - ObjectId (str): Unique identifier for this object
        - PcpFirstId (number): The first ID to be used for the PCP tag.
        - PcpIncrement (number): Amount of increment per increment step for PCP.
        - PcpIncrementStep (number): Frequency of PCP ID increment.
        - PcpUniqueCount (number): Number of unique PCP IDs to use.
        - Ps (bool): Enable/disable priority.

        Returns
        -------
        - self: This instance with matching vsiFiltersInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vsiFiltersInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vsiFiltersInfo resources from the server available through an iterator or index

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
