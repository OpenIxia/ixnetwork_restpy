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


class SwitchConfigLearnedInformation(Base):
    """NOT DEFINED
    The SwitchConfigLearnedInformation class encapsulates a list of switchConfigLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchConfigLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchConfigLearnedInformation'
    _SDM_ATT_MAP = {
        'ConfigFlags': 'configFlags',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'MissSendLength': 'missSendLength',
        'NegotiatedVersion': 'negotiatedVersion',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
    }

    def __init__(self, parent):
        super(SwitchConfigLearnedInformation, self).__init__(parent)

    @property
    def ConfigFlags(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigFlags'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MissSendLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MissSendLength'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    def find(self, ConfigFlags=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, Latency=None, LocalIp=None, MissSendLength=None, NegotiatedVersion=None, RemoteIp=None, ReplyState=None):
        """Finds and retrieves switchConfigLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchConfigLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchConfigLearnedInformation resources from the server.

        Args
        ----
        - ConfigFlags (str): NOT DEFINED
        - DataPathId (str): NOT DEFINED
        - DataPathIdAsHex (str): NOT DEFINED
        - ErrorCode (str): NOT DEFINED
        - ErrorType (str): NOT DEFINED
        - Latency (number): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - MissSendLength (number): NOT DEFINED
        - NegotiatedVersion (str): NOT DEFINED
        - RemoteIp (str): NOT DEFINED
        - ReplyState (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchConfigLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchConfigLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchConfigLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
