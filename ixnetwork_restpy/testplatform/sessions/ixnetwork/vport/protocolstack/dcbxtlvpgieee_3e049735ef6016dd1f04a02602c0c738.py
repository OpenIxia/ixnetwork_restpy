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


class DcbxTlvPgIeee(Base):
    """DCBX Priority Groups TLV for IEEE 1.01.
    The DcbxTlvPgIeee class encapsulates a required dcbxTlvPgIeee resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxTlvPgIeee'

    def __init__(self, parent):
        super(DcbxTlvPgIeee, self).__init__(parent)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PriorityGroupIdMap(self):
        """Priority group ID associated to each priority.

        Returns:
            list(number)
        """
        return self._get_attribute('priorityGroupIdMap')
    @PriorityGroupIdMap.setter
    def PriorityGroupIdMap(self, value):
        self._set_attribute('priorityGroupIdMap', value)

    @property
    def PriorityGroupPercentageMap(self):
        """Percentage associated to each priority group id.

        Returns:
            list(number)
        """
        return self._get_attribute('priorityGroupPercentageMap')
    @PriorityGroupPercentageMap.setter
    def PriorityGroupPercentageMap(self, value):
        self._set_attribute('priorityGroupPercentageMap', value)

    @property
    def TcsSupported(self):
        """Number of traffic classes supported by device.

        Returns:
            number
        """
        return self._get_attribute('tcsSupported')
    @TcsSupported.setter
    def TcsSupported(self, value):
        self._set_attribute('tcsSupported', value)

    def update(self, PriorityGroupIdMap=None, PriorityGroupPercentageMap=None, TcsSupported=None):
        """Updates a child instance of dcbxTlvPgIeee on the server.

        Args:
            PriorityGroupIdMap (list(number)): Priority group ID associated to each priority.
            PriorityGroupPercentageMap (list(number)): Percentage associated to each priority group id.
            TcsSupported (number): Number of traffic classes supported by device.

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
