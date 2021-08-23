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
from typing import List, Any, Union


class Stack(Base):
    """This object helps to specify the field properties of a protocol stack.
    The Stack class encapsulates a list of stack resources that are managed by the system.
    A list of resources can be retrieved from the server using the Stack.find() method.
    """

    __slots__ = '_stack_index'
    _SDM_NAME = 'stack'
    _SDM_ATT_MAP = {
        'DisplayName': 'displayName',
        'StackTypeId': 'stackTypeId',
        'TemplateName': 'templateName',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Stack, self).__init__(parent, list_op)
        self._stack_index = 0

    @property
    def Field(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.field.field.Field): An instance of the Field class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.field.field import Field
        if self._properties.get('Field', None) is not None:
            return self._properties.get('Field')
        else:
            return Field(self)

    @property
    def SourcePacketHeader(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sourcePacketHeader_template import SourcePacketHeader
        return SourcePacketHeader(self)

    @property
    def Iec61883624BitData(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec61883624BitData_template import Iec61883624BitData
        return Iec61883624BitData(self)

    @property
    def RealTimeTransportControlProtocol(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol_template import RealTimeTransportControlProtocol
        return RealTimeTransportControlProtocol(self)

    @property
    def Iec618831(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec618831_template import Iec618831
        return Iec618831(self)

    @property
    def H264csrc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264csrc_template import H264csrc
        return H264csrc(self)

    @property
    def H264sh(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264sh_template import H264sh
        return H264sh(self)

    @property
    def Avtpdu(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtpdu_template import Avtpdu
        return Avtpdu(self)

    @property
    def H264(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264_template import H264
        return H264(self)

    @property
    def Jpeg2000VideoFormat(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpeg2000VideoFormat_template import Jpeg2000VideoFormat
        return Jpeg2000VideoFormat(self)

    @property
    def JpegVideoFormat(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpegVideoFormat_template import JpegVideoFormat
        return JpegVideoFormat(self)

    @property
    def SdiVideoFormat(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sdiVideoFormat_template import SdiVideoFormat
        return SdiVideoFormat(self)

    @property
    def MpegtsPayload(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpegtsPayload_template import MpegtsPayload
        return MpegtsPayload(self)

    @property
    def MmaDataPayload(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmaDataPayload_template import MmaDataPayload
        return MmaDataPayload(self)

    @property
    def G723SidMode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723SidMode_template import G723SidMode
        return G723SidMode(self)

    @property
    def G723Framepacking(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking_template import G723Framepacking
        return G723Framepacking(self)

    @property
    def G723Framepacking53(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking53_template import G723Framepacking53
        return G723Framepacking53(self)

    @property
    def CN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.CN_template import CN
        return CN(self)

    @property
    def RealTimeTransportControlProtocol1733(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol1733_template import RealTimeTransportControlProtocol1733
        return RealTimeTransportControlProtocol1733(self)

    @property
    def Aal5(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.aal5_template import Aal5
        return Aal5(self)

    @property
    def AtmCell(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmCell_template import AtmCell
        return AtmCell(self)

    @property
    def AtmAAL5Frame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmAAL5Frame_template import AtmAAL5Frame
        return AtmAAL5Frame(self)

    @property
    def EthernetARP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetARP_template import EthernetARP
        return EthernetARP(self)

    @property
    def CiscoHDLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoHDLC_template import CiscoHDLC
        return CiscoHDLC(self)

    @property
    def CiscoISL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoISL_template import CiscoISL
        return CiscoISL(self)

    @property
    def CiscoFrameRelay(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoFrameRelay_template import CiscoFrameRelay
        return CiscoFrameRelay(self)

    @property
    def Ethernet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernet_template import Ethernet
        return Ethernet(self)

    @property
    def EthernetNoFCS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetNoFCS_template import EthernetNoFCS
        return EthernetNoFCS(self)

    @property
    def FrameRelay(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.frameRelay_template import FrameRelay
        return FrameRelay(self)

    @property
    def PppIPCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPCP_template import PppIPCP
        return PppIPCP(self)

    @property
    def PppIPv6CP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPv6CP_template import PppIPv6CP
        return PppIPv6CP(self)

    @property
    def Lacp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacp_template import Lacp
        return Lacp(self)

    @property
    def LacpWithoutEthernet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacpWithoutEthernet_template import LacpWithoutEthernet
        return LacpWithoutEthernet(self)

    @property
    def LlcPPP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcPPP_template import LlcPPP
        return LlcPPP(self)

    @property
    def Cfm(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cfm_template import Cfm
        return Cfm(self)

    @property
    def LinkOAM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.linkOAM_template import LinkOAM
        return LinkOAM(self)

    @property
    def Elmi(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.elmi_template import Elmi
        return Elmi(self)

    @property
    def LlcBridgedEthernet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcBridgedEthernet_template import LlcBridgedEthernet
        return LlcBridgedEthernet(self)

    @property
    def Llc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llc_template import Llc
        return Llc(self)

    @property
    def L2VPNATMCellCW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCellCW_template import L2VPNATMCellCW
        return L2VPNATMCellCW(self)

    @property
    def L2VPNATMCWFrame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCWFrame_template import L2VPNATMCWFrame
        return L2VPNATMCWFrame(self)

    @property
    def L2VPNEthernetFrame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNEthernetFrame_template import L2VPNEthernetFrame
        return L2VPNEthernetFrame(self)

    @property
    def L2VPNFrameRelayCW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayCW_template import L2VPNFrameRelayCW
        return L2VPNFrameRelayCW(self)

    @property
    def L2VPNFrameRelayRFC4619CW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayRFC4619CW_template import L2VPNFrameRelayRFC4619CW
        return L2VPNFrameRelayRFC4619CW(self)

    @property
    def L2VPNFrameRelay(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelay_template import L2VPNFrameRelay
        return L2VPNFrameRelay(self)

    @property
    def L2VPNPPPHDLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPPHDLC_template import L2VPNPPPHDLC
        return L2VPNPPPHDLC(self)

    @property
    def L2VPNHDLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNHDLC_template import L2VPNHDLC
        return L2VPNHDLC(self)

    @property
    def L2VPNPPP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPP_template import L2VPNPPP
        return L2VPNPPP(self)

    @property
    def L2VPNVCTypeIPCW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNVCTypeIPCW_template import L2VPNVCTypeIPCW
        return L2VPNVCTypeIPCW(self)

    @property
    def MacInMAC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMAC_template import MacInMAC
        return MacInMAC(self)

    @property
    def MacInMACNoFcs(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACNoFcs_template import MacInMACNoFcs
        return MacInMACNoFcs(self)

    @property
    def MarkerPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.markerPDU_template import MarkerPDU
        return MarkerPDU(self)

    @property
    def Mpls(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpls_template import Mpls
        return Mpls(self)

    @property
    def Mplsenull(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mplsenull_template import Mplsenull
        return Mplsenull(self)

    @property
    def MstpBPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mstpBPDU_template import MstpBPDU
        return MstpBPDU(self)

    @property
    def MPLSTPEthernetFrame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.MPLSTPEthernetFrame_template import MPLSTPEthernetFrame
        return MPLSTPEthernetFrame(self)

    @property
    def OamCCM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oamCCM_template import OamCCM
        return OamCCM(self)

    @property
    def Ppp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ppp_template import Ppp
        return Ppp(self)

    @property
    def PppWithoutHDLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppWithoutHDLC_template import PppWithoutHDLC
        return PppWithoutHDLC(self)

    @property
    def PppLCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppLCP_template import PppLCP
        return PppLCP(self)

    @property
    def PppPAPCHAP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppPAPCHAP_template import PppPAPCHAP
        return PppPAPCHAP(self)

    @property
    def PppoEDiscovery(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoEDiscovery_template import PppoEDiscovery
        return PppoEDiscovery(self)

    @property
    def PppoESession(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoESession_template import PppoESession
        return PppoESession(self)

    @property
    def PTPv2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2_template import PTPv2
        return PTPv2(self)

    @property
    def EthernetRARP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetRARP_template import EthernetRARP
        return EthernetRARP(self)

    @property
    def RstpBPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rstpBPDU_template import RstpBPDU
        return RstpBPDU(self)

    @property
    def LlcSNAP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcSNAP_template import LlcSNAP
        return LlcSNAP(self)

    @property
    def Snap(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.snap_template import Snap
        return Snap(self)

    @property
    def StpCfgBPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpCfgBPDU_template import StpCfgBPDU
        return StpCfgBPDU(self)

    @property
    def StpTCNBPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpTCNBPDU_template import StpTCNBPDU
        return StpTCNBPDU(self)

    @property
    def VcMuxBridgedEthernet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxBridgedEthernet_template import VcMuxBridgedEthernet
        return VcMuxBridgedEthernet(self)

    @property
    def VcMuxPPP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxPPP_template import VcMuxPPP
        return VcMuxPPP(self)

    @property
    def Vlan(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vlan_template import Vlan
        return Vlan(self)

    @property
    def Vntag(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vntag_template import Vntag
        return Vntag(self)

    @property
    def Vic(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vic_template import Vic
        return Vic(self)

    @property
    def VplsEthernet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vplsEthernet_template import VplsEthernet
        return VplsEthernet(self)

    @property
    def FcoE(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcoE_template import FcoE
        return FcoE(self)

    @property
    def FCoEFabricLogoEnode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoEnode_template import FCoEFabricLogoEnode
        return FCoEFabricLogoEnode(self)

    @property
    def FCoEFabricLogoLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsAcc_template import FCoEFabricLogoLsAcc
        return FCoEFabricLogoLsAcc(self)

    @property
    def FCoEFabricLogoLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsRjt_template import FCoEFabricLogoLsRjt
        return FCoEFabricLogoLsRjt(self)

    @property
    def FCoEFlogiLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsAcc_template import FCoEFlogiLsAcc
        return FCoEFlogiLsAcc(self)

    @property
    def FCoEFlogiLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsRjt_template import FCoEFlogiLsRjt
        return FCoEFlogiLsRjt(self)

    @property
    def FCoEFlogiRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiRequest_template import FCoEFlogiRequest
        return FCoEFlogiRequest(self)

    @property
    def FCoEPlogiLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsAcc_template import FCoEPlogiLsAcc
        return FCoEPlogiLsAcc(self)

    @property
    def FCoEPlogiLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsRjt_template import FCoEPlogiLsRjt
        return FCoEPlogiLsRjt(self)

    @property
    def FCoEPlogiRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiRequest_template import FCoEPlogiRequest
        return FCoEPlogiRequest(self)

    @property
    def FCoENpivFdicsLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdicsLsAcc_template import FCoENpivFdicsLsAcc
        return FCoENpivFdicsLsAcc(self)

    @property
    def FCoENpivFdiscLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscLsRjt_template import FCoENpivFdiscLsRjt
        return FCoENpivFdiscLsRjt(self)

    @property
    def FCoENpivFdiscRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscRequest_template import FCoENpivFdiscRequest
        return FCoENpivFdiscRequest(self)

    @property
    def FCoERscn(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERscn_template import FCoERscn
        return FCoERscn(self)

    @property
    def FCoEScrRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEScrRequest_template import FCoEScrRequest
        return FCoEScrRequest(self)

    @property
    def FCoEGCSID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGCSID_template import FCoEGCSID
        return FCoEGCSID(self)

    @property
    def FCoEGANXT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGANXT_template import FCoEGANXT
        return FCoEGANXT(self)

    @property
    def FCoEGIEIL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEIL_template import FCoEGIEIL
        return FCoEGIEIL(self)

    @property
    def FCoEGIDPN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDPN_template import FCoEGIDPN
        return FCoEGIDPN(self)

    @property
    def FCoEGFPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFPNID_template import FCoEGFPNID
        return FCoEGFPNID(self)

    @property
    def FCoEGPSC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPSC_template import FCoEGPSC
        return FCoEGPSC(self)

    @property
    def FCoEGSES(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSES_template import FCoEGSES
        return FCoEGSES(self)

    @property
    def FCoEGPNFT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNFT_template import FCoEGPNFT
        return FCoEGPNFT(self)

    @property
    def FCoEGIEILN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEILN_template import FCoEGIEILN
        return FCoEGIEILN(self)

    @property
    def FCoEGAPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGAPNL_template import FCoEGAPNL
        return FCoEGAPNL(self)

    @property
    def FCoEGSPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSPNID_template import FCoEGSPNID
        return FCoEGSPNID(self)

    @property
    def FCoERSNNNN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSNNNN_template import FCoERSNNNN
        return FCoERSNNNN(self)

    @property
    def FCoEGNPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNPL_template import FCoEGNPL
        return FCoEGNPL(self)

    @property
    def FCoEGPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPL_template import FCoEGPL
        return FCoEGPL(self)

    @property
    def FCoEGNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNID_template import FCoEGNID
        return FCoEGNID(self)

    @property
    def FCoERPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLT_template import FCoERPLT
        return FCoERPLT(self)

    @property
    def FCoERIELN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERIELN_template import FCoERIELN
        return FCoERIELN(self)

    @property
    def FCoEGPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNL_template import FCoEGPNL
        return FCoEGPNL(self)

    @property
    def FCoEGNNFT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNFT_template import FCoEGNNFT
        return FCoEGNNFT(self)

    @property
    def FCoEGPLNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLNL_template import FCoEGPLNL
        return FCoEGPLNL(self)

    @property
    def FCoERFTID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFTID_template import FCoERFTID
        return FCoERFTID(self)

    @property
    def FCoEGPLML(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLML_template import FCoEGPLML
        return FCoEGPLML(self)

    @property
    def FCoEGPS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPS_template import FCoEGPS
        return FCoEGPS(self)

    @property
    def FCoERCSID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERCSID_template import FCoERCSID
        return FCoERCSID(self)

    @property
    def FCoEGSNNNN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSNNNN_template import FCoEGSNNNN
        return FCoEGSNNNN(self)

    @property
    def FCoEGNNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNID_template import FCoEGNNID
        return FCoEGNNID(self)

    @property
    def FCoEGMID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMID_template import FCoEGMID
        return FCoEGMID(self)

    @property
    def FCoEGIET(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIET_template import FCoEGIET
        return FCoEGIET(self)

    @property
    def FCoERPLM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLM_template import FCoERPLM
        return FCoERPLM(self)

    @property
    def FCoEGPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAB_template import FCoEGPAB
        return FCoEGPAB(self)

    @property
    def FCoEGIEAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEAG_template import FCoEGIEAG
        return FCoEGIEAG(self)

    @property
    def FCoEGIEL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEL_template import FCoEGIEL
        return FCoEGIEL(self)

    @property
    def FCoEGPAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAG_template import FCoEGPAG
        return FCoEGPAG(self)

    @property
    def FCoEGIDFT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDFT_template import FCoEGIDFT
        return FCoEGIDFT(self)

    @property
    def FCoEGFFID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFFID_template import FCoEGFFID
        return FCoEGFFID(self)

    @property
    def FCoEGMAL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMAL_template import FCoEGMAL
        return FCoEGMAL(self)

    @property
    def FCoEGPT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPT_template import FCoEGPT
        return FCoEGPT(self)

    @property
    def FCoEGPTID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPTID_template import FCoEGPTID
        return FCoEGPTID(self)

    @property
    def FCoEGATIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGATIN_template import FCoEGATIN
        return FCoEGATIN(self)

    @property
    def FCoERFFID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFFID_template import FCoERFFID
        return FCoERFFID(self)

    @property
    def FCoERPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPNL_template import FCoERPNL
        return FCoERPNL(self)

    @property
    def FCoEGDID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGDID_template import FCoEGDID
        return FCoEGDID(self)

    @property
    def FCoEGTIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGTIN_template import FCoEGTIN
        return FCoEGTIN(self)

    @property
    def FCoERPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPL_template import FCoERPL
        return FCoERPL(self)

    @property
    def FCoEGPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLT_template import FCoEGPLT
        return FCoEGPLT(self)

    @property
    def FCoERNNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERNNID_template import FCoERNNID
        return FCoERNNID(self)

    @property
    def FCoEGPPN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPPN_template import FCoEGPPN
        return FCoEGPPN(self)

    @property
    def FCoEGPFCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPFCP_template import FCoEGPFCP
        return FCoEGPFCP(self)

    @property
    def FCoEGPLI(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLI_template import FCoEGPLI
        return FCoEGPLI(self)

    @property
    def FCoEGFN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFN_template import FCoEGFN
        return FCoEGFN(self)

    @property
    def FCoERPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPAB_template import FCoERPAB
        return FCoERPAB(self)

    @property
    def FCoEGFTID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFTID_template import FCoEGFTID
        return FCoEGFTID(self)

    @property
    def FCoERSPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSPNID_template import FCoERSPNID
        return FCoERSPNID(self)

    @property
    def FCoEGIDNN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDNN_template import FCoEGIDNN
        return FCoEGIDNN(self)

    @property
    def FCoEGPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNID_template import FCoEGPNID
        return FCoEGPNID(self)

    @property
    def FCoEEFPSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWRJT_template import FCoEEFPSWRJT
        return FCoEEFPSWRJT(self)

    @property
    def FCoEEFPSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWACC_template import FCoEEFPSWACC
        return FCoEEFPSWACC(self)

    @property
    def FCoEESCSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWACC_template import FCoEESCSWACC
        return FCoEESCSWACC(self)

    @property
    def FCoERDISWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWRJT_template import FCoERDISWRJT
        return FCoERDISWRJT(self)

    @property
    def FCoEMRRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRRequest_template import FCoEMRRequest
        return FCoEMRRequest(self)

    @property
    def FCoELSARequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSARequest_template import FCoELSARequest
        return FCoELSARequest(self)

    @property
    def FCoEDIASWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWRJT_template import FCoEDIASWRJT
        return FCoEDIASWRJT(self)

    @property
    def FCoEMRSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWRJT_template import FCoEMRSWRJT
        return FCoEMRSWRJT(self)

    @property
    def FCoEDIASWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWACC_template import FCoEDIASWACC
        return FCoEDIASWACC(self)

    @property
    def FCoERDISWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWACC_template import FCoERDISWACC
        return FCoERDISWACC(self)

    @property
    def FCoEESCSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWRJT_template import FCoEESCSWRJT
        return FCoEESCSWRJT(self)

    @property
    def FCoELSURequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSURequest_template import FCoELSURequest
        return FCoELSURequest(self)

    @property
    def FCoEESCRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCRequest_template import FCoEESCRequest
        return FCoEESCRequest(self)

    @property
    def FCoEELPSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWACC_template import FCoEELPSWACC
        return FCoEELPSWACC(self)

    @property
    def FCoEELPSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWRJT_template import FCoEELPSWRJT
        return FCoEELPSWRJT(self)

    @property
    def FCoEMRSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWACC_template import FCoEMRSWACC
        return FCoEMRSWACC(self)

    @property
    def FCoEELPRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPRequest_template import FCoEELPRequest
        return FCoEELPRequest(self)

    @property
    def FCoEDIARequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIARequest_template import FCoEDIARequest
        return FCoEDIARequest(self)

    @property
    def FCoERDIRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDIRequest_template import FCoERDIRequest
        return FCoERDIRequest(self)

    @property
    def FCoEHLORequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEHLORequest_template import FCoEHLORequest
        return FCoEHLORequest(self)

    @property
    def FCoEEFPRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPRequest_template import FCoEEFPRequest
        return FCoEEFPRequest(self)

    @property
    def Fip(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fip_template import Fip
        return Fip(self)

    @property
    def FipClearVirtualLinksFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipClearVirtualLinksFcf_template import FipClearVirtualLinksFcf
        return FipClearVirtualLinksFcf(self)

    @property
    def FipDiscoveryAdvertisementFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoveryAdvertisementFcf_template import FipDiscoveryAdvertisementFcf
        return FipDiscoveryAdvertisementFcf(self)

    @property
    def FipDiscoverySolicitationEnode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationEnode_template import FipDiscoverySolicitationEnode
        return FipDiscoverySolicitationEnode(self)

    @property
    def FipDiscoverySolicitationFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationFcf_template import FipDiscoverySolicitationFcf
        return FipDiscoverySolicitationFcf(self)

    @property
    def FipElpRequestFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpRequestFcf_template import FipElpRequestFcf
        return FipElpRequestFcf(self)

    @property
    def FipElpSwAccFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwAccFcf_template import FipElpSwAccFcf
        return FipElpSwAccFcf(self)

    @property
    def FipElpSwRjtFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwRjtFcf_template import FipElpSwRjtFcf
        return FipElpSwRjtFcf(self)

    @property
    def FipFabricLogoEnode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoEnode_template import FipFabricLogoEnode
        return FipFabricLogoEnode(self)

    @property
    def FipFabricLogoLsAccFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsAccFcf_template import FipFabricLogoLsAccFcf
        return FipFabricLogoLsAccFcf(self)

    @property
    def FipFabricLogoLsRjtFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsRjtFcf_template import FipFabricLogoLsRjtFcf
        return FipFabricLogoLsRjtFcf(self)

    @property
    def FipFlogiLsAccFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsAccFcf_template import FipFlogiLsAccFcf
        return FipFlogiLsAccFcf(self)

    @property
    def FipFlogiLsRjtFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsRjtFcf_template import FipFlogiLsRjtFcf
        return FipFlogiLsRjtFcf(self)

    @property
    def FipFlogiRequestEnode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiRequestEnode_template import FipFlogiRequestEnode
        return FipFlogiRequestEnode(self)

    @property
    def FipKeepAliveEnode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveEnode_template import FipKeepAliveEnode
        return FipKeepAliveEnode(self)

    @property
    def FipKeepAliveVnport(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveVnport_template import FipKeepAliveVnport
        return FipKeepAliveVnport(self)

    @property
    def FipNpivFdicsLsAccFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdicsLsAccFcf_template import FipNpivFdicsLsAccFcf
        return FipNpivFdicsLsAccFcf(self)

    @property
    def FipNpivFdiscLsRjtFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscLsRjtFcf_template import FipNpivFdiscLsRjtFcf
        return FipNpivFdiscLsRjtFcf(self)

    @property
    def FipNpivFdiscRequestEnode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscRequestEnode_template import FipNpivFdiscRequestEnode
        return FipNpivFdiscRequestEnode(self)

    @property
    def FipVendorSpecific(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVendorSpecific_template import FipVendorSpecific
        return FipVendorSpecific(self)

    @property
    def FipVlanNotificationFcf(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanNotificationFcf_template import FipVlanNotificationFcf
        return FipVlanNotificationFcf(self)

    @property
    def FipVlanRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanRequest_template import FipVlanRequest
        return FipVlanRequest(self)

    @property
    def FcFabricLogoEnode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoEnode_template import FcFabricLogoEnode
        return FcFabricLogoEnode(self)

    @property
    def FcFabricLogoLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsAcc_template import FcFabricLogoLsAcc
        return FcFabricLogoLsAcc(self)

    @property
    def FcFabricLogoLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsRjt_template import FcFabricLogoLsRjt
        return FcFabricLogoLsRjt(self)

    @property
    def FcFlogiLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsAcc_template import FcFlogiLsAcc
        return FcFlogiLsAcc(self)

    @property
    def FcFlogiLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsRjt_template import FcFlogiLsRjt
        return FcFlogiLsRjt(self)

    @property
    def FcFlogiRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiRequest_template import FcFlogiRequest
        return FcFlogiRequest(self)

    @property
    def FcPlogiLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsAcc_template import FcPlogiLsAcc
        return FcPlogiLsAcc(self)

    @property
    def FcPlogiLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsRjt_template import FcPlogiLsRjt
        return FcPlogiLsRjt(self)

    @property
    def FcPlogiRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiRequest_template import FcPlogiRequest
        return FcPlogiRequest(self)

    @property
    def FcNpivFdicsLsAcc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdicsLsAcc_template import FcNpivFdicsLsAcc
        return FcNpivFdicsLsAcc(self)

    @property
    def FcNpivFdiscLsRjt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscLsRjt_template import FcNpivFdiscLsRjt
        return FcNpivFdiscLsRjt(self)

    @property
    def FcNpivFdiscRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscRequest_template import FcNpivFdiscRequest
        return FcNpivFdiscRequest(self)

    @property
    def FcScrRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcScrRequest_template import FcScrRequest
        return FcScrRequest(self)

    @property
    def FcRscn(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRscn_template import FcRscn
        return FcRscn(self)

    @property
    def FCGCSID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGCSID_template import FCGCSID
        return FCGCSID(self)

    @property
    def FCGANXT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGANXT_template import FCGANXT
        return FCGANXT(self)

    @property
    def FCGIEIL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEIL_template import FCGIEIL
        return FCGIEIL(self)

    @property
    def FCGIDPN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIDPN_template import FCGIDPN
        return FCGIDPN(self)

    @property
    def FCGFPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFPNID_template import FCGFPNID
        return FCGFPNID(self)

    @property
    def FCGPSC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPSC_template import FCGPSC
        return FCGPSC(self)

    @property
    def FCGSES(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGSES_template import FCGSES
        return FCGSES(self)

    @property
    def FCGPNFT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPNFT_template import FCGPNFT
        return FCGPNFT(self)

    @property
    def FCGIEILN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEILN_template import FCGIEILN
        return FCGIEILN(self)

    @property
    def FCGAPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGAPNL_template import FCGAPNL
        return FCGAPNL(self)

    @property
    def FCGSPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGSPNID_template import FCGSPNID
        return FCGSPNID(self)

    @property
    def FCRSNNNN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRSNNNN_template import FCRSNNNN
        return FCRSNNNN(self)

    @property
    def FCGNPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNPL_template import FCGNPL
        return FCGNPL(self)

    @property
    def FCGPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPL_template import FCGPL
        return FCGPL(self)

    @property
    def FCGNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNID_template import FCGNID
        return FCGNID(self)

    @property
    def FCRPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPLT_template import FCRPLT
        return FCRPLT(self)

    @property
    def FCRIELN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRIELN_template import FCRIELN
        return FCRIELN(self)

    @property
    def FCGPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPNL_template import FCGPNL
        return FCGPNL(self)

    @property
    def FCGNNFT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNNFT_template import FCGNNFT
        return FCGNNFT(self)

    @property
    def FCGPLNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLNL_template import FCGPLNL
        return FCGPLNL(self)

    @property
    def FCRFTID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRFTID_template import FCRFTID
        return FCRFTID(self)

    @property
    def FCGPLML(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLML_template import FCGPLML
        return FCGPLML(self)

    @property
    def FCGPS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPS_template import FCGPS
        return FCGPS(self)

    @property
    def FCRCSID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRCSID_template import FCRCSID
        return FCRCSID(self)

    @property
    def FCGSNNNN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGSNNNN_template import FCGSNNNN
        return FCGSNNNN(self)

    @property
    def FCGNNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNNID_template import FCGNNID
        return FCGNNID(self)

    @property
    def FCGMID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGMID_template import FCGMID
        return FCGMID(self)

    @property
    def FCGIET(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIET_template import FCGIET
        return FCGIET(self)

    @property
    def FCRPLM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPLM_template import FCRPLM
        return FCRPLM(self)

    @property
    def FCGPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPAB_template import FCGPAB
        return FCGPAB(self)

    @property
    def FCGIEAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEAG_template import FCGIEAG
        return FCGIEAG(self)

    @property
    def FCGIEL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEL_template import FCGIEL
        return FCGIEL(self)

    @property
    def FCGPAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPAG_template import FCGPAG
        return FCGPAG(self)

    @property
    def FCGIDFT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIDFT_template import FCGIDFT
        return FCGIDFT(self)

    @property
    def FCGFFID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFFID_template import FCGFFID
        return FCGFFID(self)

    @property
    def FCGMAL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGMAL_template import FCGMAL
        return FCGMAL(self)

    @property
    def FCGPT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPT_template import FCGPT
        return FCGPT(self)

    @property
    def FCGPTID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPTID_template import FCGPTID
        return FCGPTID(self)

    @property
    def FCGATIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGATIN_template import FCGATIN
        return FCGATIN(self)

    @property
    def FCRFFID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRFFID_template import FCRFFID
        return FCRFFID(self)

    @property
    def FCRPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPNL_template import FCRPNL
        return FCRPNL(self)

    @property
    def FCGDID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGDID_template import FCGDID
        return FCGDID(self)

    @property
    def FCGTIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGTIN_template import FCGTIN
        return FCGTIN(self)

    @property
    def FCRPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPL_template import FCRPL
        return FCRPL(self)

    @property
    def FCGPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLT_template import FCGPLT
        return FCGPLT(self)

    @property
    def FCRNNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRNNID_template import FCRNNID
        return FCRNNID(self)

    @property
    def FCGPPN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPPN_template import FCGPPN
        return FCGPPN(self)

    @property
    def FCGPFCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPFCP_template import FCGPFCP
        return FCGPFCP(self)

    @property
    def FCGPLI(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLI_template import FCGPLI
        return FCGPLI(self)

    @property
    def FCGFN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFN_template import FCGFN
        return FCGFN(self)

    @property
    def FCDAID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDAID_template import FCDAID
        return FCDAID(self)

    @property
    def FCRPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPAB_template import FCRPAB
        return FCRPAB(self)

    @property
    def FCGFTID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFTID_template import FCGFTID
        return FCGFTID(self)

    @property
    def FCRSPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRSPNID_template import FCRSPNID
        return FCRSPNID(self)

    @property
    def FCGIDNN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIDNN_template import FCGIDNN
        return FCGIDNN(self)

    @property
    def FCGPNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPNID_template import FCGPNID
        return FCGPNID(self)

    @property
    def FCEFPSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCEFPSWRJT_template import FCEFPSWRJT
        return FCEFPSWRJT(self)

    @property
    def FCEFPSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCEFPSWACC_template import FCEFPSWACC
        return FCEFPSWACC(self)

    @property
    def FCESCSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCESCSWACC_template import FCESCSWACC
        return FCESCSWACC(self)

    @property
    def FCRDISWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRDISWRJT_template import FCRDISWRJT
        return FCRDISWRJT(self)

    @property
    def FCMRRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCMRRequest_template import FCMRRequest
        return FCMRRequest(self)

    @property
    def FCLSARequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCLSARequest_template import FCLSARequest
        return FCLSARequest(self)

    @property
    def FCDIASWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDIASWRJT_template import FCDIASWRJT
        return FCDIASWRJT(self)

    @property
    def FCMRSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCMRSWRJT_template import FCMRSWRJT
        return FCMRSWRJT(self)

    @property
    def FCDIASWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDIASWACC_template import FCDIASWACC
        return FCDIASWACC(self)

    @property
    def FCRDISWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRDISWACC_template import FCRDISWACC
        return FCRDISWACC(self)

    @property
    def FCESCSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCESCSWRJT_template import FCESCSWRJT
        return FCESCSWRJT(self)

    @property
    def FCLSURequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCLSURequest_template import FCLSURequest
        return FCLSURequest(self)

    @property
    def FCESCRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCESCRequest_template import FCESCRequest
        return FCESCRequest(self)

    @property
    def FCELPSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCELPSWACC_template import FCELPSWACC
        return FCELPSWACC(self)

    @property
    def FCELPSWRJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCELPSWRJT_template import FCELPSWRJT
        return FCELPSWRJT(self)

    @property
    def FCMRSWACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCMRSWACC_template import FCMRSWACC
        return FCMRSWACC(self)

    @property
    def FCELPRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCELPRequest_template import FCELPRequest
        return FCELPRequest(self)

    @property
    def FCDIARequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDIARequest_template import FCDIARequest
        return FCDIARequest(self)

    @property
    def FCRDIRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRDIRequest_template import FCRDIRequest
        return FCRDIRequest(self)

    @property
    def FCHLORequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCHLORequest_template import FCHLORequest
        return FCHLORequest(self)

    @property
    def FCEFPRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCEFPRequest_template import FCEFPRequest
        return FCEFPRequest(self)

    @property
    def MacInMACv42(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACv42_template import MacInMACv42
        return MacInMACv42(self)

    @property
    def PfcPause(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pfcPause_template import PfcPause
        return PfcPause(self)

    @property
    def Tmpls(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tmpls_template import Tmpls
        return Tmpls(self)

    @property
    def Lldp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lldp_template import Lldp
        return Lldp(self)

    @property
    def Ecp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ecp_template import Ecp
        return Ecp(self)

    @property
    def Esmc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.esmc_template import Esmc
        return Esmc(self)

    @property
    def Trill(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trill_template import Trill
        return Trill(self)

    @property
    def Trillrbchannel(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trillrbchannel_template import Trillrbchannel
        return Trillrbchannel(self)

    @property
    def Trilloamechoreq(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trilloamechoreq_template import Trilloamechoreq
        return Trilloamechoreq(self)

    @property
    def Trilloamechoreply(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trilloamechoreply_template import Trilloamechoreply
        return Trilloamechoreply(self)

    @property
    def Fabricpath(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fabricpath_template import Fabricpath
        return Fabricpath(self)

    @property
    def Pbb(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pbb_template import Pbb
        return Pbb(self)

    @property
    def Avtp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtp_template import Avtp
        return Avtp(self)

    @property
    def MaapHeader(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.maapHeader_template import MaapHeader
        return MaapHeader(self)

    @property
    def MsrpMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpMessage_template import MsrpMessage
        return MsrpMessage(self)

    @property
    def MsrpVectorAttribute(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpVectorAttribute_template import MsrpVectorAttribute
        return MsrpVectorAttribute(self)

    @property
    def MmrpMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpMessage_template import MmrpMessage
        return MmrpMessage(self)

    @property
    def MmrpVectorAttribute(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpVectorAttribute_template import MmrpVectorAttribute
        return MmrpVectorAttribute(self)

    @property
    def MvrpMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpMessage_template import MvrpMessage
        return MvrpMessage(self)

    @property
    def MvrpVectorAttribute(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpVectorAttribute_template import MvrpVectorAttribute
        return MvrpVectorAttribute(self)

    @property
    def MrpThreePackedEvent(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpThreePackedEvent_template import MrpThreePackedEvent
        return MrpThreePackedEvent(self)

    @property
    def MrpFourPackedEvent(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpFourPackedEvent_template import MrpFourPackedEvent
        return MrpFourPackedEvent(self)

    @property
    def EndMark(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.endMark_template import EndMark
        return EndMark(self)

    @property
    def BMacHeader(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bMacHeader_template import BMacHeader
        return BMacHeader(self)

    @property
    def BVlanHeader(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bVlanHeader_template import BVlanHeader
        return BVlanHeader(self)

    @property
    def ITagHeader(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iTagHeader_template import ITagHeader
        return ITagHeader(self)

    @property
    def PreferredPwMplsCw(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.preferredPwMplsCw_template import PreferredPwMplsCw
        return PreferredPwMplsCw(self)

    @property
    def RTag(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rTag_template import RTag
        return RTag(self)

    @property
    def Macsec(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macsec_template import Macsec
        return Macsec(self)

    @property
    def MacsecHw(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macsecHw_template import MacsecHw
        return MacsecHw(self)

    @property
    def PayloadProtocolType(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.payloadProtocolType_template import PayloadProtocolType
        return PayloadProtocolType(self)

    @property
    def Amt(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.amt_template import Amt
        return Amt(self)

    @property
    def Cgmp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cgmp_template import Cgmp
        return Cgmp(self)

    @property
    def Ddp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ddp_template import Ddp
        return Ddp(self)

    @property
    def IsisL1CSNPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1CSNPDU_template import IsisL1CSNPDU
        return IsisL1CSNPDU(self)

    @property
    def IsisLevel1LANHelloPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LANHelloPDU_template import IsisLevel1LANHelloPDU
        return IsisLevel1LANHelloPDU(self)

    @property
    def IsisLevel1LinkStatePDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LinkStatePDU_template import IsisLevel1LinkStatePDU
        return IsisLevel1LinkStatePDU(self)

    @property
    def IsisL1PSNPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1PSNPDU_template import IsisL1PSNPDU
        return IsisL1PSNPDU(self)

    @property
    def IsisL2CSNPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2CSNPDU_template import IsisL2CSNPDU
        return IsisL2CSNPDU(self)

    @property
    def IsisLevel2LANHelloPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LANHelloPDU_template import IsisLevel2LANHelloPDU
        return IsisLevel2LANHelloPDU(self)

    @property
    def IsisLevel2LinkStatePDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LinkStatePDU_template import IsisLevel2LinkStatePDU
        return IsisLevel2LinkStatePDU(self)

    @property
    def IsisL2PSNPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2PSNPDU_template import IsisL2PSNPDU
        return IsisL2PSNPDU(self)

    @property
    def IsisPPPHelloPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisPPPHelloPDU_template import IsisPPPHelloPDU
        return IsisPPPHelloPDU(self)

    @property
    def IsisL1McastCSNPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastCSNPDU_template import IsisL1McastCSNPDU
        return IsisL1McastCSNPDU(self)

    @property
    def IsisL1McastLinkStatePDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastLinkStatePDU_template import IsisL1McastLinkStatePDU
        return IsisL1McastLinkStatePDU(self)

    @property
    def IsisL1McastPSNPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastPSNPDU_template import IsisL1McastPSNPDU
        return IsisL1McastPSNPDU(self)

    @property
    def Ipv6Authentication(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Authentication_template import Ipv6Authentication
        return Ipv6Authentication(self)

    @property
    def Ipv6Encapsulation(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Encapsulation_template import Ipv6Encapsulation
        return Ipv6Encapsulation(self)

    @property
    def Ipv6Pseudo(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Pseudo_template import Ipv6Pseudo
        return Ipv6Pseudo(self)

    @property
    def Ipv6Routing(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Routing_template import Ipv6Routing
        return Ipv6Routing(self)

    @property
    def Ipv6RoutingType0(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType0_template import Ipv6RoutingType0
        return Ipv6RoutingType0(self)

    @property
    def Ipv6RoutingType2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType2_template import Ipv6RoutingType2
        return Ipv6RoutingType2(self)

    @property
    def Ipv6RoutingType4(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType4_template import Ipv6RoutingType4
        return Ipv6RoutingType4(self)

    @property
    def Ipv6GSRHType4(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6GSRHType4_template import Ipv6GSRHType4
        return Ipv6GSRHType4(self)

    @property
    def Ipv4(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv4_template import Ipv4
        return Ipv4(self)

    @property
    def Ipv6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6_template import Ipv6
        return Ipv6(self)

    @property
    def Ipv6GSRH(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6GSRH_template import Ipv6GSRH
        return Ipv6GSRH(self)

    @property
    def Ipv6Fragment(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Fragment_template import Ipv6Fragment
        return Ipv6Fragment(self)

    @property
    def Ipv6HopByHopOptions(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptions_template import Ipv6HopByHopOptions
        return Ipv6HopByHopOptions(self)

    @property
    def Ipv6HopByHopOptionsWithIOAM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptionsWithIOAM_template import Ipv6HopByHopOptionsWithIOAM
        return Ipv6HopByHopOptionsWithIOAM(self)

    @property
    def Ipv6DestinationOptions(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6DestinationOptions_template import Ipv6DestinationOptions
        return Ipv6DestinationOptions(self)

    @property
    def Icmpv1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv1_template import Icmpv1
        return Icmpv1(self)

    @property
    def Icmpv2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv2_template import Icmpv2
        return Icmpv2(self)

    @property
    def Icmpv9(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv9_template import Icmpv9
        return Icmpv9(self)

    @property
    def Icmpv6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv6_template import Icmpv6
        return Icmpv6(self)

    @property
    def Igmpv1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv1_template import Igmpv1
        return Igmpv1(self)

    @property
    def Igmpv2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv2_template import Igmpv2
        return Igmpv2(self)

    @property
    def Igmpv3MembershipQuery(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipQuery_template import Igmpv3MembershipQuery
        return Igmpv3MembershipQuery(self)

    @property
    def Igmpv3MembershipReport(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipReport_template import Igmpv3MembershipReport
        return Igmpv3MembershipReport(self)

    @property
    def Ipx(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipx_template import Ipx
        return Ipx(self)

    @property
    def Gre(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gre_template import Gre
        return Gre(self)

    @property
    def GTPuOptionalFields(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gTPuOptionalFields_template import GTPuOptionalFields
        return GTPuOptionalFields(self)

    @property
    def Gtpu(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gtpu_template import Gtpu
        return Gtpu(self)

    @property
    def L2TPv3ControlIP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlIP_template import L2TPv3ControlIP
        return L2TPv3ControlIP(self)

    @property
    def L2TPv3DataIP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataIP_template import L2TPv3DataIP
        return L2TPv3DataIP(self)

    @property
    def MinimalIP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.minimalIP_template import MinimalIP
        return MinimalIP(self)

    @property
    def Mldv1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv1_template import Mldv1
        return Mldv1(self)

    @property
    def Mldv2Query(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Query_template import Mldv2Query
        return Mldv2Query(self)

    @property
    def Mldv2Report(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Report_template import Mldv2Report
        return Mldv2Report(self)

    @property
    def MobileIPv6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIPv6_template import MobileIPv6
        return MobileIPv6(self)

    @property
    def Nvgre(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nvgre_template import Nvgre
        return Nvgre(self)

    @property
    def Ospfv2Hello(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2Hello_template import Ospfv2Hello
        return Ospfv2Hello(self)

    @property
    def Ospfv2DatabaseDescription(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2DatabaseDescription_template import Ospfv2DatabaseDescription
        return Ospfv2DatabaseDescription(self)

    @property
    def Ospfv2LSAAcknowledgement(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAAcknowledgement_template import Ospfv2LSAAcknowledgement
        return Ospfv2LSAAcknowledgement(self)

    @property
    def Ospfv2LSARequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSARequest_template import Ospfv2LSARequest
        return Ospfv2LSARequest(self)

    @property
    def Ospfv2LSAUpdate(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAUpdate_template import Ospfv2LSAUpdate
        return Ospfv2LSAUpdate(self)

    @property
    def Ospfv3Hello(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3Hello_template import Ospfv3Hello
        return Ospfv3Hello(self)

    @property
    def Ospfv3DatabaseDescription(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3DatabaseDescription_template import Ospfv3DatabaseDescription
        return Ospfv3DatabaseDescription(self)

    @property
    def Ospfv3LSAAcknowledgement(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAAcknowledgement_template import Ospfv3LSAAcknowledgement
        return Ospfv3LSAAcknowledgement(self)

    @property
    def Ospfv3LSARequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSARequest_template import Ospfv3LSARequest
        return Ospfv3LSARequest(self)

    @property
    def Ospfv3LSAUpdate(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAUpdate_template import Ospfv3LSAUpdate
        return Ospfv3LSAUpdate(self)

    @property
    def PimdmAssert(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmAssert_template import PimdmAssert
        return PimdmAssert(self)

    @property
    def PimdmGraftGraftAckMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmGraftGraftAckMessage_template import PimdmGraftGraftAckMessage
        return PimdmGraftGraftAckMessage(self)

    @property
    def PimdmHelloMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmHelloMessage_template import PimdmHelloMessage
        return PimdmHelloMessage(self)

    @property
    def PimdmJoinPruneMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmJoinPruneMessage_template import PimdmJoinPruneMessage
        return PimdmJoinPruneMessage(self)

    @property
    def PimdmStateRefresh(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmStateRefresh_template import PimdmStateRefresh
        return PimdmStateRefresh(self)

    @property
    def PimAssert(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimAssert_template import PimAssert
        return PimAssert(self)

    @property
    def PimBootstrapMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimBootstrapMessage_template import PimBootstrapMessage
        return PimBootstrapMessage(self)

    @property
    def PimCandidateRPAdvMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimCandidateRPAdvMessage_template import PimCandidateRPAdvMessage
        return PimCandidateRPAdvMessage(self)

    @property
    def PimHelloMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimHelloMessage_template import PimHelloMessage
        return PimHelloMessage(self)

    @property
    def PimJoinPruneMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimJoinPruneMessage_template import PimJoinPruneMessage
        return PimJoinPruneMessage(self)

    @property
    def PimRegister(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegister_template import PimRegister
        return PimRegister(self)

    @property
    def PimRegisterStopMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegisterStopMessage_template import PimRegisterStopMessage
        return PimRegisterStopMessage(self)

    @property
    def Rsvp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rsvp_template import Rsvp
        return Rsvp(self)

    @property
    def Rgmp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rgmp_template import Rgmp
        return Rgmp(self)

    @property
    def Rtmp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtmp_template import Rtmp
        return Rtmp(self)

    @property
    def Vxlan(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlan_template import Vxlan
        return Vxlan(self)

    @property
    def Geneve(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneve_template import Geneve
        return Geneve(self)

    @property
    def Genevewithtelemetry(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.genevewithtelemetry_template import Genevewithtelemetry
        return Genevewithtelemetry(self)

    @property
    def Intmetadata(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intmetadata_template import Intmetadata
        return Intmetadata(self)

    @property
    def Intshimheader(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intshimheader_template import Intshimheader
        return Intshimheader(self)

    @property
    def Intprobemarker(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intprobemarker_template import Intprobemarker
        return Intprobemarker(self)

    @property
    def Bier(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bier_template import Bier
        return Bier(self)

    @property
    def ECpri(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpri_template import ECpri
        return ECpri(self)

    @property
    def ECpriMsgType0(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType0_template import ECpriMsgType0
        return ECpriMsgType0(self)

    @property
    def ECpriMsgType1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType1_template import ECpriMsgType1
        return ECpriMsgType1(self)

    @property
    def ECpriMsgType2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType2_template import ECpriMsgType2
        return ECpriMsgType2(self)

    @property
    def ECpriMsgType3(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType3_template import ECpriMsgType3
        return ECpriMsgType3(self)

    @property
    def ECpriMsgType4(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType4_template import ECpriMsgType4
        return ECpriMsgType4(self)

    @property
    def ECpriMsgType5(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType5_template import ECpriMsgType5
        return ECpriMsgType5(self)

    @property
    def ECpriMsgType6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType6_template import ECpriMsgType6
        return ECpriMsgType6(self)

    @property
    def ECpriMsgType7(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType7_template import ECpriMsgType7
        return ECpriMsgType7(self)

    @property
    def ECpriFaultNotify(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriFaultNotify_template import ECpriFaultNotify
        return ECpriFaultNotify(self)

    @property
    def ECpriUserData(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriUserData_template import ECpriUserData
        return ECpriUserData(self)

    @property
    def Tcp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tcp_template import Tcp
        return Tcp(self)

    @property
    def Udp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.udp_template import Udp
        return Udp(self)

    @property
    def Bfd(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bfd_template import Bfd
        return Bfd(self)

    @property
    def LISPMapRegister(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRegister_template import LISPMapRegister
        return LISPMapRegister(self)

    @property
    def LISPMapRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRequest_template import LISPMapRequest
        return LISPMapRequest(self)

    @property
    def LISPMapReply(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapReply_template import LISPMapReply
        return LISPMapReply(self)

    @property
    def LISPEncapsulatedControlMessage(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPEncapsulatedControlMessage_template import LISPEncapsulatedControlMessage
        return LISPEncapsulatedControlMessage(self)

    @property
    def LISPMapNotify(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapNotify_template import LISPMapNotify
        return LISPMapNotify(self)

    @property
    def LISP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISP_template import LISP
        return LISP(self)

    @property
    def Dhcp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcp_template import Dhcp
        return Dhcp(self)

    @property
    def Dnsquery(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dnsquery_template import Dnsquery
        return Dnsquery(self)

    @property
    def Dnsresponse(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dnsresponse_template import Dnsresponse
        return Dnsresponse(self)

    @property
    def DhcpWithPadding(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpWithPadding_template import DhcpWithPadding
        return DhcpWithPadding(self)

    @property
    def Dhcpv6ClientServer(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6ClientServer_template import Dhcpv6ClientServer
        return Dhcpv6ClientServer(self)

    @property
    def Dhcpv6Relay(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6Relay_template import Dhcpv6Relay
        return Dhcpv6Relay(self)

    @property
    def LdpNotification(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpNotification_template import LdpNotification
        return LdpNotification(self)

    @property
    def LdpHello(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpHello_template import LdpHello
        return LdpHello(self)

    @property
    def LdpInitialization(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpInitialization_template import LdpInitialization
        return LdpInitialization(self)

    @property
    def LdpKeepAlive(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpKeepAlive_template import LdpKeepAlive
        return LdpKeepAlive(self)

    @property
    def LdpAddress(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddress_template import LdpAddress
        return LdpAddress(self)

    @property
    def LdpAddresWithdraw(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddresWithdraw_template import LdpAddresWithdraw
        return LdpAddresWithdraw(self)

    @property
    def LdpLabelMapping(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelMapping_template import LdpLabelMapping
        return LdpLabelMapping(self)

    @property
    def LdpLabelRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRequest_template import LdpLabelRequest
        return LdpLabelRequest(self)

    @property
    def LdpLabelAbortRequest(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelAbortRequest_template import LdpLabelAbortRequest
        return LdpLabelAbortRequest(self)

    @property
    def LdpLabelWithdraw(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelWithdraw_template import LdpLabelWithdraw
        return LdpLabelWithdraw(self)

    @property
    def LdpLabelRelease(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRelease_template import LdpLabelRelease
        return LdpLabelRelease(self)

    @property
    def L2TPv2Control(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Control_template import L2TPv2Control
        return L2TPv2Control(self)

    @property
    def L2TPv2Data(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Data_template import L2TPv2Data
        return L2TPv2Data(self)

    @property
    def L2TPv3ControlUDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlUDP_template import L2TPv3ControlUDP
        return L2TPv3ControlUDP(self)

    @property
    def L2TPv3DataUDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataUDP_template import L2TPv3DataUDP
        return L2TPv3DataUDP(self)

    @property
    def MobileIP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIP_template import MobileIP
        return MobileIP(self)

    @property
    def Msdp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msdp_template import Msdp
        return Msdp(self)

    @property
    def PTPv2udp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2udp_template import PTPv2udp
        return PTPv2udp(self)

    @property
    def Rip1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip1_template import Rip1
        return Rip1(self)

    @property
    def Rip2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip2_template import Rip2
        return Rip2(self)

    @property
    def Ripng(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ripng_template import Ripng
        return Ripng(self)

    @property
    def Rtp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtp_template import Rtp
        return Rtp(self)

    @property
    def HTTPGET(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTPGET_template import HTTPGET
        return HTTPGET(self)

    @property
    def HTTP200OK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTP200OK_template import HTTP200OK
        return HTTP200OK(self)

    @property
    def RTSPDESCRIBE(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSPDESCRIBE_template import RTSPDESCRIBE
        return RTSPDESCRIBE(self)

    @property
    def RTSPReply(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSPReply_template import RTSPReply
        return RTSPReply(self)

    @property
    def IMAPRequestCapability(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAPRequestCapability_template import IMAPRequestCapability
        return IMAPRequestCapability(self)

    @property
    def IMAPResponseCapabilityOK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAPResponseCapabilityOK_template import IMAPResponseCapabilityOK
        return IMAPResponseCapabilityOK(self)

    @property
    def POPRETR1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POPRETR1_template import POPRETR1
        return POPRETR1(self)

    @property
    def POPOK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POPOK_template import POPOK
        return POPOK(self)

    @property
    def SMTPMAILFROM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTPMAILFROM_template import SMTPMAILFROM
        return SMTPMAILFROM(self)

    @property
    def SMTP250OK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTP250OK_template import SMTP250OK
        return SMTP250OK(self)

    @property
    def TDSRemoteProcedureCall(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDSRemoteProcedureCall_template import TDSRemoteProcedureCall
        return TDSRemoteProcedureCall(self)

    @property
    def TDSResponse(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDSResponse_template import TDSResponse
        return TDSResponse(self)

    @property
    def ISCSIDataOut(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSIDataOut_template import ISCSIDataOut
        return ISCSIDataOut(self)

    @property
    def ISCSIDataIn(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSIDataIn_template import ISCSIDataIn
        return ISCSIDataIn(self)

    @property
    def Ntp(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ntp_template import Ntp
        return Ntp(self)

    @property
    def Custom(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.custom_template import Custom
        return Custom(self)

    @property
    def Fc(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fc_template import Fc
        return Fc(self)

    @property
    def DisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The display name of the stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisplayName'])

    @property
    def StackTypeId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackTypeId'])

    @property
    def TemplateName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indiates the protocol template name that is added to a packet in a stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TemplateName'])

    def add(self):
        """Adds a new stack resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved stack resources using find and the newly added stack resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, DisplayName=None, StackTypeId=None, TemplateName=None):
        # type: (str, str, str) -> Stack
        """Finds and retrieves stack resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve stack resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all stack resources from the server.

        Args
        ----
        - DisplayName (str): The display name of the stack.
        - StackTypeId (str): 
        - TemplateName (str): Indiates the protocol template name that is added to a packet in a stack.

        Returns
        -------
        - self: This instance with matching stack resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of stack data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the stack resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Append(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the append operation on the server.

        Append a protocol template after the specified stack object reference.

        DEPRECATED append(Arg2=href, async_operation=bool)string
        --------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('append', payload=payload, response_object=None)

    def AppendProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the appendProtocol operation on the server.

        Append a protocol template after the specified stack object reference.

        appendProtocol(Arg2=href, async_operation=bool)href
        ---------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/.../stack): This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('appendProtocol', payload=payload, response_object=None)

    def GetValidProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getValidProtocols operation on the server.

        Retrieves the list of recommended protocols that can be added on top of the current protocol.

        getValidProtocols(async_operation=bool)list
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This exec returns an array containing: the name of the protocol, the reference of the protocol and the type of it (successor or ancestor)

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getValidProtocols', payload=payload, response_object=None)

    def Insert(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the insert operation on the server.

        Insert a protocol template before the specified stack object reference.

        DEPRECATED insert(Arg2=href, async_operation=bool)string
        --------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('insert', payload=payload, response_object=None)

    def InsertProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the insertProtocol operation on the server.

        Insert a protocol template before the specified stack object reference.

        insertProtocol(Arg2=href, async_operation=bool)href
        ---------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/.../stack): This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('insertProtocol', payload=payload, response_object=None)

    def Remove(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the remove operation on the server.

        Delete the specified stack object reference.

        remove(async_operation=bool)
        ----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('remove', payload=payload, response_object=None)
