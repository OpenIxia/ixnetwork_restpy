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


class DcbxRange(Base):
    """
    The DcbxRange class encapsulates a required dcbxRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxRange'
    _SDM_ATT_MAP = {
        'ChassisId': 'chassisId',
        'ControlTlvMaxVersion': 'controlTlvMaxVersion',
        'DcbxEnable': 'dcbxEnable',
        'DcbxSubtype': 'dcbxSubtype',
        'DestMacAddress': 'destMacAddress',
        'Enabled': 'enabled',
        'FastInitEnable': 'fastInitEnable',
        'HoldTime': 'holdTime',
        'Name': 'name',
        'ObjectId': 'objectId',
        'Oui': 'oui',
        'PortIdInterfaceName': 'portIdInterfaceName',
        'PortIdMacAddress': 'portIdMacAddress',
        'PortIdSubType': 'portIdSubType',
        'TxDelay': 'txDelay',
        'TxInterval': 'txInterval',
    }

    def __init__(self, parent):
        super(DcbxRange, self).__init__(parent)

    @property
    def DcbxTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlv_37d6aa3b470efb288cbc76a9c77c1804.DcbxTlv): An instance of the DcbxTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlv_37d6aa3b470efb288cbc76a9c77c1804 import DcbxTlv
        return DcbxTlv(self)

    @property
    def DcbxTlvQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvqaz_208cf6f4022a5582a454a5c53e9a3b60.DcbxTlvQaz): An instance of the DcbxTlvQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvqaz_208cf6f4022a5582a454a5c53e9a3b60 import DcbxTlvQaz
        return DcbxTlvQaz(self)

    @property
    def LldpTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lldptlv_d5fbeb9514995f839bf297520a09968a.LldpTlv): An instance of the LldpTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lldptlv_d5fbeb9514995f839bf297520a09968a import LldpTlv
        return LldpTlv(self)

    @property
    def ChassisId(self):
        """
        Returns
        -------
        - str: Chassis identification for thedevice that transmitted the LLDP frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChassisId'])
    @ChassisId.setter
    def ChassisId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChassisId'], value)

    @property
    def ControlTlvMaxVersion(self):
        """
        Returns
        -------
        - number: Highest DCBX protocol version supported by the system.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControlTlvMaxVersion'])
    @ControlTlvMaxVersion.setter
    def ControlTlvMaxVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ControlTlvMaxVersion'], value)

    @property
    def DcbxEnable(self):
        """
        Returns
        -------
        - bool: Enable DCBX TLVs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DcbxEnable'])
    @DcbxEnable.setter
    def DcbxEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DcbxEnable'], value)

    @property
    def DcbxSubtype(self):
        """
        Returns
        -------
        - number: Organizationally defined subtype.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DcbxSubtype'])
    @DcbxSubtype.setter
    def DcbxSubtype(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DcbxSubtype'], value)

    @property
    def DestMacAddress(self):
        """
        Returns
        -------
        - str: The destination MAC address value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestMacAddress'])
    @DestMacAddress.setter
    def DestMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestMacAddress'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FastInitEnable(self):
        """
        Returns
        -------
        - bool: Enable fast initial retransmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastInitEnable'])
    @FastInitEnable.setter
    def FastInitEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastInitEnable'], value)

    @property
    def HoldTime(self):
        """
        Returns
        -------
        - number: Multiplier to get actual TTL value used in an LLDPDU.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HoldTime'])
    @HoldTime.setter
    def HoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HoldTime'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def Oui(self):
        """
        Returns
        -------
        - str: The vendor identifier value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Oui'])
    @Oui.setter
    def Oui(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Oui'], value)

    @property
    def PortIdInterfaceName(self):
        """
        Returns
        -------
        - str: Port identification for the device that sent the LLDP frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortIdInterfaceName'])
    @PortIdInterfaceName.setter
    def PortIdInterfaceName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortIdInterfaceName'], value)

    @property
    def PortIdMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortIdMacAddress'])
    @PortIdMacAddress.setter
    def PortIdMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortIdMacAddress'], value)

    @property
    def PortIdSubType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortIdSubType'])
    @PortIdSubType.setter
    def PortIdSubType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortIdSubType'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: Minimum delay between successive LLDP packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    @property
    def TxInterval(self):
        """
        Returns
        -------
        - number: This parameter indicates the interval at which LLDP frames are transmitted on behalf of this LLDP agent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxInterval'])
    @TxInterval.setter
    def TxInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxInterval'], value)

    def update(self, ChassisId=None, ControlTlvMaxVersion=None, DcbxEnable=None, DcbxSubtype=None, DestMacAddress=None, Enabled=None, FastInitEnable=None, HoldTime=None, Name=None, Oui=None, PortIdInterfaceName=None, PortIdMacAddress=None, PortIdSubType=None, TxDelay=None, TxInterval=None):
        """Updates dcbxRange resource on the server.

        Args
        ----
        - ChassisId (str): Chassis identification for thedevice that transmitted the LLDP frame.
        - ControlTlvMaxVersion (number): Highest DCBX protocol version supported by the system.
        - DcbxEnable (bool): Enable DCBX TLVs.
        - DcbxSubtype (number): Organizationally defined subtype.
        - DestMacAddress (str): The destination MAC address value.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FastInitEnable (bool): Enable fast initial retransmission.
        - HoldTime (number): Multiplier to get actual TTL value used in an LLDPDU.
        - Name (str): Name of range
        - Oui (str): The vendor identifier value.
        - PortIdInterfaceName (str): Port identification for the device that sent the LLDP frame.
        - PortIdMacAddress (str): 
        - PortIdSubType (number): 
        - TxDelay (number): Minimum delay between successive LLDP packets.
        - TxInterval (number): This parameter indicates the interval at which LLDP frames are transmitted on behalf of this LLDP agent.

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
