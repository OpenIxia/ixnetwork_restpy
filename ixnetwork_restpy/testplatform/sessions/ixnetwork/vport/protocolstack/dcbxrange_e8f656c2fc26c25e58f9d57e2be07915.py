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


class DcbxRange(Base):
    """
    The DcbxRange class encapsulates a required dcbxRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxRange'

    def __init__(self, parent):
        super(DcbxRange, self).__init__(parent)

    @property
    def DcbxTlv(self):
        """An instance of the DcbxTlv class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlv_fc96d45f01313fec25fdb53d107bd7e6.DcbxTlv)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlv_fc96d45f01313fec25fdb53d107bd7e6 import DcbxTlv
        return DcbxTlv(self)

    @property
    def DcbxTlvQaz(self):
        """An instance of the DcbxTlvQaz class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvqaz_980dc539ded6d12e9cec0fa0fbea1c40.DcbxTlvQaz)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvqaz_980dc539ded6d12e9cec0fa0fbea1c40 import DcbxTlvQaz
        return DcbxTlvQaz(self)

    @property
    def LldpTlv(self):
        """An instance of the LldpTlv class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lldptlv_ae302484e58c4c4eee3cf14e2213a232.LldpTlv)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lldptlv_ae302484e58c4c4eee3cf14e2213a232 import LldpTlv
        return LldpTlv(self)

    @property
    def ChassisId(self):
        """Chassis identification for thedevice that transmitted the LLDP frame.

        Returns:
            str
        """
        return self._get_attribute('chassisId')
    @ChassisId.setter
    def ChassisId(self, value):
        self._set_attribute('chassisId', value)

    @property
    def ControlTlvMaxVersion(self):
        """Highest DCBX protocol version supported by the system.

        Returns:
            number
        """
        return self._get_attribute('controlTlvMaxVersion')
    @ControlTlvMaxVersion.setter
    def ControlTlvMaxVersion(self, value):
        self._set_attribute('controlTlvMaxVersion', value)

    @property
    def DcbxEnable(self):
        """Enable DCBX TLVs.

        Returns:
            bool
        """
        return self._get_attribute('dcbxEnable')
    @DcbxEnable.setter
    def DcbxEnable(self, value):
        self._set_attribute('dcbxEnable', value)

    @property
    def DcbxSubtype(self):
        """Organizationally defined subtype.

        Returns:
            number
        """
        return self._get_attribute('dcbxSubtype')
    @DcbxSubtype.setter
    def DcbxSubtype(self, value):
        self._set_attribute('dcbxSubtype', value)

    @property
    def DestMacAddress(self):
        """The destination MAC address value.

        Returns:
            str
        """
        return self._get_attribute('destMacAddress')
    @DestMacAddress.setter
    def DestMacAddress(self, value):
        self._set_attribute('destMacAddress', value)

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
    def FastInitEnable(self):
        """Enable fast initial retransmission.

        Returns:
            bool
        """
        return self._get_attribute('fastInitEnable')
    @FastInitEnable.setter
    def FastInitEnable(self, value):
        self._set_attribute('fastInitEnable', value)

    @property
    def HoldTime(self):
        """Multiplier to get actual TTL value used in an LLDPDU.

        Returns:
            number
        """
        return self._get_attribute('holdTime')
    @HoldTime.setter
    def HoldTime(self, value):
        self._set_attribute('holdTime', value)

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
    def Oui(self):
        """The vendor identifier value.

        Returns:
            str
        """
        return self._get_attribute('oui')
    @Oui.setter
    def Oui(self, value):
        self._set_attribute('oui', value)

    @property
    def PortIdInterfaceName(self):
        """Port identification for the device that sent the LLDP frame.

        Returns:
            str
        """
        return self._get_attribute('portIdInterfaceName')
    @PortIdInterfaceName.setter
    def PortIdInterfaceName(self, value):
        self._set_attribute('portIdInterfaceName', value)

    @property
    def PortIdMacAddress(self):
        """

        Returns:
            str
        """
        return self._get_attribute('portIdMacAddress')
    @PortIdMacAddress.setter
    def PortIdMacAddress(self, value):
        self._set_attribute('portIdMacAddress', value)

    @property
    def PortIdSubType(self):
        """

        Returns:
            number
        """
        return self._get_attribute('portIdSubType')
    @PortIdSubType.setter
    def PortIdSubType(self, value):
        self._set_attribute('portIdSubType', value)

    @property
    def TxDelay(self):
        """Minimum delay between successive LLDP packets.

        Returns:
            number
        """
        return self._get_attribute('txDelay')
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute('txDelay', value)

    @property
    def TxInterval(self):
        """This parameter indicates the interval at which LLDP frames are transmitted on behalf of this LLDP agent.

        Returns:
            number
        """
        return self._get_attribute('txInterval')
    @TxInterval.setter
    def TxInterval(self, value):
        self._set_attribute('txInterval', value)

    def update(self, ChassisId=None, ControlTlvMaxVersion=None, DcbxEnable=None, DcbxSubtype=None, DestMacAddress=None, Enabled=None, FastInitEnable=None, HoldTime=None, Name=None, Oui=None, PortIdInterfaceName=None, PortIdMacAddress=None, PortIdSubType=None, TxDelay=None, TxInterval=None):
        """Updates a child instance of dcbxRange on the server.

        Args:
            ChassisId (str): Chassis identification for thedevice that transmitted the LLDP frame.
            ControlTlvMaxVersion (number): Highest DCBX protocol version supported by the system.
            DcbxEnable (bool): Enable DCBX TLVs.
            DcbxSubtype (number): Organizationally defined subtype.
            DestMacAddress (str): The destination MAC address value.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FastInitEnable (bool): Enable fast initial retransmission.
            HoldTime (number): Multiplier to get actual TTL value used in an LLDPDU.
            Name (str): Name of range
            Oui (str): The vendor identifier value.
            PortIdInterfaceName (str): Port identification for the device that sent the LLDP frame.
            PortIdMacAddress (str): 
            PortIdSubType (number): 
            TxDelay (number): Minimum delay between successive LLDP packets.
            TxInterval (number): This parameter indicates the interval at which LLDP frames are transmitted on behalf of this LLDP agent.

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
