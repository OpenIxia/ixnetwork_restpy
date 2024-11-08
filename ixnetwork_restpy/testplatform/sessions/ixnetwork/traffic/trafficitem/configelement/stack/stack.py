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


class Stack(Base):
    """This object helps to specify the field properties of a protocol stack.
    The Stack class encapsulates a list of stack resources that are managed by the system.
    A list of resources can be retrieved from the server using the Stack.find() method.
    """

    __slots__ = "_stack_index"
    _SDM_NAME = "stack"
    _SDM_ATT_MAP = {
        "DisplayName": "displayName",
        "StackTypeId": "stackTypeId",
        "TemplateName": "templateName",
    }
    _SDM_ENUM_MAP = {}

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.field.field import (
            Field,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Field", None) is not None:
                return self._properties.get("Field")
        return Field(self)

    @property
    def SourcePacketHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sourcePacketHeader_template.SourcePacketHeader): An instance of the SourcePacketHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sourcePacketHeader_template import (
            SourcePacketHeader,
        )

        return SourcePacketHeader(self)

    @property
    def Iec61883624BitData(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec61883624BitData_template.Iec61883624BitData): An instance of the Iec61883624BitData traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec61883624BitData_template import (
            Iec61883624BitData,
        )

        return Iec61883624BitData(self)

    @property
    def RealTimeTransportControlProtocol(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol_template.RealTimeTransportControlProtocol): An instance of the RealTimeTransportControlProtocol traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol_template import (
            RealTimeTransportControlProtocol,
        )

        return RealTimeTransportControlProtocol(self)

    @property
    def Iec618831(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec618831_template.Iec618831): An instance of the Iec618831 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec618831_template import (
            Iec618831,
        )

        return Iec618831(self)

    @property
    def H264csrc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264csrc_template.H264csrc): An instance of the H264csrc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264csrc_template import (
            H264csrc,
        )

        return H264csrc(self)

    @property
    def H264SH(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264SH_template.H264SH): An instance of the H264SH traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264SH_template import (
            H264SH,
        )

        return H264SH(self)

    @property
    def Avtpdu(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtpdu_template.Avtpdu): An instance of the Avtpdu traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtpdu_template import (
            Avtpdu,
        )

        return Avtpdu(self)

    @property
    def H264(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264_template.H264): An instance of the H264 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264_template import (
            H264,
        )

        return H264(self)

    @property
    def Jpeg2000VideoFormat(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpeg2000VideoFormat_template.Jpeg2000VideoFormat): An instance of the Jpeg2000VideoFormat traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpeg2000VideoFormat_template import (
            Jpeg2000VideoFormat,
        )

        return Jpeg2000VideoFormat(self)

    @property
    def JpegVideoFormat(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpegVideoFormat_template.JpegVideoFormat): An instance of the JpegVideoFormat traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpegVideoFormat_template import (
            JpegVideoFormat,
        )

        return JpegVideoFormat(self)

    @property
    def SdiVideoFormat(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sdiVideoFormat_template.SdiVideoFormat): An instance of the SdiVideoFormat traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sdiVideoFormat_template import (
            SdiVideoFormat,
        )

        return SdiVideoFormat(self)

    @property
    def MpegtsPayload(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpegtsPayload_template.MpegtsPayload): An instance of the MpegtsPayload traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpegtsPayload_template import (
            MpegtsPayload,
        )

        return MpegtsPayload(self)

    @property
    def MmaDataPayload(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmaDataPayload_template.MmaDataPayload): An instance of the MmaDataPayload traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmaDataPayload_template import (
            MmaDataPayload,
        )

        return MmaDataPayload(self)

    @property
    def G723SidMode(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723SidMode_template.G723SidMode): An instance of the G723SidMode traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723SidMode_template import (
            G723SidMode,
        )

        return G723SidMode(self)

    @property
    def G723Framepacking(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking_template.G723Framepacking): An instance of the G723Framepacking traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking_template import (
            G723Framepacking,
        )

        return G723Framepacking(self)

    @property
    def G723Framepacking53(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking53_template.G723Framepacking53): An instance of the G723Framepacking53 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking53_template import (
            G723Framepacking53,
        )

        return G723Framepacking53(self)

    @property
    def CN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.CN_template.CN): An instance of the CN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.CN_template import (
            CN,
        )

        return CN(self)

    @property
    def RealTimeTransportControlProtocol1733(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol1733_template.RealTimeTransportControlProtocol1733): An instance of the RealTimeTransportControlProtocol1733 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol1733_template import (
            RealTimeTransportControlProtocol1733,
        )

        return RealTimeTransportControlProtocol1733(self)

    @property
    def Aal5(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.aal5_template.Aal5): An instance of the Aal5 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.aal5_template import (
            Aal5,
        )

        return Aal5(self)

    @property
    def AtmCell(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmCell_template.AtmCell): An instance of the AtmCell traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmCell_template import (
            AtmCell,
        )

        return AtmCell(self)

    @property
    def AtmAAL5Frame(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmAAL5Frame_template.AtmAAL5Frame): An instance of the AtmAAL5Frame traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmAAL5Frame_template import (
            AtmAAL5Frame,
        )

        return AtmAAL5Frame(self)

    @property
    def EthernetARP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetARP_template.EthernetARP): An instance of the EthernetARP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetARP_template import (
            EthernetARP,
        )

        return EthernetARP(self)

    @property
    def CiscoHDLC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoHDLC_template.CiscoHDLC): An instance of the CiscoHDLC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoHDLC_template import (
            CiscoHDLC,
        )

        return CiscoHDLC(self)

    @property
    def CiscoISL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoISL_template.CiscoISL): An instance of the CiscoISL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoISL_template import (
            CiscoISL,
        )

        return CiscoISL(self)

    @property
    def CiscoFrameRelay(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoFrameRelay_template.CiscoFrameRelay): An instance of the CiscoFrameRelay traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoFrameRelay_template import (
            CiscoFrameRelay,
        )

        return CiscoFrameRelay(self)

    @property
    def Ethernet(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernet_template.Ethernet): An instance of the Ethernet traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernet_template import (
            Ethernet,
        )

        return Ethernet(self)

    @property
    def EthernetNoFCS(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetNoFCS_template.EthernetNoFCS): An instance of the EthernetNoFCS traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetNoFCS_template import (
            EthernetNoFCS,
        )

        return EthernetNoFCS(self)

    @property
    def FrameRelay(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.frameRelay_template.FrameRelay): An instance of the FrameRelay traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.frameRelay_template import (
            FrameRelay,
        )

        return FrameRelay(self)

    @property
    def PppIPCP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPCP_template.PppIPCP): An instance of the PppIPCP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPCP_template import (
            PppIPCP,
        )

        return PppIPCP(self)

    @property
    def PppIPv6CP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPv6CP_template.PppIPv6CP): An instance of the PppIPv6CP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPv6CP_template import (
            PppIPv6CP,
        )

        return PppIPv6CP(self)

    @property
    def Lacp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacp_template.Lacp): An instance of the Lacp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacp_template import (
            Lacp,
        )

        return Lacp(self)

    @property
    def LacpWithoutEthernet(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacpWithoutEthernet_template.LacpWithoutEthernet): An instance of the LacpWithoutEthernet traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacpWithoutEthernet_template import (
            LacpWithoutEthernet,
        )

        return LacpWithoutEthernet(self)

    @property
    def LlcPPP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcPPP_template.LlcPPP): An instance of the LlcPPP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcPPP_template import (
            LlcPPP,
        )

        return LlcPPP(self)

    @property
    def Cfm(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cfm_template.Cfm): An instance of the Cfm traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cfm_template import (
            Cfm,
        )

        return Cfm(self)

    @property
    def LinkOAM(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.linkOAM_template.LinkOAM): An instance of the LinkOAM traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.linkOAM_template import (
            LinkOAM,
        )

        return LinkOAM(self)

    @property
    def Elmi(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.elmi_template.Elmi): An instance of the Elmi traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.elmi_template import (
            Elmi,
        )

        return Elmi(self)

    @property
    def LlcBridgedEthernet(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcBridgedEthernet_template.LlcBridgedEthernet): An instance of the LlcBridgedEthernet traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcBridgedEthernet_template import (
            LlcBridgedEthernet,
        )

        return LlcBridgedEthernet(self)

    @property
    def Llc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llc_template.Llc): An instance of the Llc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llc_template import (
            Llc,
        )

        return Llc(self)

    @property
    def L2VPNATMCellCW(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCellCW_template.L2VPNATMCellCW): An instance of the L2VPNATMCellCW traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCellCW_template import (
            L2VPNATMCellCW,
        )

        return L2VPNATMCellCW(self)

    @property
    def L2VPNATMCWFrame(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCWFrame_template.L2VPNATMCWFrame): An instance of the L2VPNATMCWFrame traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCWFrame_template import (
            L2VPNATMCWFrame,
        )

        return L2VPNATMCWFrame(self)

    @property
    def L2VPNEthernetFrame(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNEthernetFrame_template.L2VPNEthernetFrame): An instance of the L2VPNEthernetFrame traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNEthernetFrame_template import (
            L2VPNEthernetFrame,
        )

        return L2VPNEthernetFrame(self)

    @property
    def L2VPNFrameRelayCW(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayCW_template.L2VPNFrameRelayCW): An instance of the L2VPNFrameRelayCW traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayCW_template import (
            L2VPNFrameRelayCW,
        )

        return L2VPNFrameRelayCW(self)

    @property
    def L2VPNFrameRelayRFC4619CW(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayRFC4619CW_template.L2VPNFrameRelayRFC4619CW): An instance of the L2VPNFrameRelayRFC4619CW traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayRFC4619CW_template import (
            L2VPNFrameRelayRFC4619CW,
        )

        return L2VPNFrameRelayRFC4619CW(self)

    @property
    def L2VPNFrameRelay(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelay_template.L2VPNFrameRelay): An instance of the L2VPNFrameRelay traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelay_template import (
            L2VPNFrameRelay,
        )

        return L2VPNFrameRelay(self)

    @property
    def L2VPNPPPHDLC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPPHDLC_template.L2VPNPPPHDLC): An instance of the L2VPNPPPHDLC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPPHDLC_template import (
            L2VPNPPPHDLC,
        )

        return L2VPNPPPHDLC(self)

    @property
    def L2VPNHDLC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNHDLC_template.L2VPNHDLC): An instance of the L2VPNHDLC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNHDLC_template import (
            L2VPNHDLC,
        )

        return L2VPNHDLC(self)

    @property
    def L2VPNPPP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPP_template.L2VPNPPP): An instance of the L2VPNPPP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPP_template import (
            L2VPNPPP,
        )

        return L2VPNPPP(self)

    @property
    def L2VPNVCTypeIPCW(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNVCTypeIPCW_template.L2VPNVCTypeIPCW): An instance of the L2VPNVCTypeIPCW traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNVCTypeIPCW_template import (
            L2VPNVCTypeIPCW,
        )

        return L2VPNVCTypeIPCW(self)

    @property
    def MacInMAC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMAC_template.MacInMAC): An instance of the MacInMAC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMAC_template import (
            MacInMAC,
        )

        return MacInMAC(self)

    @property
    def MacInMACNoFcs(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACNoFcs_template.MacInMACNoFcs): An instance of the MacInMACNoFcs traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACNoFcs_template import (
            MacInMACNoFcs,
        )

        return MacInMACNoFcs(self)

    @property
    def MarkerPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.markerPDU_template.MarkerPDU): An instance of the MarkerPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.markerPDU_template import (
            MarkerPDU,
        )

        return MarkerPDU(self)

    @property
    def Mpls(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpls_template.Mpls): An instance of the Mpls traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpls_template import (
            Mpls,
        )

        return Mpls(self)

    @property
    def Mplsenull(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mplsenull_template.Mplsenull): An instance of the Mplsenull traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mplsenull_template import (
            Mplsenull,
        )

        return Mplsenull(self)

    @property
    def MstpBPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mstpBPDU_template.MstpBPDU): An instance of the MstpBPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mstpBPDU_template import (
            MstpBPDU,
        )

        return MstpBPDU(self)

    @property
    def MPLSTPEthernetFrame(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.MPLSTPEthernetFrame_template.MPLSTPEthernetFrame): An instance of the MPLSTPEthernetFrame traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.MPLSTPEthernetFrame_template import (
            MPLSTPEthernetFrame,
        )

        return MPLSTPEthernetFrame(self)

    @property
    def OamCCM(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oamCCM_template.OamCCM): An instance of the OamCCM traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oamCCM_template import (
            OamCCM,
        )

        return OamCCM(self)

    @property
    def Ppp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ppp_template.Ppp): An instance of the Ppp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ppp_template import (
            Ppp,
        )

        return Ppp(self)

    @property
    def Pppnohdlc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppnohdlc_template.Pppnohdlc): An instance of the Pppnohdlc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppnohdlc_template import (
            Pppnohdlc,
        )

        return Pppnohdlc(self)

    @property
    def PppLCP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppLCP_template.PppLCP): An instance of the PppLCP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppLCP_template import (
            PppLCP,
        )

        return PppLCP(self)

    @property
    def PppPAPCHAP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppPAPCHAP_template.PppPAPCHAP): An instance of the PppPAPCHAP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppPAPCHAP_template import (
            PppPAPCHAP,
        )

        return PppPAPCHAP(self)

    @property
    def PppoEDiscovery(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoEDiscovery_template.PppoEDiscovery): An instance of the PppoEDiscovery traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoEDiscovery_template import (
            PppoEDiscovery,
        )

        return PppoEDiscovery(self)

    @property
    def PppoESession(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoESession_template.PppoESession): An instance of the PppoESession traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoESession_template import (
            PppoESession,
        )

        return PppoESession(self)

    @property
    def PTPv2(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2_template.PTPv2): An instance of the PTPv2 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2_template import (
            PTPv2,
        )

        return PTPv2(self)

    @property
    def EthernetRARP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetRARP_template.EthernetRARP): An instance of the EthernetRARP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetRARP_template import (
            EthernetRARP,
        )

        return EthernetRARP(self)

    @property
    def RstpBPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rstpBPDU_template.RstpBPDU): An instance of the RstpBPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rstpBPDU_template import (
            RstpBPDU,
        )

        return RstpBPDU(self)

    @property
    def LlcSNAP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcSNAP_template.LlcSNAP): An instance of the LlcSNAP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcSNAP_template import (
            LlcSNAP,
        )

        return LlcSNAP(self)

    @property
    def Snap(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.snap_template.Snap): An instance of the Snap traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.snap_template import (
            Snap,
        )

        return Snap(self)

    @property
    def StpCfgBPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpCfgBPDU_template.StpCfgBPDU): An instance of the StpCfgBPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpCfgBPDU_template import (
            StpCfgBPDU,
        )

        return StpCfgBPDU(self)

    @property
    def StpTCNBPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpTCNBPDU_template.StpTCNBPDU): An instance of the StpTCNBPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpTCNBPDU_template import (
            StpTCNBPDU,
        )

        return StpTCNBPDU(self)

    @property
    def VcMuxBridgedEthernet(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxBridgedEthernet_template.VcMuxBridgedEthernet): An instance of the VcMuxBridgedEthernet traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxBridgedEthernet_template import (
            VcMuxBridgedEthernet,
        )

        return VcMuxBridgedEthernet(self)

    @property
    def VcMuxPPP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxPPP_template.VcMuxPPP): An instance of the VcMuxPPP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxPPP_template import (
            VcMuxPPP,
        )

        return VcMuxPPP(self)

    @property
    def Vlan(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vlan_template.Vlan): An instance of the Vlan traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vlan_template import (
            Vlan,
        )

        return Vlan(self)

    @property
    def Vntag(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vntag_template.Vntag): An instance of the Vntag traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vntag_template import (
            Vntag,
        )

        return Vntag(self)

    @property
    def Vic(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vic_template.Vic): An instance of the Vic traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vic_template import (
            Vic,
        )

        return Vic(self)

    @property
    def VplsEthernet(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vplsEthernet_template.VplsEthernet): An instance of the VplsEthernet traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vplsEthernet_template import (
            VplsEthernet,
        )

        return VplsEthernet(self)

    @property
    def FcoE(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcoE_template.FcoE): An instance of the FcoE traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcoE_template import (
            FcoE,
        )

        return FcoE(self)

    @property
    def FCoEFabricLogo(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogo_template.FCoEFabricLogo): An instance of the FCoEFabricLogo traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogo_template import (
            FCoEFabricLogo,
        )

        return FCoEFabricLogo(self)

    @property
    def FCoEFabricLogoLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsAcc_template.FCoEFabricLogoLsAcc): An instance of the FCoEFabricLogoLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsAcc_template import (
            FCoEFabricLogoLsAcc,
        )

        return FCoEFabricLogoLsAcc(self)

    @property
    def FCoEFabricLogoLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsRjt_template.FCoEFabricLogoLsRjt): An instance of the FCoEFabricLogoLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsRjt_template import (
            FCoEFabricLogoLsRjt,
        )

        return FCoEFabricLogoLsRjt(self)

    @property
    def FCoEFlogiLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsAcc_template.FCoEFlogiLsAcc): An instance of the FCoEFlogiLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsAcc_template import (
            FCoEFlogiLsAcc,
        )

        return FCoEFlogiLsAcc(self)

    @property
    def FCoEFlogiLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsRjt_template.FCoEFlogiLsRjt): An instance of the FCoEFlogiLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsRjt_template import (
            FCoEFlogiLsRjt,
        )

        return FCoEFlogiLsRjt(self)

    @property
    def FCoEFlogiRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiRequest_template.FCoEFlogiRequest): An instance of the FCoEFlogiRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiRequest_template import (
            FCoEFlogiRequest,
        )

        return FCoEFlogiRequest(self)

    @property
    def FCoEPlogiLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsAcc_template.FCoEPlogiLsAcc): An instance of the FCoEPlogiLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsAcc_template import (
            FCoEPlogiLsAcc,
        )

        return FCoEPlogiLsAcc(self)

    @property
    def FCoEPlogiLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsRjt_template.FCoEPlogiLsRjt): An instance of the FCoEPlogiLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsRjt_template import (
            FCoEPlogiLsRjt,
        )

        return FCoEPlogiLsRjt(self)

    @property
    def FCoEPlogiRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiRequest_template.FCoEPlogiRequest): An instance of the FCoEPlogiRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiRequest_template import (
            FCoEPlogiRequest,
        )

        return FCoEPlogiRequest(self)

    @property
    def FCoENpivFdicsLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdicsLsAcc_template.FCoENpivFdicsLsAcc): An instance of the FCoENpivFdicsLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdicsLsAcc_template import (
            FCoENpivFdicsLsAcc,
        )

        return FCoENpivFdicsLsAcc(self)

    @property
    def FCoENpivFdiscLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscLsRjt_template.FCoENpivFdiscLsRjt): An instance of the FCoENpivFdiscLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscLsRjt_template import (
            FCoENpivFdiscLsRjt,
        )

        return FCoENpivFdiscLsRjt(self)

    @property
    def FCoENpivFdiscRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscRequest_template.FCoENpivFdiscRequest): An instance of the FCoENpivFdiscRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscRequest_template import (
            FCoENpivFdiscRequest,
        )

        return FCoENpivFdiscRequest(self)

    @property
    def FCoERscn(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERscn_template.FCoERscn): An instance of the FCoERscn traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERscn_template import (
            FCoERscn,
        )

        return FCoERscn(self)

    @property
    def FCoEScrRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEScrRequest_template.FCoEScrRequest): An instance of the FCoEScrRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEScrRequest_template import (
            FCoEScrRequest,
        )

        return FCoEScrRequest(self)

    @property
    def FCoEGCSID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGCSID_template.FCoEGCSID): An instance of the FCoEGCSID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGCSID_template import (
            FCoEGCSID,
        )

        return FCoEGCSID(self)

    @property
    def FCoEGANXT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGANXT_template.FCoEGANXT): An instance of the FCoEGANXT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGANXT_template import (
            FCoEGANXT,
        )

        return FCoEGANXT(self)

    @property
    def FCoEGIEIL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEIL_template.FCoEGIEIL): An instance of the FCoEGIEIL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEIL_template import (
            FCoEGIEIL,
        )

        return FCoEGIEIL(self)

    @property
    def FCoEGIDPN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDPN_template.FCoEGIDPN): An instance of the FCoEGIDPN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDPN_template import (
            FCoEGIDPN,
        )

        return FCoEGIDPN(self)

    @property
    def FCoEGFPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFPNID_template.FCoEGFPNID): An instance of the FCoEGFPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFPNID_template import (
            FCoEGFPNID,
        )

        return FCoEGFPNID(self)

    @property
    def FCoEGPSC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPSC_template.FCoEGPSC): An instance of the FCoEGPSC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPSC_template import (
            FCoEGPSC,
        )

        return FCoEGPSC(self)

    @property
    def FCoEGSES(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSES_template.FCoEGSES): An instance of the FCoEGSES traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSES_template import (
            FCoEGSES,
        )

        return FCoEGSES(self)

    @property
    def FCoEGPNFT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNFT_template.FCoEGPNFT): An instance of the FCoEGPNFT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNFT_template import (
            FCoEGPNFT,
        )

        return FCoEGPNFT(self)

    @property
    def FCoEGIEILN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEILN_template.FCoEGIEILN): An instance of the FCoEGIEILN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEILN_template import (
            FCoEGIEILN,
        )

        return FCoEGIEILN(self)

    @property
    def FCoEGAPNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGAPNL_template.FCoEGAPNL): An instance of the FCoEGAPNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGAPNL_template import (
            FCoEGAPNL,
        )

        return FCoEGAPNL(self)

    @property
    def FCoEGSPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSPNID_template.FCoEGSPNID): An instance of the FCoEGSPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSPNID_template import (
            FCoEGSPNID,
        )

        return FCoEGSPNID(self)

    @property
    def FCoERSNNNN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSNNNN_template.FCoERSNNNN): An instance of the FCoERSNNNN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSNNNN_template import (
            FCoERSNNNN,
        )

        return FCoERSNNNN(self)

    @property
    def FCoEGNPL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNPL_template.FCoEGNPL): An instance of the FCoEGNPL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNPL_template import (
            FCoEGNPL,
        )

        return FCoEGNPL(self)

    @property
    def FCoEGPL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPL_template.FCoEGPL): An instance of the FCoEGPL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPL_template import (
            FCoEGPL,
        )

        return FCoEGPL(self)

    @property
    def FCoEGNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNID_template.FCoEGNID): An instance of the FCoEGNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNID_template import (
            FCoEGNID,
        )

        return FCoEGNID(self)

    @property
    def FCoERPLT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLT_template.FCoERPLT): An instance of the FCoERPLT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLT_template import (
            FCoERPLT,
        )

        return FCoERPLT(self)

    @property
    def FCoERIELN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERIELN_template.FCoERIELN): An instance of the FCoERIELN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERIELN_template import (
            FCoERIELN,
        )

        return FCoERIELN(self)

    @property
    def FCoEGPNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNL_template.FCoEGPNL): An instance of the FCoEGPNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNL_template import (
            FCoEGPNL,
        )

        return FCoEGPNL(self)

    @property
    def FCoEGNNFT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNFT_template.FCoEGNNFT): An instance of the FCoEGNNFT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNFT_template import (
            FCoEGNNFT,
        )

        return FCoEGNNFT(self)

    @property
    def FCoEGPLNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLNL_template.FCoEGPLNL): An instance of the FCoEGPLNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLNL_template import (
            FCoEGPLNL,
        )

        return FCoEGPLNL(self)

    @property
    def FCoERFTID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFTID_template.FCoERFTID): An instance of the FCoERFTID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFTID_template import (
            FCoERFTID,
        )

        return FCoERFTID(self)

    @property
    def FCoEGPLML(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLML_template.FCoEGPLML): An instance of the FCoEGPLML traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLML_template import (
            FCoEGPLML,
        )

        return FCoEGPLML(self)

    @property
    def FCoEGPS(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPS_template.FCoEGPS): An instance of the FCoEGPS traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPS_template import (
            FCoEGPS,
        )

        return FCoEGPS(self)

    @property
    def FCoERCSID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERCSID_template.FCoERCSID): An instance of the FCoERCSID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERCSID_template import (
            FCoERCSID,
        )

        return FCoERCSID(self)

    @property
    def FCoEGSNNNN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSNNNN_template.FCoEGSNNNN): An instance of the FCoEGSNNNN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSNNNN_template import (
            FCoEGSNNNN,
        )

        return FCoEGSNNNN(self)

    @property
    def FCoEGNNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNID_template.FCoEGNNID): An instance of the FCoEGNNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNID_template import (
            FCoEGNNID,
        )

        return FCoEGNNID(self)

    @property
    def FCoEGMID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMID_template.FCoEGMID): An instance of the FCoEGMID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMID_template import (
            FCoEGMID,
        )

        return FCoEGMID(self)

    @property
    def FCoEGIET(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIET_template.FCoEGIET): An instance of the FCoEGIET traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIET_template import (
            FCoEGIET,
        )

        return FCoEGIET(self)

    @property
    def FCoERPLM(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLM_template.FCoERPLM): An instance of the FCoERPLM traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLM_template import (
            FCoERPLM,
        )

        return FCoERPLM(self)

    @property
    def FCoEGPAB(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAB_template.FCoEGPAB): An instance of the FCoEGPAB traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAB_template import (
            FCoEGPAB,
        )

        return FCoEGPAB(self)

    @property
    def FCoEGIEAG(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEAG_template.FCoEGIEAG): An instance of the FCoEGIEAG traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEAG_template import (
            FCoEGIEAG,
        )

        return FCoEGIEAG(self)

    @property
    def FCoEGIEL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEL_template.FCoEGIEL): An instance of the FCoEGIEL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEL_template import (
            FCoEGIEL,
        )

        return FCoEGIEL(self)

    @property
    def FCoEGPAG(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAG_template.FCoEGPAG): An instance of the FCoEGPAG traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAG_template import (
            FCoEGPAG,
        )

        return FCoEGPAG(self)

    @property
    def FCoEGIDFT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDFT_template.FCoEGIDFT): An instance of the FCoEGIDFT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDFT_template import (
            FCoEGIDFT,
        )

        return FCoEGIDFT(self)

    @property
    def FCoEGFFID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFFID_template.FCoEGFFID): An instance of the FCoEGFFID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFFID_template import (
            FCoEGFFID,
        )

        return FCoEGFFID(self)

    @property
    def FCoEGMAL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMAL_template.FCoEGMAL): An instance of the FCoEGMAL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMAL_template import (
            FCoEGMAL,
        )

        return FCoEGMAL(self)

    @property
    def FCoEGPT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPT_template.FCoEGPT): An instance of the FCoEGPT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPT_template import (
            FCoEGPT,
        )

        return FCoEGPT(self)

    @property
    def FCoEGPTID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPTID_template.FCoEGPTID): An instance of the FCoEGPTID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPTID_template import (
            FCoEGPTID,
        )

        return FCoEGPTID(self)

    @property
    def FCoEGATIN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGATIN_template.FCoEGATIN): An instance of the FCoEGATIN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGATIN_template import (
            FCoEGATIN,
        )

        return FCoEGATIN(self)

    @property
    def FCoERFFID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFFID_template.FCoERFFID): An instance of the FCoERFFID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFFID_template import (
            FCoERFFID,
        )

        return FCoERFFID(self)

    @property
    def FCoERPNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPNL_template.FCoERPNL): An instance of the FCoERPNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPNL_template import (
            FCoERPNL,
        )

        return FCoERPNL(self)

    @property
    def FCoEGDID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGDID_template.FCoEGDID): An instance of the FCoEGDID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGDID_template import (
            FCoEGDID,
        )

        return FCoEGDID(self)

    @property
    def FCoEGTIN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGTIN_template.FCoEGTIN): An instance of the FCoEGTIN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGTIN_template import (
            FCoEGTIN,
        )

        return FCoEGTIN(self)

    @property
    def FCoERPL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPL_template.FCoERPL): An instance of the FCoERPL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPL_template import (
            FCoERPL,
        )

        return FCoERPL(self)

    @property
    def FCoEGPLT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLT_template.FCoEGPLT): An instance of the FCoEGPLT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLT_template import (
            FCoEGPLT,
        )

        return FCoEGPLT(self)

    @property
    def FCoERNNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERNNID_template.FCoERNNID): An instance of the FCoERNNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERNNID_template import (
            FCoERNNID,
        )

        return FCoERNNID(self)

    @property
    def FCoEGPPN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPPN_template.FCoEGPPN): An instance of the FCoEGPPN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPPN_template import (
            FCoEGPPN,
        )

        return FCoEGPPN(self)

    @property
    def FCoEGPFCP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPFCP_template.FCoEGPFCP): An instance of the FCoEGPFCP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPFCP_template import (
            FCoEGPFCP,
        )

        return FCoEGPFCP(self)

    @property
    def FCoEGPLI(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLI_template.FCoEGPLI): An instance of the FCoEGPLI traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLI_template import (
            FCoEGPLI,
        )

        return FCoEGPLI(self)

    @property
    def FCoEGFN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFN_template.FCoEGFN): An instance of the FCoEGFN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFN_template import (
            FCoEGFN,
        )

        return FCoEGFN(self)

    @property
    def FCoERPAB(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPAB_template.FCoERPAB): An instance of the FCoERPAB traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPAB_template import (
            FCoERPAB,
        )

        return FCoERPAB(self)

    @property
    def FCoEGFTID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFTID_template.FCoEGFTID): An instance of the FCoEGFTID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFTID_template import (
            FCoEGFTID,
        )

        return FCoEGFTID(self)

    @property
    def FCoERSPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSPNID_template.FCoERSPNID): An instance of the FCoERSPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSPNID_template import (
            FCoERSPNID,
        )

        return FCoERSPNID(self)

    @property
    def FCoEGIDNN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDNN_template.FCoEGIDNN): An instance of the FCoEGIDNN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDNN_template import (
            FCoEGIDNN,
        )

        return FCoEGIDNN(self)

    @property
    def FCoEGPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNID_template.FCoEGPNID): An instance of the FCoEGPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNID_template import (
            FCoEGPNID,
        )

        return FCoEGPNID(self)

    @property
    def FCoEEFPSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWRJT_template.FCoEEFPSWRJT): An instance of the FCoEEFPSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWRJT_template import (
            FCoEEFPSWRJT,
        )

        return FCoEEFPSWRJT(self)

    @property
    def FCoEEFPSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWACC_template.FCoEEFPSWACC): An instance of the FCoEEFPSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWACC_template import (
            FCoEEFPSWACC,
        )

        return FCoEEFPSWACC(self)

    @property
    def FCoEESCSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWACC_template.FCoEESCSWACC): An instance of the FCoEESCSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWACC_template import (
            FCoEESCSWACC,
        )

        return FCoEESCSWACC(self)

    @property
    def FCoERDISWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWRJT_template.FCoERDISWRJT): An instance of the FCoERDISWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWRJT_template import (
            FCoERDISWRJT,
        )

        return FCoERDISWRJT(self)

    @property
    def FCoEMRRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRRequest_template.FCoEMRRequest): An instance of the FCoEMRRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRRequest_template import (
            FCoEMRRequest,
        )

        return FCoEMRRequest(self)

    @property
    def FCoELSARequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSARequest_template.FCoELSARequest): An instance of the FCoELSARequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSARequest_template import (
            FCoELSARequest,
        )

        return FCoELSARequest(self)

    @property
    def FCoEDIASWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWRJT_template.FCoEDIASWRJT): An instance of the FCoEDIASWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWRJT_template import (
            FCoEDIASWRJT,
        )

        return FCoEDIASWRJT(self)

    @property
    def FCoEMRSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWRJT_template.FCoEMRSWRJT): An instance of the FCoEMRSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWRJT_template import (
            FCoEMRSWRJT,
        )

        return FCoEMRSWRJT(self)

    @property
    def FCoEDIASWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWACC_template.FCoEDIASWACC): An instance of the FCoEDIASWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWACC_template import (
            FCoEDIASWACC,
        )

        return FCoEDIASWACC(self)

    @property
    def FCoERDISWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWACC_template.FCoERDISWACC): An instance of the FCoERDISWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWACC_template import (
            FCoERDISWACC,
        )

        return FCoERDISWACC(self)

    @property
    def FCoEESCSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWRJT_template.FCoEESCSWRJT): An instance of the FCoEESCSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWRJT_template import (
            FCoEESCSWRJT,
        )

        return FCoEESCSWRJT(self)

    @property
    def FCoELSURequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSURequest_template.FCoELSURequest): An instance of the FCoELSURequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSURequest_template import (
            FCoELSURequest,
        )

        return FCoELSURequest(self)

    @property
    def FCoEESCRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCRequest_template.FCoEESCRequest): An instance of the FCoEESCRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCRequest_template import (
            FCoEESCRequest,
        )

        return FCoEESCRequest(self)

    @property
    def FCoEELPSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWACC_template.FCoEELPSWACC): An instance of the FCoEELPSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWACC_template import (
            FCoEELPSWACC,
        )

        return FCoEELPSWACC(self)

    @property
    def FCoEELPSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWRJT_template.FCoEELPSWRJT): An instance of the FCoEELPSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWRJT_template import (
            FCoEELPSWRJT,
        )

        return FCoEELPSWRJT(self)

    @property
    def FCoEMRSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWACC_template.FCoEMRSWACC): An instance of the FCoEMRSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWACC_template import (
            FCoEMRSWACC,
        )

        return FCoEMRSWACC(self)

    @property
    def FCoEELPRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPRequest_template.FCoEELPRequest): An instance of the FCoEELPRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPRequest_template import (
            FCoEELPRequest,
        )

        return FCoEELPRequest(self)

    @property
    def FCoEDIARequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIARequest_template.FCoEDIARequest): An instance of the FCoEDIARequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIARequest_template import (
            FCoEDIARequest,
        )

        return FCoEDIARequest(self)

    @property
    def FCoERDIRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDIRequest_template.FCoERDIRequest): An instance of the FCoERDIRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDIRequest_template import (
            FCoERDIRequest,
        )

        return FCoERDIRequest(self)

    @property
    def FCoEHLORequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEHLORequest_template.FCoEHLORequest): An instance of the FCoEHLORequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEHLORequest_template import (
            FCoEHLORequest,
        )

        return FCoEHLORequest(self)

    @property
    def FCoEEFPRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPRequest_template.FCoEEFPRequest): An instance of the FCoEEFPRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPRequest_template import (
            FCoEEFPRequest,
        )

        return FCoEEFPRequest(self)

    @property
    def Fip(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fip_template.Fip): An instance of the Fip traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fip_template import (
            Fip,
        )

        return Fip(self)

    @property
    def FipClearVirtualLinksFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipClearVirtualLinksFcf_template.FipClearVirtualLinksFcf): An instance of the FipClearVirtualLinksFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipClearVirtualLinksFcf_template import (
            FipClearVirtualLinksFcf,
        )

        return FipClearVirtualLinksFcf(self)

    @property
    def FipDiscoveryAdvertisementFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoveryAdvertisementFcf_template.FipDiscoveryAdvertisementFcf): An instance of the FipDiscoveryAdvertisementFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoveryAdvertisementFcf_template import (
            FipDiscoveryAdvertisementFcf,
        )

        return FipDiscoveryAdvertisementFcf(self)

    @property
    def FipDiscoverySolicitationEnode(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationEnode_template.FipDiscoverySolicitationEnode): An instance of the FipDiscoverySolicitationEnode traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationEnode_template import (
            FipDiscoverySolicitationEnode,
        )

        return FipDiscoverySolicitationEnode(self)

    @property
    def FipDiscoverySolicitationFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationFcf_template.FipDiscoverySolicitationFcf): An instance of the FipDiscoverySolicitationFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationFcf_template import (
            FipDiscoverySolicitationFcf,
        )

        return FipDiscoverySolicitationFcf(self)

    @property
    def FipElpRequestFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpRequestFcf_template.FipElpRequestFcf): An instance of the FipElpRequestFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpRequestFcf_template import (
            FipElpRequestFcf,
        )

        return FipElpRequestFcf(self)

    @property
    def FipElpSwAccFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwAccFcf_template.FipElpSwAccFcf): An instance of the FipElpSwAccFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwAccFcf_template import (
            FipElpSwAccFcf,
        )

        return FipElpSwAccFcf(self)

    @property
    def FipElpSwRjtFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwRjtFcf_template.FipElpSwRjtFcf): An instance of the FipElpSwRjtFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwRjtFcf_template import (
            FipElpSwRjtFcf,
        )

        return FipElpSwRjtFcf(self)

    @property
    def FipFabricLogoEnode(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoEnode_template.FipFabricLogoEnode): An instance of the FipFabricLogoEnode traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoEnode_template import (
            FipFabricLogoEnode,
        )

        return FipFabricLogoEnode(self)

    @property
    def FipFabricLogoLsAccFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsAccFcf_template.FipFabricLogoLsAccFcf): An instance of the FipFabricLogoLsAccFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsAccFcf_template import (
            FipFabricLogoLsAccFcf,
        )

        return FipFabricLogoLsAccFcf(self)

    @property
    def FipFabricLogoLsRjtFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsRjtFcf_template.FipFabricLogoLsRjtFcf): An instance of the FipFabricLogoLsRjtFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsRjtFcf_template import (
            FipFabricLogoLsRjtFcf,
        )

        return FipFabricLogoLsRjtFcf(self)

    @property
    def FipFlogiLsAccFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsAccFcf_template.FipFlogiLsAccFcf): An instance of the FipFlogiLsAccFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsAccFcf_template import (
            FipFlogiLsAccFcf,
        )

        return FipFlogiLsAccFcf(self)

    @property
    def FipFlogiLsRjtFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsRjtFcf_template.FipFlogiLsRjtFcf): An instance of the FipFlogiLsRjtFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsRjtFcf_template import (
            FipFlogiLsRjtFcf,
        )

        return FipFlogiLsRjtFcf(self)

    @property
    def FipFlogiRequestEnode(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiRequestEnode_template.FipFlogiRequestEnode): An instance of the FipFlogiRequestEnode traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiRequestEnode_template import (
            FipFlogiRequestEnode,
        )

        return FipFlogiRequestEnode(self)

    @property
    def FipKeepAliveEnode(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveEnode_template.FipKeepAliveEnode): An instance of the FipKeepAliveEnode traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveEnode_template import (
            FipKeepAliveEnode,
        )

        return FipKeepAliveEnode(self)

    @property
    def FipKeepAliveVnport(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveVnport_template.FipKeepAliveVnport): An instance of the FipKeepAliveVnport traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveVnport_template import (
            FipKeepAliveVnport,
        )

        return FipKeepAliveVnport(self)

    @property
    def FipNpivFdicsLsAccFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdicsLsAccFcf_template.FipNpivFdicsLsAccFcf): An instance of the FipNpivFdicsLsAccFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdicsLsAccFcf_template import (
            FipNpivFdicsLsAccFcf,
        )

        return FipNpivFdicsLsAccFcf(self)

    @property
    def FipNpivFdiscLsRjtFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscLsRjtFcf_template.FipNpivFdiscLsRjtFcf): An instance of the FipNpivFdiscLsRjtFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscLsRjtFcf_template import (
            FipNpivFdiscLsRjtFcf,
        )

        return FipNpivFdiscLsRjtFcf(self)

    @property
    def FipNpivFdiscRequestEnode(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscRequestEnode_template.FipNpivFdiscRequestEnode): An instance of the FipNpivFdiscRequestEnode traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscRequestEnode_template import (
            FipNpivFdiscRequestEnode,
        )

        return FipNpivFdiscRequestEnode(self)

    @property
    def FipVendorSpecific(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVendorSpecific_template.FipVendorSpecific): An instance of the FipVendorSpecific traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVendorSpecific_template import (
            FipVendorSpecific,
        )

        return FipVendorSpecific(self)

    @property
    def FipVlanNotificationFcf(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanNotificationFcf_template.FipVlanNotificationFcf): An instance of the FipVlanNotificationFcf traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanNotificationFcf_template import (
            FipVlanNotificationFcf,
        )

        return FipVlanNotificationFcf(self)

    @property
    def FipVlanRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanRequest_template.FipVlanRequest): An instance of the FipVlanRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanRequest_template import (
            FipVlanRequest,
        )

        return FipVlanRequest(self)

    @property
    def FcFabricLogoEnode(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoEnode_template.FcFabricLogoEnode): An instance of the FcFabricLogoEnode traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoEnode_template import (
            FcFabricLogoEnode,
        )

        return FcFabricLogoEnode(self)

    @property
    def FcFabricLogoLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsAcc_template.FcFabricLogoLsAcc): An instance of the FcFabricLogoLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsAcc_template import (
            FcFabricLogoLsAcc,
        )

        return FcFabricLogoLsAcc(self)

    @property
    def FcFabricLogoLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsRjt_template.FcFabricLogoLsRjt): An instance of the FcFabricLogoLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsRjt_template import (
            FcFabricLogoLsRjt,
        )

        return FcFabricLogoLsRjt(self)

    @property
    def FcFlogiLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsAcc_template.FcFlogiLsAcc): An instance of the FcFlogiLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsAcc_template import (
            FcFlogiLsAcc,
        )

        return FcFlogiLsAcc(self)

    @property
    def FcFlogiLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsRjt_template.FcFlogiLsRjt): An instance of the FcFlogiLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsRjt_template import (
            FcFlogiLsRjt,
        )

        return FcFlogiLsRjt(self)

    @property
    def FcFlogiRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiRequest_template.FcFlogiRequest): An instance of the FcFlogiRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiRequest_template import (
            FcFlogiRequest,
        )

        return FcFlogiRequest(self)

    @property
    def FcPlogiLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsAcc_template.FcPlogiLsAcc): An instance of the FcPlogiLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsAcc_template import (
            FcPlogiLsAcc,
        )

        return FcPlogiLsAcc(self)

    @property
    def FcPlogiLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsRjt_template.FcPlogiLsRjt): An instance of the FcPlogiLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsRjt_template import (
            FcPlogiLsRjt,
        )

        return FcPlogiLsRjt(self)

    @property
    def FcPlogiRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiRequest_template.FcPlogiRequest): An instance of the FcPlogiRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiRequest_template import (
            FcPlogiRequest,
        )

        return FcPlogiRequest(self)

    @property
    def FcNpivFdicsLsAcc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdicsLsAcc_template.FcNpivFdicsLsAcc): An instance of the FcNpivFdicsLsAcc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdicsLsAcc_template import (
            FcNpivFdicsLsAcc,
        )

        return FcNpivFdicsLsAcc(self)

    @property
    def FcNpivFdiscLsRjt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscLsRjt_template.FcNpivFdiscLsRjt): An instance of the FcNpivFdiscLsRjt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscLsRjt_template import (
            FcNpivFdiscLsRjt,
        )

        return FcNpivFdiscLsRjt(self)

    @property
    def FcNpivFdiscRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscRequest_template.FcNpivFdiscRequest): An instance of the FcNpivFdiscRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscRequest_template import (
            FcNpivFdiscRequest,
        )

        return FcNpivFdiscRequest(self)

    @property
    def FcScrRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcScrRequest_template.FcScrRequest): An instance of the FcScrRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcScrRequest_template import (
            FcScrRequest,
        )

        return FcScrRequest(self)

    @property
    def FcRscn(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRscn_template.FcRscn): An instance of the FcRscn traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRscn_template import (
            FcRscn,
        )

        return FcRscn(self)

    @property
    def FCGCSID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGCSID_template.FCGCSID): An instance of the FCGCSID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGCSID_template import (
            FCGCSID,
        )

        return FCGCSID(self)

    @property
    def FCGANXT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGANXT_template.FCGANXT): An instance of the FCGANXT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGANXT_template import (
            FCGANXT,
        )

        return FCGANXT(self)

    @property
    def FCGIEIL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEIL_template.FCGIEIL): An instance of the FCGIEIL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEIL_template import (
            FCGIEIL,
        )

        return FCGIEIL(self)

    @property
    def FCGIDPN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIDPN_template.FCGIDPN): An instance of the FCGIDPN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIDPN_template import (
            FCGIDPN,
        )

        return FCGIDPN(self)

    @property
    def FCGFPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFPNID_template.FCGFPNID): An instance of the FCGFPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFPNID_template import (
            FCGFPNID,
        )

        return FCGFPNID(self)

    @property
    def FCGPSC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPSC_template.FCGPSC): An instance of the FCGPSC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPSC_template import (
            FCGPSC,
        )

        return FCGPSC(self)

    @property
    def FCGSES(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGSES_template.FCGSES): An instance of the FCGSES traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGSES_template import (
            FCGSES,
        )

        return FCGSES(self)

    @property
    def FCGPNFT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPNFT_template.FCGPNFT): An instance of the FCGPNFT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPNFT_template import (
            FCGPNFT,
        )

        return FCGPNFT(self)

    @property
    def FCGIEILN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEILN_template.FCGIEILN): An instance of the FCGIEILN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEILN_template import (
            FCGIEILN,
        )

        return FCGIEILN(self)

    @property
    def FCGAPNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGAPNL_template.FCGAPNL): An instance of the FCGAPNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGAPNL_template import (
            FCGAPNL,
        )

        return FCGAPNL(self)

    @property
    def FCGSPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGSPNID_template.FCGSPNID): An instance of the FCGSPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGSPNID_template import (
            FCGSPNID,
        )

        return FCGSPNID(self)

    @property
    def FCRSNNNN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRSNNNN_template.FCRSNNNN): An instance of the FCRSNNNN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRSNNNN_template import (
            FCRSNNNN,
        )

        return FCRSNNNN(self)

    @property
    def FCGNPL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNPL_template.FCGNPL): An instance of the FCGNPL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNPL_template import (
            FCGNPL,
        )

        return FCGNPL(self)

    @property
    def FCGPL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPL_template.FCGPL): An instance of the FCGPL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPL_template import (
            FCGPL,
        )

        return FCGPL(self)

    @property
    def FCGNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNID_template.FCGNID): An instance of the FCGNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNID_template import (
            FCGNID,
        )

        return FCGNID(self)

    @property
    def FCRPLT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPLT_template.FCRPLT): An instance of the FCRPLT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPLT_template import (
            FCRPLT,
        )

        return FCRPLT(self)

    @property
    def FCRIELN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRIELN_template.FCRIELN): An instance of the FCRIELN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRIELN_template import (
            FCRIELN,
        )

        return FCRIELN(self)

    @property
    def FCGPNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPNL_template.FCGPNL): An instance of the FCGPNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPNL_template import (
            FCGPNL,
        )

        return FCGPNL(self)

    @property
    def FCGNNFT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNNFT_template.FCGNNFT): An instance of the FCGNNFT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNNFT_template import (
            FCGNNFT,
        )

        return FCGNNFT(self)

    @property
    def FCGPLNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLNL_template.FCGPLNL): An instance of the FCGPLNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLNL_template import (
            FCGPLNL,
        )

        return FCGPLNL(self)

    @property
    def FCRFTID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRFTID_template.FCRFTID): An instance of the FCRFTID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRFTID_template import (
            FCRFTID,
        )

        return FCRFTID(self)

    @property
    def FCGPLML(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLML_template.FCGPLML): An instance of the FCGPLML traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLML_template import (
            FCGPLML,
        )

        return FCGPLML(self)

    @property
    def FCGPS(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPS_template.FCGPS): An instance of the FCGPS traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPS_template import (
            FCGPS,
        )

        return FCGPS(self)

    @property
    def FCRCSID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRCSID_template.FCRCSID): An instance of the FCRCSID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRCSID_template import (
            FCRCSID,
        )

        return FCRCSID(self)

    @property
    def FCGSNNNN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGSNNNN_template.FCGSNNNN): An instance of the FCGSNNNN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGSNNNN_template import (
            FCGSNNNN,
        )

        return FCGSNNNN(self)

    @property
    def FCGNNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNNID_template.FCGNNID): An instance of the FCGNNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGNNID_template import (
            FCGNNID,
        )

        return FCGNNID(self)

    @property
    def FCGMID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGMID_template.FCGMID): An instance of the FCGMID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGMID_template import (
            FCGMID,
        )

        return FCGMID(self)

    @property
    def FCGIET(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIET_template.FCGIET): An instance of the FCGIET traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIET_template import (
            FCGIET,
        )

        return FCGIET(self)

    @property
    def FCRPLM(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPLM_template.FCRPLM): An instance of the FCRPLM traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPLM_template import (
            FCRPLM,
        )

        return FCRPLM(self)

    @property
    def FCGPAB(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPAB_template.FCGPAB): An instance of the FCGPAB traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPAB_template import (
            FCGPAB,
        )

        return FCGPAB(self)

    @property
    def FCGIEAG(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEAG_template.FCGIEAG): An instance of the FCGIEAG traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEAG_template import (
            FCGIEAG,
        )

        return FCGIEAG(self)

    @property
    def FCGIEL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEL_template.FCGIEL): An instance of the FCGIEL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIEL_template import (
            FCGIEL,
        )

        return FCGIEL(self)

    @property
    def FCGPAG(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPAG_template.FCGPAG): An instance of the FCGPAG traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPAG_template import (
            FCGPAG,
        )

        return FCGPAG(self)

    @property
    def FCGIDFT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIDFT_template.FCGIDFT): An instance of the FCGIDFT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIDFT_template import (
            FCGIDFT,
        )

        return FCGIDFT(self)

    @property
    def FCGFFID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFFID_template.FCGFFID): An instance of the FCGFFID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFFID_template import (
            FCGFFID,
        )

        return FCGFFID(self)

    @property
    def FCGMAL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGMAL_template.FCGMAL): An instance of the FCGMAL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGMAL_template import (
            FCGMAL,
        )

        return FCGMAL(self)

    @property
    def FCGPT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPT_template.FCGPT): An instance of the FCGPT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPT_template import (
            FCGPT,
        )

        return FCGPT(self)

    @property
    def FCGPTID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPTID_template.FCGPTID): An instance of the FCGPTID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPTID_template import (
            FCGPTID,
        )

        return FCGPTID(self)

    @property
    def FCGATIN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGATIN_template.FCGATIN): An instance of the FCGATIN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGATIN_template import (
            FCGATIN,
        )

        return FCGATIN(self)

    @property
    def FCRFFID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRFFID_template.FCRFFID): An instance of the FCRFFID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRFFID_template import (
            FCRFFID,
        )

        return FCRFFID(self)

    @property
    def FCRPNL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPNL_template.FCRPNL): An instance of the FCRPNL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPNL_template import (
            FCRPNL,
        )

        return FCRPNL(self)

    @property
    def FCGDID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGDID_template.FCGDID): An instance of the FCGDID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGDID_template import (
            FCGDID,
        )

        return FCGDID(self)

    @property
    def FCGTIN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGTIN_template.FCGTIN): An instance of the FCGTIN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGTIN_template import (
            FCGTIN,
        )

        return FCGTIN(self)

    @property
    def FCRPL(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPL_template.FCRPL): An instance of the FCRPL traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPL_template import (
            FCRPL,
        )

        return FCRPL(self)

    @property
    def FCGPLT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLT_template.FCGPLT): An instance of the FCGPLT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLT_template import (
            FCGPLT,
        )

        return FCGPLT(self)

    @property
    def FCRNNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRNNID_template.FCRNNID): An instance of the FCRNNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRNNID_template import (
            FCRNNID,
        )

        return FCRNNID(self)

    @property
    def FCGPPN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPPN_template.FCGPPN): An instance of the FCGPPN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPPN_template import (
            FCGPPN,
        )

        return FCGPPN(self)

    @property
    def FCGPFCP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPFCP_template.FCGPFCP): An instance of the FCGPFCP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPFCP_template import (
            FCGPFCP,
        )

        return FCGPFCP(self)

    @property
    def FCGPLI(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLI_template.FCGPLI): An instance of the FCGPLI traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPLI_template import (
            FCGPLI,
        )

        return FCGPLI(self)

    @property
    def FCGFN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFN_template.FCGFN): An instance of the FCGFN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFN_template import (
            FCGFN,
        )

        return FCGFN(self)

    @property
    def FCDAID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCDAID_template.FCDAID): An instance of the FCDAID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCDAID_template import (
            FCDAID,
        )

        return FCDAID(self)

    @property
    def FCRPAB(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPAB_template.FCRPAB): An instance of the FCRPAB traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRPAB_template import (
            FCRPAB,
        )

        return FCRPAB(self)

    @property
    def FCGFTID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFTID_template.FCGFTID): An instance of the FCGFTID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGFTID_template import (
            FCGFTID,
        )

        return FCGFTID(self)

    @property
    def FCRSPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRSPNID_template.FCRSPNID): An instance of the FCRSPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCRSPNID_template import (
            FCRSPNID,
        )

        return FCRSPNID(self)

    @property
    def FCGIDNN(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIDNN_template.FCGIDNN): An instance of the FCGIDNN traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGIDNN_template import (
            FCGIDNN,
        )

        return FCGIDNN(self)

    @property
    def FCGPNID(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPNID_template.FCGPNID): An instance of the FCGPNID traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCGPNID_template import (
            FCGPNID,
        )

        return FCGPNID(self)

    @property
    def FcEFPSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcEFPSWRJT_template.FcEFPSWRJT): An instance of the FcEFPSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcEFPSWRJT_template import (
            FcEFPSWRJT,
        )

        return FcEFPSWRJT(self)

    @property
    def FcEFPSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcEFPSWACC_template.FcEFPSWACC): An instance of the FcEFPSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcEFPSWACC_template import (
            FcEFPSWACC,
        )

        return FcEFPSWACC(self)

    @property
    def FcESCSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcESCSWACC_template.FcESCSWACC): An instance of the FcESCSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcESCSWACC_template import (
            FcESCSWACC,
        )

        return FcESCSWACC(self)

    @property
    def FcRDISWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRDISWRJT_template.FcRDISWRJT): An instance of the FcRDISWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRDISWRJT_template import (
            FcRDISWRJT,
        )

        return FcRDISWRJT(self)

    @property
    def FcMRRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcMRRequest_template.FcMRRequest): An instance of the FcMRRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcMRRequest_template import (
            FcMRRequest,
        )

        return FcMRRequest(self)

    @property
    def FcLSARequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcLSARequest_template.FcLSARequest): An instance of the FcLSARequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcLSARequest_template import (
            FcLSARequest,
        )

        return FcLSARequest(self)

    @property
    def FcDIASWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcDIASWRJT_template.FcDIASWRJT): An instance of the FcDIASWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcDIASWRJT_template import (
            FcDIASWRJT,
        )

        return FcDIASWRJT(self)

    @property
    def FcMRSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcMRSWRJT_template.FcMRSWRJT): An instance of the FcMRSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcMRSWRJT_template import (
            FcMRSWRJT,
        )

        return FcMRSWRJT(self)

    @property
    def FcDIASWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcDIASWACC_template.FcDIASWACC): An instance of the FcDIASWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcDIASWACC_template import (
            FcDIASWACC,
        )

        return FcDIASWACC(self)

    @property
    def FcRDISWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRDISWACC_template.FcRDISWACC): An instance of the FcRDISWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRDISWACC_template import (
            FcRDISWACC,
        )

        return FcRDISWACC(self)

    @property
    def FcESCSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcESCSWRJT_template.FcESCSWRJT): An instance of the FcESCSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcESCSWRJT_template import (
            FcESCSWRJT,
        )

        return FcESCSWRJT(self)

    @property
    def FcLSURequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcLSURequest_template.FcLSURequest): An instance of the FcLSURequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcLSURequest_template import (
            FcLSURequest,
        )

        return FcLSURequest(self)

    @property
    def FcESCRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcESCRequest_template.FcESCRequest): An instance of the FcESCRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcESCRequest_template import (
            FcESCRequest,
        )

        return FcESCRequest(self)

    @property
    def FcELPSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcELPSWACC_template.FcELPSWACC): An instance of the FcELPSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcELPSWACC_template import (
            FcELPSWACC,
        )

        return FcELPSWACC(self)

    @property
    def FcELPSWRJT(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcELPSWRJT_template.FcELPSWRJT): An instance of the FcELPSWRJT traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcELPSWRJT_template import (
            FcELPSWRJT,
        )

        return FcELPSWRJT(self)

    @property
    def FcMRSWACC(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcMRSWACC_template.FcMRSWACC): An instance of the FcMRSWACC traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcMRSWACC_template import (
            FcMRSWACC,
        )

        return FcMRSWACC(self)

    @property
    def FcELPRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcELPRequest_template.FcELPRequest): An instance of the FcELPRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcELPRequest_template import (
            FcELPRequest,
        )

        return FcELPRequest(self)

    @property
    def FcDIARequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcDIARequest_template.FcDIARequest): An instance of the FcDIARequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcDIARequest_template import (
            FcDIARequest,
        )

        return FcDIARequest(self)

    @property
    def FcRDIRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRDIRequest_template.FcRDIRequest): An instance of the FcRDIRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRDIRequest_template import (
            FcRDIRequest,
        )

        return FcRDIRequest(self)

    @property
    def FcHLORequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcHLORequest_template.FcHLORequest): An instance of the FcHLORequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcHLORequest_template import (
            FcHLORequest,
        )

        return FcHLORequest(self)

    @property
    def FcEFPRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcEFPRequest_template.FcEFPRequest): An instance of the FcEFPRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcEFPRequest_template import (
            FcEFPRequest,
        )

        return FcEFPRequest(self)

    @property
    def MacInMACv42(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACv42_template.MacInMACv42): An instance of the MacInMACv42 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACv42_template import (
            MacInMACv42,
        )

        return MacInMACv42(self)

    @property
    def PfcPause(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pfcPause_template.PfcPause): An instance of the PfcPause traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pfcPause_template import (
            PfcPause,
        )

        return PfcPause(self)

    @property
    def Tmpls(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tmpls_template.Tmpls): An instance of the Tmpls traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tmpls_template import (
            Tmpls,
        )

        return Tmpls(self)

    @property
    def Lldp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lldp_template.Lldp): An instance of the Lldp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lldp_template import (
            Lldp,
        )

        return Lldp(self)

    @property
    def Ecp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ecp_template.Ecp): An instance of the Ecp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ecp_template import (
            Ecp,
        )

        return Ecp(self)

    @property
    def Esmc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.esmc_template.Esmc): An instance of the Esmc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.esmc_template import (
            Esmc,
        )

        return Esmc(self)

    @property
    def Trill(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trill_template.Trill): An instance of the Trill traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trill_template import (
            Trill,
        )

        return Trill(self)

    @property
    def Trillrbchannel(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trillrbchannel_template.Trillrbchannel): An instance of the Trillrbchannel traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trillrbchannel_template import (
            Trillrbchannel,
        )

        return Trillrbchannel(self)

    @property
    def Trilloamechoreq(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trilloamechoreq_template.Trilloamechoreq): An instance of the Trilloamechoreq traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trilloamechoreq_template import (
            Trilloamechoreq,
        )

        return Trilloamechoreq(self)

    @property
    def Trilloamechoreply(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trilloamechoreply_template.Trilloamechoreply): An instance of the Trilloamechoreply traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trilloamechoreply_template import (
            Trilloamechoreply,
        )

        return Trilloamechoreply(self)

    @property
    def Fabricpath(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fabricpath_template.Fabricpath): An instance of the Fabricpath traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fabricpath_template import (
            Fabricpath,
        )

        return Fabricpath(self)

    @property
    def Pbb(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pbb_template.Pbb): An instance of the Pbb traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pbb_template import (
            Pbb,
        )

        return Pbb(self)

    @property
    def Avtp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtp_template.Avtp): An instance of the Avtp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtp_template import (
            Avtp,
        )

        return Avtp(self)

    @property
    def MaapHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.maapHeader_template.MaapHeader): An instance of the MaapHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.maapHeader_template import (
            MaapHeader,
        )

        return MaapHeader(self)

    @property
    def MsrpMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpMessage_template.MsrpMessage): An instance of the MsrpMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpMessage_template import (
            MsrpMessage,
        )

        return MsrpMessage(self)

    @property
    def MsrpVectorAttribute(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpVectorAttribute_template.MsrpVectorAttribute): An instance of the MsrpVectorAttribute traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpVectorAttribute_template import (
            MsrpVectorAttribute,
        )

        return MsrpVectorAttribute(self)

    @property
    def MmrpMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpMessage_template.MmrpMessage): An instance of the MmrpMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpMessage_template import (
            MmrpMessage,
        )

        return MmrpMessage(self)

    @property
    def MmrpVectorAttribute(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpVectorAttribute_template.MmrpVectorAttribute): An instance of the MmrpVectorAttribute traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpVectorAttribute_template import (
            MmrpVectorAttribute,
        )

        return MmrpVectorAttribute(self)

    @property
    def MvrpMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpMessage_template.MvrpMessage): An instance of the MvrpMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpMessage_template import (
            MvrpMessage,
        )

        return MvrpMessage(self)

    @property
    def MvrpVectorAttribute(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpVectorAttribute_template.MvrpVectorAttribute): An instance of the MvrpVectorAttribute traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpVectorAttribute_template import (
            MvrpVectorAttribute,
        )

        return MvrpVectorAttribute(self)

    @property
    def MrpThreePackedEvent(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpThreePackedEvent_template.MrpThreePackedEvent): An instance of the MrpThreePackedEvent traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpThreePackedEvent_template import (
            MrpThreePackedEvent,
        )

        return MrpThreePackedEvent(self)

    @property
    def MrpFourPackedEvent(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpFourPackedEvent_template.MrpFourPackedEvent): An instance of the MrpFourPackedEvent traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpFourPackedEvent_template import (
            MrpFourPackedEvent,
        )

        return MrpFourPackedEvent(self)

    @property
    def EndMark(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.endMark_template.EndMark): An instance of the EndMark traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.endMark_template import (
            EndMark,
        )

        return EndMark(self)

    @property
    def BMacHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bMacHeader_template.BMacHeader): An instance of the BMacHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bMacHeader_template import (
            BMacHeader,
        )

        return BMacHeader(self)

    @property
    def BVlanHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bVlanHeader_template.BVlanHeader): An instance of the BVlanHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bVlanHeader_template import (
            BVlanHeader,
        )

        return BVlanHeader(self)

    @property
    def ITagHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iTagHeader_template.ITagHeader): An instance of the ITagHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iTagHeader_template import (
            ITagHeader,
        )

        return ITagHeader(self)

    @property
    def PreferedPwMPlsCw(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.preferedPwMPlsCw_template.PreferedPwMPlsCw): An instance of the PreferedPwMPlsCw traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.preferedPwMPlsCw_template import (
            PreferedPwMPlsCw,
        )

        return PreferedPwMPlsCw(self)

    @property
    def RTag(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rTag_template.RTag): An instance of the RTag traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rTag_template import (
            RTag,
        )

        return RTag(self)

    @property
    def Macsec(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macsec_template.Macsec): An instance of the Macsec traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macsec_template import (
            Macsec,
        )

        return Macsec(self)

    @property
    def MacsecHw(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.MacsecHw_template.MacsecHw): An instance of the MacsecHw traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.MacsecHw_template import (
            MacsecHw,
        )

        return MacsecHw(self)

    @property
    def PayloadProtocolType(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.payloadProtocolType_template.PayloadProtocolType): An instance of the PayloadProtocolType traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.payloadProtocolType_template import (
            PayloadProtocolType,
        )

        return PayloadProtocolType(self)

    @property
    def GlobalPause(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.globalPause_template.GlobalPause): An instance of the GlobalPause traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.globalPause_template import (
            GlobalPause,
        )

        return GlobalPause(self)

    @property
    def InfiniBandBaseTransportHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandBaseTransportHeader_template.InfiniBandBaseTransportHeader): An instance of the InfiniBandBaseTransportHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandBaseTransportHeader_template import (
            InfiniBandBaseTransportHeader,
        )

        return InfiniBandBaseTransportHeader(self)

    @property
    def InfiniBandReliableDatagramExtendedTransportHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandReliableDatagramExtendedTransportHeader_template.InfiniBandReliableDatagramExtendedTransportHeader): An instance of the InfiniBandReliableDatagramExtendedTransportHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandReliableDatagramExtendedTransportHeader_template import (
            InfiniBandReliableDatagramExtendedTransportHeader,
        )

        return InfiniBandReliableDatagramExtendedTransportHeader(self)

    @property
    def InfiniBandRdmaExtendedTransportHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandRdmaExtendedTransportHeader_template.InfiniBandRdmaExtendedTransportHeader): An instance of the InfiniBandRdmaExtendedTransportHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandRdmaExtendedTransportHeader_template import (
            InfiniBandRdmaExtendedTransportHeader,
        )

        return InfiniBandRdmaExtendedTransportHeader(self)

    @property
    def InfiniBandAtomicExtendedTransportHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandAtomicExtendedTransportHeader_template.InfiniBandAtomicExtendedTransportHeader): An instance of the InfiniBandAtomicExtendedTransportHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandAtomicExtendedTransportHeader_template import (
            InfiniBandAtomicExtendedTransportHeader,
        )

        return InfiniBandAtomicExtendedTransportHeader(self)

    @property
    def InfiniBandAckExtendedTransportHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandAckExtendedTransportHeader_template.InfiniBandAckExtendedTransportHeader): An instance of the InfiniBandAckExtendedTransportHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.infiniBandAckExtendedTransportHeader_template import (
            InfiniBandAckExtendedTransportHeader,
        )

        return InfiniBandAckExtendedTransportHeader(self)

    @property
    def Amt(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.amt_template.Amt): An instance of the Amt traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.amt_template import (
            Amt,
        )

        return Amt(self)

    @property
    def Cgmp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cgmp_template.Cgmp): An instance of the Cgmp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cgmp_template import (
            Cgmp,
        )

        return Cgmp(self)

    @property
    def Ddp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ddp_template.Ddp): An instance of the Ddp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ddp_template import (
            Ddp,
        )

        return Ddp(self)

    @property
    def IsisL1CSNPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1CSNPDU_template.IsisL1CSNPDU): An instance of the IsisL1CSNPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1CSNPDU_template import (
            IsisL1CSNPDU,
        )

        return IsisL1CSNPDU(self)

    @property
    def IsisLevel1LANHelloPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LANHelloPDU_template.IsisLevel1LANHelloPDU): An instance of the IsisLevel1LANHelloPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LANHelloPDU_template import (
            IsisLevel1LANHelloPDU,
        )

        return IsisLevel1LANHelloPDU(self)

    @property
    def IsisLevel1LinkStatePDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LinkStatePDU_template.IsisLevel1LinkStatePDU): An instance of the IsisLevel1LinkStatePDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LinkStatePDU_template import (
            IsisLevel1LinkStatePDU,
        )

        return IsisLevel1LinkStatePDU(self)

    @property
    def IsisL1PSNPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1PSNPDU_template.IsisL1PSNPDU): An instance of the IsisL1PSNPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1PSNPDU_template import (
            IsisL1PSNPDU,
        )

        return IsisL1PSNPDU(self)

    @property
    def IsisL2CSNPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2CSNPDU_template.IsisL2CSNPDU): An instance of the IsisL2CSNPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2CSNPDU_template import (
            IsisL2CSNPDU,
        )

        return IsisL2CSNPDU(self)

    @property
    def IsisLevel2LANHelloPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LANHelloPDU_template.IsisLevel2LANHelloPDU): An instance of the IsisLevel2LANHelloPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LANHelloPDU_template import (
            IsisLevel2LANHelloPDU,
        )

        return IsisLevel2LANHelloPDU(self)

    @property
    def IsisLevel2LinkStatePDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LinkStatePDU_template.IsisLevel2LinkStatePDU): An instance of the IsisLevel2LinkStatePDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LinkStatePDU_template import (
            IsisLevel2LinkStatePDU,
        )

        return IsisLevel2LinkStatePDU(self)

    @property
    def IsisL2PSNPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2PSNPDU_template.IsisL2PSNPDU): An instance of the IsisL2PSNPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2PSNPDU_template import (
            IsisL2PSNPDU,
        )

        return IsisL2PSNPDU(self)

    @property
    def IsisPointToPointHelloPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisPointToPointHelloPDU_template.IsisPointToPointHelloPDU): An instance of the IsisPointToPointHelloPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisPointToPointHelloPDU_template import (
            IsisPointToPointHelloPDU,
        )

        return IsisPointToPointHelloPDU(self)

    @property
    def IsisL1McastCSNPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastCSNPDU_template.IsisL1McastCSNPDU): An instance of the IsisL1McastCSNPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastCSNPDU_template import (
            IsisL1McastCSNPDU,
        )

        return IsisL1McastCSNPDU(self)

    @property
    def IsisL1McastLinkStatePDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastLinkStatePDU_template.IsisL1McastLinkStatePDU): An instance of the IsisL1McastLinkStatePDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastLinkStatePDU_template import (
            IsisL1McastLinkStatePDU,
        )

        return IsisL1McastLinkStatePDU(self)

    @property
    def IsisL1McastPSNPDU(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastPSNPDU_template.IsisL1McastPSNPDU): An instance of the IsisL1McastPSNPDU traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastPSNPDU_template import (
            IsisL1McastPSNPDU,
        )

        return IsisL1McastPSNPDU(self)

    @property
    def Ipv6Authentication(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Authentication_template.Ipv6Authentication): An instance of the Ipv6Authentication traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Authentication_template import (
            Ipv6Authentication,
        )

        return Ipv6Authentication(self)

    @property
    def Ipv6Encapsulation(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Encapsulation_template.Ipv6Encapsulation): An instance of the Ipv6Encapsulation traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Encapsulation_template import (
            Ipv6Encapsulation,
        )

        return Ipv6Encapsulation(self)

    @property
    def Ipv6Pseudo(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Pseudo_template.Ipv6Pseudo): An instance of the Ipv6Pseudo traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Pseudo_template import (
            Ipv6Pseudo,
        )

        return Ipv6Pseudo(self)

    @property
    def Ipv6Routing(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Routing_template.Ipv6Routing): An instance of the Ipv6Routing traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Routing_template import (
            Ipv6Routing,
        )

        return Ipv6Routing(self)

    @property
    def Ipv6RoutingType0(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType0_template.Ipv6RoutingType0): An instance of the Ipv6RoutingType0 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType0_template import (
            Ipv6RoutingType0,
        )

        return Ipv6RoutingType0(self)

    @property
    def Ipv6RoutingType2(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType2_template.Ipv6RoutingType2): An instance of the Ipv6RoutingType2 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType2_template import (
            Ipv6RoutingType2,
        )

        return Ipv6RoutingType2(self)

    @property
    def Ipv6RoutingType4(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType4_template.Ipv6RoutingType4): An instance of the Ipv6RoutingType4 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType4_template import (
            Ipv6RoutingType4,
        )

        return Ipv6RoutingType4(self)

    @property
    def Ipv6GSRHType4(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6GSRHType4_template.Ipv6GSRHType4): An instance of the Ipv6GSRHType4 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6GSRHType4_template import (
            Ipv6GSRHType4,
        )

        return Ipv6GSRHType4(self)

    @property
    def Ipv4(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv4_template.Ipv4): An instance of the Ipv4 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv4_template import (
            Ipv4,
        )

        return Ipv4(self)

    @property
    def Ipv6(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6_template.Ipv6): An instance of the Ipv6 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6_template import (
            Ipv6,
        )

        return Ipv6(self)

    @property
    def Ipv6GSRH(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6GSRH_template.Ipv6GSRH): An instance of the Ipv6GSRH traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6GSRH_template import (
            Ipv6GSRH,
        )

        return Ipv6GSRH(self)

    @property
    def Ipv6Fragment(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Fragment_template.Ipv6Fragment): An instance of the Ipv6Fragment traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Fragment_template import (
            Ipv6Fragment,
        )

        return Ipv6Fragment(self)

    @property
    def Ipv6HopByHopOptions(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptions_template.Ipv6HopByHopOptions): An instance of the Ipv6HopByHopOptions traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptions_template import (
            Ipv6HopByHopOptions,
        )

        return Ipv6HopByHopOptions(self)

    @property
    def Ipv6HopByHopOptionsWithIOAM(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptionsWithIOAM_template.Ipv6HopByHopOptionsWithIOAM): An instance of the Ipv6HopByHopOptionsWithIOAM traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptionsWithIOAM_template import (
            Ipv6HopByHopOptionsWithIOAM,
        )

        return Ipv6HopByHopOptionsWithIOAM(self)

    @property
    def Ipv6DestinationOptions(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6DestinationOptions_template.Ipv6DestinationOptions): An instance of the Ipv6DestinationOptions traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6DestinationOptions_template import (
            Ipv6DestinationOptions,
        )

        return Ipv6DestinationOptions(self)

    @property
    def Icmpv1(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv1_template.Icmpv1): An instance of the Icmpv1 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv1_template import (
            Icmpv1,
        )

        return Icmpv1(self)

    @property
    def Icmpv2(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv2_template.Icmpv2): An instance of the Icmpv2 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv2_template import (
            Icmpv2,
        )

        return Icmpv2(self)

    @property
    def Icmpv9(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv9_template.Icmpv9): An instance of the Icmpv9 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv9_template import (
            Icmpv9,
        )

        return Icmpv9(self)

    @property
    def Icmpv6(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv6_template.Icmpv6): An instance of the Icmpv6 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv6_template import (
            Icmpv6,
        )

        return Icmpv6(self)

    @property
    def Igmpv1(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv1_template.Igmpv1): An instance of the Igmpv1 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv1_template import (
            Igmpv1,
        )

        return Igmpv1(self)

    @property
    def Igmpv2(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv2_template.Igmpv2): An instance of the Igmpv2 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv2_template import (
            Igmpv2,
        )

        return Igmpv2(self)

    @property
    def Igmpv3MembershipQuery(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipQuery_template.Igmpv3MembershipQuery): An instance of the Igmpv3MembershipQuery traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipQuery_template import (
            Igmpv3MembershipQuery,
        )

        return Igmpv3MembershipQuery(self)

    @property
    def Igmpv3MembershipReport(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipReport_template.Igmpv3MembershipReport): An instance of the Igmpv3MembershipReport traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipReport_template import (
            Igmpv3MembershipReport,
        )

        return Igmpv3MembershipReport(self)

    @property
    def Ipx(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipx_template.Ipx): An instance of the Ipx traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipx_template import (
            Ipx,
        )

        return Ipx(self)

    @property
    def Gre(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gre_template.Gre): An instance of the Gre traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gre_template import (
            Gre,
        )

        return Gre(self)

    @property
    def GTPuOptionalFields(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gTPuOptionalFields_template.GTPuOptionalFields): An instance of the GTPuOptionalFields traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gTPuOptionalFields_template import (
            GTPuOptionalFields,
        )

        return GTPuOptionalFields(self)

    @property
    def Gtpu(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gtpu_template.Gtpu): An instance of the Gtpu traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gtpu_template import (
            Gtpu,
        )

        return Gtpu(self)

    @property
    def L2TPv3ControlIP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlIP_template.L2TPv3ControlIP): An instance of the L2TPv3ControlIP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlIP_template import (
            L2TPv3ControlIP,
        )

        return L2TPv3ControlIP(self)

    @property
    def L2TPv3DataIP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataIP_template.L2TPv3DataIP): An instance of the L2TPv3DataIP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataIP_template import (
            L2TPv3DataIP,
        )

        return L2TPv3DataIP(self)

    @property
    def MinimalIP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.minimalIP_template.MinimalIP): An instance of the MinimalIP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.minimalIP_template import (
            MinimalIP,
        )

        return MinimalIP(self)

    @property
    def Mldv1(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv1_template.Mldv1): An instance of the Mldv1 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv1_template import (
            Mldv1,
        )

        return Mldv1(self)

    @property
    def Mldv2Query(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Query_template.Mldv2Query): An instance of the Mldv2Query traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Query_template import (
            Mldv2Query,
        )

        return Mldv2Query(self)

    @property
    def Mldv2Report(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Report_template.Mldv2Report): An instance of the Mldv2Report traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Report_template import (
            Mldv2Report,
        )

        return Mldv2Report(self)

    @property
    def MobileIPv6(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIPv6_template.MobileIPv6): An instance of the MobileIPv6 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIPv6_template import (
            MobileIPv6,
        )

        return MobileIPv6(self)

    @property
    def Nvgre(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nvgre_template.Nvgre): An instance of the Nvgre traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nvgre_template import (
            Nvgre,
        )

        return Nvgre(self)

    @property
    def Ospfv2Hello(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2Hello_template.Ospfv2Hello): An instance of the Ospfv2Hello traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2Hello_template import (
            Ospfv2Hello,
        )

        return Ospfv2Hello(self)

    @property
    def Ospfv2DatabaseDescription(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2DatabaseDescription_template.Ospfv2DatabaseDescription): An instance of the Ospfv2DatabaseDescription traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2DatabaseDescription_template import (
            Ospfv2DatabaseDescription,
        )

        return Ospfv2DatabaseDescription(self)

    @property
    def Ospfv2LSAAcknowledgement(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAAcknowledgement_template.Ospfv2LSAAcknowledgement): An instance of the Ospfv2LSAAcknowledgement traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAAcknowledgement_template import (
            Ospfv2LSAAcknowledgement,
        )

        return Ospfv2LSAAcknowledgement(self)

    @property
    def Ospfv2LSARequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSARequest_template.Ospfv2LSARequest): An instance of the Ospfv2LSARequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSARequest_template import (
            Ospfv2LSARequest,
        )

        return Ospfv2LSARequest(self)

    @property
    def Ospfv2LSAUpdate(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAUpdate_template.Ospfv2LSAUpdate): An instance of the Ospfv2LSAUpdate traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAUpdate_template import (
            Ospfv2LSAUpdate,
        )

        return Ospfv2LSAUpdate(self)

    @property
    def Ospfv3Hello(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3Hello_template.Ospfv3Hello): An instance of the Ospfv3Hello traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3Hello_template import (
            Ospfv3Hello,
        )

        return Ospfv3Hello(self)

    @property
    def Ospfv3DatabaseDescription(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3DatabaseDescription_template.Ospfv3DatabaseDescription): An instance of the Ospfv3DatabaseDescription traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3DatabaseDescription_template import (
            Ospfv3DatabaseDescription,
        )

        return Ospfv3DatabaseDescription(self)

    @property
    def Ospfv3LSAAcknowledgement(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAAcknowledgement_template.Ospfv3LSAAcknowledgement): An instance of the Ospfv3LSAAcknowledgement traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAAcknowledgement_template import (
            Ospfv3LSAAcknowledgement,
        )

        return Ospfv3LSAAcknowledgement(self)

    @property
    def Ospfv3LSARequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSARequest_template.Ospfv3LSARequest): An instance of the Ospfv3LSARequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSARequest_template import (
            Ospfv3LSARequest,
        )

        return Ospfv3LSARequest(self)

    @property
    def Ospfv3LSAUpdate(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAUpdate_template.Ospfv3LSAUpdate): An instance of the Ospfv3LSAUpdate traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAUpdate_template import (
            Ospfv3LSAUpdate,
        )

        return Ospfv3LSAUpdate(self)

    @property
    def PimdmAssertMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmAssertMessage_template.PimdmAssertMessage): An instance of the PimdmAssertMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmAssertMessage_template import (
            PimdmAssertMessage,
        )

        return PimdmAssertMessage(self)

    @property
    def PimdmGraftGraftAckMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmGraftGraftAckMessage_template.PimdmGraftGraftAckMessage): An instance of the PimdmGraftGraftAckMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmGraftGraftAckMessage_template import (
            PimdmGraftGraftAckMessage,
        )

        return PimdmGraftGraftAckMessage(self)

    @property
    def PimdmHelloMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmHelloMessage_template.PimdmHelloMessage): An instance of the PimdmHelloMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmHelloMessage_template import (
            PimdmHelloMessage,
        )

        return PimdmHelloMessage(self)

    @property
    def PimdmJoinPruneMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmJoinPruneMessage_template.PimdmJoinPruneMessage): An instance of the PimdmJoinPruneMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmJoinPruneMessage_template import (
            PimdmJoinPruneMessage,
        )

        return PimdmJoinPruneMessage(self)

    @property
    def PimdmStateRefreshMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmStateRefreshMessage_template.PimdmStateRefreshMessage): An instance of the PimdmStateRefreshMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmStateRefreshMessage_template import (
            PimdmStateRefreshMessage,
        )

        return PimdmStateRefreshMessage(self)

    @property
    def PimAssertMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimAssertMessage_template.PimAssertMessage): An instance of the PimAssertMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimAssertMessage_template import (
            PimAssertMessage,
        )

        return PimAssertMessage(self)

    @property
    def PimBootstrapMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimBootstrapMessage_template.PimBootstrapMessage): An instance of the PimBootstrapMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimBootstrapMessage_template import (
            PimBootstrapMessage,
        )

        return PimBootstrapMessage(self)

    @property
    def PimCandidateRPAdvMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimCandidateRPAdvMessage_template.PimCandidateRPAdvMessage): An instance of the PimCandidateRPAdvMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimCandidateRPAdvMessage_template import (
            PimCandidateRPAdvMessage,
        )

        return PimCandidateRPAdvMessage(self)

    @property
    def PimHelloMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimHelloMessage_template.PimHelloMessage): An instance of the PimHelloMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimHelloMessage_template import (
            PimHelloMessage,
        )

        return PimHelloMessage(self)

    @property
    def PimJoinPruneMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimJoinPruneMessage_template.PimJoinPruneMessage): An instance of the PimJoinPruneMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimJoinPruneMessage_template import (
            PimJoinPruneMessage,
        )

        return PimJoinPruneMessage(self)

    @property
    def PimRegister(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegister_template.PimRegister): An instance of the PimRegister traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegister_template import (
            PimRegister,
        )

        return PimRegister(self)

    @property
    def PimRegisterStopMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegisterStopMessage_template.PimRegisterStopMessage): An instance of the PimRegisterStopMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegisterStopMessage_template import (
            PimRegisterStopMessage,
        )

        return PimRegisterStopMessage(self)

    @property
    def Rsvp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rsvp_template.Rsvp): An instance of the Rsvp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rsvp_template import (
            Rsvp,
        )

        return Rsvp(self)

    @property
    def Rgmp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rgmp_template.Rgmp): An instance of the Rgmp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rgmp_template import (
            Rgmp,
        )

        return Rgmp(self)

    @property
    def Rtmp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtmp_template.Rtmp): An instance of the Rtmp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtmp_template import (
            Rtmp,
        )

        return Rtmp(self)

    @property
    def Vxlan(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlan_template.Vxlan): An instance of the Vxlan traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlan_template import (
            Vxlan,
        )

        return Vxlan(self)

    @property
    def Vxlangpe(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlangpe_template.Vxlangpe): An instance of the Vxlangpe traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlangpe_template import (
            Vxlangpe,
        )

        return Vxlangpe(self)

    @property
    def Geneve(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneve_template.Geneve): An instance of the Geneve traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneve_template import (
            Geneve,
        )

        return Geneve(self)

    @property
    def Genevewithtelemetry(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.genevewithtelemetry_template.Genevewithtelemetry): An instance of the Genevewithtelemetry traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.genevewithtelemetry_template import (
            Genevewithtelemetry,
        )

        return Genevewithtelemetry(self)

    @property
    def GeneveWithIntMdv21(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneveWithIntMdv21_template.GeneveWithIntMdv21): An instance of the GeneveWithIntMdv21 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneveWithIntMdv21_template import (
            GeneveWithIntMdv21,
        )

        return GeneveWithIntMdv21(self)

    @property
    def GeneveWithIntMxv21(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneveWithIntMxv21_template.GeneveWithIntMxv21): An instance of the GeneveWithIntMxv21 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneveWithIntMxv21_template import (
            GeneveWithIntMxv21,
        )

        return GeneveWithIntMxv21(self)

    @property
    def Intmetadata(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intmetadata_template.Intmetadata): An instance of the Intmetadata traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intmetadata_template import (
            Intmetadata,
        )

        return Intmetadata(self)

    @property
    def IntMdMetadatav21(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intMdMetadatav21_template.IntMdMetadatav21): An instance of the IntMdMetadatav21 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intMdMetadatav21_template import (
            IntMdMetadatav21,
        )

        return IntMdMetadatav21(self)

    @property
    def IntMxMetadatav21(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intMxMetadatav21_template.IntMxMetadatav21): An instance of the IntMxMetadatav21 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intMxMetadatav21_template import (
            IntMxMetadatav21,
        )

        return IntMxMetadatav21(self)

    @property
    def Intshimheader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intshimheader_template.Intshimheader): An instance of the Intshimheader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intshimheader_template import (
            Intshimheader,
        )

        return Intshimheader(self)

    @property
    def IntShimHeaderv21(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intShimHeaderv21_template.IntShimHeaderv21): An instance of the IntShimHeaderv21 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intShimHeaderv21_template import (
            IntShimHeaderv21,
        )

        return IntShimHeaderv21(self)

    @property
    def IntShimHeaderVxlangpe(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intShimHeaderVxlangpe_template.IntShimHeaderVxlangpe): An instance of the IntShimHeaderVxlangpe traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intShimHeaderVxlangpe_template import (
            IntShimHeaderVxlangpe,
        )

        return IntShimHeaderVxlangpe(self)

    @property
    def Probemarker(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.probemarker_template.Probemarker): An instance of the Probemarker traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.probemarker_template import (
            Probemarker,
        )

        return Probemarker(self)

    @property
    def Bier(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bier_template.Bier): An instance of the Bier traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bier_template import (
            Bier,
        )

        return Bier(self)

    @property
    def ECpri(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpri_template.ECpri): An instance of the ECpri traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpri_template import (
            ECpri,
        )

        return ECpri(self)

    @property
    def ECpriMsgType0(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType0_template.ECpriMsgType0): An instance of the ECpriMsgType0 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType0_template import (
            ECpriMsgType0,
        )

        return ECpriMsgType0(self)

    @property
    def ECpriMsgType1(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType1_template.ECpriMsgType1): An instance of the ECpriMsgType1 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType1_template import (
            ECpriMsgType1,
        )

        return ECpriMsgType1(self)

    @property
    def ECpriMsgType2(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType2_template.ECpriMsgType2): An instance of the ECpriMsgType2 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType2_template import (
            ECpriMsgType2,
        )

        return ECpriMsgType2(self)

    @property
    def ECpriMsgType3(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType3_template.ECpriMsgType3): An instance of the ECpriMsgType3 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType3_template import (
            ECpriMsgType3,
        )

        return ECpriMsgType3(self)

    @property
    def ECpriMsgType4(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType4_template.ECpriMsgType4): An instance of the ECpriMsgType4 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType4_template import (
            ECpriMsgType4,
        )

        return ECpriMsgType4(self)

    @property
    def ECpriMsgType5(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType5_template.ECpriMsgType5): An instance of the ECpriMsgType5 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType5_template import (
            ECpriMsgType5,
        )

        return ECpriMsgType5(self)

    @property
    def ECpriMsgType6(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType6_template.ECpriMsgType6): An instance of the ECpriMsgType6 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType6_template import (
            ECpriMsgType6,
        )

        return ECpriMsgType6(self)

    @property
    def ECpriMsgType7(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType7_template.ECpriMsgType7): An instance of the ECpriMsgType7 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType7_template import (
            ECpriMsgType7,
        )

        return ECpriMsgType7(self)

    @property
    def ECpriFaultNotify(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriFaultNotify_template.ECpriFaultNotify): An instance of the ECpriFaultNotify traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriFaultNotify_template import (
            ECpriFaultNotify,
        )

        return ECpriFaultNotify(self)

    @property
    def ECpriUserData(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriUserData_template.ECpriUserData): An instance of the ECpriUserData traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriUserData_template import (
            ECpriUserData,
        )

        return ECpriUserData(self)

    @property
    def EcpriOranMsgs(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ecpriOranMsgs_template.EcpriOranMsgs): An instance of the EcpriOranMsgs traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ecpriOranMsgs_template import (
            EcpriOranMsgs,
        )

        return EcpriOranMsgs(self)

    @property
    def OranCtlrMsgs(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oranCtlrMsgs_template.OranCtlrMsgs): An instance of the OranCtlrMsgs traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oranCtlrMsgs_template import (
            OranCtlrMsgs,
        )

        return OranCtlrMsgs(self)

    @property
    def OranDataMsgs(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oranDataMsgs_template.OranDataMsgs): An instance of the OranDataMsgs traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oranDataMsgs_template import (
            OranDataMsgs,
        )

        return OranDataMsgs(self)

    @property
    def IpEncapsulatingSecurityPayload(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipEncapsulatingSecurityPayload_template.IpEncapsulatingSecurityPayload): An instance of the IpEncapsulatingSecurityPayload traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipEncapsulatingSecurityPayload_template import (
            IpEncapsulatingSecurityPayload,
        )

        return IpEncapsulatingSecurityPayload(self)

    @property
    def IpAuthenticationHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipAuthenticationHeader_template.IpAuthenticationHeader): An instance of the IpAuthenticationHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipAuthenticationHeader_template import (
            IpAuthenticationHeader,
        )

        return IpAuthenticationHeader(self)

    @property
    def IpEspOverMACsec(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipEspOverMACsec_template.IpEspOverMACsec): An instance of the IpEspOverMACsec traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipEspOverMACsec_template import (
            IpEspOverMACsec,
        )

        return IpEspOverMACsec(self)

    @property
    def NFapiP7P19sHeader(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nFapiP7P19sHeader_template.NFapiP7P19sHeader): An instance of the NFapiP7P19sHeader traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nFapiP7P19sHeader_template import (
            NFapiP7P19sHeader,
        )

        return NFapiP7P19sHeader(self)

    @property
    def NFapiPayloadMarker(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nFapiPayloadMarker_template.NFapiPayloadMarker): An instance of the NFapiPayloadMarker traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nFapiPayloadMarker_template import (
            NFapiPayloadMarker,
        )

        return NFapiPayloadMarker(self)

    @property
    def Tcp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tcp_template.Tcp): An instance of the Tcp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tcp_template import (
            Tcp,
        )

        return Tcp(self)

    @property
    def Udp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.udp_template.Udp): An instance of the Udp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.udp_template import (
            Udp,
        )

        return Udp(self)

    @property
    def Guedata(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.guedata_template.Guedata): An instance of the Guedata traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.guedata_template import (
            Guedata,
        )

        return Guedata(self)

    @property
    def Bfd(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bfd_template.Bfd): An instance of the Bfd traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bfd_template import (
            Bfd,
        )

        return Bfd(self)

    @property
    def LISPMapRegister(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRegister_template.LISPMapRegister): An instance of the LISPMapRegister traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRegister_template import (
            LISPMapRegister,
        )

        return LISPMapRegister(self)

    @property
    def LISPMapRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRequest_template.LISPMapRequest): An instance of the LISPMapRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRequest_template import (
            LISPMapRequest,
        )

        return LISPMapRequest(self)

    @property
    def LISPMapReply(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapReply_template.LISPMapReply): An instance of the LISPMapReply traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapReply_template import (
            LISPMapReply,
        )

        return LISPMapReply(self)

    @property
    def LISPEncapsulatedControlMessage(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPEncapsulatedControlMessage_template.LISPEncapsulatedControlMessage): An instance of the LISPEncapsulatedControlMessage traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPEncapsulatedControlMessage_template import (
            LISPEncapsulatedControlMessage,
        )

        return LISPEncapsulatedControlMessage(self)

    @property
    def LISPMapNotify(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapNotify_template.LISPMapNotify): An instance of the LISPMapNotify traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapNotify_template import (
            LISPMapNotify,
        )

        return LISPMapNotify(self)

    @property
    def LISP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISP_template.LISP): An instance of the LISP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISP_template import (
            LISP,
        )

        return LISP(self)

    @property
    def Dhcp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcp_template.Dhcp): An instance of the Dhcp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcp_template import (
            Dhcp,
        )

        return Dhcp(self)

    @property
    def Dnsquery(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dnsquery_template.Dnsquery): An instance of the Dnsquery traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dnsquery_template import (
            Dnsquery,
        )

        return Dnsquery(self)

    @property
    def Dnsresponse(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dnsresponse_template.Dnsresponse): An instance of the Dnsresponse traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dnsresponse_template import (
            Dnsresponse,
        )

        return Dnsresponse(self)

    @property
    def DhcpWithPadding(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpWithPadding_template.DhcpWithPadding): An instance of the DhcpWithPadding traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpWithPadding_template import (
            DhcpWithPadding,
        )

        return DhcpWithPadding(self)

    @property
    def Dhcpv6ClientServer(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6ClientServer_template.Dhcpv6ClientServer): An instance of the Dhcpv6ClientServer traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6ClientServer_template import (
            Dhcpv6ClientServer,
        )

        return Dhcpv6ClientServer(self)

    @property
    def Dhcpv6Relay(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6Relay_template.Dhcpv6Relay): An instance of the Dhcpv6Relay traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6Relay_template import (
            Dhcpv6Relay,
        )

        return Dhcpv6Relay(self)

    @property
    def LdpNotification(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpNotification_template.LdpNotification): An instance of the LdpNotification traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpNotification_template import (
            LdpNotification,
        )

        return LdpNotification(self)

    @property
    def LdpHello(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpHello_template.LdpHello): An instance of the LdpHello traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpHello_template import (
            LdpHello,
        )

        return LdpHello(self)

    @property
    def LdpInitialization(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpInitialization_template.LdpInitialization): An instance of the LdpInitialization traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpInitialization_template import (
            LdpInitialization,
        )

        return LdpInitialization(self)

    @property
    def LdpKeepAlive(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpKeepAlive_template.LdpKeepAlive): An instance of the LdpKeepAlive traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpKeepAlive_template import (
            LdpKeepAlive,
        )

        return LdpKeepAlive(self)

    @property
    def LdpAddress(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddress_template.LdpAddress): An instance of the LdpAddress traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddress_template import (
            LdpAddress,
        )

        return LdpAddress(self)

    @property
    def LdpAddressWithdraw(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddressWithdraw_template.LdpAddressWithdraw): An instance of the LdpAddressWithdraw traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddressWithdraw_template import (
            LdpAddressWithdraw,
        )

        return LdpAddressWithdraw(self)

    @property
    def LdpLabelMapping(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelMapping_template.LdpLabelMapping): An instance of the LdpLabelMapping traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelMapping_template import (
            LdpLabelMapping,
        )

        return LdpLabelMapping(self)

    @property
    def LdpLabelRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRequest_template.LdpLabelRequest): An instance of the LdpLabelRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRequest_template import (
            LdpLabelRequest,
        )

        return LdpLabelRequest(self)

    @property
    def LdpLabelAbortRequest(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelAbortRequest_template.LdpLabelAbortRequest): An instance of the LdpLabelAbortRequest traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelAbortRequest_template import (
            LdpLabelAbortRequest,
        )

        return LdpLabelAbortRequest(self)

    @property
    def LdpLabelWithdraw(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelWithdraw_template.LdpLabelWithdraw): An instance of the LdpLabelWithdraw traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelWithdraw_template import (
            LdpLabelWithdraw,
        )

        return LdpLabelWithdraw(self)

    @property
    def LdpLabelRelease(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRelease_template.LdpLabelRelease): An instance of the LdpLabelRelease traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRelease_template import (
            LdpLabelRelease,
        )

        return LdpLabelRelease(self)

    @property
    def L2TPv2Control(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Control_template.L2TPv2Control): An instance of the L2TPv2Control traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Control_template import (
            L2TPv2Control,
        )

        return L2TPv2Control(self)

    @property
    def L2TPv2Data(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Data_template.L2TPv2Data): An instance of the L2TPv2Data traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Data_template import (
            L2TPv2Data,
        )

        return L2TPv2Data(self)

    @property
    def L2TPv3ControlUDP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlUDP_template.L2TPv3ControlUDP): An instance of the L2TPv3ControlUDP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlUDP_template import (
            L2TPv3ControlUDP,
        )

        return L2TPv3ControlUDP(self)

    @property
    def L2TPv3DataUDP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataUDP_template.L2TPv3DataUDP): An instance of the L2TPv3DataUDP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataUDP_template import (
            L2TPv3DataUDP,
        )

        return L2TPv3DataUDP(self)

    @property
    def MobileIP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIP_template.MobileIP): An instance of the MobileIP traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIP_template import (
            MobileIP,
        )

        return MobileIP(self)

    @property
    def Msdp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msdp_template.Msdp): An instance of the Msdp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msdp_template import (
            Msdp,
        )

        return Msdp(self)

    @property
    def PTPv2udp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2udp_template.PTPv2udp): An instance of the PTPv2udp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2udp_template import (
            PTPv2udp,
        )

        return PTPv2udp(self)

    @property
    def Rip1(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip1_template.Rip1): An instance of the Rip1 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip1_template import (
            Rip1,
        )

        return Rip1(self)

    @property
    def Rip2(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip2_template.Rip2): An instance of the Rip2 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip2_template import (
            Rip2,
        )

        return Rip2(self)

    @property
    def Ripng(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ripng_template.Ripng): An instance of the Ripng traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ripng_template import (
            Ripng,
        )

        return Ripng(self)

    @property
    def Rtp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtp_template.Rtp): An instance of the Rtp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtp_template import (
            Rtp,
        )

        return Rtp(self)

    @property
    def HTTPGET(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTPGET_template.HTTPGET): An instance of the HTTPGET traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTPGET_template import (
            HTTPGET,
        )

        return HTTPGET(self)

    @property
    def HTTP200OK(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTP200OK_template.HTTP200OK): An instance of the HTTP200OK traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTP200OK_template import (
            HTTP200OK,
        )

        return HTTP200OK(self)

    @property
    def RTSPDESCRIBE(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSPDESCRIBE_template.RTSPDESCRIBE): An instance of the RTSPDESCRIBE traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSPDESCRIBE_template import (
            RTSPDESCRIBE,
        )

        return RTSPDESCRIBE(self)

    @property
    def RTSPReply(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSPReply_template.RTSPReply): An instance of the RTSPReply traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSPReply_template import (
            RTSPReply,
        )

        return RTSPReply(self)

    @property
    def IMAPRequestCapability(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAPRequestCapability_template.IMAPRequestCapability): An instance of the IMAPRequestCapability traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAPRequestCapability_template import (
            IMAPRequestCapability,
        )

        return IMAPRequestCapability(self)

    @property
    def IMAPResponseCapabilityOK(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAPResponseCapabilityOK_template.IMAPResponseCapabilityOK): An instance of the IMAPResponseCapabilityOK traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAPResponseCapabilityOK_template import (
            IMAPResponseCapabilityOK,
        )

        return IMAPResponseCapabilityOK(self)

    @property
    def POPRETR1(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POPRETR1_template.POPRETR1): An instance of the POPRETR1 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POPRETR1_template import (
            POPRETR1,
        )

        return POPRETR1(self)

    @property
    def POPOK(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POPOK_template.POPOK): An instance of the POPOK traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POPOK_template import (
            POPOK,
        )

        return POPOK(self)

    @property
    def SMTPMAILFROM(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTPMAILFROM_template.SMTPMAILFROM): An instance of the SMTPMAILFROM traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTPMAILFROM_template import (
            SMTPMAILFROM,
        )

        return SMTPMAILFROM(self)

    @property
    def SMTP250OK(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTP250OK_template.SMTP250OK): An instance of the SMTP250OK traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTP250OK_template import (
            SMTP250OK,
        )

        return SMTP250OK(self)

    @property
    def TDSRemoteProcedureCall(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDSRemoteProcedureCall_template.TDSRemoteProcedureCall): An instance of the TDSRemoteProcedureCall traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDSRemoteProcedureCall_template import (
            TDSRemoteProcedureCall,
        )

        return TDSRemoteProcedureCall(self)

    @property
    def TDSResponse(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDSResponse_template.TDSResponse): An instance of the TDSResponse traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDSResponse_template import (
            TDSResponse,
        )

        return TDSResponse(self)

    @property
    def ISCSIDataOut(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSIDataOut_template.ISCSIDataOut): An instance of the ISCSIDataOut traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSIDataOut_template import (
            ISCSIDataOut,
        )

        return ISCSIDataOut(self)

    @property
    def ISCSIDataIn(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSIDataIn_template.ISCSIDataIn): An instance of the ISCSIDataIn traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSIDataIn_template import (
            ISCSIDataIn,
        )

        return ISCSIDataIn(self)

    @property
    def Ntp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ntp_template.Ntp): An instance of the Ntp traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ntp_template import (
            Ntp,
        )

        return Ntp(self)

    @property
    def Roe(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.roe_template.Roe): An instance of the Roe traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.roe_template import (
            Roe,
        )

        return Roe(self)

    @property
    def Custom(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.custom_template.Custom): An instance of the Custom traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.custom_template import (
            Custom,
        )

        return Custom(self)

    @property
    def Customv2(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.customv2_template.Customv2): An instance of the Customv2 traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.customv2_template import (
            Customv2,
        )

        return Customv2(self)

    @property
    def Fc(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fc_template.Fc): An instance of the Fc traffic stack
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fc_template import (
            Fc,
        )

        return Fc(self)

    @property
    def DisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The display name of the stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisplayName"])

    @property
    def StackTypeId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackTypeId"])

    @property
    def TemplateName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indiates the protocol template name that is added to a packet in a stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TemplateName"])

    def add(self):
        """Adds a new stack resource on the json, only valid with batch add utility

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
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("append", payload=payload, response_object=None)

    def AppendProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the appendProtocol operation on the server.

        Append a protocol template after the specified stack object reference.

        appendProtocol(Arg2=href, async_operation=bool)href
        ---------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficItem/configElement/stack): This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("appendProtocol", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getValidProtocols", payload=payload, response_object=None)

    def Insert(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the insert operation on the server.

        Insert a protocol template before the specified stack object reference.

        DEPRECATED insert(Arg2=href, async_operation=bool)string
        --------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("insert", payload=payload, response_object=None)

    def InsertProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the insertProtocol operation on the server.

        Insert a protocol template before the specified stack object reference.

        insertProtocol(Arg2=href, async_operation=bool)href
        ---------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficItem/configElement/stack): This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("insertProtocol", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("remove", payload=payload, response_object=None)
