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


class DcbxTlvEtsQaz(Base):
    """DCBX ETS Configuration/Recommendation TLV for 802.1Qaz.
    The DcbxTlvEtsQaz class encapsulates a required dcbxTlvEtsQaz resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxTlvEtsQaz'
    _SDM_ATT_MAP = {
        'Cbs': 'cbs',
        'MaxTcs': 'maxTcs',
        'ObjectId': 'objectId',
        'TcGroupBwPercentMap': 'tcGroupBwPercentMap',
        'TcGroupPriorityMap': 'tcGroupPriorityMap',
        'TcGroupTsaMap': 'tcGroupTsaMap',
        'TlvSendOrder': 'tlvSendOrder',
        'TlvSendRestriction': 'tlvSendRestriction',
        'Willing': 'willing',
    }

    def __init__(self, parent):
        super(DcbxTlvEtsQaz, self).__init__(parent)

    @property
    def Cbs(self):
        """
        Returns
        -------
        - bool: Indicates whether the station supports credit-based shaper transmission selection algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cbs'])
    @Cbs.setter
    def Cbs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cbs'], value)

    @property
    def MaxTcs(self):
        """
        Returns
        -------
        - number: Number of traffic classes supported by device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxTcs'])
    @MaxTcs.setter
    def MaxTcs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxTcs'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def TcGroupBwPercentMap(self):
        """
        Returns
        -------
        - list(number): Bandwidth percentage
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcGroupBwPercentMap'])
    @TcGroupBwPercentMap.setter
    def TcGroupBwPercentMap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcGroupBwPercentMap'], value)

    @property
    def TcGroupPriorityMap(self):
        """
        Returns
        -------
        - list(number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcGroupPriorityMap'])
    @TcGroupPriorityMap.setter
    def TcGroupPriorityMap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcGroupPriorityMap'], value)

    @property
    def TcGroupTsaMap(self):
        """
        Returns
        -------
        - list(number): Transmission selection algorithm
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcGroupTsaMap'])
    @TcGroupTsaMap.setter
    def TcGroupTsaMap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcGroupTsaMap'], value)

    @property
    def TlvSendOrder(self):
        """
        Returns
        -------
        - number: Configure the order in which the ETS TLVs are sent
        """
        return self._get_attribute(self._SDM_ATT_MAP['TlvSendOrder'])
    @TlvSendOrder.setter
    def TlvSendOrder(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TlvSendOrder'], value)

    @property
    def TlvSendRestriction(self):
        """
        Returns
        -------
        - number: Configure if ETS will send the Configuration TLV, Recommendation TLV or both
        """
        return self._get_attribute(self._SDM_ATT_MAP['TlvSendRestriction'])
    @TlvSendRestriction.setter
    def TlvSendRestriction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TlvSendRestriction'], value)

    @property
    def Willing(self):
        """
        Returns
        -------
        - bool: Indicates whether this feature accepts its configuration from remote peers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Willing'])
    @Willing.setter
    def Willing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Willing'], value)

    def update(self, Cbs=None, MaxTcs=None, TcGroupBwPercentMap=None, TcGroupPriorityMap=None, TcGroupTsaMap=None, TlvSendOrder=None, TlvSendRestriction=None, Willing=None):
        """Updates dcbxTlvEtsQaz resource on the server.

        Args
        ----
        - Cbs (bool): Indicates whether the station supports credit-based shaper transmission selection algorithm.
        - MaxTcs (number): Number of traffic classes supported by device.
        - TcGroupBwPercentMap (list(number)): Bandwidth percentage
        - TcGroupPriorityMap (list(number)): 
        - TcGroupTsaMap (list(number)): Transmission selection algorithm
        - TlvSendOrder (number): Configure the order in which the ETS TLVs are sent
        - TlvSendRestriction (number): Configure if ETS will send the Configuration TLV, Recommendation TLV or both
        - Willing (bool): Indicates whether this feature accepts its configuration from remote peers.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)