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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class LspPwRange(Base):
    """This object helps to configure the lsp pw range values.
    The LspPwRange class encapsulates a list of lspPwRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the LspPwRange.find() method.
    The list can be managed by using the LspPwRange.add() and LspPwRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "lspPwRange"
    _SDM_ATT_MAP = {
        "AlarmTrafficClass": "alarmTrafficClass",
        "AlarmType": "alarmType",
        "ApsTrafficClass": "apsTrafficClass",
        "ApsType": "apsType",
        "CccvInterval": "cccvInterval",
        "CccvTrafficClass": "cccvTrafficClass",
        "CccvType": "cccvType",
        "Description": "description",
        "DestAcId": "destAcId",
        "DestAcIdStep": "destAcIdStep",
        "DestGlobalId": "destGlobalId",
        "DestLspNumber": "destLspNumber",
        "DestLspNumberStep": "destLspNumberStep",
        "DestMepId": "destMepId",
        "DestMepIdStep": "destMepIdStep",
        "DestNodeId": "destNodeId",
        "DestTunnelNumber": "destTunnelNumber",
        "DestTunnelNumberStep": "destTunnelNumberStep",
        "DestVplsIdAsNumber": "destVplsIdAsNumber",
        "DestVplsIdAsNumberStep": "destVplsIdAsNumberStep",
        "DestVplsIdAssignedNumber": "destVplsIdAssignedNumber",
        "DestVplsIdAssignedNumberStep": "destVplsIdAssignedNumberStep",
        "DestVplsIdIpAddress": "destVplsIdIpAddress",
        "DestVplsIdIpAddressStep": "destVplsIdIpAddressStep",
        "DestVplsIdType": "destVplsIdType",
        "DmTimeFormat": "dmTimeFormat",
        "DmTrafficClass": "dmTrafficClass",
        "DmType": "dmType",
        "EnableVlan": "enableVlan",
        "Enabled": "enabled",
        "IpAddress": "ipAddress",
        "IpAddressMask": "ipAddressMask",
        "IpAddressStep": "ipAddressStep",
        "IpHostPerLsp": "ipHostPerLsp",
        "IpType": "ipType",
        "LmCounterType": "lmCounterType",
        "LmInitialRxValue": "lmInitialRxValue",
        "LmInitialTxValue": "lmInitialTxValue",
        "LmRxStep": "lmRxStep",
        "LmTrafficClass": "lmTrafficClass",
        "LmTxStep": "lmTxStep",
        "LmType": "lmType",
        "LspIncomingLabel": "lspIncomingLabel",
        "LspIncomingLabelStep": "lspIncomingLabelStep",
        "LspOutgoingLabel": "lspOutgoingLabel",
        "LspOutgoingLabelStep": "lspOutgoingLabelStep",
        "MacAddress": "macAddress",
        "MacPerPw": "macPerPw",
        "MegIdIntegerStep": "megIdIntegerStep",
        "MegIdPrefix": "megIdPrefix",
        "MegLevel": "megLevel",
        "MinRxInterval": "minRxInterval",
        "MinTxInterval": "minTxInterval",
        "NumberOfLsp": "numberOfLsp",
        "NumberOfPwPerLsp": "numberOfPwPerLsp",
        "OnDemandCvTrafficClass": "onDemandCvTrafficClass",
        "PeerLspOrPwRange": "peerLspOrPwRange",
        "PeerNestedLspPwRange": "peerNestedLspPwRange",
        "PwIncomingLabel": "pwIncomingLabel",
        "PwIncomingLabelStep": "pwIncomingLabelStep",
        "PwIncomingLabelStepAcrossLsp": "pwIncomingLabelStepAcrossLsp",
        "PwOutgoingLabel": "pwOutgoingLabel",
        "PwOutgoingLabelStep": "pwOutgoingLabelStep",
        "PwOutgoingLabelStepAcrossLsp": "pwOutgoingLabelStepAcrossLsp",
        "PwStatusFaultReplyInterval": "pwStatusFaultReplyInterval",
        "PwStatusTrafficClass": "pwStatusTrafficClass",
        "RangeRole": "rangeRole",
        "RepeatMac": "repeatMac",
        "Revertive": "revertive",
        "SkipZeroVlanId": "skipZeroVlanId",
        "SrcAcId": "srcAcId",
        "SrcAcIdStep": "srcAcIdStep",
        "SrcGlobalId": "srcGlobalId",
        "SrcLspNumber": "srcLspNumber",
        "SrcLspNumberStep": "srcLspNumberStep",
        "SrcMepId": "srcMepId",
        "SrcMepIdStep": "srcMepIdStep",
        "SrcNodeId": "srcNodeId",
        "SrcTunnelNumber": "srcTunnelNumber",
        "SrcTunnelNumberStep": "srcTunnelNumberStep",
        "SrcVplsIdAsNumber": "srcVplsIdAsNumber",
        "SrcVplsIdAsNumberStep": "srcVplsIdAsNumberStep",
        "SrcVplsIdAssignedNumber": "srcVplsIdAssignedNumber",
        "SrcVplsIdAssignedNumberStep": "srcVplsIdAssignedNumberStep",
        "SrcVplsIdIpAddress": "srcVplsIdIpAddress",
        "SrcVplsIdIpAddressStep": "srcVplsIdIpAddressStep",
        "SrcVplsIdType": "srcVplsIdType",
        "SupportSlowStart": "supportSlowStart",
        "TrafficGroupId": "trafficGroupId",
        "TypeOfProtectionSwitching": "typeOfProtectionSwitching",
        "TypeOfRange": "typeOfRange",
        "VlanCount": "vlanCount",
        "VlanId": "vlanId",
        "VlanIncrementMode": "vlanIncrementMode",
        "VlanPriority": "vlanPriority",
        "VlanTpId": "vlanTpId",
        "WaitToRevertTime": "waitToRevertTime",
    }
    _SDM_ENUM_MAP = {
        "alarmType": ["ietf", "y1731"],
        "apsType": ["ietf", "y1731"],
        "cccvType": ["bfdCc", "bfdCccv", "y1731", "none"],
        "destVplsIdType": ["asNumber", "ipAddress", "asNumber4Bytes"],
        "dmTimeFormat": ["ieee", "ntp"],
        "dmType": ["ietf", "y1731"],
        "ipType": ["ipv4", "ipv6"],
        "lmCounterType": ["32Bit", "64Bit"],
        "lmType": ["ietf", "y1731"],
        "rangeRole": ["none", "working", "protect"],
        "srcVplsIdType": ["asNumber", "ipAddress", "asNumber4Bytes"],
        "typeOfProtectionSwitching": [
            "1+1Unidirectional",
            "1:1Bidirectional",
            "1+1Bidirectional",
        ],
        "typeOfRange": ["lsp", "pw", "nestedLspPw"],
        "vlanIncrementMode": [
            "noIncrement",
            "parallelIncrement",
            "innerFirst",
            "outerFirst",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(LspPwRange, self).__init__(parent, list_op)

    @property
    def AlarmTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Alarm Traffic Class for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlarmTrafficClass"])

    @AlarmTrafficClass.setter
    def AlarmTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlarmTrafficClass"], value)

    @property
    def AlarmType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ietf | y1731): This signifies the Alarm Type. Possible values include IETF and Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlarmType"])

    @AlarmType.setter
    def AlarmType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlarmType"], value)

    @property
    def ApsTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Traffic Class of the APS message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsTrafficClass"])

    @ApsTrafficClass.setter
    def ApsTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApsTrafficClass"], value)

    @property
    def ApsType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ietf | y1731): This signifies the APS type. Possible values include IETF and Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsType"])

    @ApsType.setter
    def ApsType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApsType"], value)

    @property
    def CccvInterval(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This signifies the CCCV Interval in milliseconds.If cccv type is bfd then this field will take any value between 3-600000, if cccv type is y1731 then cccv interval can be configured to values available in the drop down menu.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CccvInterval"])

    @CccvInterval.setter
    def CccvInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CccvInterval"], value)

    @property
    def CccvTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the CCCV Traffic Class.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CccvTrafficClass"])

    @CccvTrafficClass.setter
    def CccvTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CccvTrafficClass"], value)

    @property
    def CccvType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bfdCc | bfdCccv | y1731 | none): This signifies the CCCV Type. Possible values include BFD CC, Y.1731 and None.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CccvType"])

    @CccvType.setter
    def CccvType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CccvType"], value)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the description of the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @Description.setter
    def Description(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Description"], value)

    @property
    def DestAcId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the destination AC id. This is the ac id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestAcId"])

    @DestAcId.setter
    def DestAcId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestAcId"], value)

    @property
    def DestAcIdStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the destination AC id step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestAcIdStep"])

    @DestAcIdStep.setter
    def DestAcIdStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestAcIdStep"], value)

    @property
    def DestGlobalId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the global id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestGlobalId"])

    @DestGlobalId.setter
    def DestGlobalId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestGlobalId"], value)

    @property
    def DestLspNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the lsp number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestLspNumber"])

    @DestLspNumber.setter
    def DestLspNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestLspNumber"], value)

    @property
    def DestLspNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the source LSP Number step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestLspNumberStep"])

    @DestLspNumberStep.setter
    def DestLspNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestLspNumberStep"], value)

    @property
    def DestMepId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the destination MEP Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestMepId"])

    @DestMepId.setter
    def DestMepId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestMepId"], value)

    @property
    def DestMepIdStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Destination MEP Id step value in integer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestMepIdStep"])

    @DestMepIdStep.setter
    def DestMepIdStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestMepIdStep"], value)

    @property
    def DestNodeId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the destination node id. This is the node id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestNodeId"])

    @DestNodeId.setter
    def DestNodeId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestNodeId"], value)

    @property
    def DestTunnelNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the tunnel number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestTunnelNumber"])

    @DestTunnelNumber.setter
    def DestTunnelNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestTunnelNumber"], value)

    @property
    def DestTunnelNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the destination tunnel number step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestTunnelNumberStep"])

    @DestTunnelNumberStep.setter
    def DestTunnelNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestTunnelNumberStep"], value)

    @property
    def DestVplsIdAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestVplsIdAsNumber"])

    @DestVplsIdAsNumber.setter
    def DestVplsIdAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestVplsIdAsNumber"], value)

    @property
    def DestVplsIdAsNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the step of destination vpls id AS number by which the AS number will be incremented if there are multiple LSP/PW in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestVplsIdAsNumberStep"])

    @DestVplsIdAsNumberStep.setter
    def DestVplsIdAsNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestVplsIdAsNumberStep"], value)

    @property
    def DestVplsIdAssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the destination VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber, the max value can be 4294967295.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestVplsIdAssignedNumber"])

    @DestVplsIdAssignedNumber.setter
    def DestVplsIdAssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestVplsIdAssignedNumber"], value)

    @property
    def DestVplsIdAssignedNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestVplsIdAssignedNumberStep"])

    @DestVplsIdAssignedNumberStep.setter
    def DestVplsIdAssignedNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestVplsIdAssignedNumberStep"], value)

    @property
    def DestVplsIdIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This specifies the IP Address configured as destination VPLS Id IP Address when VPLS Id type is set as ipAddress.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestVplsIdIpAddress"])

    @DestVplsIdIpAddress.setter
    def DestVplsIdIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestVplsIdIpAddress"], value)

    @property
    def DestVplsIdIpAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the step of ip address by which the ip address will be incremented if there are multiple LSP/PW in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestVplsIdIpAddressStep"])

    @DestVplsIdIpAddressStep.setter
    def DestVplsIdIpAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestVplsIdIpAddressStep"], value)

    @property
    def DestVplsIdType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(asNumber | ipAddress | asNumber4Bytes): This signifies the destination VplsId type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestVplsIdType"])

    @DestVplsIdType.setter
    def DestVplsIdType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestVplsIdType"], value)

    @property
    def DmTimeFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ieee | ntp): This signifies the DM Time Format. Possible values include IEEE and NTP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmTimeFormat"])

    @DmTimeFormat.setter
    def DmTimeFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmTimeFormat"], value)

    @property
    def DmTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the DM Traffic Class for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmTrafficClass"])

    @DmTrafficClass.setter
    def DmTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmTrafficClass"], value)

    @property
    def DmType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ietf | y1731): This signifies the DM Type. Possible values include IETF and Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmType"])

    @DmType.setter
    def DmType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmType"], value)

    @property
    def EnableVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the MAC Traffic will have a vlan header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVlan"])

    @EnableVlan.setter
    def EnableVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVlan"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of this LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def IpAddressMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the IP Address Mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressMask"])

    @IpAddressMask.setter
    def IpAddressMask(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressMask"], value)

    @property
    def IpAddressStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the IP Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressStep"])

    @IpAddressStep.setter
    def IpAddressStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressStep"], value)

    @property
    def IpHostPerLsp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the total number of IP hosts per lsp.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpHostPerLsp"])

    @IpHostPerLsp.setter
    def IpHostPerLsp(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpHostPerLsp"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4 | ipv6): This signifies the IP Type. Possible values include IPv4 and IPv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def LmCounterType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(32Bit | 64Bit): This signifies the LM Counter Type. Possible values include 32 Bit and 64 Bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmCounterType"])

    @LmCounterType.setter
    def LmCounterType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmCounterType"], value)

    @property
    def LmInitialRxValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Initial Rx value for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmInitialRxValue"])

    @LmInitialRxValue.setter
    def LmInitialRxValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmInitialRxValue"], value)

    @property
    def LmInitialTxValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Initial Tx value for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmInitialTxValue"])

    @LmInitialTxValue.setter
    def LmInitialTxValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmInitialTxValue"], value)

    @property
    def LmRxStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Rx step value for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmRxStep"])

    @LmRxStep.setter
    def LmRxStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmRxStep"], value)

    @property
    def LmTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Traffic Class.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmTrafficClass"])

    @LmTrafficClass.setter
    def LmTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmTrafficClass"], value)

    @property
    def LmTxStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LM Tx Step value for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmTxStep"])

    @LmTxStep.setter
    def LmTxStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmTxStep"], value)

    @property
    def LmType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ietf | y1731): This signifies the LM Type. Possible values include IETF and Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmType"])

    @LmType.setter
    def LmType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmType"], value)

    @property
    def LspIncomingLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LSP Incoming label value. All mpls-tp packets are expected to be received with this LSP label value, if there is a mismatch of this value with the peer's outgoing LSP label value, cccv sessions will not come up.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspIncomingLabel"])

    @LspIncomingLabel.setter
    def LspIncomingLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspIncomingLabel"], value)

    @property
    def LspIncomingLabelStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LSP Incoming Label Step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspIncomingLabelStep"])

    @LspIncomingLabelStep.setter
    def LspIncomingLabelStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspIncomingLabelStep"], value)

    @property
    def LspOutgoingLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LSP Outgoing Label value. All mpls-tp packets are transmitted with this LSP label from the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspOutgoingLabel"])

    @LspOutgoingLabel.setter
    def LspOutgoingLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspOutgoingLabel"], value)

    @property
    def LspOutgoingLabelStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the LSP Outgoing Label Step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspOutgoingLabelStep"])

    @LspOutgoingLabelStep.setter
    def LspOutgoingLabelStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspOutgoingLabelStep"], value)

    @property
    def MacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the starting MAC address of the range, this will be used for traffic generation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacAddress"])

    @MacAddress.setter
    def MacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacAddress"], value)

    @property
    def MacPerPw(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of MACs behind each PW, these are the MACs that are used for traffic generation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacPerPw"])

    @MacPerPw.setter
    def MacPerPw(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacPerPw"], value)

    @property
    def MegIdIntegerStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the MEG Id step value in integer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MegIdIntegerStep"])

    @MegIdIntegerStep.setter
    def MegIdIntegerStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MegIdIntegerStep"], value)

    @property
    def MegIdPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the prefix for the MEG Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MegIdPrefix"])

    @MegIdPrefix.setter
    def MegIdPrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MegIdPrefix"], value)

    @property
    def MegLevel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the peer range of the nested LSP PW value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MegLevel"])

    @MegLevel.setter
    def MegLevel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MegLevel"], value)

    @property
    def MinRxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the CCCV minimum receive interval of cc messages, in milliseconds. Not valid for cccv type y1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRxInterval"])

    @MinRxInterval.setter
    def MinRxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRxInterval"], value)

    @property
    def MinTxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the CCCV minimum transmit interval of cc messages, in milliseconds. Valid for all types of cccv.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinTxInterval"])

    @MinTxInterval.setter
    def MinTxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinTxInterval"], value)

    @property
    def NumberOfLsp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the total number of LSPs for this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfLsp"])

    @NumberOfLsp.setter
    def NumberOfLsp(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfLsp"], value)

    @property
    def NumberOfPwPerLsp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the total number of PWs per LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfPwPerLsp"])

    @NumberOfPwPerLsp.setter
    def NumberOfPwPerLsp(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfPwPerLsp"], value)

    @property
    def OnDemandCvTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the On Demand CV Traffic Class for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnDemandCvTrafficClass"])

    @OnDemandCvTrafficClass.setter
    def OnDemandCvTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnDemandCvTrafficClass"], value)

    @property
    def PeerLspOrPwRange(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange): This signifies the type of Peer LSP Or PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerLspOrPwRange"])

    @PeerLspOrPwRange.setter
    def PeerLspOrPwRange(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeerLspOrPwRange"], value)

    @property
    def PeerNestedLspPwRange(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange): This signifies the peer range of the nested LSP PW value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerNestedLspPwRange"])

    @PeerNestedLspPwRange.setter
    def PeerNestedLspPwRange(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeerNestedLspPwRange"], value)

    @property
    def PwIncomingLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Incoming Label value. All mpls-tp packets are expected to be received with this PW label value, if there is a mismatch of this value with the peer's outgoing PW label value, cccv sessions will not come up.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwIncomingLabel"])

    @PwIncomingLabel.setter
    def PwIncomingLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwIncomingLabel"], value)

    @property
    def PwIncomingLabelStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Incoming Label Step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwIncomingLabelStep"])

    @PwIncomingLabelStep.setter
    def PwIncomingLabelStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwIncomingLabelStep"], value)

    @property
    def PwIncomingLabelStepAcrossLsp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Incoming Label Step value across LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwIncomingLabelStepAcrossLsp"])

    @PwIncomingLabelStepAcrossLsp.setter
    def PwIncomingLabelStepAcrossLsp(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwIncomingLabelStepAcrossLsp"], value)

    @property
    def PwOutgoingLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Outgoing Label value. All mpls-tp packets are transmitted with this PW label from the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwOutgoingLabel"])

    @PwOutgoingLabel.setter
    def PwOutgoingLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwOutgoingLabel"], value)

    @property
    def PwOutgoingLabelStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Outgoing Label Step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwOutgoingLabelStep"])

    @PwOutgoingLabelStep.setter
    def PwOutgoingLabelStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwOutgoingLabelStep"], value)

    @property
    def PwOutgoingLabelStepAcrossLsp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Outgoing Label Step value across LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwOutgoingLabelStepAcrossLsp"])

    @PwOutgoingLabelStepAcrossLsp.setter
    def PwOutgoingLabelStepAcrossLsp(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwOutgoingLabelStepAcrossLsp"], value)

    @property
    def PwStatusFaultReplyInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Status Fault Reply Interval in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwStatusFaultReplyInterval"])

    @PwStatusFaultReplyInterval.setter
    def PwStatusFaultReplyInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwStatusFaultReplyInterval"], value)

    @property
    def PwStatusTrafficClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the PW Status Traffic Class for LSP PW Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PwStatusTrafficClass"])

    @PwStatusTrafficClass.setter
    def PwStatusTrafficClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PwStatusTrafficClass"], value)

    @property
    def RangeRole(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | working | protect): This signifies the role of the range. Possible values include None, Working and Protect.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeRole"])

    @RangeRole.setter
    def RangeRole(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeRole"], value)

    @property
    def RepeatMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, and the Count is greater than 1, the same address value will be repeated for all MAC addresses within a PW.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RepeatMac"])

    @RepeatMac.setter
    def RepeatMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RepeatMac"], value)

    @property
    def Revertive(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the switching mode, whether revertive or non-revertive.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Revertive"])

    @Revertive.setter
    def Revertive(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Revertive"], value)

    @property
    def SkipZeroVlanId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the VLAN Id 0 will not be used for any MAC.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SkipZeroVlanId"])

    @SkipZeroVlanId.setter
    def SkipZeroVlanId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SkipZeroVlanId"], value)

    @property
    def SrcAcId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the AC Id that is carried in the Echo Request message that is transmitted from this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcAcId"])

    @SrcAcId.setter
    def SrcAcId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcAcId"], value)

    @property
    def SrcAcIdStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the source AC id step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcAcIdStep"])

    @SrcAcIdStep.setter
    def SrcAcIdStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcAcIdStep"], value)

    @property
    def SrcGlobalId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the source global id. This is the global id that is carried in the Echo Request message that is transmitted from this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcGlobalId"])

    @SrcGlobalId.setter
    def SrcGlobalId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcGlobalId"], value)

    @property
    def SrcLspNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the lsp number that is carried in the Echo Request message that is transmitted from this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcLspNumber"])

    @SrcLspNumber.setter
    def SrcLspNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcLspNumber"], value)

    @property
    def SrcLspNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the source LSP Number step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcLspNumberStep"])

    @SrcLspNumberStep.setter
    def SrcLspNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcLspNumberStep"], value)

    @property
    def SrcMepId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the source MEP Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcMepId"])

    @SrcMepId.setter
    def SrcMepId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcMepId"], value)

    @property
    def SrcMepIdStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Source MEP Id step value in integer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcMepIdStep"])

    @SrcMepIdStep.setter
    def SrcMepIdStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcMepIdStep"], value)

    @property
    def SrcNodeId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the node id that is carried in the Echo Request message that is transmitted from this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcNodeId"])

    @SrcNodeId.setter
    def SrcNodeId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcNodeId"], value)

    @property
    def SrcTunnelNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the tunnel number that is carried in the Echo Request message that is transmitted from this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcTunnelNumber"])

    @SrcTunnelNumber.setter
    def SrcTunnelNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcTunnelNumber"], value)

    @property
    def SrcTunnelNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the source tunnel number step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcTunnelNumberStep"])

    @SrcTunnelNumberStep.setter
    def SrcTunnelNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcTunnelNumberStep"], value)

    @property
    def SrcVplsIdAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcVplsIdAsNumber"])

    @SrcVplsIdAsNumber.setter
    def SrcVplsIdAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcVplsIdAsNumber"], value)

    @property
    def SrcVplsIdAsNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the step of AS number by which the number is incremented if there are multiple LSP/PW in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcVplsIdAsNumberStep"])

    @SrcVplsIdAsNumberStep.setter
    def SrcVplsIdAsNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcVplsIdAsNumberStep"], value)

    @property
    def SrcVplsIdAssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the source VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber the max value can be 4294967295.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcVplsIdAssignedNumber"])

    @SrcVplsIdAssignedNumber.setter
    def SrcVplsIdAssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcVplsIdAssignedNumber"], value)

    @property
    def SrcVplsIdAssignedNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This specifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcVplsIdAssignedNumberStep"])

    @SrcVplsIdAssignedNumberStep.setter
    def SrcVplsIdAssignedNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcVplsIdAssignedNumberStep"], value)

    @property
    def SrcVplsIdIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the IP Address configured as Source VPLS Id IP Address when VPLS Id type is set as ipAddress.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcVplsIdIpAddress"])

    @SrcVplsIdIpAddress.setter
    def SrcVplsIdIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcVplsIdIpAddress"], value)

    @property
    def SrcVplsIdIpAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the step of ip address by which it is incremented if there are multiple LSP/PW in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcVplsIdIpAddressStep"])

    @SrcVplsIdIpAddressStep.setter
    def SrcVplsIdIpAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcVplsIdIpAddressStep"], value)

    @property
    def SrcVplsIdType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(asNumber | ipAddress | asNumber4Bytes): This specifies the source VplsId type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcVplsIdType"])

    @SrcVplsIdType.setter
    def SrcVplsIdType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcVplsIdType"], value)

    @property
    def SupportSlowStart(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: This signifies the Support Slow Start. This field is valid only for cccv type bfd and grayed out for y1731. If this is enabled then cccv interval for the peer is not matched for bfd session establishment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportSlowStart"])

    @SupportSlowStart.setter
    def SupportSlowStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportSlowStart"], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): This signifies the Traffic Group Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    @property
    def TypeOfProtectionSwitching(self):
        # type: () -> str
        """
        Returns
        -------
        - str(1+1Unidirectional | 1:1Bidirectional | 1+1Bidirectional): This signifies different types of protection switching mechanism.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypeOfProtectionSwitching"])

    @TypeOfProtectionSwitching.setter
    def TypeOfProtectionSwitching(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypeOfProtectionSwitching"], value)

    @property
    def TypeOfRange(self):
        # type: () -> str
        """
        Returns
        -------
        - str(lsp | pw | nestedLspPw): This signifies the type of range. Possible values include LSP, PW and Nested PW and LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypeOfRange"])

    @TypeOfRange.setter
    def TypeOfRange(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypeOfRange"], value)

    @property
    def VlanCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of VLANs configured for this MAC Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanCount"])

    @VlanCount.setter
    def VlanCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanCount"], value)

    @property
    def VlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the VLAN option is enabled for the current MAC Range and a VLAN Id may be added to the packet, to identify the VLAN that the packet belongs to.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanIncrementMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): This signifies the mode that defines how the VLAN will be incremented across MACs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanIncrementMode"])

    @VlanIncrementMode.setter
    def VlanIncrementMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanIncrementMode"], value)

    @property
    def VlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the user priority of the VLAN tag. This may have a value from 0 through 7.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    @property
    def VlanTpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the EtherType that identifies the protocol header that follows the VLAN header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanTpId"])

    @VlanTpId.setter
    def VlanTpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanTpId"], value)

    @property
    def WaitToRevertTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the duration after which data traffic will be switched from protect to working path once working path has recovered from signal fail. This is configurable only if Revertive is checked.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WaitToRevertTime"])

    @WaitToRevertTime.setter
    def WaitToRevertTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WaitToRevertTime"], value)

    def update(
        self,
        AlarmTrafficClass=None,
        AlarmType=None,
        ApsTrafficClass=None,
        ApsType=None,
        CccvInterval=None,
        CccvTrafficClass=None,
        CccvType=None,
        Description=None,
        DestAcId=None,
        DestAcIdStep=None,
        DestGlobalId=None,
        DestLspNumber=None,
        DestLspNumberStep=None,
        DestMepId=None,
        DestMepIdStep=None,
        DestNodeId=None,
        DestTunnelNumber=None,
        DestTunnelNumberStep=None,
        DestVplsIdAsNumber=None,
        DestVplsIdAsNumberStep=None,
        DestVplsIdAssignedNumber=None,
        DestVplsIdAssignedNumberStep=None,
        DestVplsIdIpAddress=None,
        DestVplsIdIpAddressStep=None,
        DestVplsIdType=None,
        DmTimeFormat=None,
        DmTrafficClass=None,
        DmType=None,
        EnableVlan=None,
        Enabled=None,
        IpAddress=None,
        IpAddressMask=None,
        IpAddressStep=None,
        IpHostPerLsp=None,
        IpType=None,
        LmCounterType=None,
        LmInitialRxValue=None,
        LmInitialTxValue=None,
        LmRxStep=None,
        LmTrafficClass=None,
        LmTxStep=None,
        LmType=None,
        LspIncomingLabel=None,
        LspIncomingLabelStep=None,
        LspOutgoingLabel=None,
        LspOutgoingLabelStep=None,
        MacAddress=None,
        MacPerPw=None,
        MegIdIntegerStep=None,
        MegIdPrefix=None,
        MegLevel=None,
        MinRxInterval=None,
        MinTxInterval=None,
        NumberOfLsp=None,
        NumberOfPwPerLsp=None,
        OnDemandCvTrafficClass=None,
        PeerLspOrPwRange=None,
        PeerNestedLspPwRange=None,
        PwIncomingLabel=None,
        PwIncomingLabelStep=None,
        PwIncomingLabelStepAcrossLsp=None,
        PwOutgoingLabel=None,
        PwOutgoingLabelStep=None,
        PwOutgoingLabelStepAcrossLsp=None,
        PwStatusFaultReplyInterval=None,
        PwStatusTrafficClass=None,
        RangeRole=None,
        RepeatMac=None,
        Revertive=None,
        SkipZeroVlanId=None,
        SrcAcId=None,
        SrcAcIdStep=None,
        SrcGlobalId=None,
        SrcLspNumber=None,
        SrcLspNumberStep=None,
        SrcMepId=None,
        SrcMepIdStep=None,
        SrcNodeId=None,
        SrcTunnelNumber=None,
        SrcTunnelNumberStep=None,
        SrcVplsIdAsNumber=None,
        SrcVplsIdAsNumberStep=None,
        SrcVplsIdAssignedNumber=None,
        SrcVplsIdAssignedNumberStep=None,
        SrcVplsIdIpAddress=None,
        SrcVplsIdIpAddressStep=None,
        SrcVplsIdType=None,
        SupportSlowStart=None,
        TrafficGroupId=None,
        TypeOfProtectionSwitching=None,
        TypeOfRange=None,
        VlanCount=None,
        VlanId=None,
        VlanIncrementMode=None,
        VlanPriority=None,
        VlanTpId=None,
        WaitToRevertTime=None,
    ):
        # type: (int, str, int, str, int, int, str, str, int, int, int, int, int, int, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, str, int, int, int, str, str, int, int, int, int, int, str, int, int, int, int, str, int, int, str, int, int, int, int, int, int, str, str, int, int, int, int, int, int, int, int, str, bool, bool, bool, int, int, int, int, int, int, int, int, int, int, int, int, int, int, str, str, str, bool, str, str, str, int, str, str, str, str, int) -> LspPwRange
        """Updates lspPwRange resource on the server.

        Args
        ----
        - AlarmTrafficClass (number): This signifies the Alarm Traffic Class for LSP PW Range.
        - AlarmType (str(ietf | y1731)): This signifies the Alarm Type. Possible values include IETF and Y.1731.
        - ApsTrafficClass (number): This signifies the Traffic Class of the APS message.
        - ApsType (str(ietf | y1731)): This signifies the APS type. Possible values include IETF and Y.1731.
        - CccvInterval (number): This signifies the CCCV Interval in milliseconds.If cccv type is bfd then this field will take any value between 3-600000, if cccv type is y1731 then cccv interval can be configured to values available in the drop down menu.
        - CccvTrafficClass (number): This signifies the CCCV Traffic Class.
        - CccvType (str(bfdCc | bfdCccv | y1731 | none)): This signifies the CCCV Type. Possible values include BFD CC, Y.1731 and None.
        - Description (str): This signifies the description of the range.
        - DestAcId (number): This signifies the destination AC id. This is the ac id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestAcIdStep (number): This signifies the destination AC id step value.
        - DestGlobalId (number): This signifies the global id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestLspNumber (number): This signifies the lsp number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestLspNumberStep (number): This signifies the source LSP Number step value.
        - DestMepId (number): This signifies the destination MEP Id.
        - DestMepIdStep (number): This signifies the Destination MEP Id step value in integer.
        - DestNodeId (number): This signifies the destination node id. This is the node id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestTunnelNumber (number): This signifies the tunnel number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestTunnelNumberStep (number): This signifies the destination tunnel number step value.
        - DestVplsIdAsNumber (number): This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        - DestVplsIdAsNumberStep (number): This signifies the step of destination vpls id AS number by which the AS number will be incremented if there are multiple LSP/PW in the range.
        - DestVplsIdAssignedNumber (number): This signifies the destination VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber, the max value can be 4294967295.
        - DestVplsIdAssignedNumberStep (number): This signifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        - DestVplsIdIpAddress (str): This specifies the IP Address configured as destination VPLS Id IP Address when VPLS Id type is set as ipAddress.
        - DestVplsIdIpAddressStep (str): This signifies the step of ip address by which the ip address will be incremented if there are multiple LSP/PW in the range.
        - DestVplsIdType (str(asNumber | ipAddress | asNumber4Bytes)): This signifies the destination VplsId type.
        - DmTimeFormat (str(ieee | ntp)): This signifies the DM Time Format. Possible values include IEEE and NTP.
        - DmTrafficClass (number): This signifies the DM Traffic Class for LSP PW Range.
        - DmType (str(ietf | y1731)): This signifies the DM Type. Possible values include IETF and Y.1731.
        - EnableVlan (bool): If true, the MAC Traffic will have a vlan header.
        - Enabled (bool): This signifies the enablement of this LSP PW Range.
        - IpAddress (str): This signifies the IP address.
        - IpAddressMask (number): This signifies the IP Address Mask.
        - IpAddressStep (number): This signifies the IP Address Step Value.
        - IpHostPerLsp (number): This signifies the total number of IP hosts per lsp.
        - IpType (str(ipv4 | ipv6)): This signifies the IP Type. Possible values include IPv4 and IPv6.
        - LmCounterType (str(32Bit | 64Bit)): This signifies the LM Counter Type. Possible values include 32 Bit and 64 Bit.
        - LmInitialRxValue (number): This signifies the LM Initial Rx value for LSP PW Range.
        - LmInitialTxValue (number): This signifies the LM Initial Tx value for LSP PW Range.
        - LmRxStep (number): This signifies the LM Rx step value for LSP PW Range.
        - LmTrafficClass (number): This signifies the LM Traffic Class.
        - LmTxStep (number): This signifies the LM Tx Step value for LSP PW Range.
        - LmType (str(ietf | y1731)): This signifies the LM Type. Possible values include IETF and Y.1731.
        - LspIncomingLabel (number): This signifies the LSP Incoming label value. All mpls-tp packets are expected to be received with this LSP label value, if there is a mismatch of this value with the peer's outgoing LSP label value, cccv sessions will not come up.
        - LspIncomingLabelStep (number): This signifies the LSP Incoming Label Step value.
        - LspOutgoingLabel (number): This signifies the LSP Outgoing Label value. All mpls-tp packets are transmitted with this LSP label from the port.
        - LspOutgoingLabelStep (number): This signifies the LSP Outgoing Label Step value.
        - MacAddress (str): This signifies the starting MAC address of the range, this will be used for traffic generation.
        - MacPerPw (number): This signifies the number of MACs behind each PW, these are the MACs that are used for traffic generation.
        - MegIdIntegerStep (number): This signifies the MEG Id step value in integer.
        - MegIdPrefix (str): This signifies the prefix for the MEG Id.
        - MegLevel (number): This signifies the peer range of the nested LSP PW value.
        - MinRxInterval (number): This signifies the CCCV minimum receive interval of cc messages, in milliseconds. Not valid for cccv type y1731.
        - MinTxInterval (number): This signifies the CCCV minimum transmit interval of cc messages, in milliseconds. Valid for all types of cccv.
        - NumberOfLsp (number): This signifies the total number of LSPs for this range.
        - NumberOfPwPerLsp (number): This signifies the total number of PWs per LSP.
        - OnDemandCvTrafficClass (number): This signifies the On Demand CV Traffic Class for LSP PW Range.
        - PeerLspOrPwRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange)): This signifies the type of Peer LSP Or PW Range.
        - PeerNestedLspPwRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange)): This signifies the peer range of the nested LSP PW value.
        - PwIncomingLabel (number): This signifies the PW Incoming Label value. All mpls-tp packets are expected to be received with this PW label value, if there is a mismatch of this value with the peer's outgoing PW label value, cccv sessions will not come up.
        - PwIncomingLabelStep (number): This signifies the PW Incoming Label Step value.
        - PwIncomingLabelStepAcrossLsp (number): This signifies the PW Incoming Label Step value across LSPs.
        - PwOutgoingLabel (number): This signifies the PW Outgoing Label value. All mpls-tp packets are transmitted with this PW label from the port.
        - PwOutgoingLabelStep (number): This signifies the PW Outgoing Label Step value.
        - PwOutgoingLabelStepAcrossLsp (number): This signifies the PW Outgoing Label Step value across LSPs.
        - PwStatusFaultReplyInterval (number): This signifies the PW Status Fault Reply Interval in seconds.
        - PwStatusTrafficClass (number): This signifies the PW Status Traffic Class for LSP PW Range.
        - RangeRole (str(none | working | protect)): This signifies the role of the range. Possible values include None, Working and Protect.
        - RepeatMac (bool): If true, and the Count is greater than 1, the same address value will be repeated for all MAC addresses within a PW.
        - Revertive (bool): This signifies the switching mode, whether revertive or non-revertive.
        - SkipZeroVlanId (bool): This signifies the VLAN Id 0 will not be used for any MAC.
        - SrcAcId (number): This signifies the AC Id that is carried in the Echo Request message that is transmitted from this port.
        - SrcAcIdStep (number): This signifies the source AC id step value.
        - SrcGlobalId (number): This signifies the source global id. This is the global id that is carried in the Echo Request message that is transmitted from this port.
        - SrcLspNumber (number): This signifies the lsp number that is carried in the Echo Request message that is transmitted from this port.
        - SrcLspNumberStep (number): This signifies the source LSP Number step value.
        - SrcMepId (number): This signifies the source MEP Id.
        - SrcMepIdStep (number): This signifies the Source MEP Id step value in integer.
        - SrcNodeId (number): This signifies the node id that is carried in the Echo Request message that is transmitted from this port.
        - SrcTunnelNumber (number): This signifies the tunnel number that is carried in the Echo Request message that is transmitted from this port.
        - SrcTunnelNumberStep (number): This signifies the source tunnel number step value.
        - SrcVplsIdAsNumber (number): This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        - SrcVplsIdAsNumberStep (number): This signifies the step of AS number by which the number is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdAssignedNumber (number): This signifies the source VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber the max value can be 4294967295.
        - SrcVplsIdAssignedNumberStep (number): This specifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdIpAddress (str): This signifies the IP Address configured as Source VPLS Id IP Address when VPLS Id type is set as ipAddress.
        - SrcVplsIdIpAddressStep (str): This signifies the step of ip address by which it is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdType (str(asNumber | ipAddress | asNumber4Bytes)): This specifies the source VplsId type.
        - SupportSlowStart (bool): This signifies the Support Slow Start. This field is valid only for cccv type bfd and grayed out for y1731. If this is enabled then cccv interval for the peer is not matched for bfd session establishment.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): This signifies the Traffic Group Id.
        - TypeOfProtectionSwitching (str(1+1Unidirectional | 1:1Bidirectional | 1+1Bidirectional)): This signifies different types of protection switching mechanism.
        - TypeOfRange (str(lsp | pw | nestedLspPw)): This signifies the type of range. Possible values include LSP, PW and Nested PW and LSP.
        - VlanCount (number): This signifies the number of VLANs configured for this MAC Range.
        - VlanId (str): This signifies the VLAN option is enabled for the current MAC Range and a VLAN Id may be added to the packet, to identify the VLAN that the packet belongs to.
        - VlanIncrementMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): This signifies the mode that defines how the VLAN will be incremented across MACs.
        - VlanPriority (str): This signifies the user priority of the VLAN tag. This may have a value from 0 through 7.
        - VlanTpId (str): This signifies the EtherType that identifies the protocol header that follows the VLAN header.
        - WaitToRevertTime (number): This signifies the duration after which data traffic will be switched from protect to working path once working path has recovered from signal fail. This is configurable only if Revertive is checked.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AlarmTrafficClass=None,
        AlarmType=None,
        ApsTrafficClass=None,
        ApsType=None,
        CccvInterval=None,
        CccvTrafficClass=None,
        CccvType=None,
        Description=None,
        DestAcId=None,
        DestAcIdStep=None,
        DestGlobalId=None,
        DestLspNumber=None,
        DestLspNumberStep=None,
        DestMepId=None,
        DestMepIdStep=None,
        DestNodeId=None,
        DestTunnelNumber=None,
        DestTunnelNumberStep=None,
        DestVplsIdAsNumber=None,
        DestVplsIdAsNumberStep=None,
        DestVplsIdAssignedNumber=None,
        DestVplsIdAssignedNumberStep=None,
        DestVplsIdIpAddress=None,
        DestVplsIdIpAddressStep=None,
        DestVplsIdType=None,
        DmTimeFormat=None,
        DmTrafficClass=None,
        DmType=None,
        EnableVlan=None,
        Enabled=None,
        IpAddress=None,
        IpAddressMask=None,
        IpAddressStep=None,
        IpHostPerLsp=None,
        IpType=None,
        LmCounterType=None,
        LmInitialRxValue=None,
        LmInitialTxValue=None,
        LmRxStep=None,
        LmTrafficClass=None,
        LmTxStep=None,
        LmType=None,
        LspIncomingLabel=None,
        LspIncomingLabelStep=None,
        LspOutgoingLabel=None,
        LspOutgoingLabelStep=None,
        MacAddress=None,
        MacPerPw=None,
        MegIdIntegerStep=None,
        MegIdPrefix=None,
        MegLevel=None,
        MinRxInterval=None,
        MinTxInterval=None,
        NumberOfLsp=None,
        NumberOfPwPerLsp=None,
        OnDemandCvTrafficClass=None,
        PeerLspOrPwRange=None,
        PeerNestedLspPwRange=None,
        PwIncomingLabel=None,
        PwIncomingLabelStep=None,
        PwIncomingLabelStepAcrossLsp=None,
        PwOutgoingLabel=None,
        PwOutgoingLabelStep=None,
        PwOutgoingLabelStepAcrossLsp=None,
        PwStatusFaultReplyInterval=None,
        PwStatusTrafficClass=None,
        RangeRole=None,
        RepeatMac=None,
        Revertive=None,
        SkipZeroVlanId=None,
        SrcAcId=None,
        SrcAcIdStep=None,
        SrcGlobalId=None,
        SrcLspNumber=None,
        SrcLspNumberStep=None,
        SrcMepId=None,
        SrcMepIdStep=None,
        SrcNodeId=None,
        SrcTunnelNumber=None,
        SrcTunnelNumberStep=None,
        SrcVplsIdAsNumber=None,
        SrcVplsIdAsNumberStep=None,
        SrcVplsIdAssignedNumber=None,
        SrcVplsIdAssignedNumberStep=None,
        SrcVplsIdIpAddress=None,
        SrcVplsIdIpAddressStep=None,
        SrcVplsIdType=None,
        SupportSlowStart=None,
        TrafficGroupId=None,
        TypeOfProtectionSwitching=None,
        TypeOfRange=None,
        VlanCount=None,
        VlanId=None,
        VlanIncrementMode=None,
        VlanPriority=None,
        VlanTpId=None,
        WaitToRevertTime=None,
    ):
        # type: (int, str, int, str, int, int, str, str, int, int, int, int, int, int, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, str, int, int, int, str, str, int, int, int, int, int, str, int, int, int, int, str, int, int, str, int, int, int, int, int, int, str, str, int, int, int, int, int, int, int, int, str, bool, bool, bool, int, int, int, int, int, int, int, int, int, int, int, int, int, int, str, str, str, bool, str, str, str, int, str, str, str, str, int) -> LspPwRange
        """Adds a new lspPwRange resource on the server and adds it to the container.

        Args
        ----
        - AlarmTrafficClass (number): This signifies the Alarm Traffic Class for LSP PW Range.
        - AlarmType (str(ietf | y1731)): This signifies the Alarm Type. Possible values include IETF and Y.1731.
        - ApsTrafficClass (number): This signifies the Traffic Class of the APS message.
        - ApsType (str(ietf | y1731)): This signifies the APS type. Possible values include IETF and Y.1731.
        - CccvInterval (number): This signifies the CCCV Interval in milliseconds.If cccv type is bfd then this field will take any value between 3-600000, if cccv type is y1731 then cccv interval can be configured to values available in the drop down menu.
        - CccvTrafficClass (number): This signifies the CCCV Traffic Class.
        - CccvType (str(bfdCc | bfdCccv | y1731 | none)): This signifies the CCCV Type. Possible values include BFD CC, Y.1731 and None.
        - Description (str): This signifies the description of the range.
        - DestAcId (number): This signifies the destination AC id. This is the ac id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestAcIdStep (number): This signifies the destination AC id step value.
        - DestGlobalId (number): This signifies the global id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestLspNumber (number): This signifies the lsp number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestLspNumberStep (number): This signifies the source LSP Number step value.
        - DestMepId (number): This signifies the destination MEP Id.
        - DestMepIdStep (number): This signifies the Destination MEP Id step value in integer.
        - DestNodeId (number): This signifies the destination node id. This is the node id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestTunnelNumber (number): This signifies the tunnel number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestTunnelNumberStep (number): This signifies the destination tunnel number step value.
        - DestVplsIdAsNumber (number): This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        - DestVplsIdAsNumberStep (number): This signifies the step of destination vpls id AS number by which the AS number will be incremented if there are multiple LSP/PW in the range.
        - DestVplsIdAssignedNumber (number): This signifies the destination VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber, the max value can be 4294967295.
        - DestVplsIdAssignedNumberStep (number): This signifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        - DestVplsIdIpAddress (str): This specifies the IP Address configured as destination VPLS Id IP Address when VPLS Id type is set as ipAddress.
        - DestVplsIdIpAddressStep (str): This signifies the step of ip address by which the ip address will be incremented if there are multiple LSP/PW in the range.
        - DestVplsIdType (str(asNumber | ipAddress | asNumber4Bytes)): This signifies the destination VplsId type.
        - DmTimeFormat (str(ieee | ntp)): This signifies the DM Time Format. Possible values include IEEE and NTP.
        - DmTrafficClass (number): This signifies the DM Traffic Class for LSP PW Range.
        - DmType (str(ietf | y1731)): This signifies the DM Type. Possible values include IETF and Y.1731.
        - EnableVlan (bool): If true, the MAC Traffic will have a vlan header.
        - Enabled (bool): This signifies the enablement of this LSP PW Range.
        - IpAddress (str): This signifies the IP address.
        - IpAddressMask (number): This signifies the IP Address Mask.
        - IpAddressStep (number): This signifies the IP Address Step Value.
        - IpHostPerLsp (number): This signifies the total number of IP hosts per lsp.
        - IpType (str(ipv4 | ipv6)): This signifies the IP Type. Possible values include IPv4 and IPv6.
        - LmCounterType (str(32Bit | 64Bit)): This signifies the LM Counter Type. Possible values include 32 Bit and 64 Bit.
        - LmInitialRxValue (number): This signifies the LM Initial Rx value for LSP PW Range.
        - LmInitialTxValue (number): This signifies the LM Initial Tx value for LSP PW Range.
        - LmRxStep (number): This signifies the LM Rx step value for LSP PW Range.
        - LmTrafficClass (number): This signifies the LM Traffic Class.
        - LmTxStep (number): This signifies the LM Tx Step value for LSP PW Range.
        - LmType (str(ietf | y1731)): This signifies the LM Type. Possible values include IETF and Y.1731.
        - LspIncomingLabel (number): This signifies the LSP Incoming label value. All mpls-tp packets are expected to be received with this LSP label value, if there is a mismatch of this value with the peer's outgoing LSP label value, cccv sessions will not come up.
        - LspIncomingLabelStep (number): This signifies the LSP Incoming Label Step value.
        - LspOutgoingLabel (number): This signifies the LSP Outgoing Label value. All mpls-tp packets are transmitted with this LSP label from the port.
        - LspOutgoingLabelStep (number): This signifies the LSP Outgoing Label Step value.
        - MacAddress (str): This signifies the starting MAC address of the range, this will be used for traffic generation.
        - MacPerPw (number): This signifies the number of MACs behind each PW, these are the MACs that are used for traffic generation.
        - MegIdIntegerStep (number): This signifies the MEG Id step value in integer.
        - MegIdPrefix (str): This signifies the prefix for the MEG Id.
        - MegLevel (number): This signifies the peer range of the nested LSP PW value.
        - MinRxInterval (number): This signifies the CCCV minimum receive interval of cc messages, in milliseconds. Not valid for cccv type y1731.
        - MinTxInterval (number): This signifies the CCCV minimum transmit interval of cc messages, in milliseconds. Valid for all types of cccv.
        - NumberOfLsp (number): This signifies the total number of LSPs for this range.
        - NumberOfPwPerLsp (number): This signifies the total number of PWs per LSP.
        - OnDemandCvTrafficClass (number): This signifies the On Demand CV Traffic Class for LSP PW Range.
        - PeerLspOrPwRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange)): This signifies the type of Peer LSP Or PW Range.
        - PeerNestedLspPwRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange)): This signifies the peer range of the nested LSP PW value.
        - PwIncomingLabel (number): This signifies the PW Incoming Label value. All mpls-tp packets are expected to be received with this PW label value, if there is a mismatch of this value with the peer's outgoing PW label value, cccv sessions will not come up.
        - PwIncomingLabelStep (number): This signifies the PW Incoming Label Step value.
        - PwIncomingLabelStepAcrossLsp (number): This signifies the PW Incoming Label Step value across LSPs.
        - PwOutgoingLabel (number): This signifies the PW Outgoing Label value. All mpls-tp packets are transmitted with this PW label from the port.
        - PwOutgoingLabelStep (number): This signifies the PW Outgoing Label Step value.
        - PwOutgoingLabelStepAcrossLsp (number): This signifies the PW Outgoing Label Step value across LSPs.
        - PwStatusFaultReplyInterval (number): This signifies the PW Status Fault Reply Interval in seconds.
        - PwStatusTrafficClass (number): This signifies the PW Status Traffic Class for LSP PW Range.
        - RangeRole (str(none | working | protect)): This signifies the role of the range. Possible values include None, Working and Protect.
        - RepeatMac (bool): If true, and the Count is greater than 1, the same address value will be repeated for all MAC addresses within a PW.
        - Revertive (bool): This signifies the switching mode, whether revertive or non-revertive.
        - SkipZeroVlanId (bool): This signifies the VLAN Id 0 will not be used for any MAC.
        - SrcAcId (number): This signifies the AC Id that is carried in the Echo Request message that is transmitted from this port.
        - SrcAcIdStep (number): This signifies the source AC id step value.
        - SrcGlobalId (number): This signifies the source global id. This is the global id that is carried in the Echo Request message that is transmitted from this port.
        - SrcLspNumber (number): This signifies the lsp number that is carried in the Echo Request message that is transmitted from this port.
        - SrcLspNumberStep (number): This signifies the source LSP Number step value.
        - SrcMepId (number): This signifies the source MEP Id.
        - SrcMepIdStep (number): This signifies the Source MEP Id step value in integer.
        - SrcNodeId (number): This signifies the node id that is carried in the Echo Request message that is transmitted from this port.
        - SrcTunnelNumber (number): This signifies the tunnel number that is carried in the Echo Request message that is transmitted from this port.
        - SrcTunnelNumberStep (number): This signifies the source tunnel number step value.
        - SrcVplsIdAsNumber (number): This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        - SrcVplsIdAsNumberStep (number): This signifies the step of AS number by which the number is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdAssignedNumber (number): This signifies the source VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber the max value can be 4294967295.
        - SrcVplsIdAssignedNumberStep (number): This specifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdIpAddress (str): This signifies the IP Address configured as Source VPLS Id IP Address when VPLS Id type is set as ipAddress.
        - SrcVplsIdIpAddressStep (str): This signifies the step of ip address by which it is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdType (str(asNumber | ipAddress | asNumber4Bytes)): This specifies the source VplsId type.
        - SupportSlowStart (bool): This signifies the Support Slow Start. This field is valid only for cccv type bfd and grayed out for y1731. If this is enabled then cccv interval for the peer is not matched for bfd session establishment.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): This signifies the Traffic Group Id.
        - TypeOfProtectionSwitching (str(1+1Unidirectional | 1:1Bidirectional | 1+1Bidirectional)): This signifies different types of protection switching mechanism.
        - TypeOfRange (str(lsp | pw | nestedLspPw)): This signifies the type of range. Possible values include LSP, PW and Nested PW and LSP.
        - VlanCount (number): This signifies the number of VLANs configured for this MAC Range.
        - VlanId (str): This signifies the VLAN option is enabled for the current MAC Range and a VLAN Id may be added to the packet, to identify the VLAN that the packet belongs to.
        - VlanIncrementMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): This signifies the mode that defines how the VLAN will be incremented across MACs.
        - VlanPriority (str): This signifies the user priority of the VLAN tag. This may have a value from 0 through 7.
        - VlanTpId (str): This signifies the EtherType that identifies the protocol header that follows the VLAN header.
        - WaitToRevertTime (number): This signifies the duration after which data traffic will be switched from protect to working path once working path has recovered from signal fail. This is configurable only if Revertive is checked.

        Returns
        -------
        - self: This instance with all currently retrieved lspPwRange resources using find and the newly added lspPwRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained lspPwRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AlarmTrafficClass=None,
        AlarmType=None,
        ApsTrafficClass=None,
        ApsType=None,
        CccvInterval=None,
        CccvTrafficClass=None,
        CccvType=None,
        Description=None,
        DestAcId=None,
        DestAcIdStep=None,
        DestGlobalId=None,
        DestLspNumber=None,
        DestLspNumberStep=None,
        DestMepId=None,
        DestMepIdStep=None,
        DestNodeId=None,
        DestTunnelNumber=None,
        DestTunnelNumberStep=None,
        DestVplsIdAsNumber=None,
        DestVplsIdAsNumberStep=None,
        DestVplsIdAssignedNumber=None,
        DestVplsIdAssignedNumberStep=None,
        DestVplsIdIpAddress=None,
        DestVplsIdIpAddressStep=None,
        DestVplsIdType=None,
        DmTimeFormat=None,
        DmTrafficClass=None,
        DmType=None,
        EnableVlan=None,
        Enabled=None,
        IpAddress=None,
        IpAddressMask=None,
        IpAddressStep=None,
        IpHostPerLsp=None,
        IpType=None,
        LmCounterType=None,
        LmInitialRxValue=None,
        LmInitialTxValue=None,
        LmRxStep=None,
        LmTrafficClass=None,
        LmTxStep=None,
        LmType=None,
        LspIncomingLabel=None,
        LspIncomingLabelStep=None,
        LspOutgoingLabel=None,
        LspOutgoingLabelStep=None,
        MacAddress=None,
        MacPerPw=None,
        MegIdIntegerStep=None,
        MegIdPrefix=None,
        MegLevel=None,
        MinRxInterval=None,
        MinTxInterval=None,
        NumberOfLsp=None,
        NumberOfPwPerLsp=None,
        OnDemandCvTrafficClass=None,
        PeerLspOrPwRange=None,
        PeerNestedLspPwRange=None,
        PwIncomingLabel=None,
        PwIncomingLabelStep=None,
        PwIncomingLabelStepAcrossLsp=None,
        PwOutgoingLabel=None,
        PwOutgoingLabelStep=None,
        PwOutgoingLabelStepAcrossLsp=None,
        PwStatusFaultReplyInterval=None,
        PwStatusTrafficClass=None,
        RangeRole=None,
        RepeatMac=None,
        Revertive=None,
        SkipZeroVlanId=None,
        SrcAcId=None,
        SrcAcIdStep=None,
        SrcGlobalId=None,
        SrcLspNumber=None,
        SrcLspNumberStep=None,
        SrcMepId=None,
        SrcMepIdStep=None,
        SrcNodeId=None,
        SrcTunnelNumber=None,
        SrcTunnelNumberStep=None,
        SrcVplsIdAsNumber=None,
        SrcVplsIdAsNumberStep=None,
        SrcVplsIdAssignedNumber=None,
        SrcVplsIdAssignedNumberStep=None,
        SrcVplsIdIpAddress=None,
        SrcVplsIdIpAddressStep=None,
        SrcVplsIdType=None,
        SupportSlowStart=None,
        TrafficGroupId=None,
        TypeOfProtectionSwitching=None,
        TypeOfRange=None,
        VlanCount=None,
        VlanId=None,
        VlanIncrementMode=None,
        VlanPriority=None,
        VlanTpId=None,
        WaitToRevertTime=None,
    ):
        # type: (int, str, int, str, int, int, str, str, int, int, int, int, int, int, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, str, int, int, int, str, str, int, int, int, int, int, str, int, int, int, int, str, int, int, str, int, int, int, int, int, int, str, str, int, int, int, int, int, int, int, int, str, bool, bool, bool, int, int, int, int, int, int, int, int, int, int, int, int, int, int, str, str, str, bool, str, str, str, int, str, str, str, str, int) -> LspPwRange
        """Finds and retrieves lspPwRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lspPwRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lspPwRange resources from the server.

        Args
        ----
        - AlarmTrafficClass (number): This signifies the Alarm Traffic Class for LSP PW Range.
        - AlarmType (str(ietf | y1731)): This signifies the Alarm Type. Possible values include IETF and Y.1731.
        - ApsTrafficClass (number): This signifies the Traffic Class of the APS message.
        - ApsType (str(ietf | y1731)): This signifies the APS type. Possible values include IETF and Y.1731.
        - CccvInterval (number): This signifies the CCCV Interval in milliseconds.If cccv type is bfd then this field will take any value between 3-600000, if cccv type is y1731 then cccv interval can be configured to values available in the drop down menu.
        - CccvTrafficClass (number): This signifies the CCCV Traffic Class.
        - CccvType (str(bfdCc | bfdCccv | y1731 | none)): This signifies the CCCV Type. Possible values include BFD CC, Y.1731 and None.
        - Description (str): This signifies the description of the range.
        - DestAcId (number): This signifies the destination AC id. This is the ac id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestAcIdStep (number): This signifies the destination AC id step value.
        - DestGlobalId (number): This signifies the global id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestLspNumber (number): This signifies the lsp number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestLspNumberStep (number): This signifies the source LSP Number step value.
        - DestMepId (number): This signifies the destination MEP Id.
        - DestMepIdStep (number): This signifies the Destination MEP Id step value in integer.
        - DestNodeId (number): This signifies the destination node id. This is the node id that is expected on the peer, if there is a mismatch with the one configured on the peer LSP/PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestTunnelNumber (number): This signifies the tunnel number that is expected on the peer, if there is a mismatch with the one configured on the peer LSP or PW, On Demand Ping and On Demand Traceroute will result in failure.
        - DestTunnelNumberStep (number): This signifies the destination tunnel number step value.
        - DestVplsIdAsNumber (number): This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        - DestVplsIdAsNumberStep (number): This signifies the step of destination vpls id AS number by which the AS number will be incremented if there are multiple LSP/PW in the range.
        - DestVplsIdAssignedNumber (number): This signifies the destination VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber, the max value can be 4294967295.
        - DestVplsIdAssignedNumberStep (number): This signifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        - DestVplsIdIpAddress (str): This specifies the IP Address configured as destination VPLS Id IP Address when VPLS Id type is set as ipAddress.
        - DestVplsIdIpAddressStep (str): This signifies the step of ip address by which the ip address will be incremented if there are multiple LSP/PW in the range.
        - DestVplsIdType (str(asNumber | ipAddress | asNumber4Bytes)): This signifies the destination VplsId type.
        - DmTimeFormat (str(ieee | ntp)): This signifies the DM Time Format. Possible values include IEEE and NTP.
        - DmTrafficClass (number): This signifies the DM Traffic Class for LSP PW Range.
        - DmType (str(ietf | y1731)): This signifies the DM Type. Possible values include IETF and Y.1731.
        - EnableVlan (bool): If true, the MAC Traffic will have a vlan header.
        - Enabled (bool): This signifies the enablement of this LSP PW Range.
        - IpAddress (str): This signifies the IP address.
        - IpAddressMask (number): This signifies the IP Address Mask.
        - IpAddressStep (number): This signifies the IP Address Step Value.
        - IpHostPerLsp (number): This signifies the total number of IP hosts per lsp.
        - IpType (str(ipv4 | ipv6)): This signifies the IP Type. Possible values include IPv4 and IPv6.
        - LmCounterType (str(32Bit | 64Bit)): This signifies the LM Counter Type. Possible values include 32 Bit and 64 Bit.
        - LmInitialRxValue (number): This signifies the LM Initial Rx value for LSP PW Range.
        - LmInitialTxValue (number): This signifies the LM Initial Tx value for LSP PW Range.
        - LmRxStep (number): This signifies the LM Rx step value for LSP PW Range.
        - LmTrafficClass (number): This signifies the LM Traffic Class.
        - LmTxStep (number): This signifies the LM Tx Step value for LSP PW Range.
        - LmType (str(ietf | y1731)): This signifies the LM Type. Possible values include IETF and Y.1731.
        - LspIncomingLabel (number): This signifies the LSP Incoming label value. All mpls-tp packets are expected to be received with this LSP label value, if there is a mismatch of this value with the peer's outgoing LSP label value, cccv sessions will not come up.
        - LspIncomingLabelStep (number): This signifies the LSP Incoming Label Step value.
        - LspOutgoingLabel (number): This signifies the LSP Outgoing Label value. All mpls-tp packets are transmitted with this LSP label from the port.
        - LspOutgoingLabelStep (number): This signifies the LSP Outgoing Label Step value.
        - MacAddress (str): This signifies the starting MAC address of the range, this will be used for traffic generation.
        - MacPerPw (number): This signifies the number of MACs behind each PW, these are the MACs that are used for traffic generation.
        - MegIdIntegerStep (number): This signifies the MEG Id step value in integer.
        - MegIdPrefix (str): This signifies the prefix for the MEG Id.
        - MegLevel (number): This signifies the peer range of the nested LSP PW value.
        - MinRxInterval (number): This signifies the CCCV minimum receive interval of cc messages, in milliseconds. Not valid for cccv type y1731.
        - MinTxInterval (number): This signifies the CCCV minimum transmit interval of cc messages, in milliseconds. Valid for all types of cccv.
        - NumberOfLsp (number): This signifies the total number of LSPs for this range.
        - NumberOfPwPerLsp (number): This signifies the total number of PWs per LSP.
        - OnDemandCvTrafficClass (number): This signifies the On Demand CV Traffic Class for LSP PW Range.
        - PeerLspOrPwRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange)): This signifies the type of Peer LSP Or PW Range.
        - PeerNestedLspPwRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocols/mplsTp/router/interface/lspPwRange)): This signifies the peer range of the nested LSP PW value.
        - PwIncomingLabel (number): This signifies the PW Incoming Label value. All mpls-tp packets are expected to be received with this PW label value, if there is a mismatch of this value with the peer's outgoing PW label value, cccv sessions will not come up.
        - PwIncomingLabelStep (number): This signifies the PW Incoming Label Step value.
        - PwIncomingLabelStepAcrossLsp (number): This signifies the PW Incoming Label Step value across LSPs.
        - PwOutgoingLabel (number): This signifies the PW Outgoing Label value. All mpls-tp packets are transmitted with this PW label from the port.
        - PwOutgoingLabelStep (number): This signifies the PW Outgoing Label Step value.
        - PwOutgoingLabelStepAcrossLsp (number): This signifies the PW Outgoing Label Step value across LSPs.
        - PwStatusFaultReplyInterval (number): This signifies the PW Status Fault Reply Interval in seconds.
        - PwStatusTrafficClass (number): This signifies the PW Status Traffic Class for LSP PW Range.
        - RangeRole (str(none | working | protect)): This signifies the role of the range. Possible values include None, Working and Protect.
        - RepeatMac (bool): If true, and the Count is greater than 1, the same address value will be repeated for all MAC addresses within a PW.
        - Revertive (bool): This signifies the switching mode, whether revertive or non-revertive.
        - SkipZeroVlanId (bool): This signifies the VLAN Id 0 will not be used for any MAC.
        - SrcAcId (number): This signifies the AC Id that is carried in the Echo Request message that is transmitted from this port.
        - SrcAcIdStep (number): This signifies the source AC id step value.
        - SrcGlobalId (number): This signifies the source global id. This is the global id that is carried in the Echo Request message that is transmitted from this port.
        - SrcLspNumber (number): This signifies the lsp number that is carried in the Echo Request message that is transmitted from this port.
        - SrcLspNumberStep (number): This signifies the source LSP Number step value.
        - SrcMepId (number): This signifies the source MEP Id.
        - SrcMepIdStep (number): This signifies the Source MEP Id step value in integer.
        - SrcNodeId (number): This signifies the node id that is carried in the Echo Request message that is transmitted from this port.
        - SrcTunnelNumber (number): This signifies the tunnel number that is carried in the Echo Request message that is transmitted from this port.
        - SrcTunnelNumberStep (number): This signifies the source tunnel number step value.
        - SrcVplsIdAsNumber (number): This signifies the AS Number configured as Source VPLS Id AS Number when VPLS Id type is set as asNumber or asNumber4Bytes. If it is asNumber then the max AS Number can be 65535 and when it is asNumber4Bytes the max value can be 4294967295.
        - SrcVplsIdAsNumberStep (number): This signifies the step of AS number by which the number is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdAssignedNumber (number): This signifies the source VPLS Id Assigned Number. If the VPLS Id type is configured as either ipAddress or asNumber4Bytes then the max Assigned Number can be 65535 and when it is asNumber the max value can be 4294967295.
        - SrcVplsIdAssignedNumberStep (number): This specifies the step of Assigned number by which the number is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdIpAddress (str): This signifies the IP Address configured as Source VPLS Id IP Address when VPLS Id type is set as ipAddress.
        - SrcVplsIdIpAddressStep (str): This signifies the step of ip address by which it is incremented if there are multiple LSP/PW in the range.
        - SrcVplsIdType (str(asNumber | ipAddress | asNumber4Bytes)): This specifies the source VplsId type.
        - SupportSlowStart (bool): This signifies the Support Slow Start. This field is valid only for cccv type bfd and grayed out for y1731. If this is enabled then cccv interval for the peer is not matched for bfd session establishment.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): This signifies the Traffic Group Id.
        - TypeOfProtectionSwitching (str(1+1Unidirectional | 1:1Bidirectional | 1+1Bidirectional)): This signifies different types of protection switching mechanism.
        - TypeOfRange (str(lsp | pw | nestedLspPw)): This signifies the type of range. Possible values include LSP, PW and Nested PW and LSP.
        - VlanCount (number): This signifies the number of VLANs configured for this MAC Range.
        - VlanId (str): This signifies the VLAN option is enabled for the current MAC Range and a VLAN Id may be added to the packet, to identify the VLAN that the packet belongs to.
        - VlanIncrementMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): This signifies the mode that defines how the VLAN will be incremented across MACs.
        - VlanPriority (str): This signifies the user priority of the VLAN tag. This may have a value from 0 through 7.
        - VlanTpId (str): This signifies the EtherType that identifies the protocol header that follows the VLAN header.
        - WaitToRevertTime (number): This signifies the duration after which data traffic will be switched from protect to working path once working path has recovered from signal fail. This is configurable only if Revertive is checked.

        Returns
        -------
        - self: This instance with matching lspPwRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lspPwRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lspPwRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
