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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OfChannelSwitchLearnedInfo(Base):
    """This object allows to configure the OF Channel Switch learned information parameters.
    The OfChannelSwitchLearnedInfo class encapsulates a list of ofChannelSwitchLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelSwitchLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannelSwitchLearnedInfo'
    _SDM_ATT_MAP = {
        'ActionsSupported': 'actionsSupported',
        'AveragePacketInReplyDelay': 'averagePacketInReplyDelay',
        'Capabilities': 'capabilities',
        'ConfigFlags': 'configFlags',
        'ConfiguredPacketInReplyCount': 'configuredPacketInReplyCount',
        'ConfiguredPacketInSentCount': 'configuredPacketInSentCount',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'FlowRate': 'flowRate',
        'GenerationId': 'generationId',
        'LastErrorCode': 'lastErrorCode',
        'LastErrorType': 'lastErrorType',
        'LocalIp': 'localIp',
        'MaxBufferSize': 'maxBufferSize',
        'MaxPacketInBytes': 'maxPacketInBytes',
        'NegotiatedVersion': 'negotiatedVersion',
        'NumberOfAuxiliaryConnection': 'numberOfAuxiliaryConnection',
        'NumberOfErrorsSent': 'numberOfErrorsSent',
        'NumberOfPorts': 'numberOfPorts',
        'NumberofTable': 'numberofTable',
        'RemoteIp': 'remoteIp',
        'RemotePortNumber': 'remotePortNumber',
        'SessionType': 'sessionType',
    }

    def __init__(self, parent):
        super(OfChannelSwitchLearnedInfo, self).__init__(parent)

    @property
    def OfChannelPortsSwitchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportsswitchlearnedinfo_770d062c951b9c0656d18c015b1eec07.OfChannelPortsSwitchLearnedInfo): An instance of the OfChannelPortsSwitchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportsswitchlearnedinfo_770d062c951b9c0656d18c015b1eec07 import OfChannelPortsSwitchLearnedInfo
        return OfChannelPortsSwitchLearnedInfo(self)

    @property
    def OfChannelSessionPeersLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelsessionpeerslearnedinformation_377947b17842c6df2a85c6dec7bb2f70.OfChannelSessionPeersLearnedInformation): An instance of the OfChannelSessionPeersLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelsessionpeerslearnedinformation_377947b17842c6df2a85c6dec7bb2f70 import OfChannelSessionPeersLearnedInformation
        return OfChannelSessionPeersLearnedInformation(self)

    @property
    def ActionsSupported(self):
        """
        Returns
        -------
        - str: This describes the actions supported by the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionsSupported'])

    @property
    def AveragePacketInReplyDelay(self):
        """DEPRECATED 
        Returns
        -------
        - number: This describes the average delay between Packet-In sent from Switch and reply received from Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AveragePacketInReplyDelay'])
    @AveragePacketInReplyDelay.setter
    def AveragePacketInReplyDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AveragePacketInReplyDelay'], value)

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - str: This describes the OF Channel capabilities of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Capabilities'])

    @property
    def ConfigFlags(self):
        """
        Returns
        -------
        - str: This describes the Flags for fragmentation handling.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigFlags'])

    @property
    def ConfiguredPacketInReplyCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: This describes the Packet-In sent from Switch from configured Packet-In Ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredPacketInReplyCount'])
    @ConfiguredPacketInReplyCount.setter
    def ConfiguredPacketInReplyCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConfiguredPacketInReplyCount'], value)

    @property
    def ConfiguredPacketInSentCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: This describes the Packet-In reply received from Controller for Packet-In sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredPacketInSentCount'])
    @ConfiguredPacketInSentCount.setter
    def ConfiguredPacketInSentCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConfiguredPacketInSentCount'], value)

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: This describes the datapath ID of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: This describes the datapath ID, in hexadecimal format, of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def FlowRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowRate'])

    @property
    def GenerationId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerationId'])

    @property
    def LastErrorCode(self):
        """
        Returns
        -------
        - str: This describes the code for the last error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastErrorCode'])

    @property
    def LastErrorType(self):
        """
        Returns
        -------
        - str: This describes the type of error for the last error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastErrorType'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: This describes the local IP address of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MaxBufferSize(self):
        """
        Returns
        -------
        - number: This describes the maximum number of packets that can be stored in the buffer of the switch at a time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBufferSize'])

    @property
    def MaxPacketInBytes(self):
        """
        Returns
        -------
        - number: This describes the max amount of data to be sent in the Packet-In message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPacketInBytes'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - number: This describes the OpenFlow version supported by this configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def NumberOfAuxiliaryConnection(self):
        """DEPRECATED 
        Returns
        -------
        - number: This describes the number of auxiliary connections.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfAuxiliaryConnection'])
    @NumberOfAuxiliaryConnection.setter
    def NumberOfAuxiliaryConnection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfAuxiliaryConnection'], value)

    @property
    def NumberOfErrorsSent(self):
        """
        Returns
        -------
        - number: This describes the number of errors received by the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfErrorsSent'])

    @property
    def NumberOfPorts(self):
        """
        Returns
        -------
        - number: This describes the number of ports in the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfPorts'])

    @property
    def NumberofTable(self):
        """
        Returns
        -------
        - number: This describes the number of tables in the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberofTable'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: This describes the IP address of the remote end of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def RemotePortNumber(self):
        """DEPRECATED 
        Returns
        -------
        - number: This describes the TCP port number of the remote end of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemotePortNumber'])
    @RemotePortNumber.setter
    def RemotePortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemotePortNumber'], value)

    @property
    def SessionType(self):
        """
        Returns
        -------
        - str: This describes the type of OpenFlow session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionType'])

    def update(self, AveragePacketInReplyDelay=None, ConfiguredPacketInReplyCount=None, ConfiguredPacketInSentCount=None, NumberOfAuxiliaryConnection=None, RemotePortNumber=None):
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

    def find(self, ActionsSupported=None, AveragePacketInReplyDelay=None, Capabilities=None, ConfigFlags=None, ConfiguredPacketInReplyCount=None, ConfiguredPacketInSentCount=None, DataPathId=None, DataPathIdAsHex=None, FlowRate=None, GenerationId=None, LastErrorCode=None, LastErrorType=None, LocalIp=None, MaxBufferSize=None, MaxPacketInBytes=None, NegotiatedVersion=None, NumberOfAuxiliaryConnection=None, NumberOfErrorsSent=None, NumberOfPorts=None, NumberofTable=None, RemoteIp=None, RemotePortNumber=None, SessionType=None):
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

    def AddRecordForTrigger(self):
        """Executes the addRecordForTrigger operation on the server.

        API to add record for trigger to be sent.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('addRecordForTrigger', payload=payload, response_object=None)
