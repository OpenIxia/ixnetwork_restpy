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


class FcFportVnPortRange(Base):
    """
    The FcFportVnPortRange class encapsulates a required fcFportVnPortRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'fcFportVnPortRange'

    def __init__(self, parent):
        super(FcFportVnPortRange, self).__init__(parent)

    @property
    def B2bRxSize(self):
        """
        Returns
        -------
        - number: The buffer-to-buffer receive data field size in bytes.
        """
        return self._get_attribute('b2bRxSize')
    @B2bRxSize.setter
    def B2bRxSize(self, value):
        self._set_attribute('b2bRxSize', value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The number of N_Ports allocated by this range.
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NodeWwnIncrement(self):
        """
        Returns
        -------
        - str: The Node Name incrementing value for this N_Port range.
        """
        return self._get_attribute('nodeWwnIncrement')
    @NodeWwnIncrement.setter
    def NodeWwnIncrement(self, value):
        self._set_attribute('nodeWwnIncrement', value)

    @property
    def NodeWwnStart(self):
        """
        Returns
        -------
        - str: The Node Name starting value for this N_Port range.
        """
        return self._get_attribute('nodeWwnStart')
    @NodeWwnStart.setter
    def NodeWwnStart(self, value):
        self._set_attribute('nodeWwnStart', value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

    @property
    def PlogiDestId(self):
        """
        Returns
        -------
        - str: Indicates FCIDs and WWNs that can be used as destination for PLOGI requests.
        """
        return self._get_attribute('plogiDestId')
    @PlogiDestId.setter
    def PlogiDestId(self, value):
        self._set_attribute('plogiDestId', value)

    @property
    def PlogiEnabled(self):
        """
        Returns
        -------
        - bool: Enables these N_Ports to attempt a PLOGI connection with specified destinations.
        """
        return self._get_attribute('plogiEnabled')
    @PlogiEnabled.setter
    def PlogiEnabled(self, value):
        self._set_attribute('plogiEnabled', value)

    @property
    def PlogiMeshMode(self):
        """
        Returns
        -------
        - str: The association mode between PLOGI initiators and targets.
        """
        return self._get_attribute('plogiMeshMode')
    @PlogiMeshMode.setter
    def PlogiMeshMode(self, value):
        self._set_attribute('plogiMeshMode', value)

    @property
    def PlogiTargetName(self):
        """
        Returns
        -------
        - str: Indicates the N_Port range used as destination for PLOGI requests.
        """
        return self._get_attribute('plogiTargetName')
    @PlogiTargetName.setter
    def PlogiTargetName(self, value):
        self._set_attribute('plogiTargetName', value)

    @property
    def PortIdIncrement(self):
        """
        Returns
        -------
        - str: The increment value used to generate new FC_ID values.
        """
        return self._get_attribute('portIdIncrement')
    @PortIdIncrement.setter
    def PortIdIncrement(self, value):
        self._set_attribute('portIdIncrement', value)

    @property
    def PortIdStart(self):
        """
        Returns
        -------
        - str: The FC_ID value assigned to first N_Port.
        """
        return self._get_attribute('portIdStart')
    @PortIdStart.setter
    def PortIdStart(self, value):
        self._set_attribute('portIdStart', value)

    @property
    def PortWwnIncrement(self):
        """
        Returns
        -------
        - str: The Port Name incrementing value for this N_Port range.
        """
        return self._get_attribute('portWwnIncrement')
    @PortWwnIncrement.setter
    def PortWwnIncrement(self, value):
        self._set_attribute('portWwnIncrement', value)

    @property
    def PortWwnStart(self):
        """
        Returns
        -------
        - str: The Port Name starting value for this N_Port range.
        """
        return self._get_attribute('portWwnStart')
    @PortWwnStart.setter
    def PortWwnStart(self, value):
        self._set_attribute('portWwnStart', value)

    @property
    def Simulated(self):
        """
        Returns
        -------
        - bool: Enables these N_Ports to be simulated behind F_Port.
        """
        return self._get_attribute('simulated')
    @Simulated.setter
    def Simulated(self, value):
        self._set_attribute('simulated', value)

    @property
    def VxPortName(self):
        """
        Returns
        -------
        - str: The F_Port interface associated with this range
        """
        return self._get_attribute('vxPortName')
    @VxPortName.setter
    def VxPortName(self, value):
        self._set_attribute('vxPortName', value)

    def update(self, B2bRxSize=None, Count=None, Enabled=None, Name=None, NodeWwnIncrement=None, NodeWwnStart=None, PlogiDestId=None, PlogiEnabled=None, PlogiMeshMode=None, PlogiTargetName=None, PortIdIncrement=None, PortIdStart=None, PortWwnIncrement=None, PortWwnStart=None, Simulated=None, VxPortName=None):
        """Updates fcFportVnPortRange resource on the server.

        Args
        ----
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - Count (number): The number of N_Ports allocated by this range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - NodeWwnIncrement (str): The Node Name incrementing value for this N_Port range.
        - NodeWwnStart (str): The Node Name starting value for this N_Port range.
        - PlogiDestId (str): Indicates FCIDs and WWNs that can be used as destination for PLOGI requests.
        - PlogiEnabled (bool): Enables these N_Ports to attempt a PLOGI connection with specified destinations.
        - PlogiMeshMode (str): The association mode between PLOGI initiators and targets.
        - PlogiTargetName (str): Indicates the N_Port range used as destination for PLOGI requests.
        - PortIdIncrement (str): The increment value used to generate new FC_ID values.
        - PortIdStart (str): The FC_ID value assigned to first N_Port.
        - PortWwnIncrement (str): The Port Name incrementing value for this N_Port range.
        - PortWwnStart (str): The Port Name starting value for this N_Port range.
        - Simulated (bool): Enables these N_Ports to be simulated behind F_Port.
        - VxPortName (str): The F_Port interface associated with this range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

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
