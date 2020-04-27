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


class RsvpP2mpIngressLsps(Base):
    """RSVP-TE P2MP Head (Ingress) LSPs
    The RsvpP2mpIngressLsps class encapsulates a required rsvpP2mpIngressLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvpP2mpIngressLsps'

    def __init__(self, parent):
        super(RsvpP2mpIngressLsps, self).__init__(parent)

    @property
    def RsvpDetourSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist.RsvpDetourSubObjectsList): An instance of the RsvpDetourSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist import RsvpDetourSubObjectsList
        return RsvpDetourSubObjectsList(self)

    @property
    def RsvpIngressRROSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist.RsvpIngressRROSubObjectsList): An instance of the RsvpIngressRROSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist import RsvpIngressRROSubObjectsList
        return RsvpIngressRROSubObjectsList(self)

    @property
    def RsvpP2mpIngressSubLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresssublsps.RsvpP2mpIngressSubLsps): An instance of the RsvpP2mpIngressSubLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresssublsps import RsvpP2mpIngressSubLsps
        return RsvpP2mpIngressSubLsps(self)._select()

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
        return Tag(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def AutoGenerateSessionName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Generate Session Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('autoGenerateSessionName'))

    @property
    def BackupLspId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup LSP Id Pool Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('backupLspId'))

    @property
    def BandwidthProtectionDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth Protection Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthProtectionDesired'))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DelayLspSwitchOver(self):
        """
        Returns
        -------
        - bool: Delay LSP switch over
        """
        return self._get_attribute('delayLspSwitchOver')
    @DelayLspSwitchOver.setter
    def DelayLspSwitchOver(self, value):
        self._set_attribute('delayLspSwitchOver', value)

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def EnableFastReroute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Fast Reroute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableFastReroute'))

    @property
    def EnablePathReOptimization(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Path Re-Optimization
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enablePathReOptimization'))

    @property
    def EnablePeriodicReEvaluationRequest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Periodic Re-Evaluation Request
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enablePeriodicReEvaluationRequest'))

    @property
    def ExcludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Exclude Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('excludeAny'))

    @property
    def FacilityBackupDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Facility Backup Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('facilityBackupDesired'))

    @property
    def FastRerouteBandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth (bps)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fastRerouteBandwidth'))

    @property
    def FastRerouteExcludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Exclude Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fastRerouteExcludeAny'))

    @property
    def FastRerouteHoldingPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Holding Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fastRerouteHoldingPriority'))

    @property
    def FastRerouteIncludeAll(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fastRerouteIncludeAll'))

    @property
    def FastRerouteIncludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fastRerouteIncludeAny'))

    @property
    def FastRerouteSetupPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Setup Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fastRerouteSetupPriority'))

    @property
    def HoldingPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Holding Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('holdingPriority'))

    @property
    def HopLimit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hop Limit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('hopLimit'))

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAll'))

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAny'))

    @property
    def IncludeConnectedIpOnTop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include connected IP on top
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeConnectedIpOnTop'))

    @property
    def IncludeHeadIpAtBottom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Head IP at bottom
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeHeadIpAtBottom'))

    @property
    def IngressP2mpSubLspRanges(self):
        """
        Returns
        -------
        - number: Number of P2MP Ingress Sub LSPs configured per RSVP-TE P2MP Ingress LSP
        """
        return self._get_attribute('ingressP2mpSubLspRanges')
    @IngressP2mpSubLspRanges.setter
    def IngressP2mpSubLspRanges(self, value):
        self._set_attribute('ingressP2mpSubLspRanges', value)

    @property
    def InsertIPv6ExplicitNull(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Insert IPv6 explicit NULL
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('insertIPv6ExplicitNull'))

    @property
    def LabelRecordingDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Recording Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('labelRecordingDesired'))

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute('localIp')

    @property
    def LocalProtectionDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Protection Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('localProtectionDesired'))

    @property
    def LspId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lspId'))

    @property
    def LspSwitchOverDelayTime(self):
        """
        Returns
        -------
        - number: LSP Switch Over Delay timer (sec)
        """
        return self._get_attribute('lspSwitchOverDelayTime')
    @LspSwitchOverDelayTime.setter
    def LspSwitchOverDelayTime(self, value):
        self._set_attribute('lspSwitchOverDelayTime', value)

    @property
    def MaximumPacketSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Packet Size (in Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maximumPacketSize'))

    @property
    def MinimumPolicedUnit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Policed Unit (in Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('minimumPolicedUnit'))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NodeProtectionDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node Protection Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('nodeProtectionDesired'))

    @property
    def NumberOfDetourSubObjects(self):
        """
        Returns
        -------
        - number: Number Of Detour Sub-Objects
        """
        return self._get_attribute('numberOfDetourSubObjects')
    @NumberOfDetourSubObjects.setter
    def NumberOfDetourSubObjects(self, value):
        self._set_attribute('numberOfDetourSubObjects', value)

    @property
    def NumberOfRroSubObjects(self):
        """
        Returns
        -------
        - number: Number Of RRO Sub-Objects
        """
        return self._get_attribute('numberOfRroSubObjects')
    @NumberOfRroSubObjects.setter
    def NumberOfRroSubObjects(self, value):
        self._set_attribute('numberOfRroSubObjects', value)

    @property
    def OneToOneBackupDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): One To One Backup Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('oneToOneBackupDesired'))

    @property
    def P2mpIdAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P2MP ID displayed in Integer format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('p2mpIdAsNumber'))

    @property
    def P2mpIdIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P2MP ID displayed in IP Address format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('p2mpIdIp'))

    @property
    def PeakDataRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peak Data Rate (in Bytes per seconds)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('peakDataRate'))

    @property
    def ReEvaluationRequestInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Re-Evaluation Request Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('reEvaluationRequestInterval'))

    @property
    def RefreshInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Refresh Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('refreshInterval'))

    @property
    def ResourceAffinities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Resource Affinities
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('resourceAffinities'))

    @property
    def SeStyleDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SE Style Desired
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('seStyleDesired'))

    @property
    def SendDetour(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send Detour
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sendDetour'))

    @property
    def SendRro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send RRO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sendRro'))

    @property
    def SessionName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Session Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sessionName'))

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Setup Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('setupPriority'))

    @property
    def SourceIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sourceIpv4'))

    @property
    def SourceIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sourceIpv6'))

    @property
    def State(self):
        """
        Returns
        -------
        - list(str[down | none | notStarted | up]): State
        """
        return self._get_attribute('state')

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout Multiplier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('timeoutMultiplier'))

    @property
    def TokenBucketRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Token Bucket Rate (in Bytes per seconds)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tokenBucketRate'))

    @property
    def TokenBucketSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Token Bucket Size (in Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tokenBucketSize'))

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tunnelId'))

    @property
    def TypeP2mpId(self):
        """
        Returns
        -------
        - str(p2MPId | iP): P2MP ID Type
        """
        return self._get_attribute('typeP2mpId')
    @TypeP2mpId.setter
    def TypeP2mpId(self, value):
        self._set_attribute('typeP2mpId', value)

    @property
    def UsingHeadendIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Using Headend IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('usingHeadendIp'))

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
        return self._update(locals())

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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

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
