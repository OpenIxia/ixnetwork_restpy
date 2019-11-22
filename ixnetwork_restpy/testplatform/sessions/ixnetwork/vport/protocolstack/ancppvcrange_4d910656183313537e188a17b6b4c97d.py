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


class AncpPvcRange(Base):
    """Range of multiple PVCs for fine grained configuration
    The AncpPvcRange class encapsulates a required ancpPvcRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ancpPvcRange'

    def __init__(self, parent):
        super(AncpPvcRange, self).__init__(parent)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IncrementMode(self):
        """May take the following values: 0 (VCI first), 1 (VPI first), 2 (Both)

        Returns:
            number
        """
        return self._get_attribute('incrementMode')
    @IncrementMode.setter
    def IncrementMode(self, value):
        self._set_attribute('incrementMode', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def VciFirstId(self):
        """First ATM VCI value to use

        Returns:
            number
        """
        return self._get_attribute('vciFirstId')
    @VciFirstId.setter
    def VciFirstId(self, value):
        self._set_attribute('vciFirstId', value)

    @property
    def VciIncrement(self):
        """Step size for VCI increment

        Returns:
            number
        """
        return self._get_attribute('vciIncrement')
    @VciIncrement.setter
    def VciIncrement(self, value):
        self._set_attribute('vciIncrement', value)

    @property
    def VciIncrementStep(self):
        """Increment VCI every 'vciIncrementStep' addresses

        Returns:
            number
        """
        return self._get_attribute('vciIncrementStep')
    @VciIncrementStep.setter
    def VciIncrementStep(self, value):
        self._set_attribute('vciIncrementStep', value)

    @property
    def VciUniqueCount(self):
        """Number of VCIs

        Returns:
            number
        """
        return self._get_attribute('vciUniqueCount')
    @VciUniqueCount.setter
    def VciUniqueCount(self, value):
        self._set_attribute('vciUniqueCount', value)

    @property
    def VpiFirstId(self):
        """First ATM VPI value to use.

        Returns:
            number
        """
        return self._get_attribute('vpiFirstId')
    @VpiFirstId.setter
    def VpiFirstId(self, value):
        self._set_attribute('vpiFirstId', value)

    @property
    def VpiIncrement(self):
        """Step size for VPI increment

        Returns:
            number
        """
        return self._get_attribute('vpiIncrement')
    @VpiIncrement.setter
    def VpiIncrement(self, value):
        self._set_attribute('vpiIncrement', value)

    @property
    def VpiIncrementStep(self):
        """Increment VPI every 'vpiIncrementStep' addresses

        Returns:
            number
        """
        return self._get_attribute('vpiIncrementStep')
    @VpiIncrementStep.setter
    def VpiIncrementStep(self, value):
        self._set_attribute('vpiIncrementStep', value)

    @property
    def VpiUniqueCount(self):
        """Number of VPIs

        Returns:
            number
        """
        return self._get_attribute('vpiUniqueCount')
    @VpiUniqueCount.setter
    def VpiUniqueCount(self, value):
        self._set_attribute('vpiUniqueCount', value)

    def update(self, Enabled=None, IncrementMode=None, Name=None, VciFirstId=None, VciIncrement=None, VciIncrementStep=None, VciUniqueCount=None, VpiFirstId=None, VpiIncrement=None, VpiIncrementStep=None, VpiUniqueCount=None):
        """Updates a child instance of ancpPvcRange on the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IncrementMode (number): May take the following values: 0 (VCI first), 1 (VPI first), 2 (Both)
            Name (str): Name of range
            VciFirstId (number): First ATM VCI value to use
            VciIncrement (number): Step size for VCI increment
            VciIncrementStep (number): Increment VCI every 'vciIncrementStep' addresses
            VciUniqueCount (number): Number of VCIs
            VpiFirstId (number): First ATM VPI value to use.
            VpiIncrement (number): Step size for VPI increment
            VpiIncrementStep (number): Increment VPI every 'vpiIncrementStep' addresses
            VpiUniqueCount (number): Number of VPIs

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
