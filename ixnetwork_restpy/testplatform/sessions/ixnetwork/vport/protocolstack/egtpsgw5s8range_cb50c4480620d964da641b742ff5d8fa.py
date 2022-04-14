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


class EgtpSgw5S8Range(Base):
    """SGW Range
    The EgtpSgw5S8Range class encapsulates a required egtpSgw5S8Range resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "egtpSgw5S8Range"
    _SDM_ATT_MAP = {
        "BearerResourceCommandN3": "bearerResourceCommandN3",
        "BearerResourceCommandT3": "bearerResourceCommandT3",
        "CreateSessionN3": "createSessionN3",
        "CreateSessiontT3": "createSessiontT3",
        "DeleteBearerCommandN3": "deleteBearerCommandN3",
        "DeleteBearerCommandT3": "deleteBearerCommandT3",
        "DeleteSessionN3": "deleteSessionN3",
        "DeleteSessionT3": "deleteSessionT3",
        "EchoRequestN3": "echoRequestN3",
        "EchoRequestT3": "echoRequestT3",
        "EnableEchoRequest": "enableEchoRequest",
        "Enabled": "enabled",
        "ModifyBearerCommandN3": "modifyBearerCommandN3",
        "ModifyBearerCommandT3": "modifyBearerCommandT3",
        "ModifyBearerN3": "modifyBearerN3",
        "ModifyBearerT3": "modifyBearerT3",
        "Name": "name",
        "ObjectId": "objectId",
        "RatType": "ratType",
        "SrcUdpPort": "srcUdpPort",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EgtpSgw5S8Range, self).__init__(parent, list_op)

    @property
    def BearerResourceCommandN3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of retransmissions that will be permitted for a Bearer Resource Cmd message
        """
        return self._get_attribute(self._SDM_ATT_MAP["BearerResourceCommandN3"])

    @BearerResourceCommandN3.setter
    def BearerResourceCommandN3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BearerResourceCommandN3"], value)

    @property
    def BearerResourceCommandT3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait for a Bearer Resource Command message. Bearer Resource Command is a tunnel management message that is sent from an MME to an SGW and forwarded to PGW as a part of the UE requested bearer resource modification procedure. The message is also sent on the S4 interface by a SGSN to a SGW and on the S5/S8 interface by a SGW to a PGW as part of the MS-initiated modification procedure, or secondary PDP context activation procedure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BearerResourceCommandT3"])

    @BearerResourceCommandT3.setter
    def BearerResourceCommandT3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BearerResourceCommandT3"], value)

    @property
    def CreateSessionN3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of retransmissions that will be permitted for a Create Session Response message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CreateSessionN3"])

    @CreateSessionN3.setter
    def CreateSessionN3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CreateSessionN3"], value)

    @property
    def CreateSessiontT3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait for a Create Session Response message. Create Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the E-UTRAN Initial Attach and UE Requested PDN Connectivity procedures.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CreateSessiontT3"])

    @CreateSessiontT3.setter
    def CreateSessiontT3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CreateSessiontT3"], value)

    @property
    def DeleteBearerCommandN3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of retransmissions that will be permitted for a Delete Bearer Command message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeleteBearerCommandN3"])

    @DeleteBearerCommandN3.setter
    def DeleteBearerCommandN3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeleteBearerCommandN3"], value)

    @property
    def DeleteBearerCommandT3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait for a Delete Bearer Command message. Delete Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as a part of the eNodeB-requested bearer release or MME-Initiated Dedicated Bearer Deactivation procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the MS and SGSN Initiated non Default Bearer Deactivation procedure using S4.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeleteBearerCommandT3"])

    @DeleteBearerCommandT3.setter
    def DeleteBearerCommandT3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeleteBearerCommandT3"], value)

    @property
    def DeleteSessionN3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of retransmissions that will be permitted for a Delete Session Response message
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeleteSessionN3"])

    @DeleteSessionN3.setter
    def DeleteSessionN3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeleteSessionN3"], value)

    @property
    def DeleteSessionT3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait for a Delete Session Response message. Delete Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the EUTRAN Initial Attach procedure; the UE, HSS or MME Initiated Detach procedure; and the UE or MME Requested PDN Disconnection procedure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeleteSessionT3"])

    @DeleteSessionT3.setter
    def DeleteSessionT3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeleteSessionT3"], value)

    @property
    def EchoRequestN3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of Echo Request retransmissions that will be permitted when no Echo Response has been received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoRequestN3"])

    @EchoRequestN3.setter
    def EchoRequestN3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoRequestN3"], value)

    @property
    def EchoRequestT3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait for an Echo Response message from the remote end point, in response to an Echo Request.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoRequestT3"])

    @EchoRequestT3.setter
    def EchoRequestT3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoRequestT3"], value)

    @property
    def EnableEchoRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set to true to send echo request
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEchoRequest"])

    @EnableEchoRequest.setter
    def EnableEchoRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEchoRequest"], value)

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
    def ModifyBearerCommandN3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of retransmissions that will be permitted for a Modify Bearer Command message
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModifyBearerCommandN3"])

    @ModifyBearerCommandN3.setter
    def ModifyBearerCommandN3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ModifyBearerCommandN3"], value)

    @property
    def ModifyBearerCommandT3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait for a Modify Bearer Command message. Modify Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS Modification procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS modification
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModifyBearerCommandT3"])

    @ModifyBearerCommandT3.setter
    def ModifyBearerCommandT3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ModifyBearerCommandT3"], value)

    @property
    def ModifyBearerN3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of retransmissions that will be permitted for a Modify Bearer Request message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModifyBearerN3"])

    @ModifyBearerN3.setter
    def ModifyBearerN3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ModifyBearerN3"], value)

    @property
    def ModifyBearerT3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait for a Modify Bearer Response message. Modify Bearer Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interfaces by the PGW to the SGW, as part of several procedures.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModifyBearerT3"])

    @ModifyBearerT3.setter
    def ModifyBearerT3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ModifyBearerT3"], value)

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
    def RatType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Radio Access Technology Type that the MME will include, whenever necessary, in its messages towards the SGW
        """
        return self._get_attribute(self._SDM_ATT_MAP["RatType"])

    @RatType.setter
    def RatType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RatType"], value)

    @property
    def SrcUdpPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Source UDP port for control plane messages (0 for random)
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcUdpPort"])

    @SrcUdpPort.setter
    def SrcUdpPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcUdpPort"], value)

    def update(
        self,
        BearerResourceCommandN3=None,
        BearerResourceCommandT3=None,
        CreateSessionN3=None,
        CreateSessiontT3=None,
        DeleteBearerCommandN3=None,
        DeleteBearerCommandT3=None,
        DeleteSessionN3=None,
        DeleteSessionT3=None,
        EchoRequestN3=None,
        EchoRequestT3=None,
        EnableEchoRequest=None,
        Enabled=None,
        ModifyBearerCommandN3=None,
        ModifyBearerCommandT3=None,
        ModifyBearerN3=None,
        ModifyBearerT3=None,
        Name=None,
        RatType=None,
        SrcUdpPort=None,
    ):
        # type: (int, int, int, int, int, int, int, int, int, int, bool, bool, int, int, int, int, str, str, int) -> EgtpSgw5S8Range
        """Updates egtpSgw5S8Range resource on the server.

        Args
        ----
        - BearerResourceCommandN3 (number): Maximum number of retransmissions that will be permitted for a Bearer Resource Cmd message
        - BearerResourceCommandT3 (number): Number of seconds to wait for a Bearer Resource Command message. Bearer Resource Command is a tunnel management message that is sent from an MME to an SGW and forwarded to PGW as a part of the UE requested bearer resource modification procedure. The message is also sent on the S4 interface by a SGSN to a SGW and on the S5/S8 interface by a SGW to a PGW as part of the MS-initiated modification procedure, or secondary PDP context activation procedure.
        - CreateSessionN3 (number): Maximum number of retransmissions that will be permitted for a Create Session Response message.
        - CreateSessiontT3 (number): Number of seconds to wait for a Create Session Response message. Create Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the E-UTRAN Initial Attach and UE Requested PDN Connectivity procedures.
        - DeleteBearerCommandN3 (number): Maximum number of retransmissions that will be permitted for a Delete Bearer Command message.
        - DeleteBearerCommandT3 (number): Number of seconds to wait for a Delete Bearer Command message. Delete Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as a part of the eNodeB-requested bearer release or MME-Initiated Dedicated Bearer Deactivation procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the MS and SGSN Initiated non Default Bearer Deactivation procedure using S4.
        - DeleteSessionN3 (number): Maximum number of retransmissions that will be permitted for a Delete Session Response message
        - DeleteSessionT3 (number): Number of seconds to wait for a Delete Session Response message. Delete Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the EUTRAN Initial Attach procedure; the UE, HSS or MME Initiated Detach procedure; and the UE or MME Requested PDN Disconnection procedure.
        - EchoRequestN3 (number): Maximum number of Echo Request retransmissions that will be permitted when no Echo Response has been received.
        - EchoRequestT3 (number): Number of seconds to wait for an Echo Response message from the remote end point, in response to an Echo Request.
        - EnableEchoRequest (bool): Set to true to send echo request
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ModifyBearerCommandN3 (number): Maximum number of retransmissions that will be permitted for a Modify Bearer Command message
        - ModifyBearerCommandT3 (number): Number of seconds to wait for a Modify Bearer Command message. Modify Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS Modification procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS modification
        - ModifyBearerN3 (number): Maximum number of retransmissions that will be permitted for a Modify Bearer Request message.
        - ModifyBearerT3 (number): Number of seconds to wait for a Modify Bearer Response message. Modify Bearer Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interfaces by the PGW to the SGW, as part of several procedures.
        - Name (str): Name of range
        - RatType (str): The Radio Access Technology Type that the MME will include, whenever necessary, in its messages towards the SGW
        - SrcUdpPort (number): Source UDP port for control plane messages (0 for random)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BearerResourceCommandN3=None,
        BearerResourceCommandT3=None,
        CreateSessionN3=None,
        CreateSessiontT3=None,
        DeleteBearerCommandN3=None,
        DeleteBearerCommandT3=None,
        DeleteSessionN3=None,
        DeleteSessionT3=None,
        EchoRequestN3=None,
        EchoRequestT3=None,
        EnableEchoRequest=None,
        Enabled=None,
        ModifyBearerCommandN3=None,
        ModifyBearerCommandT3=None,
        ModifyBearerN3=None,
        ModifyBearerT3=None,
        Name=None,
        ObjectId=None,
        RatType=None,
        SrcUdpPort=None,
    ):
        # type: (int, int, int, int, int, int, int, int, int, int, bool, bool, int, int, int, int, str, str, str, int) -> EgtpSgw5S8Range
        """Finds and retrieves egtpSgw5S8Range resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egtpSgw5S8Range resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egtpSgw5S8Range resources from the server.

        Args
        ----
        - BearerResourceCommandN3 (number): Maximum number of retransmissions that will be permitted for a Bearer Resource Cmd message
        - BearerResourceCommandT3 (number): Number of seconds to wait for a Bearer Resource Command message. Bearer Resource Command is a tunnel management message that is sent from an MME to an SGW and forwarded to PGW as a part of the UE requested bearer resource modification procedure. The message is also sent on the S4 interface by a SGSN to a SGW and on the S5/S8 interface by a SGW to a PGW as part of the MS-initiated modification procedure, or secondary PDP context activation procedure.
        - CreateSessionN3 (number): Maximum number of retransmissions that will be permitted for a Create Session Response message.
        - CreateSessiontT3 (number): Number of seconds to wait for a Create Session Response message. Create Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the E-UTRAN Initial Attach and UE Requested PDN Connectivity procedures.
        - DeleteBearerCommandN3 (number): Maximum number of retransmissions that will be permitted for a Delete Bearer Command message.
        - DeleteBearerCommandT3 (number): Number of seconds to wait for a Delete Bearer Command message. Delete Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as a part of the eNodeB-requested bearer release or MME-Initiated Dedicated Bearer Deactivation procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the MS and SGSN Initiated non Default Bearer Deactivation procedure using S4.
        - DeleteSessionN3 (number): Maximum number of retransmissions that will be permitted for a Delete Session Response message
        - DeleteSessionT3 (number): Number of seconds to wait for a Delete Session Response message. Delete Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the EUTRAN Initial Attach procedure; the UE, HSS or MME Initiated Detach procedure; and the UE or MME Requested PDN Disconnection procedure.
        - EchoRequestN3 (number): Maximum number of Echo Request retransmissions that will be permitted when no Echo Response has been received.
        - EchoRequestT3 (number): Number of seconds to wait for an Echo Response message from the remote end point, in response to an Echo Request.
        - EnableEchoRequest (bool): Set to true to send echo request
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ModifyBearerCommandN3 (number): Maximum number of retransmissions that will be permitted for a Modify Bearer Command message
        - ModifyBearerCommandT3 (number): Number of seconds to wait for a Modify Bearer Command message. Modify Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS Modification procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS modification
        - ModifyBearerN3 (number): Maximum number of retransmissions that will be permitted for a Modify Bearer Request message.
        - ModifyBearerT3 (number): Number of seconds to wait for a Modify Bearer Response message. Modify Bearer Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interfaces by the PGW to the SGW, as part of several procedures.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - RatType (str): The Radio Access Technology Type that the MME will include, whenever necessary, in its messages towards the SGW
        - SrcUdpPort (number): Source UDP port for control plane messages (0 for random)

        Returns
        -------
        - self: This instance with matching egtpSgw5S8Range resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egtpSgw5S8Range data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egtpSgw5S8Range resources from the server available through an iterator or index

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
