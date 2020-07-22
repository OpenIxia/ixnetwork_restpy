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


class DescriptionStatLearnedInformation(Base):
    """This object allows to configure the descriptionStatLearnedInformation ports.
    The DescriptionStatLearnedInformation class encapsulates a list of descriptionStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the DescriptionStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'descriptionStatLearnedInformation'
    _SDM_ATT_MAP = {
        'DataPathDescription': 'dataPathDescription',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'HardwareDescription': 'hardwareDescription',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'ManufacturerDescription': 'manufacturerDescription',
        'NegotiatedVersion': 'negotiatedVersion',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'SerialNumber': 'serialNumber',
        'SoftwareDescription': 'softwareDescription',
    }

    def __init__(self, parent):
        super(DescriptionStatLearnedInformation, self).__init__(parent)

    @property
    def DataPathDescription(self):
        """
        Returns
        -------
        - str: Indicates a description of datapath.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathDescription'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: Indicates the datapath ID of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: Indicates the datapath ID, in Hex, of the switch.
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
    def HardwareDescription(self):
        """
        Returns
        -------
        - str: Indicates the hardware description of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HardwareDescription'])

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
    def ManufacturerDescription(self):
        """
        Returns
        -------
        - str: Indicates the description of the switch manufacturer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ManufacturerDescription'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

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

    @property
    def SerialNumber(self):
        """
        Returns
        -------
        - str: Indicates the Serial Number of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SerialNumber'])

    @property
    def SoftwareDescription(self):
        """
        Returns
        -------
        - str: Indicates the description of the software installed on the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SoftwareDescription'])

    def find(self, DataPathDescription=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, HardwareDescription=None, Latency=None, LocalIp=None, ManufacturerDescription=None, NegotiatedVersion=None, RemoteIp=None, ReplyState=None, SerialNumber=None, SoftwareDescription=None):
        """Finds and retrieves descriptionStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve descriptionStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all descriptionStatLearnedInformation resources from the server.

        Args
        ----
        - DataPathDescription (str): Indicates a description of datapath.
        - DataPathId (str): Indicates the datapath ID of the switch.
        - DataPathIdAsHex (str): Indicates the datapath ID, in Hex, of the switch.
        - ErrorCode (str): Signifies the error code of the error received.
        - ErrorType (str): Signifies the type of the error received.
        - HardwareDescription (str): Indicates the hardware description of the switch.
        - Latency (number): Indicates the duration elapsed (in microsecond) between the learned info request and response.
        - LocalIp (str): Indicates the local IP of the Controller.
        - ManufacturerDescription (str): Indicates the description of the switch manufacturer.
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - RemoteIp (str): Indicates the IP of the remote end of the OF Channel.
        - ReplyState (str): Indicates the reply state of the switch.
        - SerialNumber (str): Indicates the Serial Number of the switch.
        - SoftwareDescription (str): Indicates the description of the software installed on the switch.

        Returns
        -------
        - self: This instance with matching descriptionStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of descriptionStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the descriptionStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
