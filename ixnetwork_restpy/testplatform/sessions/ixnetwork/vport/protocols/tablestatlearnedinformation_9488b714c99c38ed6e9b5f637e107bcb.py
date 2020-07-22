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


class TableStatLearnedInformation(Base):
    """This object allows to configure the table statistics trigger parameters.
    The TableStatLearnedInformation class encapsulates a list of tableStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the TableStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tableStatLearnedInformation'
    _SDM_ATT_MAP = {
        'ActiveCount': 'activeCount',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'LookupCount': 'lookupCount',
        'MatchedCount': 'matchedCount',
        'MaxEntries': 'maxEntries',
        'NegotiatedVersion': 'negotiatedVersion',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'TableId': 'tableId',
        'TableName': 'tableName',
        'Wildcards': 'wildcards',
    }

    def __init__(self, parent):
        super(TableStatLearnedInformation, self).__init__(parent)

    @property
    def ActiveCount(self):
        """
        Returns
        -------
        - number: Indicates the number of active entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActiveCount'])

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
        - str: Signifies the error code of the error received
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
    def LookupCount(self):
        """
        Returns
        -------
        - str: Indicates the number of packets looked up in table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LookupCount'])

    @property
    def MatchedCount(self):
        """
        Returns
        -------
        - str: Indicates the number of packets that hit table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchedCount'])

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - number: Indicates the maximum number of entries supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxEntries'])

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
    def TableId(self):
        """
        Returns
        -------
        - str: Indicates the Identifier of table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])

    @property
    def TableName(self):
        """
        Returns
        -------
        - str: Indicates a name of the table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableName'])

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - str: Indicates the Wildcards that are supported by the table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Wildcards'])

    def find(self, ActiveCount=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, Latency=None, LocalIp=None, LookupCount=None, MatchedCount=None, MaxEntries=None, NegotiatedVersion=None, RemoteIp=None, ReplyState=None, TableId=None, TableName=None, Wildcards=None):
        """Finds and retrieves tableStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tableStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tableStatLearnedInformation resources from the server.

        Args
        ----
        - ActiveCount (number): Indicates the number of active entries.
        - DataPathId (str): Indicates the Datapath ID of the switch.
        - DataPathIdAsHex (str): Indicates the Datapath ID, in hexadecimal format, of the switch.
        - ErrorCode (str): Signifies the error code of the error received
        - ErrorType (str): Signifies the type of the error received.
        - Latency (number): Indicates the duration elapsed (in microsecond) between the learned info request and response.
        - LocalIp (str): Indicates the local IP of the Controller.
        - LookupCount (str): Indicates the number of packets looked up in table.
        - MatchedCount (str): Indicates the number of packets that hit table.
        - MaxEntries (number): Indicates the maximum number of entries supported.
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - RemoteIp (str): Indicates the IP of the remote end of the OF Channel.
        - ReplyState (str): Indicates the reply state of the switch.
        - TableId (str): Indicates the Identifier of table.
        - TableName (str): Indicates a name of the table.
        - Wildcards (str): Indicates the Wildcards that are supported by the table.

        Returns
        -------
        - self: This instance with matching tableStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tableStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tableStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
