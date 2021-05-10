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


class EvbStationRange(Base):
    """Manages a range of Edge Virtual Bridging Stations.
    The EvbStationRange class encapsulates a required evbStationRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'evbStationRange'
    _SDM_ATT_MAP = {
        'ChannelCapability': 'channelCapability',
        'ChassisId': 'chassisId',
        'DefaultEr': 'defaultEr',
        'Enabled': 'enabled',
        'HoldTime': 'holdTime',
        'Name': 'name',
        'ObjectId': 'objectId',
        'PortIdInterfaceName': 'portIdInterfaceName',
        'PortIdMacAddress': 'portIdMacAddress',
        'PortIdSubType': 'portIdSubType',
        'SComponentMode': 'sComponentMode',
        'TxDelay': 'txDelay',
        'TxInterval': 'txInterval',
    }

    def __init__(self, parent):
        super(EvbStationRange, self).__init__(parent)

    @property
    def ErRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.errange_162ea2ac786a0c4f518cef35d874b832.ErRange): An instance of the ErRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.errange_162ea2ac786a0c4f518cef35d874b832 import ErRange
        return ErRange(self)

    @property
    def ChannelCapability(self):
        """
        Returns
        -------
        - number: Advertised Channel Capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChannelCapability'])
    @ChannelCapability.setter
    def ChannelCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChannelCapability'], value)

    @property
    def ChassisId(self):
        """
        Returns
        -------
        - str: The Chassis ID that will be advertised in the mandatory LLDP TLVs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChassisId'])
    @ChassisId.setter
    def ChassisId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChassisId'], value)

    @property
    def DefaultEr(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../erRange): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultEr'])
    @DefaultEr.setter
    def DefaultEr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DefaultEr'], value)

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
    def PortIdInterfaceName(self):
        """
        Returns
        -------
        - str: 
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
        - number: Pop-up used for configuring the port id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortIdSubType'])
    @PortIdSubType.setter
    def PortIdSubType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortIdSubType'], value)

    @property
    def SComponentMode(self):
        """
        Returns
        -------
        - str: This field is a dropdown that will indicate the behavior of S-Component negotiation -Disabled: no CDCP packets are sent, no VLANs are set on ER interface (only one ER can be associated to the EVB Station) -Disabled with CDCP: CDCP TLV sent has s-bit disabled and default (1/1) SCh-ID/SVID pair, no VLANs are set on ER interface (only one ER can be associated to the EVB Station) -Manual Config: no CDCP packets are set, ER interfaces will have SVID set manually -CDCP: CDCP TLVs will advertise the configured SChID/SVID (if SVID is 0, ERs expect SVID from bridge)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SComponentMode'])
    @SComponentMode.setter
    def SComponentMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SComponentMode'], value)

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

    def update(self, ChannelCapability=None, ChassisId=None, DefaultEr=None, Enabled=None, HoldTime=None, Name=None, PortIdInterfaceName=None, PortIdMacAddress=None, PortIdSubType=None, SComponentMode=None, TxDelay=None, TxInterval=None):
        """Updates evbStationRange resource on the server.

        Args
        ----
        - ChannelCapability (number): Advertised Channel Capability.
        - ChassisId (str): The Chassis ID that will be advertised in the mandatory LLDP TLVs.
        - DefaultEr (str(None | /api/v1/sessions/1/ixnetwork/vport/.../erRange)): 
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - HoldTime (number): Multiplier to get actual TTL value used in an LLDPDU.
        - Name (str): Name of range
        - PortIdInterfaceName (str): 
        - PortIdMacAddress (str): 
        - PortIdSubType (number): Pop-up used for configuring the port id.
        - SComponentMode (str): This field is a dropdown that will indicate the behavior of S-Component negotiation -Disabled: no CDCP packets are sent, no VLANs are set on ER interface (only one ER can be associated to the EVB Station) -Disabled with CDCP: CDCP TLV sent has s-bit disabled and default (1/1) SCh-ID/SVID pair, no VLANs are set on ER interface (only one ER can be associated to the EVB Station) -Manual Config: no CDCP packets are set, ER interfaces will have SVID set manually -CDCP: CDCP TLVs will advertise the configured SChID/SVID (if SVID is 0, ERs expect SVID from bridge)
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
