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


class L2VcRange(Base):
    """This object holds information about a VC range to be associated with an LDP L2 VPN interface.
    The L2VcRange class encapsulates a list of l2VcRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2VcRange.find() method.
    The list can be managed by using the L2VcRange.add() and L2VcRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2VcRange'

    def __init__(self, parent):
        super(L2VcRange, self).__init__(parent)

    @property
    def L2MacVlanRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2macvlanrange_5a4764ecb2090c3cb5bf1f57bd41a9a7.L2MacVlanRange): An instance of the L2MacVlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2macvlanrange_5a4764ecb2090c3cb5bf1f57bd41a9a7 import L2MacVlanRange
        return L2MacVlanRange(self)._select()

    @property
    def L2VcIpRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vciprange_4d188f24f6d2bfb72e746757f1210344.L2VcIpRange): An instance of the L2VcIpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vciprange_4d188f24f6d2bfb72e746757f1210344 import L2VcIpRange
        return L2VcIpRange(self)._select()

    @property
    def CapableOfReassembly(self):
        """
        Returns
        -------
        - bool: If enabled, makes the interface capable of reassembly.
        """
        return self._get_attribute('capableOfReassembly')
    @CapableOfReassembly.setter
    def CapableOfReassembly(self, value):
        self._set_attribute('capableOfReassembly', value)

    @property
    def Cas(self):
        """
        Returns
        -------
        - str(e1Trunk | t1EsfTrunk | t1SfTrunk): It signifies the CAS value.
        """
        return self._get_attribute('cas')
    @Cas.setter
    def Cas(self, value):
        self._set_attribute('cas', value)

    @property
    def CeIpAddress(self):
        """
        Returns
        -------
        - str: The IP address of attached CE endpoint. If IP Type is set to Ipv4, then the default is 0.0.0.0, and if the IP type is set to Ipv6, then the default is 0:0:0:0:0:0:0:0.
        """
        return self._get_attribute('ceIpAddress')
    @CeIpAddress.setter
    def CeIpAddress(self, value):
        self._set_attribute('ceIpAddress', value)

    @property
    def CemOption(self):
        """
        Returns
        -------
        - number: The value of the CEM option.
        """
        return self._get_attribute('cemOption')
    @CemOption.setter
    def CemOption(self, value):
        self._set_attribute('cemOption', value)

    @property
    def CemPayload(self):
        """
        Returns
        -------
        - number: If enabled, indicates that there is a Circuit Emulation Service over MPLS (CEM) payload.
        """
        return self._get_attribute('cemPayload')
    @CemPayload.setter
    def CemPayload(self, value):
        self._set_attribute('cemPayload', value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: (In octets) The 8-bit VC information Length field. It indicates the length of the (2-octet) VC ID field plus combined length of all of the parameters in the VC FEC element.
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        """
        return self._get_attribute('description')
    @Description.setter
    def Description(self, value):
        self._set_attribute('description', value)

    @property
    def DoNotExpandIntoVcs(self):
        """
        Returns
        -------
        - bool: If true, the VC ranges do not expand into individual VCs.
        """
        return self._get_attribute('doNotExpandIntoVcs')
    @DoNotExpandIntoVcs.setter
    def DoNotExpandIntoVcs(self, value):
        self._set_attribute('doNotExpandIntoVcs', value)

    @property
    def DownInterval(self):
        """
        Returns
        -------
        - number: Time interval for which the PW status will remain down. (Default= 60 seconds)
        """
        return self._get_attribute('downInterval')
    @DownInterval.setter
    def DownInterval(self, value):
        self._set_attribute('downInterval', value)

    @property
    def DownStartInterval(self):
        """
        Returns
        -------
        - number: The duration in time after session becomes up and a notification message being sent to make the session down. (Default= 30 seconds)
        """
        return self._get_attribute('downStartInterval')
    @DownStartInterval.setter
    def DownStartInterval(self, value):
        self._set_attribute('downStartInterval', value)

    @property
    def EnableBfdIpUdpCv(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableBfdIpUdpCv')
    @EnableBfdIpUdpCv.setter
    def EnableBfdIpUdpCv(self, value):
        self._set_attribute('enableBfdIpUdpCv', value)

    @property
    def EnableBfdPwAchCv(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableBfdPwAchCv')
    @EnableBfdPwAchCv.setter
    def EnableBfdPwAchCv(self, value):
        self._set_attribute('enableBfdPwAchCv', value)

    @property
    def EnableCBit(self):
        """
        Returns
        -------
        - bool: Controls generation of the control word.
        """
        return self._get_attribute('enableCBit')
    @EnableCBit.setter
    def EnableCBit(self, value):
        self._set_attribute('enableCBit', value)

    @property
    def EnableCccvNegotiation(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableCccvNegotiation')
    @EnableCccvNegotiation.setter
    def EnableCccvNegotiation(self, value):
        self._set_attribute('enableCccvNegotiation', value)

    @property
    def EnableCemOption(self):
        """
        Returns
        -------
        - bool: Enable the Circuit Emulation over MPLS option, for encapsulation of TDM signals.
        """
        return self._get_attribute('enableCemOption')
    @EnableCemOption.setter
    def EnableCemOption(self, value):
        self._set_attribute('enableCemOption', value)

    @property
    def EnableCemPayload(self):
        """
        Returns
        -------
        - bool: Enable the Circuit Emulation over MPLS payload.
        """
        return self._get_attribute('enableCemPayload')
    @EnableCemPayload.setter
    def EnableCemPayload(self, value):
        self._set_attribute('enableCemPayload', value)

    @property
    def EnableDescriptionPresent(self):
        """
        Returns
        -------
        - bool: If enabled, indicates that an optional interface description is present.
        """
        return self._get_attribute('enableDescriptionPresent')
    @EnableDescriptionPresent.setter
    def EnableDescriptionPresent(self, value):
        self._set_attribute('enableDescriptionPresent', value)

    @property
    def EnableLspPingCv(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableLspPingCv')
    @EnableLspPingCv.setter
    def EnableLspPingCv(self, value):
        self._set_attribute('enableLspPingCv', value)

    @property
    def EnableMaxAtmPresent(self):
        """
        Returns
        -------
        - bool: Enables the generation of an interface parameter field with the maximum number of concatenated ATM cells. (default = 0)
        """
        return self._get_attribute('enableMaxAtmPresent')
    @EnableMaxAtmPresent.setter
    def EnableMaxAtmPresent(self, value):
        self._set_attribute('enableMaxAtmPresent', value)

    @property
    def EnableMtuPresent(self):
        """
        Returns
        -------
        - bool: This attribute enables the generation of an MTU interface parameter field.
        """
        return self._get_attribute('enableMtuPresent')
    @EnableMtuPresent.setter
    def EnableMtuPresent(self, value):
        self._set_attribute('enableMtuPresent', value)

    @property
    def EnablePacking(self):
        """
        Returns
        -------
        - bool: (For L2 VC FEC ranges and in Unsolicited Label Distribution Mode ONLY.) If enabled, L2 VC FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        """
        return self._get_attribute('enablePacking')
    @EnablePacking.setter
    def EnablePacking(self, value):
        self._set_attribute('enablePacking', value)

    @property
    def EnablePwAchCc(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enablePwAchCc')
    @EnablePwAchCc.setter
    def EnablePwAchCc(self, value):
        self._set_attribute('enablePwAchCc', value)

    @property
    def EnablePwStatusTlv(self):
        """
        Returns
        -------
        - bool: If checked, this enables the use of PW status TLV in notification messages to notify the PW status.
        """
        return self._get_attribute('enablePwStatusTlv')
    @EnablePwStatusTlv.setter
    def EnablePwStatusTlv(self, value):
        self._set_attribute('enablePwStatusTlv', value)

    @property
    def EnableRouterAlertCc(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableRouterAlertCc')
    @EnableRouterAlertCc.setter
    def EnableRouterAlertCc(self, value):
        self._set_attribute('enableRouterAlertCc', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables use of this VC range.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FecType(self):
        """
        Returns
        -------
        - str(pwIdFec | generalizedIdFecVpls): The FEC type. The options are: PW Id FEC 0x80, Generalized Id FEC 0x81 VPLS.
        """
        return self._get_attribute('fecType')
    @FecType.setter
    def FecType(self, value):
        self._set_attribute('fecType', value)

    @property
    def Frequency(self):
        """
        Returns
        -------
        - number: It is the frequency.
        """
        return self._get_attribute('frequency')
    @Frequency.setter
    def Frequency(self, value):
        self._set_attribute('frequency', value)

    @property
    def IncludeRtpHeader(self):
        """
        Returns
        -------
        - bool: If true, includes the RTP header.
        """
        return self._get_attribute('includeRtpHeader')
    @IncludeRtpHeader.setter
    def IncludeRtpHeader(self, value):
        self._set_attribute('includeRtpHeader', value)

    @property
    def IncludeSsrc(self):
        """
        Returns
        -------
        - bool: If true, enables SSRC.
        """
        return self._get_attribute('includeSsrc')
    @IncludeSsrc.setter
    def IncludeSsrc(self, value):
        self._set_attribute('includeSsrc', value)

    @property
    def IncludeTdmBitrate(self):
        """
        Returns
        -------
        - bool: If true, enables TDM bit rate.
        """
        return self._get_attribute('includeTdmBitrate')
    @IncludeTdmBitrate.setter
    def IncludeTdmBitrate(self, value):
        self._set_attribute('includeTdmBitrate', value)

    @property
    def IncludeTdmOption(self):
        """
        Returns
        -------
        - bool: If true, includes the TDM option.
        """
        return self._get_attribute('includeTdmOption')
    @IncludeTdmOption.setter
    def IncludeTdmOption(self, value):
        self._set_attribute('includeTdmOption', value)

    @property
    def IncludeTdmPayload(self):
        """
        Returns
        -------
        - bool: If true, enables TDM payload.
        """
        return self._get_attribute('includeTdmPayload')
    @IncludeTdmPayload.setter
    def IncludeTdmPayload(self, value):
        self._set_attribute('includeTdmPayload', value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - number: The type (IPv4 or IPv6) of the neighbor.
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def LabelMode(self):
        """
        Returns
        -------
        - str(none | increment): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        """
        return self._get_attribute('labelMode')
    @LabelMode.setter
    def LabelMode(self, value):
        self._set_attribute('labelMode', value)

    @property
    def LabelStart(self):
        """
        Returns
        -------
        - number: The first label in the range of labels. The default is 16.
        """
        return self._get_attribute('labelStart')
    @LabelStart.setter
    def LabelStart(self, value):
        self._set_attribute('labelStart', value)

    @property
    def MaxNumberOfAtmCells(self):
        """
        Returns
        -------
        - number: The maximum number of ATM cells which may be concatenated and sent in a single MPLS frame. This parameter is part of the FEC element.
        """
        return self._get_attribute('maxNumberOfAtmCells')
    @MaxNumberOfAtmCells.setter
    def MaxNumberOfAtmCells(self, value):
        self._set_attribute('maxNumberOfAtmCells', value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: (in octets) The 2-octet value for the maximum Transmission Unit (MTU).
        """
        return self._get_attribute('mtu')
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute('mtu', value)

    @property
    def PayloadType(self):
        """
        Returns
        -------
        - number: It is the payload type.
        """
        return self._get_attribute('payloadType')
    @PayloadType.setter
    def PayloadType(self, value):
        self._set_attribute('payloadType', value)

    @property
    def PeerAddress(self):
        """
        Returns
        -------
        - str: The IPv4 address of the LDP router which is the peer for this VC range.
        """
        return self._get_attribute('peerAddress')
    @PeerAddress.setter
    def PeerAddress(self, value):
        self._set_attribute('peerAddress', value)

    @property
    def ProvisioningModel(self):
        """
        Returns
        -------
        - str(manualConfiguration | bgpAutoDiscovery): Editable dropdown to denote the Provisioning Model.
        """
        return self._get_attribute('provisioningModel')
    @ProvisioningModel.setter
    def ProvisioningModel(self, value):
        self._set_attribute('provisioningModel', value)

    @property
    def PwStatusCode(self):
        """
        Returns
        -------
        - number: This is an editable dropdown to denote the PW status. This field is editable. The range is from 0x00000001 - 0xFFFFFFFF.
        """
        return self._get_attribute('pwStatusCode')
    @PwStatusCode.setter
    def PwStatusCode(self, value):
        self._set_attribute('pwStatusCode', value)

    @property
    def RepeatCount(self):
        """
        Returns
        -------
        - number: The number of times to repeat the above processes. The default is 1.
        """
        return self._get_attribute('repeatCount')
    @RepeatCount.setter
    def RepeatCount(self, value):
        self._set_attribute('repeatCount', value)

    @property
    def SendPwStatus(self):
        """
        Returns
        -------
        - bool: If checked, it signifies whether to send a notification message with a PW status for the corresponding PW.
        """
        return self._get_attribute('sendPwStatus')
    @SendPwStatus.setter
    def SendPwStatus(self, value):
        self._set_attribute('sendPwStatus', value)

    @property
    def SourceAiiAsIp(self):
        """
        Returns
        -------
        - str: The IP address.
        """
        return self._get_attribute('sourceAiiAsIp')
    @SourceAiiAsIp.setter
    def SourceAiiAsIp(self, value):
        self._set_attribute('sourceAiiAsIp', value)

    @property
    def SourceAiiAsNumber(self):
        """
        Returns
        -------
        - number: The numerical value indicating the AS of the Source AII.
        """
        return self._get_attribute('sourceAiiAsNumber')
    @SourceAiiAsNumber.setter
    def SourceAiiAsNumber(self, value):
        self._set_attribute('sourceAiiAsNumber', value)

    @property
    def SourceAiiType(self):
        """
        Returns
        -------
        - str(number | ipAddress): Editable dropdown. The options are: AS, IP.
        """
        return self._get_attribute('sourceAiiType')
    @SourceAiiType.setter
    def SourceAiiType(self, value):
        self._set_attribute('sourceAiiType', value)

    @property
    def Sp(self):
        """
        Returns
        -------
        - str(hexVal0 | hexVal1 | hexVal2 | hexVal3): It signifies the SP value.
        """
        return self._get_attribute('sp')
    @Sp.setter
    def Sp(self, value):
        self._set_attribute('sp', value)

    @property
    def Ssrc(self):
        """
        Returns
        -------
        - number: Indicates the SSRC value.
        """
        return self._get_attribute('ssrc')
    @Ssrc.setter
    def Ssrc(self, value):
        self._set_attribute('ssrc', value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: The number to increment the peer address by.
        """
        return self._get_attribute('step')
    @Step.setter
    def Step(self, value):
        self._set_attribute('step', value)

    @property
    def TargetAiiAsIp(self):
        """
        Returns
        -------
        - str: The IP address of the Target AII.
        """
        return self._get_attribute('targetAiiAsIp')
    @TargetAiiAsIp.setter
    def TargetAiiAsIp(self, value):
        self._set_attribute('targetAiiAsIp', value)

    @property
    def TargetAiiAsNumber(self):
        """
        Returns
        -------
        - number: The numerical value of the Target AII.
        """
        return self._get_attribute('targetAiiAsNumber')
    @TargetAiiAsNumber.setter
    def TargetAiiAsNumber(self, value):
        self._set_attribute('targetAiiAsNumber', value)

    @property
    def TargetAiiType(self):
        """
        Returns
        -------
        - str(number | ipAddress): Editable dropdown. The options are: AS, IP.
        """
        return self._get_attribute('targetAiiType')
    @TargetAiiType.setter
    def TargetAiiType(self, value):
        self._set_attribute('targetAiiType', value)

    @property
    def TdmBitrate(self):
        """
        Returns
        -------
        - number: The tdm bit rate.
        """
        return self._get_attribute('tdmBitrate')
    @TdmBitrate.setter
    def TdmBitrate(self, value):
        self._set_attribute('tdmBitrate', value)

    @property
    def TdmDataSize(self):
        """
        Returns
        -------
        - number: Indicates the TDM data size.
        """
        return self._get_attribute('tdmDataSize')
    @TdmDataSize.setter
    def TdmDataSize(self, value):
        self._set_attribute('tdmDataSize', value)

    @property
    def TimestampMode(self):
        """
        Returns
        -------
        - str(absolute | differential): The time stamp mode.
        """
        return self._get_attribute('timestampMode')
    @TimestampMode.setter
    def TimestampMode(self, value):
        self._set_attribute('timestampMode', value)

    @property
    def UpInterval(self):
        """
        Returns
        -------
        - number: Time interval for which the same process to be repeated. (Default = 30 sec)
        """
        return self._get_attribute('upInterval')
    @UpInterval.setter
    def UpInterval(self, value):
        self._set_attribute('upInterval', value)

    @property
    def VcId(self):
        """
        Returns
        -------
        - number: The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        """
        return self._get_attribute('vcId')
    @VcId.setter
    def VcId(self, value):
        self._set_attribute('vcId', value)

    @property
    def VcIdStep(self):
        """
        Returns
        -------
        - number: The increment step to be added to each additional VC ID in the range of VC IDs.
        """
        return self._get_attribute('vcIdStep')
    @VcIdStep.setter
    def VcIdStep(self, value):
        self._set_attribute('vcIdStep', value)

    @property
    def VplsIdAsNumber(self):
        """
        Returns
        -------
        - number: The 2 byte unsigned integer value indicating the VPLS ID AS Number.
        """
        return self._get_attribute('vplsIdAsNumber')
    @VplsIdAsNumber.setter
    def VplsIdAsNumber(self, value):
        self._set_attribute('vplsIdAsNumber', value)

    @property
    def VplsIdAsNumberStep(self):
        """
        Returns
        -------
        - number: The 2 byte unsigned integer value indicating the VPLS ID AS Number Step.
        """
        return self._get_attribute('vplsIdAsNumberStep')
    @VplsIdAsNumberStep.setter
    def VplsIdAsNumberStep(self, value):
        self._set_attribute('vplsIdAsNumberStep', value)

    @property
    def VplsIdAssignedNumber(self):
        """
        Returns
        -------
        - number: The 2 or 4 byte unsigned integer value dependent on the vplsIdType
        """
        return self._get_attribute('vplsIdAssignedNumber')
    @VplsIdAssignedNumber.setter
    def VplsIdAssignedNumber(self, value):
        self._set_attribute('vplsIdAssignedNumber', value)

    @property
    def VplsIdAssignedNumberStep(self):
        """
        Returns
        -------
        - number: The 2 or 4 byte unsigned integer value dependent on the vplsIdType.
        """
        return self._get_attribute('vplsIdAssignedNumberStep')
    @VplsIdAssignedNumberStep.setter
    def VplsIdAssignedNumberStep(self, value):
        self._set_attribute('vplsIdAssignedNumberStep', value)

    @property
    def VplsIdCount(self):
        """
        Returns
        -------
        - number: The 4 byte unsigned integer indicating the VPLS ID Count.
        """
        return self._get_attribute('vplsIdCount')
    @VplsIdCount.setter
    def VplsIdCount(self, value):
        self._set_attribute('vplsIdCount', value)

    @property
    def VplsIdIpAddress(self):
        """
        Returns
        -------
        - str: The IP address of the VPLS Id.
        """
        return self._get_attribute('vplsIdIpAddress')
    @VplsIdIpAddress.setter
    def VplsIdIpAddress(self, value):
        self._set_attribute('vplsIdIpAddress', value)

    @property
    def VplsIdIpAddressStep(self):
        """
        Returns
        -------
        - str: The IP address of the VPLS Id.
        """
        return self._get_attribute('vplsIdIpAddressStep')
    @VplsIdIpAddressStep.setter
    def VplsIdIpAddressStep(self, value):
        self._set_attribute('vplsIdIpAddressStep', value)

    @property
    def VplsIdType(self):
        """
        Returns
        -------
        - str(asNumber | ipAddress): Editable dropdown. The options are: AS, IP.
        """
        return self._get_attribute('vplsIdType')
    @VplsIdType.setter
    def VplsIdType(self, value):
        self._set_attribute('vplsIdType', value)

    def update(self, CapableOfReassembly=None, Cas=None, CeIpAddress=None, CemOption=None, CemPayload=None, Count=None, Description=None, DoNotExpandIntoVcs=None, DownInterval=None, DownStartInterval=None, EnableBfdIpUdpCv=None, EnableBfdPwAchCv=None, EnableCBit=None, EnableCccvNegotiation=None, EnableCemOption=None, EnableCemPayload=None, EnableDescriptionPresent=None, EnableLspPingCv=None, EnableMaxAtmPresent=None, EnableMtuPresent=None, EnablePacking=None, EnablePwAchCc=None, EnablePwStatusTlv=None, EnableRouterAlertCc=None, Enabled=None, FecType=None, Frequency=None, IncludeRtpHeader=None, IncludeSsrc=None, IncludeTdmBitrate=None, IncludeTdmOption=None, IncludeTdmPayload=None, IpType=None, LabelMode=None, LabelStart=None, MaxNumberOfAtmCells=None, Mtu=None, PayloadType=None, PeerAddress=None, ProvisioningModel=None, PwStatusCode=None, RepeatCount=None, SendPwStatus=None, SourceAiiAsIp=None, SourceAiiAsNumber=None, SourceAiiType=None, Sp=None, Ssrc=None, Step=None, TargetAiiAsIp=None, TargetAiiAsNumber=None, TargetAiiType=None, TdmBitrate=None, TdmDataSize=None, TimestampMode=None, UpInterval=None, VcId=None, VcIdStep=None, VplsIdAsNumber=None, VplsIdAsNumberStep=None, VplsIdAssignedNumber=None, VplsIdAssignedNumberStep=None, VplsIdCount=None, VplsIdIpAddress=None, VplsIdIpAddressStep=None, VplsIdType=None):
        """Updates l2VcRange resource on the server.

        Args
        ----
        - CapableOfReassembly (bool): If enabled, makes the interface capable of reassembly.
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): It signifies the CAS value.
        - CeIpAddress (str): The IP address of attached CE endpoint. If IP Type is set to Ipv4, then the default is 0.0.0.0, and if the IP type is set to Ipv6, then the default is 0:0:0:0:0:0:0:0.
        - CemOption (number): The value of the CEM option.
        - CemPayload (number): If enabled, indicates that there is a Circuit Emulation Service over MPLS (CEM) payload.
        - Count (number): (In octets) The 8-bit VC information Length field. It indicates the length of the (2-octet) VC ID field plus combined length of all of the parameters in the VC FEC element.
        - Description (str): An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        - DoNotExpandIntoVcs (bool): If true, the VC ranges do not expand into individual VCs.
        - DownInterval (number): Time interval for which the PW status will remain down. (Default= 60 seconds)
        - DownStartInterval (number): The duration in time after session becomes up and a notification message being sent to make the session down. (Default= 30 seconds)
        - EnableBfdIpUdpCv (bool): NOT DEFINED
        - EnableBfdPwAchCv (bool): NOT DEFINED
        - EnableCBit (bool): Controls generation of the control word.
        - EnableCccvNegotiation (bool): NOT DEFINED
        - EnableCemOption (bool): Enable the Circuit Emulation over MPLS option, for encapsulation of TDM signals.
        - EnableCemPayload (bool): Enable the Circuit Emulation over MPLS payload.
        - EnableDescriptionPresent (bool): If enabled, indicates that an optional interface description is present.
        - EnableLspPingCv (bool): NOT DEFINED
        - EnableMaxAtmPresent (bool): Enables the generation of an interface parameter field with the maximum number of concatenated ATM cells. (default = 0)
        - EnableMtuPresent (bool): This attribute enables the generation of an MTU interface parameter field.
        - EnablePacking (bool): (For L2 VC FEC ranges and in Unsolicited Label Distribution Mode ONLY.) If enabled, L2 VC FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        - EnablePwAchCc (bool): NOT DEFINED
        - EnablePwStatusTlv (bool): If checked, this enables the use of PW status TLV in notification messages to notify the PW status.
        - EnableRouterAlertCc (bool): NOT DEFINED
        - Enabled (bool): Enables use of this VC range.
        - FecType (str(pwIdFec | generalizedIdFecVpls)): The FEC type. The options are: PW Id FEC 0x80, Generalized Id FEC 0x81 VPLS.
        - Frequency (number): It is the frequency.
        - IncludeRtpHeader (bool): If true, includes the RTP header.
        - IncludeSsrc (bool): If true, enables SSRC.
        - IncludeTdmBitrate (bool): If true, enables TDM bit rate.
        - IncludeTdmOption (bool): If true, includes the TDM option.
        - IncludeTdmPayload (bool): If true, enables TDM payload.
        - IpType (number): The type (IPv4 or IPv6) of the neighbor.
        - LabelMode (str(none | increment)): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        - LabelStart (number): The first label in the range of labels. The default is 16.
        - MaxNumberOfAtmCells (number): The maximum number of ATM cells which may be concatenated and sent in a single MPLS frame. This parameter is part of the FEC element.
        - Mtu (number): (in octets) The 2-octet value for the maximum Transmission Unit (MTU).
        - PayloadType (number): It is the payload type.
        - PeerAddress (str): The IPv4 address of the LDP router which is the peer for this VC range.
        - ProvisioningModel (str(manualConfiguration | bgpAutoDiscovery)): Editable dropdown to denote the Provisioning Model.
        - PwStatusCode (number): This is an editable dropdown to denote the PW status. This field is editable. The range is from 0x00000001 - 0xFFFFFFFF.
        - RepeatCount (number): The number of times to repeat the above processes. The default is 1.
        - SendPwStatus (bool): If checked, it signifies whether to send a notification message with a PW status for the corresponding PW.
        - SourceAiiAsIp (str): The IP address.
        - SourceAiiAsNumber (number): The numerical value indicating the AS of the Source AII.
        - SourceAiiType (str(number | ipAddress)): Editable dropdown. The options are: AS, IP.
        - Sp (str(hexVal0 | hexVal1 | hexVal2 | hexVal3)): It signifies the SP value.
        - Ssrc (number): Indicates the SSRC value.
        - Step (number): The number to increment the peer address by.
        - TargetAiiAsIp (str): The IP address of the Target AII.
        - TargetAiiAsNumber (number): The numerical value of the Target AII.
        - TargetAiiType (str(number | ipAddress)): Editable dropdown. The options are: AS, IP.
        - TdmBitrate (number): The tdm bit rate.
        - TdmDataSize (number): Indicates the TDM data size.
        - TimestampMode (str(absolute | differential)): The time stamp mode.
        - UpInterval (number): Time interval for which the same process to be repeated. (Default = 30 sec)
        - VcId (number): The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        - VcIdStep (number): The increment step to be added to each additional VC ID in the range of VC IDs.
        - VplsIdAsNumber (number): The 2 byte unsigned integer value indicating the VPLS ID AS Number.
        - VplsIdAsNumberStep (number): The 2 byte unsigned integer value indicating the VPLS ID AS Number Step.
        - VplsIdAssignedNumber (number): The 2 or 4 byte unsigned integer value dependent on the vplsIdType
        - VplsIdAssignedNumberStep (number): The 2 or 4 byte unsigned integer value dependent on the vplsIdType.
        - VplsIdCount (number): The 4 byte unsigned integer indicating the VPLS ID Count.
        - VplsIdIpAddress (str): The IP address of the VPLS Id.
        - VplsIdIpAddressStep (str): The IP address of the VPLS Id.
        - VplsIdType (str(asNumber | ipAddress)): Editable dropdown. The options are: AS, IP.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, CapableOfReassembly=None, Cas=None, CeIpAddress=None, CemOption=None, CemPayload=None, Count=None, Description=None, DoNotExpandIntoVcs=None, DownInterval=None, DownStartInterval=None, EnableBfdIpUdpCv=None, EnableBfdPwAchCv=None, EnableCBit=None, EnableCccvNegotiation=None, EnableCemOption=None, EnableCemPayload=None, EnableDescriptionPresent=None, EnableLspPingCv=None, EnableMaxAtmPresent=None, EnableMtuPresent=None, EnablePacking=None, EnablePwAchCc=None, EnablePwStatusTlv=None, EnableRouterAlertCc=None, Enabled=None, FecType=None, Frequency=None, IncludeRtpHeader=None, IncludeSsrc=None, IncludeTdmBitrate=None, IncludeTdmOption=None, IncludeTdmPayload=None, IpType=None, LabelMode=None, LabelStart=None, MaxNumberOfAtmCells=None, Mtu=None, PayloadType=None, PeerAddress=None, ProvisioningModel=None, PwStatusCode=None, RepeatCount=None, SendPwStatus=None, SourceAiiAsIp=None, SourceAiiAsNumber=None, SourceAiiType=None, Sp=None, Ssrc=None, Step=None, TargetAiiAsIp=None, TargetAiiAsNumber=None, TargetAiiType=None, TdmBitrate=None, TdmDataSize=None, TimestampMode=None, UpInterval=None, VcId=None, VcIdStep=None, VplsIdAsNumber=None, VplsIdAsNumberStep=None, VplsIdAssignedNumber=None, VplsIdAssignedNumberStep=None, VplsIdCount=None, VplsIdIpAddress=None, VplsIdIpAddressStep=None, VplsIdType=None):
        """Adds a new l2VcRange resource on the server and adds it to the container.

        Args
        ----
        - CapableOfReassembly (bool): If enabled, makes the interface capable of reassembly.
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): It signifies the CAS value.
        - CeIpAddress (str): The IP address of attached CE endpoint. If IP Type is set to Ipv4, then the default is 0.0.0.0, and if the IP type is set to Ipv6, then the default is 0:0:0:0:0:0:0:0.
        - CemOption (number): The value of the CEM option.
        - CemPayload (number): If enabled, indicates that there is a Circuit Emulation Service over MPLS (CEM) payload.
        - Count (number): (In octets) The 8-bit VC information Length field. It indicates the length of the (2-octet) VC ID field plus combined length of all of the parameters in the VC FEC element.
        - Description (str): An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        - DoNotExpandIntoVcs (bool): If true, the VC ranges do not expand into individual VCs.
        - DownInterval (number): Time interval for which the PW status will remain down. (Default= 60 seconds)
        - DownStartInterval (number): The duration in time after session becomes up and a notification message being sent to make the session down. (Default= 30 seconds)
        - EnableBfdIpUdpCv (bool): NOT DEFINED
        - EnableBfdPwAchCv (bool): NOT DEFINED
        - EnableCBit (bool): Controls generation of the control word.
        - EnableCccvNegotiation (bool): NOT DEFINED
        - EnableCemOption (bool): Enable the Circuit Emulation over MPLS option, for encapsulation of TDM signals.
        - EnableCemPayload (bool): Enable the Circuit Emulation over MPLS payload.
        - EnableDescriptionPresent (bool): If enabled, indicates that an optional interface description is present.
        - EnableLspPingCv (bool): NOT DEFINED
        - EnableMaxAtmPresent (bool): Enables the generation of an interface parameter field with the maximum number of concatenated ATM cells. (default = 0)
        - EnableMtuPresent (bool): This attribute enables the generation of an MTU interface parameter field.
        - EnablePacking (bool): (For L2 VC FEC ranges and in Unsolicited Label Distribution Mode ONLY.) If enabled, L2 VC FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        - EnablePwAchCc (bool): NOT DEFINED
        - EnablePwStatusTlv (bool): If checked, this enables the use of PW status TLV in notification messages to notify the PW status.
        - EnableRouterAlertCc (bool): NOT DEFINED
        - Enabled (bool): Enables use of this VC range.
        - FecType (str(pwIdFec | generalizedIdFecVpls)): The FEC type. The options are: PW Id FEC 0x80, Generalized Id FEC 0x81 VPLS.
        - Frequency (number): It is the frequency.
        - IncludeRtpHeader (bool): If true, includes the RTP header.
        - IncludeSsrc (bool): If true, enables SSRC.
        - IncludeTdmBitrate (bool): If true, enables TDM bit rate.
        - IncludeTdmOption (bool): If true, includes the TDM option.
        - IncludeTdmPayload (bool): If true, enables TDM payload.
        - IpType (number): The type (IPv4 or IPv6) of the neighbor.
        - LabelMode (str(none | increment)): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        - LabelStart (number): The first label in the range of labels. The default is 16.
        - MaxNumberOfAtmCells (number): The maximum number of ATM cells which may be concatenated and sent in a single MPLS frame. This parameter is part of the FEC element.
        - Mtu (number): (in octets) The 2-octet value for the maximum Transmission Unit (MTU).
        - PayloadType (number): It is the payload type.
        - PeerAddress (str): The IPv4 address of the LDP router which is the peer for this VC range.
        - ProvisioningModel (str(manualConfiguration | bgpAutoDiscovery)): Editable dropdown to denote the Provisioning Model.
        - PwStatusCode (number): This is an editable dropdown to denote the PW status. This field is editable. The range is from 0x00000001 - 0xFFFFFFFF.
        - RepeatCount (number): The number of times to repeat the above processes. The default is 1.
        - SendPwStatus (bool): If checked, it signifies whether to send a notification message with a PW status for the corresponding PW.
        - SourceAiiAsIp (str): The IP address.
        - SourceAiiAsNumber (number): The numerical value indicating the AS of the Source AII.
        - SourceAiiType (str(number | ipAddress)): Editable dropdown. The options are: AS, IP.
        - Sp (str(hexVal0 | hexVal1 | hexVal2 | hexVal3)): It signifies the SP value.
        - Ssrc (number): Indicates the SSRC value.
        - Step (number): The number to increment the peer address by.
        - TargetAiiAsIp (str): The IP address of the Target AII.
        - TargetAiiAsNumber (number): The numerical value of the Target AII.
        - TargetAiiType (str(number | ipAddress)): Editable dropdown. The options are: AS, IP.
        - TdmBitrate (number): The tdm bit rate.
        - TdmDataSize (number): Indicates the TDM data size.
        - TimestampMode (str(absolute | differential)): The time stamp mode.
        - UpInterval (number): Time interval for which the same process to be repeated. (Default = 30 sec)
        - VcId (number): The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        - VcIdStep (number): The increment step to be added to each additional VC ID in the range of VC IDs.
        - VplsIdAsNumber (number): The 2 byte unsigned integer value indicating the VPLS ID AS Number.
        - VplsIdAsNumberStep (number): The 2 byte unsigned integer value indicating the VPLS ID AS Number Step.
        - VplsIdAssignedNumber (number): The 2 or 4 byte unsigned integer value dependent on the vplsIdType
        - VplsIdAssignedNumberStep (number): The 2 or 4 byte unsigned integer value dependent on the vplsIdType.
        - VplsIdCount (number): The 4 byte unsigned integer indicating the VPLS ID Count.
        - VplsIdIpAddress (str): The IP address of the VPLS Id.
        - VplsIdIpAddressStep (str): The IP address of the VPLS Id.
        - VplsIdType (str(asNumber | ipAddress)): Editable dropdown. The options are: AS, IP.

        Returns
        -------
        - self: This instance with all currently retrieved l2VcRange resources using find and the newly added l2VcRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained l2VcRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CapableOfReassembly=None, Cas=None, CeIpAddress=None, CemOption=None, CemPayload=None, Count=None, Description=None, DoNotExpandIntoVcs=None, DownInterval=None, DownStartInterval=None, EnableBfdIpUdpCv=None, EnableBfdPwAchCv=None, EnableCBit=None, EnableCccvNegotiation=None, EnableCemOption=None, EnableCemPayload=None, EnableDescriptionPresent=None, EnableLspPingCv=None, EnableMaxAtmPresent=None, EnableMtuPresent=None, EnablePacking=None, EnablePwAchCc=None, EnablePwStatusTlv=None, EnableRouterAlertCc=None, Enabled=None, FecType=None, Frequency=None, IncludeRtpHeader=None, IncludeSsrc=None, IncludeTdmBitrate=None, IncludeTdmOption=None, IncludeTdmPayload=None, IpType=None, LabelMode=None, LabelStart=None, MaxNumberOfAtmCells=None, Mtu=None, PayloadType=None, PeerAddress=None, ProvisioningModel=None, PwStatusCode=None, RepeatCount=None, SendPwStatus=None, SourceAiiAsIp=None, SourceAiiAsNumber=None, SourceAiiType=None, Sp=None, Ssrc=None, Step=None, TargetAiiAsIp=None, TargetAiiAsNumber=None, TargetAiiType=None, TdmBitrate=None, TdmDataSize=None, TimestampMode=None, UpInterval=None, VcId=None, VcIdStep=None, VplsIdAsNumber=None, VplsIdAsNumberStep=None, VplsIdAssignedNumber=None, VplsIdAssignedNumberStep=None, VplsIdCount=None, VplsIdIpAddress=None, VplsIdIpAddressStep=None, VplsIdType=None):
        """Finds and retrieves l2VcRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2VcRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2VcRange resources from the server.

        Args
        ----
        - CapableOfReassembly (bool): If enabled, makes the interface capable of reassembly.
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): It signifies the CAS value.
        - CeIpAddress (str): The IP address of attached CE endpoint. If IP Type is set to Ipv4, then the default is 0.0.0.0, and if the IP type is set to Ipv6, then the default is 0:0:0:0:0:0:0:0.
        - CemOption (number): The value of the CEM option.
        - CemPayload (number): If enabled, indicates that there is a Circuit Emulation Service over MPLS (CEM) payload.
        - Count (number): (In octets) The 8-bit VC information Length field. It indicates the length of the (2-octet) VC ID field plus combined length of all of the parameters in the VC FEC element.
        - Description (str): An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        - DoNotExpandIntoVcs (bool): If true, the VC ranges do not expand into individual VCs.
        - DownInterval (number): Time interval for which the PW status will remain down. (Default= 60 seconds)
        - DownStartInterval (number): The duration in time after session becomes up and a notification message being sent to make the session down. (Default= 30 seconds)
        - EnableBfdIpUdpCv (bool): NOT DEFINED
        - EnableBfdPwAchCv (bool): NOT DEFINED
        - EnableCBit (bool): Controls generation of the control word.
        - EnableCccvNegotiation (bool): NOT DEFINED
        - EnableCemOption (bool): Enable the Circuit Emulation over MPLS option, for encapsulation of TDM signals.
        - EnableCemPayload (bool): Enable the Circuit Emulation over MPLS payload.
        - EnableDescriptionPresent (bool): If enabled, indicates that an optional interface description is present.
        - EnableLspPingCv (bool): NOT DEFINED
        - EnableMaxAtmPresent (bool): Enables the generation of an interface parameter field with the maximum number of concatenated ATM cells. (default = 0)
        - EnableMtuPresent (bool): This attribute enables the generation of an MTU interface parameter field.
        - EnablePacking (bool): (For L2 VC FEC ranges and in Unsolicited Label Distribution Mode ONLY.) If enabled, L2 VC FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        - EnablePwAchCc (bool): NOT DEFINED
        - EnablePwStatusTlv (bool): If checked, this enables the use of PW status TLV in notification messages to notify the PW status.
        - EnableRouterAlertCc (bool): NOT DEFINED
        - Enabled (bool): Enables use of this VC range.
        - FecType (str(pwIdFec | generalizedIdFecVpls)): The FEC type. The options are: PW Id FEC 0x80, Generalized Id FEC 0x81 VPLS.
        - Frequency (number): It is the frequency.
        - IncludeRtpHeader (bool): If true, includes the RTP header.
        - IncludeSsrc (bool): If true, enables SSRC.
        - IncludeTdmBitrate (bool): If true, enables TDM bit rate.
        - IncludeTdmOption (bool): If true, includes the TDM option.
        - IncludeTdmPayload (bool): If true, enables TDM payload.
        - IpType (number): The type (IPv4 or IPv6) of the neighbor.
        - LabelMode (str(none | increment)): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        - LabelStart (number): The first label in the range of labels. The default is 16.
        - MaxNumberOfAtmCells (number): The maximum number of ATM cells which may be concatenated and sent in a single MPLS frame. This parameter is part of the FEC element.
        - Mtu (number): (in octets) The 2-octet value for the maximum Transmission Unit (MTU).
        - PayloadType (number): It is the payload type.
        - PeerAddress (str): The IPv4 address of the LDP router which is the peer for this VC range.
        - ProvisioningModel (str(manualConfiguration | bgpAutoDiscovery)): Editable dropdown to denote the Provisioning Model.
        - PwStatusCode (number): This is an editable dropdown to denote the PW status. This field is editable. The range is from 0x00000001 - 0xFFFFFFFF.
        - RepeatCount (number): The number of times to repeat the above processes. The default is 1.
        - SendPwStatus (bool): If checked, it signifies whether to send a notification message with a PW status for the corresponding PW.
        - SourceAiiAsIp (str): The IP address.
        - SourceAiiAsNumber (number): The numerical value indicating the AS of the Source AII.
        - SourceAiiType (str(number | ipAddress)): Editable dropdown. The options are: AS, IP.
        - Sp (str(hexVal0 | hexVal1 | hexVal2 | hexVal3)): It signifies the SP value.
        - Ssrc (number): Indicates the SSRC value.
        - Step (number): The number to increment the peer address by.
        - TargetAiiAsIp (str): The IP address of the Target AII.
        - TargetAiiAsNumber (number): The numerical value of the Target AII.
        - TargetAiiType (str(number | ipAddress)): Editable dropdown. The options are: AS, IP.
        - TdmBitrate (number): The tdm bit rate.
        - TdmDataSize (number): Indicates the TDM data size.
        - TimestampMode (str(absolute | differential)): The time stamp mode.
        - UpInterval (number): Time interval for which the same process to be repeated. (Default = 30 sec)
        - VcId (number): The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        - VcIdStep (number): The increment step to be added to each additional VC ID in the range of VC IDs.
        - VplsIdAsNumber (number): The 2 byte unsigned integer value indicating the VPLS ID AS Number.
        - VplsIdAsNumberStep (number): The 2 byte unsigned integer value indicating the VPLS ID AS Number Step.
        - VplsIdAssignedNumber (number): The 2 or 4 byte unsigned integer value dependent on the vplsIdType
        - VplsIdAssignedNumberStep (number): The 2 or 4 byte unsigned integer value dependent on the vplsIdType.
        - VplsIdCount (number): The 4 byte unsigned integer indicating the VPLS ID Count.
        - VplsIdIpAddress (str): The IP address of the VPLS Id.
        - VplsIdIpAddressStep (str): The IP address of the VPLS Id.
        - VplsIdType (str(asNumber | ipAddress)): Editable dropdown. The options are: AS, IP.

        Returns
        -------
        - self: This instance with matching l2VcRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of l2VcRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2VcRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
