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


class FcFportVnPortRange(Base):
    """
    The FcFportVnPortRange class encapsulates a required fcFportVnPortRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fcFportVnPortRange"
    _SDM_ATT_MAP = {
        "B2bRxSize": "b2bRxSize",
        "Count": "count",
        "Enabled": "enabled",
        "Name": "name",
        "NodeWwnIncrement": "nodeWwnIncrement",
        "NodeWwnStart": "nodeWwnStart",
        "ObjectId": "objectId",
        "PlogiDestId": "plogiDestId",
        "PlogiEnabled": "plogiEnabled",
        "PlogiMeshMode": "plogiMeshMode",
        "PlogiTargetName": "plogiTargetName",
        "PortIdIncrement": "portIdIncrement",
        "PortIdStart": "portIdStart",
        "PortWwnIncrement": "portWwnIncrement",
        "PortWwnStart": "portWwnStart",
        "Simulated": "simulated",
        "VxPortName": "vxPortName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FcFportVnPortRange, self).__init__(parent, list_op)

    @property
    def B2bRxSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The buffer-to-buffer receive data field size in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["B2bRxSize"])

    @B2bRxSize.setter
    def B2bRxSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["B2bRxSize"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of N_Ports allocated by this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

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
    def NodeWwnIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Node Name incrementing value for this N_Port range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NodeWwnIncrement"])

    @NodeWwnIncrement.setter
    def NodeWwnIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NodeWwnIncrement"], value)

    @property
    def NodeWwnStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Node Name starting value for this N_Port range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NodeWwnStart"])

    @NodeWwnStart.setter
    def NodeWwnStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NodeWwnStart"], value)

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
    def PlogiDestId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates FCIDs and WWNs that can be used as destination for PLOGI requests.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiDestId"])

    @PlogiDestId.setter
    def PlogiDestId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiDestId"], value)

    @property
    def PlogiEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables these N_Ports to attempt a PLOGI connection with specified destinations.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiEnabled"])

    @PlogiEnabled.setter
    def PlogiEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiEnabled"], value)

    @property
    def PlogiMeshMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The association mode between PLOGI initiators and targets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiMeshMode"])

    @PlogiMeshMode.setter
    def PlogiMeshMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiMeshMode"], value)

    @property
    def PlogiTargetName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the N_Port range used as destination for PLOGI requests.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiTargetName"])

    @PlogiTargetName.setter
    def PlogiTargetName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiTargetName"], value)

    @property
    def PortIdIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment value used to generate new FC_ID values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdIncrement"])

    @PortIdIncrement.setter
    def PortIdIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdIncrement"], value)

    @property
    def PortIdStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The FC_ID value assigned to first N_Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdStart"])

    @PortIdStart.setter
    def PortIdStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdStart"], value)

    @property
    def PortWwnIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Port Name incrementing value for this N_Port range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortWwnIncrement"])

    @PortWwnIncrement.setter
    def PortWwnIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortWwnIncrement"], value)

    @property
    def PortWwnStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Port Name starting value for this N_Port range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortWwnStart"])

    @PortWwnStart.setter
    def PortWwnStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortWwnStart"], value)

    @property
    def Simulated(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables these N_Ports to be simulated behind F_Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Simulated"])

    @Simulated.setter
    def Simulated(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Simulated"], value)

    @property
    def VxPortName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The F_Port interface associated with this range
        """
        return self._get_attribute(self._SDM_ATT_MAP["VxPortName"])

    @VxPortName.setter
    def VxPortName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VxPortName"], value)

    def update(
        self,
        B2bRxSize=None,
        Count=None,
        Enabled=None,
        Name=None,
        NodeWwnIncrement=None,
        NodeWwnStart=None,
        PlogiDestId=None,
        PlogiEnabled=None,
        PlogiMeshMode=None,
        PlogiTargetName=None,
        PortIdIncrement=None,
        PortIdStart=None,
        PortWwnIncrement=None,
        PortWwnStart=None,
        Simulated=None,
        VxPortName=None,
    ):
        # type: (int, int, bool, str, str, str, str, bool, str, str, str, str, str, str, bool, str) -> FcFportVnPortRange
        """Updates fcFportVnPortRange resource on the server.

        Args
        ----
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - Count (number): The number of N_Ports allocated by this range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - NodeWwnIncrement (str): The Node Name incrementing value for this N_Port range.
        - NodeWwnStart (str): The Node Name starting value for this N_Port range.
        - PlogiDestId (str): Indicates FCIDs and WWNs that can be used as destination for PLOGI requests.
        - PlogiEnabled (bool): Enables these N_Ports to attempt a PLOGI connection with specified destinations.
        - PlogiMeshMode (str): The association mode between PLOGI initiators and targets.
        - PlogiTargetName (str): Indicates the N_Port range used as destination for PLOGI requests.
        - PortIdIncrement (str): The increment value used to generate new FC_ID values.
        - PortIdStart (str): The FC_ID value assigned to first N_Port.
        - PortWwnIncrement (str): The Port Name incrementing value for this N_Port range.
        - PortWwnStart (str): The Port Name starting value for this N_Port range.
        - Simulated (bool): Enables these N_Ports to be simulated behind F_Port.
        - VxPortName (str): The F_Port interface associated with this range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        B2bRxSize=None,
        Count=None,
        Enabled=None,
        Name=None,
        NodeWwnIncrement=None,
        NodeWwnStart=None,
        ObjectId=None,
        PlogiDestId=None,
        PlogiEnabled=None,
        PlogiMeshMode=None,
        PlogiTargetName=None,
        PortIdIncrement=None,
        PortIdStart=None,
        PortWwnIncrement=None,
        PortWwnStart=None,
        Simulated=None,
        VxPortName=None,
    ):
        # type: (int, int, bool, str, str, str, str, str, bool, str, str, str, str, str, str, bool, str) -> FcFportVnPortRange
        """Finds and retrieves fcFportVnPortRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcFportVnPortRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcFportVnPortRange resources from the server.

        Args
        ----
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - Count (number): The number of N_Ports allocated by this range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - NodeWwnIncrement (str): The Node Name incrementing value for this N_Port range.
        - NodeWwnStart (str): The Node Name starting value for this N_Port range.
        - ObjectId (str): Unique identifier for this object
        - PlogiDestId (str): Indicates FCIDs and WWNs that can be used as destination for PLOGI requests.
        - PlogiEnabled (bool): Enables these N_Ports to attempt a PLOGI connection with specified destinations.
        - PlogiMeshMode (str): The association mode between PLOGI initiators and targets.
        - PlogiTargetName (str): Indicates the N_Port range used as destination for PLOGI requests.
        - PortIdIncrement (str): The increment value used to generate new FC_ID values.
        - PortIdStart (str): The FC_ID value assigned to first N_Port.
        - PortWwnIncrement (str): The Port Name incrementing value for this N_Port range.
        - PortWwnStart (str): The Port Name starting value for this N_Port range.
        - Simulated (bool): Enables these N_Ports to be simulated behind F_Port.
        - VxPortName (str): The F_Port interface associated with this range

        Returns
        -------
        - self: This instance with matching fcFportVnPortRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcFportVnPortRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcFportVnPortRange resources from the server available through an iterator or index

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
