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


class FcFportVxPort(Base):
    """Configuration parameters for one FC F_Port interface.
    The FcFportVxPort class encapsulates a required fcFportVxPort resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'fcFportVxPort'

    def __init__(self, parent):
        super(FcFportVxPort, self).__init__(parent)

    @property
    def B2bRxSize(self):
        """The buffer-to-buffer receive data field size in bytes.

        Returns:
            number
        """
        return self._get_attribute('b2bRxSize')
    @B2bRxSize.setter
    def B2bRxSize(self, value):
        self._set_attribute('b2bRxSize', value)

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
    def FabricName(self):
        """The Fabric Name value assigned to this interface.

        Returns:
            str
        """
        return self._get_attribute('fabricName')
    @FabricName.setter
    def FabricName(self, value):
        self._set_attribute('fabricName', value)

    @property
    def FdiscRejectInterval(self):
        """When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FDISC request. If N = 0, no FDISC request will be rejected. If N = 1, every FDISC request will be rejected. If N = 10, then the first 9 FDISC requests will be accepted, and the 10th will be rejected.

        Returns:
            number
        """
        return self._get_attribute('fdiscRejectInterval')
    @FdiscRejectInterval.setter
    def FdiscRejectInterval(self, value):
        self._set_attribute('fdiscRejectInterval', value)

    @property
    def FlogiRejectInterval(self):
        """When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FLOGI request. If N = 0, no FLOGI request will be rejected. If N = 1, every FLOGI request will be rejected. If N = 10, then the first 9 FLOGI requests will be accepted, and the 10th will be rejected.

        Returns:
            number
        """
        return self._get_attribute('flogiRejectInterval')
    @FlogiRejectInterval.setter
    def FlogiRejectInterval(self, value):
        self._set_attribute('flogiRejectInterval', value)

    @property
    def LogoRejectInterval(self):
        """When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th LOGO request. If N = 0, no LOGO request will be rejected. If N = 1, every LOGO request will be rejected. If N = 10, then the first 9 LOGO requests will be accepted, and the 10th will be rejected.

        Returns:
            number
        """
        return self._get_attribute('logoRejectInterval')
    @LogoRejectInterval.setter
    def LogoRejectInterval(self, value):
        self._set_attribute('logoRejectInterval', value)

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
    def NameServer(self):
        """Select this option to respond to Name Service requests.

        Returns:
            bool
        """
        return self._get_attribute('nameServer')
    @NameServer.setter
    def NameServer(self, value):
        self._set_attribute('nameServer', value)

    @property
    def NameServerCommands(self):
        """Signifies the Name Server Commands that will be accepted by the forwarder.

        Returns:
            list(number)
        """
        return self._get_attribute('nameServerCommands')
    @NameServerCommands.setter
    def NameServerCommands(self, value):
        self._set_attribute('nameServerCommands', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def OperatingMode(self):
        """Describes the operating mode for this interface.

        Returns:
            str
        """
        return self._get_attribute('operatingMode')
    @OperatingMode.setter
    def OperatingMode(self, value):
        self._set_attribute('operatingMode', value)

    @property
    def PlogiRejectInterval(self):
        """When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th PLOGI request. If N = 0, no PLOGI request will be rejected. If N = 1, every PLOGI request will be rejected. If N = 10, then the first 9 PLOGI requests will be accepted, and the 10th will be rejected.

        Returns:
            number
        """
        return self._get_attribute('plogiRejectInterval')
    @PlogiRejectInterval.setter
    def PlogiRejectInterval(self, value):
        self._set_attribute('plogiRejectInterval', value)

    @property
    def SwitchName(self):
        """The Switch Name value assigned to this interface.

        Returns:
            str
        """
        return self._get_attribute('switchName')
    @SwitchName.setter
    def SwitchName(self, value):
        self._set_attribute('switchName', value)

    def update(self, B2bRxSize=None, Enabled=None, FabricName=None, FdiscRejectInterval=None, FlogiRejectInterval=None, LogoRejectInterval=None, Name=None, NameServer=None, NameServerCommands=None, OperatingMode=None, PlogiRejectInterval=None, SwitchName=None):
        """Updates a child instance of fcFportVxPort on the server.

        Args:
            B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FabricName (str): The Fabric Name value assigned to this interface.
            FdiscRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FDISC request. If N = 0, no FDISC request will be rejected. If N = 1, every FDISC request will be rejected. If N = 10, then the first 9 FDISC requests will be accepted, and the 10th will be rejected.
            FlogiRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th FLOGI request. If N = 0, no FLOGI request will be rejected. If N = 1, every FLOGI request will be rejected. If N = 10, then the first 9 FLOGI requests will be accepted, and the 10th will be rejected.
            LogoRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th LOGO request. If N = 0, no LOGO request will be rejected. If N = 1, every LOGO request will be rejected. If N = 10, then the first 9 LOGO requests will be accepted, and the 10th will be rejected.
            Name (str): Name of range
            NameServer (bool): Select this option to respond to Name Service requests.
            NameServerCommands (list(number)): Signifies the Name Server Commands that will be accepted by the forwarder.
            OperatingMode (str): Describes the operating mode for this interface.
            PlogiRejectInterval (number): When the user enters N, IxNetwork F_Port will send out one LS_RJT for every N-th PLOGI request. If N = 0, no PLOGI request will be rejected. If N = 1, every PLOGI request will be rejected. If N = 10, then the first 9 PLOGI requests will be accepted, and the 10th will be rejected.
            SwitchName (str): The Switch Name value assigned to this interface.

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
