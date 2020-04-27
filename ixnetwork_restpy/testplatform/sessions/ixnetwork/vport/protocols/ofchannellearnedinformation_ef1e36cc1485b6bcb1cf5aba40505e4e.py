# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class OfChannelLearnedInformation(Base):
    """Signifies the learned information of the OF channel.
    The OfChannelLearnedInformation class encapsulates a list of ofChannelLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannelLearnedInformation'

    def __init__(self, parent):
        super(OfChannelLearnedInformation, self).__init__(parent)

    @property
    def ControllerAuxiliaryConnectionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllerauxiliaryconnectionlearnedinfo_9eeafcbd85aaba7bdb049639b94b6c77.ControllerAuxiliaryConnectionLearnedInfo): An instance of the ControllerAuxiliaryConnectionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllerauxiliaryconnectionlearnedinfo_9eeafcbd85aaba7bdb049639b94b6c77 import ControllerAuxiliaryConnectionLearnedInfo
        return ControllerAuxiliaryConnectionLearnedInfo(self)

    @property
    def OfChannelPortsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportslearnedinformation_2fc799d2883d0af5807bac410b3d880b.OfChannelPortsLearnedInformation): An instance of the OfChannelPortsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelportslearnedinformation_2fc799d2883d0af5807bac410b3d880b import OfChannelPortsLearnedInformation
        return OfChannelPortsLearnedInformation(self)

    @property
    def ActionsSupported(self):
        """
        Returns
        -------
        - str: Signifies the types of actions supported by the switch.
        """
        return self._get_attribute('actionsSupported')

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - str: Signifies the capabilities of the switch.
        """
        return self._get_attribute('capabilities')

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: Indicates the datapath ID of the OpenFlow switch.
        """
        return self._get_attribute('dataPathId')

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: Indicates the datapath ID of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute('dataPathIdAsHex')

    @property
    def FlowRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('flowRate')

    @property
    def GenerationId(self):
        """
        Returns
        -------
        - str: The generation ID number.
        """
        return self._get_attribute('generationId')

    @property
    def LastErrorCode(self):
        """
        Returns
        -------
        - str: Signifies the error code of the last error received.
        """
        return self._get_attribute('lastErrorCode')

    @property
    def LastErrorType(self):
        """
        Returns
        -------
        - str: Signifies the type of the last error received.
        """
        return self._get_attribute('lastErrorType')

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Signifies the local IP address of the selected interface.
        """
        return self._get_attribute('localIp')

    @property
    def LocalPortNumber(self):
        """
        Returns
        -------
        - number: Signifies the local port number identifier.
        """
        return self._get_attribute('localPortNumber')

    @property
    def MaxBufferSize(self):
        """
        Returns
        -------
        - number: Signifies the maximum configurable buffer size.
        """
        return self._get_attribute('maxBufferSize')

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - number: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute('negotiatedVersion')

    @property
    def NumberOfErrorsReceived(self):
        """
        Returns
        -------
        - number: Signifies the total number of errors received from the emulation start time.
        """
        return self._get_attribute('numberOfErrorsReceived')

    @property
    def NumberOfPorts(self):
        """
        Returns
        -------
        - number: Signifies the number of ports used.
        """
        return self._get_attribute('numberOfPorts')

    @property
    def NumberOfTables(self):
        """
        Returns
        -------
        - number: Signifies the number of tables supported.
        """
        return self._get_attribute('numberOfTables')

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: Signifies the Remote IP address of the selected interface.
        """
        return self._get_attribute('remoteIp')

    @property
    def RemotePortNumber(self):
        """
        Returns
        -------
        - number: Signifies the remote port number identifier.
        """
        return self._get_attribute('remotePortNumber')

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: Signifies the reply state of the OF Channel.
        """
        return self._get_attribute('replyState')

    @property
    def Role(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('role')

    @property
    def SessionType(self):
        """
        Returns
        -------
        - str: Signifies the type of OpenFlow session supported by the switch.
        """
        return self._get_attribute('sessionType')

    def find(self, ActionsSupported=None, Capabilities=None, DataPathId=None, DataPathIdAsHex=None, FlowRate=None, GenerationId=None, LastErrorCode=None, LastErrorType=None, LocalIp=None, LocalPortNumber=None, MaxBufferSize=None, NegotiatedVersion=None, NumberOfErrorsReceived=None, NumberOfPorts=None, NumberOfTables=None, RemoteIp=None, RemotePortNumber=None, ReplyState=None, Role=None, SessionType=None):
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
        return self._select(locals())

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

    def AddRecordForTrigger(self):
        """Executes the addRecordForTrigger operation on the server.

        This describes the record added for trigger settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('addRecordForTrigger', payload=payload, response_object=None)

    def ConfigureOfChannel(self):
        """Executes the configureOfChannel operation on the server.

        It is a command that will configure controller OF channel from controller OF channel learned information.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('configureOfChannel', payload=payload, response_object=None)
