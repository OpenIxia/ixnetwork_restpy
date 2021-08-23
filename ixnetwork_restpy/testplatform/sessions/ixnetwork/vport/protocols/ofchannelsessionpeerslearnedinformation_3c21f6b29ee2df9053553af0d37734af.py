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
from typing import List, Any, Union


class OfChannelSessionPeersLearnedInformation(Base):
    """NOT DEFINED
    The OfChannelSessionPeersLearnedInformation class encapsulates a list of ofChannelSessionPeersLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelSessionPeersLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannelSessionPeersLearnedInformation'
    _SDM_ATT_MAP = {
        'AveragePacketInReplyDelay': 'averagePacketInReplyDelay',
        'ConfiguredPacketInReplyCount': 'configuredPacketInReplyCount',
        'ConfiguredPacketInSentCount': 'configuredPacketInSentCount',
        'LocalPortNumber': 'localPortNumber',
        'MasterFlowRemovedMask': 'masterFlowRemovedMask',
        'MasterPacketInMask': 'masterPacketInMask',
        'MasterPortStatusMask': 'masterPortStatusMask',
        'PacketInTxRate': 'packetInTxRate',
        'PacketOutRxRate': 'packetOutRxRate',
        'RemoteIp': 'remoteIp',
        'RemotePortNumber': 'remotePortNumber',
        'ReplyState': 'replyState',
        'Role': 'role',
        'SlaveFlowRemovedMask': 'slaveFlowRemovedMask',
        'SlavePacketInMask': 'slavePacketInMask',
        'SlavePortStatusMask': 'slavePortStatusMask',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(OfChannelSessionPeersLearnedInformation, self).__init__(parent, list_op)

    @property
    def SwitchAuxiliaryConnectionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchauxiliaryconnectionlearnedinfo_f79c51c709a70b2062dfab3a58ebde80.SwitchAuxiliaryConnectionLearnedInfo): An instance of the SwitchAuxiliaryConnectionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchauxiliaryconnectionlearnedinfo_f79c51c709a70b2062dfab3a58ebde80 import SwitchAuxiliaryConnectionLearnedInfo
        if self._properties.get('SwitchAuxiliaryConnectionLearnedInfo', None) is not None:
            return self._properties.get('SwitchAuxiliaryConnectionLearnedInfo')
        else:
            return SwitchAuxiliaryConnectionLearnedInfo(self)

    @property
    def AveragePacketInReplyDelay(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['AveragePacketInReplyDelay'])

    @property
    def ConfiguredPacketInReplyCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredPacketInReplyCount'])

    @property
    def ConfiguredPacketInSentCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredPacketInSentCount'])

    @property
    def LocalPortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPortNumber'])

    @property
    def MasterFlowRemovedMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterFlowRemovedMask'])

    @property
    def MasterPacketInMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterPacketInMask'])

    @property
    def MasterPortStatusMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterPortStatusMask'])

    @property
    def PacketInTxRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Per second transmission rate of PacketIn messages from the time of protocol start. This is calculated only if Calculate PacketOut Rx Rate is enabled for the switch otherwise it is always 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketInTxRate'])

    @property
    def PacketOutRxRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Per second reception rate of PacketOut messages from the time of protocol start. This is calculated only if Calculate PacketOut Rx Rate is enabled for the switch otherwise it is always 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutRxRate'])

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def RemotePortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemotePortNumber'])

    @property
    def ReplyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    @property
    def Role(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Role'])

    @property
    def SlaveFlowRemovedMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SlaveFlowRemovedMask'])

    @property
    def SlavePacketInMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SlavePacketInMask'])

    @property
    def SlavePortStatusMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SlavePortStatusMask'])

    def add(self):
        """Adds a new ofChannelSessionPeersLearnedInformation resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved ofChannelSessionPeersLearnedInformation resources using find and the newly added ofChannelSessionPeersLearnedInformation resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AveragePacketInReplyDelay=None, ConfiguredPacketInReplyCount=None, ConfiguredPacketInSentCount=None, LocalPortNumber=None, MasterFlowRemovedMask=None, MasterPacketInMask=None, MasterPortStatusMask=None, PacketInTxRate=None, PacketOutRxRate=None, RemoteIp=None, RemotePortNumber=None, ReplyState=None, Role=None, SlaveFlowRemovedMask=None, SlavePacketInMask=None, SlavePortStatusMask=None):
        # type: (str, str, str, int, int, int, int, int, int, str, int, str, str, int, int, int) -> OfChannelSessionPeersLearnedInformation
        """Finds and retrieves ofChannelSessionPeersLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofChannelSessionPeersLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofChannelSessionPeersLearnedInformation resources from the server.

        Args
        ----
        - AveragePacketInReplyDelay (str): NOT DEFINED
        - ConfiguredPacketInReplyCount (str): NOT DEFINED
        - ConfiguredPacketInSentCount (str): NOT DEFINED
        - LocalPortNumber (number): NOT DEFINED
        - MasterFlowRemovedMask (number): NOT DEFINED
        - MasterPacketInMask (number): NOT DEFINED
        - MasterPortStatusMask (number): NOT DEFINED
        - PacketInTxRate (number): Per second transmission rate of PacketIn messages from the time of protocol start. This is calculated only if Calculate PacketOut Rx Rate is enabled for the switch otherwise it is always 0.
        - PacketOutRxRate (number): Per second reception rate of PacketOut messages from the time of protocol start. This is calculated only if Calculate PacketOut Rx Rate is enabled for the switch otherwise it is always 0.
        - RemoteIp (str): NOT DEFINED
        - RemotePortNumber (number): NOT DEFINED
        - ReplyState (str): NOT DEFINED
        - Role (str): NOT DEFINED
        - SlaveFlowRemovedMask (number): NOT DEFINED
        - SlavePacketInMask (number): NOT DEFINED
        - SlavePortStatusMask (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching ofChannelSessionPeersLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofChannelSessionPeersLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofChannelSessionPeersLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
