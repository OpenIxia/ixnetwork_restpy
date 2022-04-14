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


class OfChannelSwitchLearnedInfo(Base):
    """This object allows to configure the OF Channel Switch learned information parameters.
    The OfChannelSwitchLearnedInfo class encapsulates a list of ofChannelSwitchLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelSwitchLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ofChannelSwitchLearnedInfo"
    _SDM_ATT_MAP = {
        "ActionsSupported": "actionsSupported",
        "AveragePacketInReplyDelay": "averagePacketInReplyDelay",
        "Capabilities": "capabilities",
        "ConfigFlags": "configFlags",
        "ConfiguredPacketInReplyCount": "configuredPacketInReplyCount",
        "ConfiguredPacketInSentCount": "configuredPacketInSentCount",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "FlowRate": "flowRate",
        "GenerationId": "generationId",
        "LastErrorCode": "lastErrorCode",
        "LastErrorType": "lastErrorType",
        "LocalIp": "localIp",
        "MaxBufferSize": "maxBufferSize",
        "MaxPacketInBytes": "maxPacketInBytes",
        "NegotiatedVersion": "negotiatedVersion",
        "NumberOfAuxiliaryConnection": "numberOfAuxiliaryConnection",
        "NumberOfErrorsSent": "numberOfErrorsSent",
        "NumberOfPorts": "numberOfPorts",
        "NumberofTable": "numberofTable",
        "RemoteIp": "remoteIp",
        "RemotePortNumber": "remotePortNumber",
        "SessionType": "sessionType",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OfChannelSwitchLearnedInfo, self).__init__(parent, list_op)

    @property
    def OfChannelPortsSwitchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportsswitchlearnedinfo_aec9a10c2a9e74373f5bedf440b84b76.OfChannelPortsSwitchLearnedInfo): An instance of the OfChannelPortsSwitchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportsswitchlearnedinfo_aec9a10c2a9e74373f5bedf440b84b76 import (
            OfChannelPortsSwitchLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("OfChannelPortsSwitchLearnedInfo", None)
                is not None
            ):
                return self._properties.get("OfChannelPortsSwitchLearnedInfo")
        return OfChannelPortsSwitchLearnedInfo(self)

    @property
    def OfChannelSessionPeersLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelsessionpeerslearnedinformation_3c21f6b29ee2df9053553af0d37734af.OfChannelSessionPeersLearnedInformation): An instance of the OfChannelSessionPeersLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelsessionpeerslearnedinformation_3c21f6b29ee2df9053553af0d37734af import (
            OfChannelSessionPeersLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("OfChannelSessionPeersLearnedInformation", None)
                is not None
            ):
                return self._properties.get("OfChannelSessionPeersLearnedInformation")
        return OfChannelSessionPeersLearnedInformation(self)

    @property
    def ActionsSupported(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the actions supported by the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActionsSupported"])

    @property
    def AveragePacketInReplyDelay(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This describes the average delay between Packet-In sent from Switch and reply received from Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AveragePacketInReplyDelay"])

    @AveragePacketInReplyDelay.setter
    def AveragePacketInReplyDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AveragePacketInReplyDelay"], value)

    @property
    def Capabilities(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the OF Channel capabilities of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Capabilities"])

    @property
    def ConfigFlags(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the Flags for fragmentation handling.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfigFlags"])

    @property
    def ConfiguredPacketInReplyCount(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This describes the Packet-In sent from Switch from configured Packet-In Ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfiguredPacketInReplyCount"])

    @ConfiguredPacketInReplyCount.setter
    def ConfiguredPacketInReplyCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConfiguredPacketInReplyCount"], value)

    @property
    def ConfiguredPacketInSentCount(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This describes the Packet-In reply received from Controller for Packet-In sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfiguredPacketInSentCount"])

    @ConfiguredPacketInSentCount.setter
    def ConfiguredPacketInSentCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConfiguredPacketInSentCount"], value)

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the datapath ID of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathId"])

    @property
    def DataPathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the datapath ID, in hexadecimal format, of the switch.
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
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GenerationId"])

    @property
    def LastErrorCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the code for the last error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastErrorCode"])

    @property
    def LastErrorType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the type of error for the last error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastErrorType"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the local IP address of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def MaxBufferSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the maximum number of packets that can be stored in the buffer of the switch at a time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxBufferSize"])

    @property
    def MaxPacketInBytes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the max amount of data to be sent in the Packet-In message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxPacketInBytes"])

    @property
    def NegotiatedVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the OpenFlow version supported by this configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatedVersion"])

    @property
    def NumberOfAuxiliaryConnection(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This describes the number of auxiliary connections.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfAuxiliaryConnection"])

    @NumberOfAuxiliaryConnection.setter
    def NumberOfAuxiliaryConnection(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfAuxiliaryConnection"], value)

    @property
    def NumberOfErrorsSent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the number of errors received by the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfErrorsSent"])

    @property
    def NumberOfPorts(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the number of ports in the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfPorts"])

    @property
    def NumberofTable(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the number of tables in the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofTable"])

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the IP address of the remote end of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteIp"])

    @property
    def RemotePortNumber(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This describes the TCP port number of the remote end of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemotePortNumber"])

    @RemotePortNumber.setter
    def RemotePortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemotePortNumber"], value)

    @property
    def SessionType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This describes the type of OpenFlow session.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionType"])

    def update(
        self,
        AveragePacketInReplyDelay=None,
        ConfiguredPacketInReplyCount=None,
        ConfiguredPacketInSentCount=None,
        NumberOfAuxiliaryConnection=None,
        RemotePortNumber=None,
    ):
        # type: (int, int, int, int, int) -> OfChannelSwitchLearnedInfo
        """Updates ofChannelSwitchLearnedInfo resource on the server.

        Args
        ----
        - AveragePacketInReplyDelay (number): This describes the average delay between Packet-In sent from Switch and reply received from Controller.
        - ConfiguredPacketInReplyCount (number): This describes the Packet-In sent from Switch from configured Packet-In Ranges.
        - ConfiguredPacketInSentCount (number): This describes the Packet-In reply received from Controller for Packet-In sent.
        - NumberOfAuxiliaryConnection (number): This describes the number of auxiliary connections.
        - RemotePortNumber (number): This describes the TCP port number of the remote end of the OF Channel.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AveragePacketInReplyDelay=None,
        ConfiguredPacketInReplyCount=None,
        ConfiguredPacketInSentCount=None,
        NumberOfAuxiliaryConnection=None,
        RemotePortNumber=None,
    ):
        # type: (int, int, int, int, int) -> OfChannelSwitchLearnedInfo
        """Adds a new ofChannelSwitchLearnedInfo resource on the json, only valid with batch add utility

        Args
        ----
        - AveragePacketInReplyDelay (number): This describes the average delay between Packet-In sent from Switch and reply received from Controller.
        - ConfiguredPacketInReplyCount (number): This describes the Packet-In sent from Switch from configured Packet-In Ranges.
        - ConfiguredPacketInSentCount (number): This describes the Packet-In reply received from Controller for Packet-In sent.
        - NumberOfAuxiliaryConnection (number): This describes the number of auxiliary connections.
        - RemotePortNumber (number): This describes the TCP port number of the remote end of the OF Channel.

        Returns
        -------
        - self: This instance with all currently retrieved ofChannelSwitchLearnedInfo resources using find and the newly added ofChannelSwitchLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActionsSupported=None,
        AveragePacketInReplyDelay=None,
        Capabilities=None,
        ConfigFlags=None,
        ConfiguredPacketInReplyCount=None,
        ConfiguredPacketInSentCount=None,
        DataPathId=None,
        DataPathIdAsHex=None,
        FlowRate=None,
        GenerationId=None,
        LastErrorCode=None,
        LastErrorType=None,
        LocalIp=None,
        MaxBufferSize=None,
        MaxPacketInBytes=None,
        NegotiatedVersion=None,
        NumberOfAuxiliaryConnection=None,
        NumberOfErrorsSent=None,
        NumberOfPorts=None,
        NumberofTable=None,
        RemoteIp=None,
        RemotePortNumber=None,
        SessionType=None,
    ):
        # type: (str, int, str, str, int, int, str, str, int, int, str, str, str, int, int, int, int, int, int, int, str, int, str) -> OfChannelSwitchLearnedInfo
        """Finds and retrieves ofChannelSwitchLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofChannelSwitchLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofChannelSwitchLearnedInfo resources from the server.

        Args
        ----
        - ActionsSupported (str): This describes the actions supported by the switch.
        - AveragePacketInReplyDelay (number): This describes the average delay between Packet-In sent from Switch and reply received from Controller.
        - Capabilities (str): This describes the OF Channel capabilities of the switch.
        - ConfigFlags (str): This describes the Flags for fragmentation handling.
        - ConfiguredPacketInReplyCount (number): This describes the Packet-In sent from Switch from configured Packet-In Ranges.
        - ConfiguredPacketInSentCount (number): This describes the Packet-In reply received from Controller for Packet-In sent.
        - DataPathId (str): This describes the datapath ID of the switch.
        - DataPathIdAsHex (str): This describes the datapath ID, in hexadecimal format, of the switch.
        - FlowRate (number): NOT DEFINED
        - GenerationId (number): NOT DEFINED
        - LastErrorCode (str): This describes the code for the last error received.
        - LastErrorType (str): This describes the type of error for the last error received.
        - LocalIp (str): This describes the local IP address of the switch.
        - MaxBufferSize (number): This describes the maximum number of packets that can be stored in the buffer of the switch at a time.
        - MaxPacketInBytes (number): This describes the max amount of data to be sent in the Packet-In message.
        - NegotiatedVersion (number): This describes the OpenFlow version supported by this configuration.
        - NumberOfAuxiliaryConnection (number): This describes the number of auxiliary connections.
        - NumberOfErrorsSent (number): This describes the number of errors received by the switch.
        - NumberOfPorts (number): This describes the number of ports in the switch.
        - NumberofTable (number): This describes the number of tables in the switch.
        - RemoteIp (str): This describes the IP address of the remote end of the OF Channel.
        - RemotePortNumber (number): This describes the TCP port number of the remote end of the OF Channel.
        - SessionType (str): This describes the type of OpenFlow session.

        Returns
        -------
        - self: This instance with matching ofChannelSwitchLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofChannelSwitchLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofChannelSwitchLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddRecordForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the addRecordForTrigger operation on the server.

        API to add record for trigger to be sent.

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
