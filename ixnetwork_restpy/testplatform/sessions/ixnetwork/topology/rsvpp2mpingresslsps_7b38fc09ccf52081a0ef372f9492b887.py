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


class RsvpP2mpIngressLsps(Base):
    """RSVP-TE P2MP Head (Ingress) LSPs
    The RsvpP2mpIngressLsps class encapsulates a required rsvpP2mpIngressLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvpP2mpIngressLsps'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AutoGenerateSessionName': 'autoGenerateSessionName',
        'BackupLspId': 'backupLspId',
        'BandwidthProtectionDesired': 'bandwidthProtectionDesired',
        'Count': 'count',
        'DelayLspSwitchOver': 'delayLspSwitchOver',
        'DescriptiveName': 'descriptiveName',
        'EnableFastReroute': 'enableFastReroute',
        'EnablePathReOptimization': 'enablePathReOptimization',
        'EnablePeriodicReEvaluationRequest': 'enablePeriodicReEvaluationRequest',
        'ExcludeAny': 'excludeAny',
        'FacilityBackupDesired': 'facilityBackupDesired',
        'FastRerouteBandwidth': 'fastRerouteBandwidth',
        'FastRerouteExcludeAny': 'fastRerouteExcludeAny',
        'FastRerouteHoldingPriority': 'fastRerouteHoldingPriority',
        'FastRerouteIncludeAll': 'fastRerouteIncludeAll',
        'FastRerouteIncludeAny': 'fastRerouteIncludeAny',
        'FastRerouteSetupPriority': 'fastRerouteSetupPriority',
        'HoldingPriority': 'holdingPriority',
        'HopLimit': 'hopLimit',
        'IncludeAll': 'includeAll',
        'IncludeAny': 'includeAny',
        'IncludeConnectedIpOnTop': 'includeConnectedIpOnTop',
        'IncludeHeadIpAtBottom': 'includeHeadIpAtBottom',
        'IngressP2mpSubLspRanges': 'ingressP2mpSubLspRanges',
        'InsertIPv6ExplicitNull': 'insertIPv6ExplicitNull',
        'LabelRecordingDesired': 'labelRecordingDesired',
        'LocalIp': 'localIp',
        'LocalProtectionDesired': 'localProtectionDesired',
        'LspId': 'lspId',
        'LspSwitchOverDelayTime': 'lspSwitchOverDelayTime',
        'MaximumPacketSize': 'maximumPacketSize',
        'MinimumPolicedUnit': 'minimumPolicedUnit',
        'Name': 'name',
        'NodeProtectionDesired': 'nodeProtectionDesired',
        'NumberOfDetourSubObjects': 'numberOfDetourSubObjects',
        'NumberOfRroSubObjects': 'numberOfRroSubObjects',
        'OneToOneBackupDesired': 'oneToOneBackupDesired',
        'P2mpIdAsNumber': 'p2mpIdAsNumber',
        'P2mpIdIp': 'p2mpIdIp',
        'PeakDataRate': 'peakDataRate',
        'ReEvaluationRequestInterval': 'reEvaluationRequestInterval',
        'RefreshInterval': 'refreshInterval',
        'ResourceAffinities': 'resourceAffinities',
        'SeStyleDesired': 'seStyleDesired',
        'SendDetour': 'sendDetour',
        'SendRro': 'sendRro',
        'SessionName': 'sessionName',
        'SetupPriority': 'setupPriority',
        'SourceIpv4': 'sourceIpv4',
        'SourceIpv6': 'sourceIpv6',
        'State': 'state',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TokenBucketRate': 'tokenBucketRate',
        'TokenBucketSize': 'tokenBucketSize',
        'TunnelId': 'tunnelId',
        'TypeP2mpId': 'typeP2mpId',
        'UsingHeadendIp': 'usingHeadendIp',
    }

    def __init__(self, parent):
        super(RsvpP2mpIngressLsps, self).__init__(parent)

    @property
    def RsvpDetourSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist_9740d38add800b02d578822ebd9149be.RsvpDetourSubObjectsList): An instance of the RsvpDetourSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist_9740d38add800b02d578822ebd9149be import RsvpDetourSubObjectsList
        return RsvpDetourSubObjectsList(self)

    @property
    def RsvpIngressRroSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist_a21ca5185e1490831d56bb810b32d086.RsvpIngressRroSubObjectsList): An instance of the RsvpIngressRroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist_a21ca5185e1490831d56bb810b32d086 import RsvpIngressRroSubObjectsList
        return RsvpIngressRroSubObjectsList(self)

    @property
    def RsvpP2mpIngressSubLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresssublsps_c610bddfdb08c054e463708b863af4f0.RsvpP2mpIngressSubLsps): An instance of the RsvpP2mpIngressSubLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresssublsps_c610bddfdb08c054e463708b863af4f0 import RsvpP2mpIngressSubLsps
        return RsvpP2mpIngressSubLsps(self)._select()

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AutoGenerateSessionName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Generate Session Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoGenerateSessionName']))

    @property
    def BackupLspId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup LSP Id Pool Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspId']))

    @property
    def BandwidthProtectionDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth Protection Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthProtectionDesired']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DelayLspSwitchOver(self):
        """
        Returns
        -------
        - bool: Delay LSP switch over
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayLspSwitchOver'])
    @DelayLspSwitchOver.setter
    def DelayLspSwitchOver(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayLspSwitchOver'], value)

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableFastReroute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Fast Reroute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFastReroute']))

    @property
    def EnablePathReOptimization(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Path Re-Optimization
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePathReOptimization']))

    @property
    def EnablePeriodicReEvaluationRequest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Periodic Re-Evaluation Request
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicReEvaluationRequest']))

    @property
    def ExcludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Exclude Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAny']))

    @property
    def FacilityBackupDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Facility Backup Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FacilityBackupDesired']))

    @property
    def FastRerouteBandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth (bps)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FastRerouteBandwidth']))

    @property
    def FastRerouteExcludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Exclude Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FastRerouteExcludeAny']))

    @property
    def FastRerouteHoldingPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Holding Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FastRerouteHoldingPriority']))

    @property
    def FastRerouteIncludeAll(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAll']))

    @property
    def FastRerouteIncludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAny']))

    @property
    def FastRerouteSetupPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Setup Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FastRerouteSetupPriority']))

    @property
    def HoldingPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Holding Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HoldingPriority']))

    @property
    def HopLimit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hop Limit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HopLimit']))

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAll']))

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAny']))

    @property
    def IncludeConnectedIpOnTop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include connected IP on top
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeConnectedIpOnTop']))

    @property
    def IncludeHeadIpAtBottom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Head IP at bottom
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeHeadIpAtBottom']))

    @property
    def IngressP2mpSubLspRanges(self):
        """
        Returns
        -------
        - number: Number of P2MP Ingress Sub LSPs configured per RSVP-TE P2MP Ingress LSP
        """
        return self._get_attribute(self._SDM_ATT_MAP['IngressP2mpSubLspRanges'])
    @IngressP2mpSubLspRanges.setter
    def IngressP2mpSubLspRanges(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IngressP2mpSubLspRanges'], value)

    @property
    def InsertIPv6ExplicitNull(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Insert IPv6 explicit NULL
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InsertIPv6ExplicitNull']))

    @property
    def LabelRecordingDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Recording Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelRecordingDesired']))

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def LocalProtectionDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Protection Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalProtectionDesired']))

    @property
    def LspId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspId']))

    @property
    def LspSwitchOverDelayTime(self):
        """
        Returns
        -------
        - number: LSP Switch Over Delay timer (sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspSwitchOverDelayTime'])
    @LspSwitchOverDelayTime.setter
    def LspSwitchOverDelayTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspSwitchOverDelayTime'], value)

    @property
    def MaximumPacketSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Packet Size (in Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaximumPacketSize']))

    @property
    def MinimumPolicedUnit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Policed Unit (in Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinimumPolicedUnit']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NodeProtectionDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node Protection Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NodeProtectionDesired']))

    @property
    def NumberOfDetourSubObjects(self):
        """
        Returns
        -------
        - number: Number Of Detour Sub-Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfDetourSubObjects'])
    @NumberOfDetourSubObjects.setter
    def NumberOfDetourSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfDetourSubObjects'], value)

    @property
    def NumberOfRroSubObjects(self):
        """
        Returns
        -------
        - number: Number Of RRO Sub-Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRroSubObjects'])
    @NumberOfRroSubObjects.setter
    def NumberOfRroSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRroSubObjects'], value)

    @property
    def OneToOneBackupDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): One To One Backup Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OneToOneBackupDesired']))

    @property
    def P2mpIdAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P2MP ID displayed in Integer format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['P2mpIdAsNumber']))

    @property
    def P2mpIdIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P2MP ID displayed in IP Address format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['P2mpIdIp']))

    @property
    def PeakDataRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peak Data Rate (in Bytes per seconds)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeakDataRate']))

    @property
    def ReEvaluationRequestInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Re-Evaluation Request Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReEvaluationRequestInterval']))

    @property
    def RefreshInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Refresh Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RefreshInterval']))

    @property
    def ResourceAffinities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Resource Affinities
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResourceAffinities']))

    @property
    def SeStyleDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SE Style Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SeStyleDesired']))

    @property
    def SendDetour(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send Detour
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendDetour']))

    @property
    def SendRro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send RRO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendRro']))

    @property
    def SessionName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Session Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SessionName']))

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Setup Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetupPriority']))

    @property
    def SourceIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIpv4']))

    @property
    def SourceIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIpv6']))

    @property
    def State(self):
        """
        Returns
        -------
        - list(str[down | none | notStarted | up]): State
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout Multiplier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier']))

    @property
    def TokenBucketRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Token Bucket Rate (in Bytes per seconds)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TokenBucketRate']))

    @property
    def TokenBucketSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Token Bucket Size (in Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TokenBucketSize']))

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TunnelId']))

    @property
    def TypeP2mpId(self):
        """
        Returns
        -------
        - str(p2MPId | iP): P2MP ID Type
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeP2mpId'])
    @TypeP2mpId.setter
    def TypeP2mpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeP2mpId'], value)

    @property
    def UsingHeadendIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Using Headend IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UsingHeadendIp']))

    def update(self, DelayLspSwitchOver=None, IngressP2mpSubLspRanges=None, LspSwitchOverDelayTime=None, Name=None, NumberOfDetourSubObjects=None, NumberOfRroSubObjects=None, TypeP2mpId=None):
        """Updates rsvpP2mpIngressLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - DelayLspSwitchOver (bool): Delay LSP switch over
        - IngressP2mpSubLspRanges (number): Number of P2MP Ingress Sub LSPs configured per RSVP-TE P2MP Ingress LSP
        - LspSwitchOverDelayTime (number): LSP Switch Over Delay timer (sec)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfDetourSubObjects (number): Number Of Detour Sub-Objects
        - NumberOfRroSubObjects (number): Number Of RRO Sub-Objects
        - TypeP2mpId (str(p2MPId | iP)): P2MP ID Type

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AutoGenerateSessionName=None, BackupLspId=None, BandwidthProtectionDesired=None, EnableFastReroute=None, EnablePathReOptimization=None, EnablePeriodicReEvaluationRequest=None, ExcludeAny=None, FacilityBackupDesired=None, FastRerouteBandwidth=None, FastRerouteExcludeAny=None, FastRerouteHoldingPriority=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteSetupPriority=None, HoldingPriority=None, HopLimit=None, IncludeAll=None, IncludeAny=None, IncludeConnectedIpOnTop=None, IncludeHeadIpAtBottom=None, InsertIPv6ExplicitNull=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspId=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, OneToOneBackupDesired=None, P2mpIdAsNumber=None, P2mpIdIp=None, PeakDataRate=None, ReEvaluationRequestInterval=None, RefreshInterval=None, ResourceAffinities=None, SeStyleDesired=None, SendDetour=None, SendRro=None, SessionName=None, SetupPriority=None, SourceIpv4=None, SourceIpv6=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None, TunnelId=None, UsingHeadendIp=None):
        """Base class infrastructure that gets a list of rsvpP2mpIngressLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AutoGenerateSessionName (str): optional regex of autoGenerateSessionName
        - BackupLspId (str): optional regex of backupLspId
        - BandwidthProtectionDesired (str): optional regex of bandwidthProtectionDesired
        - EnableFastReroute (str): optional regex of enableFastReroute
        - EnablePathReOptimization (str): optional regex of enablePathReOptimization
        - EnablePeriodicReEvaluationRequest (str): optional regex of enablePeriodicReEvaluationRequest
        - ExcludeAny (str): optional regex of excludeAny
        - FacilityBackupDesired (str): optional regex of facilityBackupDesired
        - FastRerouteBandwidth (str): optional regex of fastRerouteBandwidth
        - FastRerouteExcludeAny (str): optional regex of fastRerouteExcludeAny
        - FastRerouteHoldingPriority (str): optional regex of fastRerouteHoldingPriority
        - FastRerouteIncludeAll (str): optional regex of fastRerouteIncludeAll
        - FastRerouteIncludeAny (str): optional regex of fastRerouteIncludeAny
        - FastRerouteSetupPriority (str): optional regex of fastRerouteSetupPriority
        - HoldingPriority (str): optional regex of holdingPriority
        - HopLimit (str): optional regex of hopLimit
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeConnectedIpOnTop (str): optional regex of includeConnectedIpOnTop
        - IncludeHeadIpAtBottom (str): optional regex of includeHeadIpAtBottom
        - InsertIPv6ExplicitNull (str): optional regex of insertIPv6ExplicitNull
        - LabelRecordingDesired (str): optional regex of labelRecordingDesired
        - LocalProtectionDesired (str): optional regex of localProtectionDesired
        - LspId (str): optional regex of lspId
        - MaximumPacketSize (str): optional regex of maximumPacketSize
        - MinimumPolicedUnit (str): optional regex of minimumPolicedUnit
        - NodeProtectionDesired (str): optional regex of nodeProtectionDesired
        - OneToOneBackupDesired (str): optional regex of oneToOneBackupDesired
        - P2mpIdAsNumber (str): optional regex of p2mpIdAsNumber
        - P2mpIdIp (str): optional regex of p2mpIdIp
        - PeakDataRate (str): optional regex of peakDataRate
        - ReEvaluationRequestInterval (str): optional regex of reEvaluationRequestInterval
        - RefreshInterval (str): optional regex of refreshInterval
        - ResourceAffinities (str): optional regex of resourceAffinities
        - SeStyleDesired (str): optional regex of seStyleDesired
        - SendDetour (str): optional regex of sendDetour
        - SendRro (str): optional regex of sendRro
        - SessionName (str): optional regex of sessionName
        - SetupPriority (str): optional regex of setupPriority
        - SourceIpv4 (str): optional regex of sourceIpv4
        - SourceIpv6 (str): optional regex of sourceIpv6
        - TimeoutMultiplier (str): optional regex of timeoutMultiplier
        - TokenBucketRate (str): optional regex of tokenBucketRate
        - TokenBucketSize (str): optional regex of tokenBucketSize
        - TunnelId (str): optional regex of tunnelId
        - UsingHeadendIp (str): optional regex of usingHeadendIp

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def InitiateP2mpPathReoptimization(self, *args, **kwargs):
        """Executes the initiateP2mpPathReoptimization operation on the server.

        Send P2MP Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        initiateP2mpPathReoptimization(SessionIndices=list)
        ---------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        initiateP2mpPathReoptimization(SessionIndices=string)
        -----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('initiateP2mpPathReoptimization', payload=payload, response_object=None)

    def InitiatePathReoptimization(self, *args, **kwargs):
        """Executes the initiatePathReoptimization operation on the server.

        Initiate Path Reoptimization

        initiatePathReoptimization(Arg2=list)list
        -----------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('initiatePathReoptimization', payload=payload, response_object=None)

    def MakeBeforeBreak(self, *args, **kwargs):
        """Executes the makeBeforeBreak operation on the server.

        Make Before Break

        makeBeforeBreak(Arg2=list)list
        ------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('makeBeforeBreak', payload=payload, response_object=None)

    def P2mpMakeBeforeBreak(self, *args, **kwargs):
        """Executes the p2mpMakeBeforeBreak operation on the server.

        Initiate P2MP Make Before Break for selected Head Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        p2mpMakeBeforeBreak(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        p2mpMakeBeforeBreak(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('p2mpMakeBeforeBreak', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Activate/Enable P2MP Tunnel selected Head Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        start(Arg2=list)list
        --------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Deactivate/Disable P2MP selected Tunnel Head Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stop(Arg2=list)list
        -------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
