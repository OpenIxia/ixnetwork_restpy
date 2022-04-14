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


class OfChannelLearnedInformation(Base):
    """Signifies the learned information of the OF channel.
    The OfChannelLearnedInformation class encapsulates a list of ofChannelLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ofChannelLearnedInformation"
    _SDM_ATT_MAP = {
        "ActionsSupported": "actionsSupported",
        "Capabilities": "capabilities",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "FlowRate": "flowRate",
        "GenerationId": "generationId",
        "LastErrorCode": "lastErrorCode",
        "LastErrorType": "lastErrorType",
        "LocalIp": "localIp",
        "LocalPortNumber": "localPortNumber",
        "MaxBufferSize": "maxBufferSize",
        "NegotiatedVersion": "negotiatedVersion",
        "NumberOfErrorsReceived": "numberOfErrorsReceived",
        "NumberOfPorts": "numberOfPorts",
        "NumberOfTables": "numberOfTables",
        "RemoteIp": "remoteIp",
        "RemotePortNumber": "remotePortNumber",
        "ReplyState": "replyState",
        "Role": "role",
        "SessionType": "sessionType",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OfChannelLearnedInformation, self).__init__(parent, list_op)

    @property
    def ControllerAuxiliaryConnectionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllerauxiliaryconnectionlearnedinfo_ab5a755c40a9da1388ea17855c2a32b0.ControllerAuxiliaryConnectionLearnedInfo): An instance of the ControllerAuxiliaryConnectionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllerauxiliaryconnectionlearnedinfo_ab5a755c40a9da1388ea17855c2a32b0 import (
            ControllerAuxiliaryConnectionLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("ControllerAuxiliaryConnectionLearnedInfo", None)
                is not None
            ):
                return self._properties.get("ControllerAuxiliaryConnectionLearnedInfo")
        return ControllerAuxiliaryConnectionLearnedInfo(self)

    @property
    def OfChannelPortsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportslearnedinformation_4d9d59409f73e69eb94129e9e84242be.OfChannelPortsLearnedInformation): An instance of the OfChannelPortsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportslearnedinformation_4d9d59409f73e69eb94129e9e84242be import (
            OfChannelPortsLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("OfChannelPortsLearnedInformation", None)
                is not None
            ):
                return self._properties.get("OfChannelPortsLearnedInformation")
        return OfChannelPortsLearnedInformation(self)

    @property
    def ActionsSupported(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the types of actions supported by the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActionsSupported"])

    @property
    def Capabilities(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the capabilities of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Capabilities"])

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the datapath ID of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathId"])

    @property
    def DataPathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the datapath ID of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathIdAsHex"])

    @property
    def FlowRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowRate"])

    @property
    def GenerationId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The generation ID number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GenerationId"])

    @property
    def LastErrorCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the error code of the last error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastErrorCode"])

    @property
    def LastErrorType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the type of the last error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastErrorType"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the local IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def LocalPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the local port number identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPortNumber"])

    @property
    def MaxBufferSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the maximum configurable buffer size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxBufferSize"])

    @property
    def NegotiatedVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatedVersion"])

    @property
    def NumberOfErrorsReceived(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the total number of errors received from the emulation start time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfErrorsReceived"])

    @property
    def NumberOfPorts(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the number of ports used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfPorts"])

    @property
    def NumberOfTables(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the number of tables supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfTables"])

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteIp"])

    @property
    def RemotePortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the remote port number identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemotePortNumber"])

    @property
    def ReplyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the reply state of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplyState"])

    @property
    def Role(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Role"])

    @property
    def SessionType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the type of OpenFlow session supported by the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionType"])

    def add(self):
        """Adds a new ofChannelLearnedInformation resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved ofChannelLearnedInformation resources using find and the newly added ofChannelLearnedInformation resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActionsSupported=None,
        Capabilities=None,
        DataPathId=None,
        DataPathIdAsHex=None,
        FlowRate=None,
        GenerationId=None,
        LastErrorCode=None,
        LastErrorType=None,
        LocalIp=None,
        LocalPortNumber=None,
        MaxBufferSize=None,
        NegotiatedVersion=None,
        NumberOfErrorsReceived=None,
        NumberOfPorts=None,
        NumberOfTables=None,
        RemoteIp=None,
        RemotePortNumber=None,
        ReplyState=None,
        Role=None,
        SessionType=None,
    ):
        # type: (str, str, str, str, int, str, str, str, str, int, int, int, int, int, int, str, int, str, str, str) -> OfChannelLearnedInformation
        """Finds and retrieves ofChannelLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofChannelLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofChannelLearnedInformation resources from the server.

        Args
        ----
        - ActionsSupported (str): Signifies the types of actions supported by the switch.
        - Capabilities (str): Signifies the capabilities of the switch.
        - DataPathId (str): Indicates the datapath ID of the OpenFlow switch.
        - DataPathIdAsHex (str): Indicates the datapath ID of the OpenFlow switch in hexadecimal format.
        - FlowRate (number): NOT DEFINED
        - GenerationId (str): The generation ID number.
        - LastErrorCode (str): Signifies the error code of the last error received.
        - LastErrorType (str): Signifies the type of the last error received.
        - LocalIp (str): Signifies the local IP address of the selected interface.
        - LocalPortNumber (number): Signifies the local port number identifier.
        - MaxBufferSize (number): Signifies the maximum configurable buffer size.
        - NegotiatedVersion (number): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - NumberOfErrorsReceived (number): Signifies the total number of errors received from the emulation start time.
        - NumberOfPorts (number): Signifies the number of ports used.
        - NumberOfTables (number): Signifies the number of tables supported.
        - RemoteIp (str): Signifies the Remote IP address of the selected interface.
        - RemotePortNumber (number): Signifies the remote port number identifier.
        - ReplyState (str): Signifies the reply state of the OF Channel.
        - Role (str): NOT DEFINED
        - SessionType (str): Signifies the type of OpenFlow session supported by the switch.

        Returns
        -------
        - self: This instance with matching ofChannelLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofChannelLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofChannelLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddRecordForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the addRecordForTrigger operation on the server.

        This describes the record added for trigger settings.

        addRecordForTrigger(async_operation=bool)bool
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "addRecordForTrigger", payload=payload, response_object=None
        )

    def ConfigureOfChannel(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the configureOfChannel operation on the server.

        It is a command that will configure controller OF channel from controller OF channel learned information.

        configureOfChannel(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "configureOfChannel", payload=payload, response_object=None
        )
