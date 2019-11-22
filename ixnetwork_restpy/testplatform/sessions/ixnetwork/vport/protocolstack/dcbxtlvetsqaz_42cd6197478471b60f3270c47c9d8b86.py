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


class DcbxTlvEtsQaz(Base):
    """DCBX ETS Configuration/Recommendation TLV for 802.1Qaz.
    The DcbxTlvEtsQaz class encapsulates a required dcbxTlvEtsQaz resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxTlvEtsQaz'

    def __init__(self, parent):
        super(DcbxTlvEtsQaz, self).__init__(parent)

    @property
    def Cbs(self):
        """Indicates whether the station supports credit-based shaper transmission selection algorithm.

        Returns:
            bool
        """
        return self._get_attribute('cbs')
    @Cbs.setter
    def Cbs(self, value):
        self._set_attribute('cbs', value)

    @property
    def MaxTcs(self):
        """Number of traffic classes supported by device.

        Returns:
            number
        """
        return self._get_attribute('maxTcs')
    @MaxTcs.setter
    def MaxTcs(self, value):
        self._set_attribute('maxTcs', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def TcGroupBwPercentMap(self):
        """Bandwidth percentage

        Returns:
            list(number)
        """
        return self._get_attribute('tcGroupBwPercentMap')
    @TcGroupBwPercentMap.setter
    def TcGroupBwPercentMap(self, value):
        self._set_attribute('tcGroupBwPercentMap', value)

    @property
    def TcGroupPriorityMap(self):
        """

        Returns:
            list(number)
        """
        return self._get_attribute('tcGroupPriorityMap')
    @TcGroupPriorityMap.setter
    def TcGroupPriorityMap(self, value):
        self._set_attribute('tcGroupPriorityMap', value)

    @property
    def TcGroupTsaMap(self):
        """Transmission selection algorithm

        Returns:
            list(number)
        """
        return self._get_attribute('tcGroupTsaMap')
    @TcGroupTsaMap.setter
    def TcGroupTsaMap(self, value):
        self._set_attribute('tcGroupTsaMap', value)

    @property
    def TlvSendOrder(self):
        """Configure the order in which the ETS TLVs are sent

        Returns:
            number
        """
        return self._get_attribute('tlvSendOrder')
    @TlvSendOrder.setter
    def TlvSendOrder(self, value):
        self._set_attribute('tlvSendOrder', value)

    @property
    def TlvSendRestriction(self):
        """Configure if ETS will send the Configuration TLV, Recommendation TLV or both

        Returns:
            number
        """
        return self._get_attribute('tlvSendRestriction')
    @TlvSendRestriction.setter
    def TlvSendRestriction(self, value):
        self._set_attribute('tlvSendRestriction', value)

    @property
    def Willing(self):
        """Indicates whether this feature accepts its configuration from remote peers.

        Returns:
            bool
        """
        return self._get_attribute('willing')
    @Willing.setter
    def Willing(self, value):
        self._set_attribute('willing', value)

    def update(self, Cbs=None, MaxTcs=None, TcGroupBwPercentMap=None, TcGroupPriorityMap=None, TcGroupTsaMap=None, TlvSendOrder=None, TlvSendRestriction=None, Willing=None):
        """Updates a child instance of dcbxTlvEtsQaz on the server.

        Args:
            Cbs (bool): Indicates whether the station supports credit-based shaper transmission selection algorithm.
            MaxTcs (number): Number of traffic classes supported by device.
            TcGroupBwPercentMap (list(number)): Bandwidth percentage
            TcGroupPriorityMap (list(number)): 
            TcGroupTsaMap (list(number)): Transmission selection algorithm
            TlvSendOrder (number): Configure the order in which the ETS TLVs are sent
            TlvSendRestriction (number): Configure if ETS will send the Configuration TLV, Recommendation TLV or both
            Willing (bool): Indicates whether this feature accepts its configuration from remote peers.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
