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


class QueueConfigLearnedInformation(Base):
    """This object allows to define the queue configuration learned information parameters of the switch.
    The QueueConfigLearnedInformation class encapsulates a list of queueConfigLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the QueueConfigLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'queueConfigLearnedInformation'
    _SDM_ATT_MAP = {
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'ExperimenterId': 'experimenterId',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'NegotiatedVersion': 'negotiatedVersion',
        'PortNumber': 'portNumber',
        'PropertyRate': 'propertyRate',
        'QueueId': 'queueId',
        'QueuePortNumber': 'queuePortNumber',
        'QueueProperty': 'queueProperty',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
    }

    def __init__(self, parent):
        super(QueueConfigLearnedInformation, self).__init__(parent)

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID, in hexadecimal format, of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: Signifies the error code of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: Signifies the type of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: The experimenter data field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: Value of the Experimenter data length field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - number: Value of the experimenter ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: Indicates the duration elapsed (in microsecond) between the learned info request and response.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Indicates the local IP of the Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - number: Indicates the Port number to which the queue belongs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumber'])

    @property
    def PropertyRate(self):
        """
        Returns
        -------
        - number: Indicates the minimum transmission rate of the queue if the queue supports the minimum rate property
        """
        return self._get_attribute(self._SDM_ATT_MAP['PropertyRate'])

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: Indicates the identifier of the queue
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])

    @property
    def QueuePortNumber(self):
        """
        Returns
        -------
        - number: The Switch port number on which Queue has been configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueuePortNumber'])

    @property
    def QueueProperty(self):
        """
        Returns
        -------
        - str: Indicates the supported properties of the queue.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueProperty'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: Indicates the IP of the remote end of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: Indicates the reply state of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    def find(self, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterId=None, Latency=None, LocalIp=None, NegotiatedVersion=None, PortNumber=None, PropertyRate=None, QueueId=None, QueuePortNumber=None, QueueProperty=None, RemoteIp=None, ReplyState=None):
        """Finds and retrieves queueConfigLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve queueConfigLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all queueConfigLearnedInformation resources from the server.

        Args
        ----
        - DataPathId (str): Indicates the Datapath ID of the switch.
        - DataPathIdAsHex (str): Indicates the Datapath ID, in hexadecimal format, of the switch.
        - ErrorCode (str): Signifies the error code of the error received.
        - ErrorType (str): Signifies the type of the error received.
        - ExperimenterData (str): The experimenter data field value.
        - ExperimenterDataLength (number): Value of the Experimenter data length field.
        - ExperimenterId (number): Value of the experimenter ID field.
        - Latency (number): Indicates the duration elapsed (in microsecond) between the learned info request and response.
        - LocalIp (str): Indicates the local IP of the Controller.
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - PortNumber (number): Indicates the Port number to which the queue belongs.
        - PropertyRate (number): Indicates the minimum transmission rate of the queue if the queue supports the minimum rate property
        - QueueId (number): Indicates the identifier of the queue
        - QueuePortNumber (number): The Switch port number on which Queue has been configured.
        - QueueProperty (str): Indicates the supported properties of the queue.
        - RemoteIp (str): Indicates the IP of the remote end of the OF Channel.
        - ReplyState (str): Indicates the reply state of the switch.

        Returns
        -------
        - self: This instance with matching queueConfigLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of queueConfigLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the queueConfigLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
