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


class FcFportVxPort(Base):
    """Configuration parameters for one FC F_Port interface.
    The FcFportVxPort class encapsulates a required fcFportVxPort resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fcFportVxPort"
    _SDM_ATT_MAP = {
        "B2bRxSize": "b2bRxSize",
        "Enabled": "enabled",
        "FabricName": "fabricName",
        "FdiscRejectInterval": "fdiscRejectInterval",
        "FlogiRejectInterval": "flogiRejectInterval",
        "LogoRejectInterval": "logoRejectInterval",
        "Name": "name",
        "NameServer": "nameServer",
        "NameServerCommands": "nameServerCommands",
        "ObjectId": "objectId",
        "OperatingMode": "operatingMode",
        "PlogiRejectInterval": "plogiRejectInterval",
        "SwitchName": "switchName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FcFportVxPort, self).__init__(parent, list_op)

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
    def FabricName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Fabric Name value assigned to this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FabricName"])

    @FabricName.setter
    def FabricName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FabricName"], value)

    @property
    def FdiscRejectInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FDISC request. If N = 0, no FDISC request will be rejected. If N = 1, every FDISC request will be rejected. If N = 10, then the first 9 FDISC requests will be accepted, and the 10th will be rejected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FdiscRejectInterval"])

    @FdiscRejectInterval.setter
    def FdiscRejectInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FdiscRejectInterval"], value)

    @property
    def FlogiRejectInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FLOGI request. If N = 0, no FLOGI request will be rejected. If N = 1, every FLOGI request will be rejected. If N = 10, then the first 9 FLOGI requests will be accepted, and the 10th will be rejected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlogiRejectInterval"])

    @FlogiRejectInterval.setter
    def FlogiRejectInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlogiRejectInterval"], value)

    @property
    def LogoRejectInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th LOGO request. If N = 0, no LOGO request will be rejected. If N = 1, every LOGO request will be rejected. If N = 10, then the first 9 LOGO requests will be accepted, and the 10th will be rejected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LogoRejectInterval"])

    @LogoRejectInterval.setter
    def LogoRejectInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LogoRejectInterval"], value)

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
    def NameServer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select this option to respond to Name Service requests.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NameServer"])

    @NameServer.setter
    def NameServer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NameServer"], value)

    @property
    def NameServerCommands(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Signifies the Name Server Commands that will be accepted by the forwarder.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NameServerCommands"])

    @NameServerCommands.setter
    def NameServerCommands(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["NameServerCommands"], value)

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
    def OperatingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the operating mode for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OperatingMode"])

    @OperatingMode.setter
    def OperatingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OperatingMode"], value)

    @property
    def PlogiRejectInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th PLOGI request. If N = 0, no PLOGI request will be rejected. If N = 1, every PLOGI request will be rejected. If N = 10, then the first 9 PLOGI requests will be accepted, and the 10th will be rejected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiRejectInterval"])

    @PlogiRejectInterval.setter
    def PlogiRejectInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiRejectInterval"], value)

    @property
    def SwitchName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Switch Name value assigned to this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchName"])

    @SwitchName.setter
    def SwitchName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchName"], value)

    def update(
        self,
        B2bRxSize=None,
        Enabled=None,
        FabricName=None,
        FdiscRejectInterval=None,
        FlogiRejectInterval=None,
        LogoRejectInterval=None,
        Name=None,
        NameServer=None,
        NameServerCommands=None,
        OperatingMode=None,
        PlogiRejectInterval=None,
        SwitchName=None,
    ):
        # type: (int, bool, str, int, int, int, str, bool, List[int], str, int, str) -> FcFportVxPort
        """Updates fcFportVxPort resource on the server.

        Args
        ----
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FabricName (str): The Fabric Name value assigned to this interface.
        - FdiscRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FDISC request. If N = 0, no FDISC request will be rejected. If N = 1, every FDISC request will be rejected. If N = 10, then the first 9 FDISC requests will be accepted, and the 10th will be rejected.
        - FlogiRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FLOGI request. If N = 0, no FLOGI request will be rejected. If N = 1, every FLOGI request will be rejected. If N = 10, then the first 9 FLOGI requests will be accepted, and the 10th will be rejected.
        - LogoRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th LOGO request. If N = 0, no LOGO request will be rejected. If N = 1, every LOGO request will be rejected. If N = 10, then the first 9 LOGO requests will be accepted, and the 10th will be rejected.
        - Name (str): Name of range
        - NameServer (bool): Select this option to respond to Name Service requests.
        - NameServerCommands (list(number)): Signifies the Name Server Commands that will be accepted by the forwarder.
        - OperatingMode (str): Describes the operating mode for this interface.
        - PlogiRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th PLOGI request. If N = 0, no PLOGI request will be rejected. If N = 1, every PLOGI request will be rejected. If N = 10, then the first 9 PLOGI requests will be accepted, and the 10th will be rejected.
        - SwitchName (str): The Switch Name value assigned to this interface.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        B2bRxSize=None,
        Enabled=None,
        FabricName=None,
        FdiscRejectInterval=None,
        FlogiRejectInterval=None,
        LogoRejectInterval=None,
        Name=None,
        NameServer=None,
        NameServerCommands=None,
        ObjectId=None,
        OperatingMode=None,
        PlogiRejectInterval=None,
        SwitchName=None,
    ):
        # type: (int, bool, str, int, int, int, str, bool, List[int], str, str, int, str) -> FcFportVxPort
        """Finds and retrieves fcFportVxPort resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcFportVxPort resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcFportVxPort resources from the server.

        Args
        ----
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FabricName (str): The Fabric Name value assigned to this interface.
        - FdiscRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FDISC request. If N = 0, no FDISC request will be rejected. If N = 1, every FDISC request will be rejected. If N = 10, then the first 9 FDISC requests will be accepted, and the 10th will be rejected.
        - FlogiRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FLOGI request. If N = 0, no FLOGI request will be rejected. If N = 1, every FLOGI request will be rejected. If N = 10, then the first 9 FLOGI requests will be accepted, and the 10th will be rejected.
        - LogoRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th LOGO request. If N = 0, no LOGO request will be rejected. If N = 1, every LOGO request will be rejected. If N = 10, then the first 9 LOGO requests will be accepted, and the 10th will be rejected.
        - Name (str): Name of range
        - NameServer (bool): Select this option to respond to Name Service requests.
        - NameServerCommands (list(number)): Signifies the Name Server Commands that will be accepted by the forwarder.
        - ObjectId (str): Unique identifier for this object
        - OperatingMode (str): Describes the operating mode for this interface.
        - PlogiRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th PLOGI request. If N = 0, no PLOGI request will be rejected. If N = 1, every PLOGI request will be rejected. If N = 10, then the first 9 PLOGI requests will be accepted, and the 10th will be rejected.
        - SwitchName (str): The Switch Name value assigned to this interface.

        Returns
        -------
        - self: This instance with matching fcFportVxPort resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcFportVxPort data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcFportVxPort resources from the server available through an iterator or index

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
