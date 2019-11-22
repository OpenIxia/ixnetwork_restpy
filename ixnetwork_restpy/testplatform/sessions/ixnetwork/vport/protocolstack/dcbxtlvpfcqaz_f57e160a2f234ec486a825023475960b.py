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


class DcbxTlvPfcQaz(Base):
    """DCBX Priority-based Flow Control Configuration TLV for 802.1Qaz.
    The DcbxTlvPfcQaz class encapsulates a required dcbxTlvPfcQaz resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxTlvPfcQaz'

    def __init__(self, parent):
        super(DcbxTlvPfcQaz, self).__init__(parent)

    @property
    def Mbc(self):
        """MACsec Bypass Capability Bit. Indicates whether the station is capable of bypassing MACsec when MACsec is disabled.

        Returns:
            bool
        """
        return self._get_attribute('mbc')
    @Mbc.setter
    def Mbc(self, value):
        self._set_attribute('mbc', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PfcCapability(self):
        """How many traffic classes may simultaneously support PFC.

        Returns:
            number
        """
        return self._get_attribute('pfcCapability')
    @PfcCapability.setter
    def PfcCapability(self, value):
        self._set_attribute('pfcCapability', value)

    @property
    def PfcEnableVector(self):
        """enable/disable PFC for each priority.

        Returns:
            list(number)
        """
        return self._get_attribute('pfcEnableVector')
    @PfcEnableVector.setter
    def PfcEnableVector(self, value):
        self._set_attribute('pfcEnableVector', value)

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

    def update(self, Mbc=None, PfcCapability=None, PfcEnableVector=None, Willing=None):
        """Updates a child instance of dcbxTlvPfcQaz on the server.

        Args:
            Mbc (bool): MACsec Bypass Capability Bit. Indicates whether the station is capable of bypassing MACsec when MACsec is disabled.
            PfcCapability (number): How many traffic classes may simultaneously support PFC.
            PfcEnableVector (list(number)): enable/disable PFC for each priority.
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
