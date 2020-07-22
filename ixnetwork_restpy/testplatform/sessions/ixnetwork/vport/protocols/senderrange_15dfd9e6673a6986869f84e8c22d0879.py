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


class SenderRange(Base):
    """Holds the information related to the originating routers for the MPLS tunnels being simulated in Ingress cases.
    The SenderRange class encapsulates a list of senderRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SenderRange.find() method.
    The list can be managed by using the SenderRange.add() and SenderRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'senderRange'
    _SDM_ATT_MAP = {
        'AutoGenerateSessionName': 'autoGenerateSessionName',
        'BackupLspIdPoolStart': 'backupLspIdPoolStart',
        'Bandwidth': 'bandwidth',
        'BandwidthProtectionDesired': 'bandwidthProtectionDesired',
        'EnableBfdMpls': 'enableBfdMpls',
        'EnableFastReroute': 'enableFastReroute',
        'EnableLspPing': 'enableLspPing',
        'EnablePathReoptimization': 'enablePathReoptimization',
        'EnablePeriodicReEvaluationRequest': 'enablePeriodicReEvaluationRequest',
        'EnableResourceAffinities': 'enableResourceAffinities',
        'Enabled': 'enabled',
        'ExcludeAny': 'excludeAny',
        'FastRerouteBandwidth': 'fastRerouteBandwidth',
        'FastRerouteDetour': 'fastRerouteDetour',
        'FastRerouteExcludeAny': 'fastRerouteExcludeAny',
        'FastRerouteFacilityBackupDesired': 'fastRerouteFacilityBackupDesired',
        'FastRerouteHoldingPriority': 'fastRerouteHoldingPriority',
        'FastRerouteHopLimit': 'fastRerouteHopLimit',
        'FastRerouteIncludeAll': 'fastRerouteIncludeAll',
        'FastRerouteIncludeAny': 'fastRerouteIncludeAny',
        'FastRerouteOne2OneBackupDesired': 'fastRerouteOne2OneBackupDesired',
        'FastRerouteSendDetour': 'fastRerouteSendDetour',
        'FastRerouteSetupPriority': 'fastRerouteSetupPriority',
        'HoldingPriority': 'holdingPriority',
        'IncludeAll': 'includeAll',
        'IncludeAny': 'includeAny',
        'IpCount': 'ipCount',
        'IpStart': 'ipStart',
        'LabelRecordingDesired': 'labelRecordingDesired',
        'LocalProtectionDesired': 'localProtectionDesired',
        'LspIdCount': 'lspIdCount',
        'LspIdStart': 'lspIdStart',
        'MaximumPacketSize': 'maximumPacketSize',
        'MinimumPolicedUnit': 'minimumPolicedUnit',
        'NodeProtectionDesired': 'nodeProtectionDesired',
        'PathTearTlv': 'pathTearTlv',
        'PathTlv': 'pathTlv',
        'PeakDataRate': 'peakDataRate',
        'ReEvaluationRequestInterval': 'reEvaluationRequestInterval',
        'RefreshInterval': 'refreshInterval',
        'SeStyleDesired': 'seStyleDesired',
        'SessionName': 'sessionName',
        'SetupPriority': 'setupPriority',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TokenBucketRate': 'tokenBucketRate',
        'TokenBucketSize': 'tokenBucketSize',
    }

    def __init__(self, parent):
        super(SenderRange, self).__init__(parent)

    @property
    def TunnelHeadToLeaf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtoleaf_e69a9a69601e0735ed9794ff412c72e6.TunnelHeadToLeaf): An instance of the TunnelHeadToLeaf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtoleaf_e69a9a69601e0735ed9794ff412c72e6 import TunnelHeadToLeaf
        return TunnelHeadToLeaf(self)

    @property
    def TunnelHeadTrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtrafficendpoint_399e6e14fa13954b413c4572ebd3725e.TunnelHeadTrafficEndPoint): An instance of the TunnelHeadTrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtrafficendpoint_399e6e14fa13954b413c4572ebd3725e import TunnelHeadTrafficEndPoint
        return TunnelHeadTrafficEndPoint(self)

    @property
    def AutoGenerateSessionName(self):
        """
        Returns
        -------
        - bool: If enabled, the session name is generated automatically. If it is not enabled, the session name field is activated and must be filled in.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoGenerateSessionName'])
    @AutoGenerateSessionName.setter
    def AutoGenerateSessionName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoGenerateSessionName'], value)

    @property
    def BackupLspIdPoolStart(self):
        """
        Returns
        -------
        - number: It helps to set the LSP Id for the re-optimized LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BackupLspIdPoolStart'])
    @BackupLspIdPoolStart.setter
    def BackupLspIdPoolStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BackupLspIdPoolStart'], value)

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - str: The bandwidth requested for the connection, expressed in kbits/sec.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Bandwidth'])
    @Bandwidth.setter
    def Bandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Bandwidth'], value)

    @property
    def BandwidthProtectionDesired(self):
        """
        Returns
        -------
        - bool: Indicates that PLRs should skip at least the next node for a backup path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BandwidthProtectionDesired'])
    @BandwidthProtectionDesired.setter
    def BandwidthProtectionDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BandwidthProtectionDesired'], value)

    @property
    def EnableBfdMpls(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdMpls'])
    @EnableBfdMpls.setter
    def EnableBfdMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdMpls'], value)

    @property
    def EnableFastReroute(self):
        """
        Returns
        -------
        - bool: Enables the use of the fast reroute feature.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFastReroute'])
    @EnableFastReroute.setter
    def EnableFastReroute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFastReroute'], value)

    @property
    def EnableLspPing(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLspPing'])
    @EnableLspPing.setter
    def EnableLspPing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLspPing'], value)

    @property
    def EnablePathReoptimization(self):
        """
        Returns
        -------
        - bool: If true, enables the Path Re-optimization option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePathReoptimization'])
    @EnablePathReoptimization.setter
    def EnablePathReoptimization(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePathReoptimization'], value)

    @property
    def EnablePeriodicReEvaluationRequest(self):
        """
        Returns
        -------
        - bool: If true, enables the head LSR to send periodic path re-evaluation request in every Re-Optimization Interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicReEvaluationRequest'])
    @EnablePeriodicReEvaluationRequest.setter
    def EnablePeriodicReEvaluationRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePeriodicReEvaluationRequest'], value)

    @property
    def EnableResourceAffinities(self):
        """
        Returns
        -------
        - bool: Enables the use of RSVP resource class affinities for LSP tunnels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableResourceAffinities'])
    @EnableResourceAffinities.setter
    def EnableResourceAffinities(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableResourceAffinities'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the sender range entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ExcludeAny(self):
        """
        Returns
        -------
        - number: Represents a set of attribute filters associated with a tunnel, any of which renders a link unacceptable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExcludeAny'])
    @ExcludeAny.setter
    def ExcludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExcludeAny'], value)

    @property
    def FastRerouteBandwidth(self):
        """
        Returns
        -------
        - str: An estimate of the bandwidth needed for the protection path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteBandwidth'])
    @FastRerouteBandwidth.setter
    def FastRerouteBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteBandwidth'], value)

    @property
    def FastRerouteDetour(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str)): Used to provide backup LSP tunnels for local repair of LSP tunnels, in the event of failure of a node or link. Contains the specifics of the detour LSPs: nodes to use and nodes to avoid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteDetour'])
    @FastRerouteDetour.setter
    def FastRerouteDetour(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteDetour'], value)

    @property
    def FastRerouteExcludeAny(self):
        """
        Returns
        -------
        - number: Capability filters used to dictate which backup paths are acceptable or unacceptable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteExcludeAny'])
    @FastRerouteExcludeAny.setter
    def FastRerouteExcludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteExcludeAny'], value)

    @property
    def FastRerouteFacilityBackupDesired(self):
        """
        Returns
        -------
        - bool: If enabled, indicates that facility backup should be used. With this method, the MPLS label stack allows the creation of a bypass tunnel to protect a set of LSPs with similar characteristics/constraints. Protects both links and nodes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteFacilityBackupDesired'])
    @FastRerouteFacilityBackupDesired.setter
    def FastRerouteFacilityBackupDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteFacilityBackupDesired'], value)

    @property
    def FastRerouteHoldingPriority(self):
        """
        Returns
        -------
        - number: The priority value for the backup path, pertaining to holding resources - whether a session can be preempted BY another session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteHoldingPriority'])
    @FastRerouteHoldingPriority.setter
    def FastRerouteHoldingPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteHoldingPriority'], value)

    @property
    def FastRerouteHopLimit(self):
        """
        Returns
        -------
        - number: Indicates the number of extra hops that may be added by a protection path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteHopLimit'])
    @FastRerouteHopLimit.setter
    def FastRerouteHopLimit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteHopLimit'], value)

    @property
    def FastRerouteIncludeAll(self):
        """
        Returns
        -------
        - number: Capability filters used to dictate which backup paths are acceptable or unacceptable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAll'])
    @FastRerouteIncludeAll.setter
    def FastRerouteIncludeAll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAll'], value)

    @property
    def FastRerouteIncludeAny(self):
        """
        Returns
        -------
        - number: Capability filters used to dictate which backup paths are acceptable or unacceptable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAny'])
    @FastRerouteIncludeAny.setter
    def FastRerouteIncludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAny'], value)

    @property
    def FastRerouteOne2OneBackupDesired(self):
        """
        Returns
        -------
        - bool: If enabled, indicates that one-to-one backup should be used. With this method, one detour LSP will be created for each protected LSP for each place where the LSP could potentially be repaired locally. Protects both links and nodes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteOne2OneBackupDesired'])
    @FastRerouteOne2OneBackupDesired.setter
    def FastRerouteOne2OneBackupDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteOne2OneBackupDesired'], value)

    @property
    def FastRerouteSendDetour(self):
        """
        Returns
        -------
        - bool: Enables the generation of a DETOUR object for one to one operation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteSendDetour'])
    @FastRerouteSendDetour.setter
    def FastRerouteSendDetour(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteSendDetour'], value)

    @property
    def FastRerouteSetupPriority(self):
        """
        Returns
        -------
        - number: Indicate the priority for taking and holding resources along the backup path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteSetupPriority'])
    @FastRerouteSetupPriority.setter
    def FastRerouteSetupPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteSetupPriority'], value)

    @property
    def HoldingPriority(self):
        """
        Returns
        -------
        - number: Priority in holding onto resources. Range is 0 to 7, with 0 the highest priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HoldingPriority'])
    @HoldingPriority.setter
    def HoldingPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HoldingPriority'], value)

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - number: 32-bit value. Represents a set of attribute filters associated with a tunnel, all of which must be present for a link to be acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeAll'])
    @IncludeAll.setter
    def IncludeAll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeAll'], value)

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - number: 32-bit value. Represents a set of attribute filters associated with a tunnel, any of which makes a link acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeAny'])
    @IncludeAny.setter
    def IncludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeAny'], value)

    @property
    def IpCount(self):
        """
        Returns
        -------
        - number: The number of routers in the destination range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpCount'])
    @IpCount.setter
    def IpCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpCount'], value)

    @property
    def IpStart(self):
        """
        Returns
        -------
        - str: The IP address of the first destination router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpStart'])
    @IpStart.setter
    def IpStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpStart'], value)

    @property
    def LabelRecordingDesired(self):
        """
        Returns
        -------
        - bool: If enabled, indicates that label information is to be included when doing a route record.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelRecordingDesired'])
    @LabelRecordingDesired.setter
    def LabelRecordingDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelRecordingDesired'], value)

    @property
    def LocalProtectionDesired(self):
        """
        Returns
        -------
        - bool: (Enabled by default) This permits transit routers to use a local traffic rerouting repair mechanism in the event of a fault on an adjacent downstream link or node. This may result in a violation of the explicit route object.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalProtectionDesired'])
    @LocalProtectionDesired.setter
    def LocalProtectionDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocalProtectionDesired'], value)

    @property
    def LspIdCount(self):
        """
        Returns
        -------
        - number: The number of LSP IDs in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspIdCount'])
    @LspIdCount.setter
    def LspIdCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspIdCount'], value)

    @property
    def LspIdStart(self):
        """
        Returns
        -------
        - number: The first label-switched path ID (LSP ID) value in the range of LSP IDs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspIdStart'])
    @LspIdStart.setter
    def LspIdStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspIdStart'], value)

    @property
    def MaximumPacketSize(self):
        """
        Returns
        -------
        - number: 32-bit integer. The maximum number of bytes allowed to cross the interface in a transmitted packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumPacketSize'])
    @MaximumPacketSize.setter
    def MaximumPacketSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaximumPacketSize'], value)

    @property
    def MinimumPolicedUnit(self):
        """
        Returns
        -------
        - number: 32-bit integer. The minimum allowable size for a policed unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinimumPolicedUnit'])
    @MinimumPolicedUnit.setter
    def MinimumPolicedUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinimumPolicedUnit'], value)

    @property
    def NodeProtectionDesired(self):
        """
        Returns
        -------
        - bool: For Fast Reroute - if enabled, sets the Node Protection Desired Flag in the Session_Attribute object of the RRO message. It indicates to PLRs associated with the protected LSP path, that a backup path is desired that bypasses (avoids) at least the next node on the LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NodeProtectionDesired'])
    @NodeProtectionDesired.setter
    def NodeProtectionDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NodeProtectionDesired'], value)

    @property
    def PathTearTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): A set of custom TLVs to be included in TEAR messages, constructed with the rsvpCustomTlv command.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PathTearTlv'])
    @PathTearTlv.setter
    def PathTearTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PathTearTlv'], value)

    @property
    def PathTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): A set of custom TLVs to be included in PATH messages, constructed with the rsvpCustomTlv command.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PathTlv'])
    @PathTlv.setter
    def PathTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PathTlv'], value)

    @property
    def PeakDataRate(self):
        """
        Returns
        -------
        - number: The maximum traffic rate that can be maintained. The policing mechanism allows some burstiness, but restricts it so the overall packet transmission rate is less than the rate at which tokens.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeakDataRate'])
    @PeakDataRate.setter
    def PeakDataRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeakDataRate'], value)

    @property
    def ReEvaluationRequestInterval(self):
        """
        Returns
        -------
        - number: Represents the time period (in milliseconds) at which the path re-evaluation request is sent by the head LSR. The default value is: 180000 ms (3 mins).
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReEvaluationRequestInterval'])
    @ReEvaluationRequestInterval.setter
    def ReEvaluationRequestInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReEvaluationRequestInterval'], value)

    @property
    def RefreshInterval(self):
        """
        Returns
        -------
        - number: The interval between summary refresh messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RefreshInterval'])
    @RefreshInterval.setter
    def RefreshInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RefreshInterval'], value)

    @property
    def SeStyleDesired(self):
        """
        Returns
        -------
        - bool: This indicates that the tunnel ingress node may reroute this tunnel without tearing it down. A tunnel egress node should use the SE Style when responding with an RESV message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeStyleDesired'])
    @SeStyleDesired.setter
    def SeStyleDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SeStyleDesired'], value)

    @property
    def SessionName(self):
        """
        Returns
        -------
        - str: If enableAutoSessionName is not set, this is the name assigned to this session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionName'])
    @SessionName.setter
    def SessionName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SessionName'], value)

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - number: This is the session priority with respect to taking resources, such as preempting another session. The valid range is from 0 to 7. The highest priority is indicated by 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupPriority'])
    @SetupPriority.setter
    def SetupPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupPriority'], value)

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - number: The number of Hellos before a neighbor is declared dead.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier'])
    @TimeoutMultiplier.setter
    def TimeoutMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeoutMultiplier'], value)

    @property
    def TokenBucketRate(self):
        """
        Returns
        -------
        - number: The rate of transfer for data in a flow. In this application, it is used with a traffic policing mechanism. The data tokens enter the bucket, filling the bucket. The data from a number of tokens is combined to form and send a packet. The goal is to determine a rate which will not overflow the specified token bucket size, and cause new data (tokens) to be rejected/discarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TokenBucketRate'])
    @TokenBucketRate.setter
    def TokenBucketRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TokenBucketRate'], value)

    @property
    def TokenBucketSize(self):
        """
        Returns
        -------
        - number: The maximum capacity (in bytes) the token bucket can hold, and above which newly received tokens cannot be processed and are discarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TokenBucketSize'])
    @TokenBucketSize.setter
    def TokenBucketSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TokenBucketSize'], value)

    def update(self, AutoGenerateSessionName=None, BackupLspIdPoolStart=None, Bandwidth=None, BandwidthProtectionDesired=None, EnableBfdMpls=None, EnableFastReroute=None, EnableLspPing=None, EnablePathReoptimization=None, EnablePeriodicReEvaluationRequest=None, EnableResourceAffinities=None, Enabled=None, ExcludeAny=None, FastRerouteBandwidth=None, FastRerouteDetour=None, FastRerouteExcludeAny=None, FastRerouteFacilityBackupDesired=None, FastRerouteHoldingPriority=None, FastRerouteHopLimit=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteOne2OneBackupDesired=None, FastRerouteSendDetour=None, FastRerouteSetupPriority=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IpCount=None, IpStart=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspIdCount=None, LspIdStart=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, PathTearTlv=None, PathTlv=None, PeakDataRate=None, ReEvaluationRequestInterval=None, RefreshInterval=None, SeStyleDesired=None, SessionName=None, SetupPriority=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None):
        """Updates senderRange resource on the server.

        Args
        ----
        - AutoGenerateSessionName (bool): If enabled, the session name is generated automatically. If it is not enabled, the session name field is activated and must be filled in.
        - BackupLspIdPoolStart (number): It helps to set the LSP Id for the re-optimized LSP.
        - Bandwidth (str): The bandwidth requested for the connection, expressed in kbits/sec.
        - BandwidthProtectionDesired (bool): Indicates that PLRs should skip at least the next node for a backup path.
        - EnableBfdMpls (bool): NOT DEFINED
        - EnableFastReroute (bool): Enables the use of the fast reroute feature.
        - EnableLspPing (bool): NOT DEFINED
        - EnablePathReoptimization (bool): If true, enables the Path Re-optimization option.
        - EnablePeriodicReEvaluationRequest (bool): If true, enables the head LSR to send periodic path re-evaluation request in every Re-Optimization Interval.
        - EnableResourceAffinities (bool): Enables the use of RSVP resource class affinities for LSP tunnels.
        - Enabled (bool): Enables the sender range entry.
        - ExcludeAny (number): Represents a set of attribute filters associated with a tunnel, any of which renders a link unacceptable.
        - FastRerouteBandwidth (str): An estimate of the bandwidth needed for the protection path.
        - FastRerouteDetour (list(dict(arg1:str,arg2:str))): Used to provide backup LSP tunnels for local repair of LSP tunnels, in the event of failure of a node or link. Contains the specifics of the detour LSPs: nodes to use and nodes to avoid.
        - FastRerouteExcludeAny (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteFacilityBackupDesired (bool): If enabled, indicates that facility backup should be used. With this method, the MPLS label stack allows the creation of a bypass tunnel to protect a set of LSPs with similar characteristics/constraints. Protects both links and nodes.
        - FastRerouteHoldingPriority (number): The priority value for the backup path, pertaining to holding resources - whether a session can be preempted BY another session.
        - FastRerouteHopLimit (number): Indicates the number of extra hops that may be added by a protection path.
        - FastRerouteIncludeAll (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteIncludeAny (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteOne2OneBackupDesired (bool): If enabled, indicates that one-to-one backup should be used. With this method, one detour LSP will be created for each protected LSP for each place where the LSP could potentially be repaired locally. Protects both links and nodes.
        - FastRerouteSendDetour (bool): Enables the generation of a DETOUR object for one to one operation.
        - FastRerouteSetupPriority (number): Indicate the priority for taking and holding resources along the backup path.
        - HoldingPriority (number): Priority in holding onto resources. Range is 0 to 7, with 0 the highest priority.
        - IncludeAll (number): 32-bit value. Represents a set of attribute filters associated with a tunnel, all of which must be present for a link to be acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        - IncludeAny (number): 32-bit value. Represents a set of attribute filters associated with a tunnel, any of which makes a link acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        - IpCount (number): The number of routers in the destination range.
        - IpStart (str): The IP address of the first destination router.
        - LabelRecordingDesired (bool): If enabled, indicates that label information is to be included when doing a route record.
        - LocalProtectionDesired (bool): (Enabled by default) This permits transit routers to use a local traffic rerouting repair mechanism in the event of a fault on an adjacent downstream link or node. This may result in a violation of the explicit route object.
        - LspIdCount (number): The number of LSP IDs in the range.
        - LspIdStart (number): The first label-switched path ID (LSP ID) value in the range of LSP IDs.
        - MaximumPacketSize (number): 32-bit integer. The maximum number of bytes allowed to cross the interface in a transmitted packet.
        - MinimumPolicedUnit (number): 32-bit integer. The minimum allowable size for a policed unit.
        - NodeProtectionDesired (bool): For Fast Reroute - if enabled, sets the Node Protection Desired Flag in the Session_Attribute object of the RRO message. It indicates to PLRs associated with the protected LSP path, that a backup path is desired that bypasses (avoids) at least the next node on the LSP.
        - PathTearTlv (list(dict(arg1:number,arg2:number,arg3:str))): A set of custom TLVs to be included in TEAR messages, constructed with the rsvpCustomTlv command.
        - PathTlv (list(dict(arg1:number,arg2:number,arg3:str))): A set of custom TLVs to be included in PATH messages, constructed with the rsvpCustomTlv command.
        - PeakDataRate (number): The maximum traffic rate that can be maintained. The policing mechanism allows some burstiness, but restricts it so the overall packet transmission rate is less than the rate at which tokens.
        - ReEvaluationRequestInterval (number): Represents the time period (in milliseconds) at which the path re-evaluation request is sent by the head LSR. The default value is: 180000 ms (3 mins).
        - RefreshInterval (number): The interval between summary refresh messages.
        - SeStyleDesired (bool): This indicates that the tunnel ingress node may reroute this tunnel without tearing it down. A tunnel egress node should use the SE Style when responding with an RESV message.
        - SessionName (str): If enableAutoSessionName is not set, this is the name assigned to this session.
        - SetupPriority (number): This is the session priority with respect to taking resources, such as preempting another session. The valid range is from 0 to 7. The highest priority is indicated by 0.
        - TimeoutMultiplier (number): The number of Hellos before a neighbor is declared dead.
        - TokenBucketRate (number): The rate of transfer for data in a flow. In this application, it is used with a traffic policing mechanism. The data tokens enter the bucket, filling the bucket. The data from a number of tokens is combined to form and send a packet. The goal is to determine a rate which will not overflow the specified token bucket size, and cause new data (tokens) to be rejected/discarded.
        - TokenBucketSize (number): The maximum capacity (in bytes) the token bucket can hold, and above which newly received tokens cannot be processed and are discarded.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoGenerateSessionName=None, BackupLspIdPoolStart=None, Bandwidth=None, BandwidthProtectionDesired=None, EnableBfdMpls=None, EnableFastReroute=None, EnableLspPing=None, EnablePathReoptimization=None, EnablePeriodicReEvaluationRequest=None, EnableResourceAffinities=None, Enabled=None, ExcludeAny=None, FastRerouteBandwidth=None, FastRerouteDetour=None, FastRerouteExcludeAny=None, FastRerouteFacilityBackupDesired=None, FastRerouteHoldingPriority=None, FastRerouteHopLimit=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteOne2OneBackupDesired=None, FastRerouteSendDetour=None, FastRerouteSetupPriority=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IpCount=None, IpStart=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspIdCount=None, LspIdStart=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, PathTearTlv=None, PathTlv=None, PeakDataRate=None, ReEvaluationRequestInterval=None, RefreshInterval=None, SeStyleDesired=None, SessionName=None, SetupPriority=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None):
        """Adds a new senderRange resource on the server and adds it to the container.

        Args
        ----
        - AutoGenerateSessionName (bool): If enabled, the session name is generated automatically. If it is not enabled, the session name field is activated and must be filled in.
        - BackupLspIdPoolStart (number): It helps to set the LSP Id for the re-optimized LSP.
        - Bandwidth (str): The bandwidth requested for the connection, expressed in kbits/sec.
        - BandwidthProtectionDesired (bool): Indicates that PLRs should skip at least the next node for a backup path.
        - EnableBfdMpls (bool): NOT DEFINED
        - EnableFastReroute (bool): Enables the use of the fast reroute feature.
        - EnableLspPing (bool): NOT DEFINED
        - EnablePathReoptimization (bool): If true, enables the Path Re-optimization option.
        - EnablePeriodicReEvaluationRequest (bool): If true, enables the head LSR to send periodic path re-evaluation request in every Re-Optimization Interval.
        - EnableResourceAffinities (bool): Enables the use of RSVP resource class affinities for LSP tunnels.
        - Enabled (bool): Enables the sender range entry.
        - ExcludeAny (number): Represents a set of attribute filters associated with a tunnel, any of which renders a link unacceptable.
        - FastRerouteBandwidth (str): An estimate of the bandwidth needed for the protection path.
        - FastRerouteDetour (list(dict(arg1:str,arg2:str))): Used to provide backup LSP tunnels for local repair of LSP tunnels, in the event of failure of a node or link. Contains the specifics of the detour LSPs: nodes to use and nodes to avoid.
        - FastRerouteExcludeAny (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteFacilityBackupDesired (bool): If enabled, indicates that facility backup should be used. With this method, the MPLS label stack allows the creation of a bypass tunnel to protect a set of LSPs with similar characteristics/constraints. Protects both links and nodes.
        - FastRerouteHoldingPriority (number): The priority value for the backup path, pertaining to holding resources - whether a session can be preempted BY another session.
        - FastRerouteHopLimit (number): Indicates the number of extra hops that may be added by a protection path.
        - FastRerouteIncludeAll (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteIncludeAny (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteOne2OneBackupDesired (bool): If enabled, indicates that one-to-one backup should be used. With this method, one detour LSP will be created for each protected LSP for each place where the LSP could potentially be repaired locally. Protects both links and nodes.
        - FastRerouteSendDetour (bool): Enables the generation of a DETOUR object for one to one operation.
        - FastRerouteSetupPriority (number): Indicate the priority for taking and holding resources along the backup path.
        - HoldingPriority (number): Priority in holding onto resources. Range is 0 to 7, with 0 the highest priority.
        - IncludeAll (number): 32-bit value. Represents a set of attribute filters associated with a tunnel, all of which must be present for a link to be acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        - IncludeAny (number): 32-bit value. Represents a set of attribute filters associated with a tunnel, any of which makes a link acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        - IpCount (number): The number of routers in the destination range.
        - IpStart (str): The IP address of the first destination router.
        - LabelRecordingDesired (bool): If enabled, indicates that label information is to be included when doing a route record.
        - LocalProtectionDesired (bool): (Enabled by default) This permits transit routers to use a local traffic rerouting repair mechanism in the event of a fault on an adjacent downstream link or node. This may result in a violation of the explicit route object.
        - LspIdCount (number): The number of LSP IDs in the range.
        - LspIdStart (number): The first label-switched path ID (LSP ID) value in the range of LSP IDs.
        - MaximumPacketSize (number): 32-bit integer. The maximum number of bytes allowed to cross the interface in a transmitted packet.
        - MinimumPolicedUnit (number): 32-bit integer. The minimum allowable size for a policed unit.
        - NodeProtectionDesired (bool): For Fast Reroute - if enabled, sets the Node Protection Desired Flag in the Session_Attribute object of the RRO message. It indicates to PLRs associated with the protected LSP path, that a backup path is desired that bypasses (avoids) at least the next node on the LSP.
        - PathTearTlv (list(dict(arg1:number,arg2:number,arg3:str))): A set of custom TLVs to be included in TEAR messages, constructed with the rsvpCustomTlv command.
        - PathTlv (list(dict(arg1:number,arg2:number,arg3:str))): A set of custom TLVs to be included in PATH messages, constructed with the rsvpCustomTlv command.
        - PeakDataRate (number): The maximum traffic rate that can be maintained. The policing mechanism allows some burstiness, but restricts it so the overall packet transmission rate is less than the rate at which tokens.
        - ReEvaluationRequestInterval (number): Represents the time period (in milliseconds) at which the path re-evaluation request is sent by the head LSR. The default value is: 180000 ms (3 mins).
        - RefreshInterval (number): The interval between summary refresh messages.
        - SeStyleDesired (bool): This indicates that the tunnel ingress node may reroute this tunnel without tearing it down. A tunnel egress node should use the SE Style when responding with an RESV message.
        - SessionName (str): If enableAutoSessionName is not set, this is the name assigned to this session.
        - SetupPriority (number): This is the session priority with respect to taking resources, such as preempting another session. The valid range is from 0 to 7. The highest priority is indicated by 0.
        - TimeoutMultiplier (number): The number of Hellos before a neighbor is declared dead.
        - TokenBucketRate (number): The rate of transfer for data in a flow. In this application, it is used with a traffic policing mechanism. The data tokens enter the bucket, filling the bucket. The data from a number of tokens is combined to form and send a packet. The goal is to determine a rate which will not overflow the specified token bucket size, and cause new data (tokens) to be rejected/discarded.
        - TokenBucketSize (number): The maximum capacity (in bytes) the token bucket can hold, and above which newly received tokens cannot be processed and are discarded.

        Returns
        -------
        - self: This instance with all currently retrieved senderRange resources using find and the newly added senderRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained senderRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoGenerateSessionName=None, BackupLspIdPoolStart=None, Bandwidth=None, BandwidthProtectionDesired=None, EnableBfdMpls=None, EnableFastReroute=None, EnableLspPing=None, EnablePathReoptimization=None, EnablePeriodicReEvaluationRequest=None, EnableResourceAffinities=None, Enabled=None, ExcludeAny=None, FastRerouteBandwidth=None, FastRerouteDetour=None, FastRerouteExcludeAny=None, FastRerouteFacilityBackupDesired=None, FastRerouteHoldingPriority=None, FastRerouteHopLimit=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteOne2OneBackupDesired=None, FastRerouteSendDetour=None, FastRerouteSetupPriority=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IpCount=None, IpStart=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspIdCount=None, LspIdStart=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, PathTearTlv=None, PathTlv=None, PeakDataRate=None, ReEvaluationRequestInterval=None, RefreshInterval=None, SeStyleDesired=None, SessionName=None, SetupPriority=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None):
        """Finds and retrieves senderRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve senderRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all senderRange resources from the server.

        Args
        ----
        - AutoGenerateSessionName (bool): If enabled, the session name is generated automatically. If it is not enabled, the session name field is activated and must be filled in.
        - BackupLspIdPoolStart (number): It helps to set the LSP Id for the re-optimized LSP.
        - Bandwidth (str): The bandwidth requested for the connection, expressed in kbits/sec.
        - BandwidthProtectionDesired (bool): Indicates that PLRs should skip at least the next node for a backup path.
        - EnableBfdMpls (bool): NOT DEFINED
        - EnableFastReroute (bool): Enables the use of the fast reroute feature.
        - EnableLspPing (bool): NOT DEFINED
        - EnablePathReoptimization (bool): If true, enables the Path Re-optimization option.
        - EnablePeriodicReEvaluationRequest (bool): If true, enables the head LSR to send periodic path re-evaluation request in every Re-Optimization Interval.
        - EnableResourceAffinities (bool): Enables the use of RSVP resource class affinities for LSP tunnels.
        - Enabled (bool): Enables the sender range entry.
        - ExcludeAny (number): Represents a set of attribute filters associated with a tunnel, any of which renders a link unacceptable.
        - FastRerouteBandwidth (str): An estimate of the bandwidth needed for the protection path.
        - FastRerouteDetour (list(dict(arg1:str,arg2:str))): Used to provide backup LSP tunnels for local repair of LSP tunnels, in the event of failure of a node or link. Contains the specifics of the detour LSPs: nodes to use and nodes to avoid.
        - FastRerouteExcludeAny (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteFacilityBackupDesired (bool): If enabled, indicates that facility backup should be used. With this method, the MPLS label stack allows the creation of a bypass tunnel to protect a set of LSPs with similar characteristics/constraints. Protects both links and nodes.
        - FastRerouteHoldingPriority (number): The priority value for the backup path, pertaining to holding resources - whether a session can be preempted BY another session.
        - FastRerouteHopLimit (number): Indicates the number of extra hops that may be added by a protection path.
        - FastRerouteIncludeAll (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteIncludeAny (number): Capability filters used to dictate which backup paths are acceptable or unacceptable.
        - FastRerouteOne2OneBackupDesired (bool): If enabled, indicates that one-to-one backup should be used. With this method, one detour LSP will be created for each protected LSP for each place where the LSP could potentially be repaired locally. Protects both links and nodes.
        - FastRerouteSendDetour (bool): Enables the generation of a DETOUR object for one to one operation.
        - FastRerouteSetupPriority (number): Indicate the priority for taking and holding resources along the backup path.
        - HoldingPriority (number): Priority in holding onto resources. Range is 0 to 7, with 0 the highest priority.
        - IncludeAll (number): 32-bit value. Represents a set of attribute filters associated with a tunnel, all of which must be present for a link to be acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        - IncludeAny (number): 32-bit value. Represents a set of attribute filters associated with a tunnel, any of which makes a link acceptable (with respect to this test). When all bits are set to 0 (null set), it automatically passes.
        - IpCount (number): The number of routers in the destination range.
        - IpStart (str): The IP address of the first destination router.
        - LabelRecordingDesired (bool): If enabled, indicates that label information is to be included when doing a route record.
        - LocalProtectionDesired (bool): (Enabled by default) This permits transit routers to use a local traffic rerouting repair mechanism in the event of a fault on an adjacent downstream link or node. This may result in a violation of the explicit route object.
        - LspIdCount (number): The number of LSP IDs in the range.
        - LspIdStart (number): The first label-switched path ID (LSP ID) value in the range of LSP IDs.
        - MaximumPacketSize (number): 32-bit integer. The maximum number of bytes allowed to cross the interface in a transmitted packet.
        - MinimumPolicedUnit (number): 32-bit integer. The minimum allowable size for a policed unit.
        - NodeProtectionDesired (bool): For Fast Reroute - if enabled, sets the Node Protection Desired Flag in the Session_Attribute object of the RRO message. It indicates to PLRs associated with the protected LSP path, that a backup path is desired that bypasses (avoids) at least the next node on the LSP.
        - PathTearTlv (list(dict(arg1:number,arg2:number,arg3:str))): A set of custom TLVs to be included in TEAR messages, constructed with the rsvpCustomTlv command.
        - PathTlv (list(dict(arg1:number,arg2:number,arg3:str))): A set of custom TLVs to be included in PATH messages, constructed with the rsvpCustomTlv command.
        - PeakDataRate (number): The maximum traffic rate that can be maintained. The policing mechanism allows some burstiness, but restricts it so the overall packet transmission rate is less than the rate at which tokens.
        - ReEvaluationRequestInterval (number): Represents the time period (in milliseconds) at which the path re-evaluation request is sent by the head LSR. The default value is: 180000 ms (3 mins).
        - RefreshInterval (number): The interval between summary refresh messages.
        - SeStyleDesired (bool): This indicates that the tunnel ingress node may reroute this tunnel without tearing it down. A tunnel egress node should use the SE Style when responding with an RESV message.
        - SessionName (str): If enableAutoSessionName is not set, this is the name assigned to this session.
        - SetupPriority (number): This is the session priority with respect to taking resources, such as preempting another session. The valid range is from 0 to 7. The highest priority is indicated by 0.
        - TimeoutMultiplier (number): The number of Hellos before a neighbor is declared dead.
        - TokenBucketRate (number): The rate of transfer for data in a flow. In this application, it is used with a traffic policing mechanism. The data tokens enter the bucket, filling the bucket. The data from a number of tokens is combined to form and send a packet. The goal is to determine a rate which will not overflow the specified token bucket size, and cause new data (tokens) to be rejected/discarded.
        - TokenBucketSize (number): The maximum capacity (in bytes) the token bucket can hold, and above which newly received tokens cannot be processed and are discarded.

        Returns
        -------
        - self: This instance with matching senderRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of senderRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the senderRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def DoMakeBeforeBreak(self):
        """Executes the doMakeBeforeBreak operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('doMakeBeforeBreak', payload=payload, response_object=None)

    def SendReEvaluationRequest(self):
        """Executes the sendReEvaluationRequest operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendReEvaluationRequest', payload=payload, response_object=None)
