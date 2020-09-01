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


class RsvpP2PIngressLsps(Base):
    """RSVP-TE p2p Head ( Ingress ) LSPs
    The RsvpP2PIngressLsps class encapsulates a required rsvpP2PIngressLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvpP2PIngressLsps'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AssociationId': 'associationId',
        'AutoGenerateSessionName': 'autoGenerateSessionName',
        'AutorouteTraffic': 'autorouteTraffic',
        'BackupLspEnableEro': 'backupLspEnableEro',
        'BackupLspId': 'backupLspId',
        'BackupLspMaximumPacketSize': 'backupLspMaximumPacketSize',
        'BackupLspMinimumPolicedUnit': 'backupLspMinimumPolicedUnit',
        'BackupLspNumberOfEroSubObjects': 'backupLspNumberOfEroSubObjects',
        'BackupLspPeakDataRate': 'backupLspPeakDataRate',
        'BackupLspPrefixLength': 'backupLspPrefixLength',
        'BackupLspPrependDutToEro': 'backupLspPrependDutToEro',
        'BackupLspSessionId': 'backupLspSessionId',
        'BackupLspTokenBucketRate': 'backupLspTokenBucketRate',
        'BackupLspTokenBucketSize': 'backupLspTokenBucketSize',
        'Bandwidth': 'bandwidth',
        'BandwidthProtectionDesired': 'bandwidthProtectionDesired',
        'ConfigureSyncLspObject': 'configureSyncLspObject',
        'Count': 'count',
        'DelayLspSwitchOver': 'delayLspSwitchOver',
        'DescriptiveName': 'descriptiveName',
        'DoMBBOnApplyChanges': 'doMBBOnApplyChanges',
        'EnableBfdMpls': 'enableBfdMpls',
        'EnableEro': 'enableEro',
        'EnableFastReroute': 'enableFastReroute',
        'EnableLspPing': 'enableLspPing',
        'EnableLspSelfPing': 'enableLspSelfPing',
        'EnablePathReOptimization': 'enablePathReOptimization',
        'EnablePeriodicReEvaluationRequest': 'enablePeriodicReEvaluationRequest',
        'EroSameAsPrimary': 'eroSameAsPrimary',
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
        'IncludeAssociation': 'includeAssociation',
        'InitialDelegation': 'initialDelegation',
        'InsertIPv6ExplicitNull': 'insertIPv6ExplicitNull',
        'IpDSCPofLspSelfPing': 'ipDSCPofLspSelfPing',
        'IpTTLofLspSelfPing': 'ipTTLofLspSelfPing',
        'LabelRecordingDesired': 'labelRecordingDesired',
        'LocalIp': 'localIp',
        'LocalProtectionDesired': 'localProtectionDesired',
        'LspCount': 'lspCount',
        'LspDelegationState': 'lspDelegationState',
        'LspId': 'lspId',
        'LspOperativeMode': 'lspOperativeMode',
        'LspSelfPingRetryCount': 'lspSelfPingRetryCount',
        'LspSelfPingRetryInterval': 'lspSelfPingRetryInterval',
        'LspSelfPingSessionId': 'lspSelfPingSessionId',
        'LspSelfPingStatus': 'lspSelfPingStatus',
        'LspSwitchOverDelayTime': 'lspSwitchOverDelayTime',
        'MaximumPacketSize': 'maximumPacketSize',
        'MinimumPolicedUnit': 'minimumPolicedUnit',
        'Name': 'name',
        'NodeProtectionDesired': 'nodeProtectionDesired',
        'NumberOfDetourSubObjects': 'numberOfDetourSubObjects',
        'NumberOfEroSubObjects': 'numberOfEroSubObjects',
        'NumberOfRroSubObjects': 'numberOfRroSubObjects',
        'OneToOneBackupDesired': 'oneToOneBackupDesired',
        'PccIp': 'pccIp',
        'PeakDataRate': 'peakDataRate',
        'PpagTLVType': 'ppagTLVType',
        'PrefixLength': 'prefixLength',
        'PrependDutToEro': 'prependDutToEro',
        'ProtectionLsp': 'protectionLsp',
        'ReDelegationTimerStatus': 'reDelegationTimerStatus',
        'ReEvaluationRequestInterval': 'reEvaluationRequestInterval',
        'RedelegationTimeoutInterval': 'redelegationTimeoutInterval',
        'RefreshInterval': 'refreshInterval',
        'RemoteIp': 'remoteIp',
        'ResourceAffinities': 'resourceAffinities',
        'SeStyleDesired': 'seStyleDesired',
        'SendDetour': 'sendDetour',
        'SendRro': 'sendRro',
        'SessionInformation': 'sessionInformation',
        'SessionName': 'sessionName',
        'SetupPriority': 'setupPriority',
        'SourceIp': 'sourceIp',
        'SourceIpv6': 'sourceIpv6',
        'StandbyMode': 'standbyMode',
        'State': 'state',
        'TSpecSameAsPrimary': 'tSpecSameAsPrimary',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TokenBucketRate': 'tokenBucketRate',
        'TokenBucketSize': 'tokenBucketSize',
        'TunnelId': 'tunnelId',
        'UsingHeadendIp': 'usingHeadendIp',
    }

    def __init__(self, parent):
        super(RsvpP2PIngressLsps, self).__init__(parent)

    @property
    def BackupLspEROSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.backuplsperosubobjectslist_0daa9e1df4598df831fc9c6266f38cb9.BackupLspEROSubObjectsList): An instance of the BackupLspEROSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.backuplsperosubobjectslist_0daa9e1df4598df831fc9c6266f38cb9 import BackupLspEROSubObjectsList
        return BackupLspEROSubObjectsList(self)

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
    def RsvpEROSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvperosubobjectslist_a93377fcf5a0e9cd238eac8616f8ff4c.RsvpEROSubObjectsList): An instance of the RsvpEROSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvperosubobjectslist_a93377fcf5a0e9cd238eac8616f8ff4c import RsvpEROSubObjectsList
        return RsvpEROSubObjectsList(self)

    @property
    def RsvpIngressRROSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist_cae3516af342fb3a35d3ff26ac4f830e.RsvpIngressRROSubObjectsList): An instance of the RsvpIngressRROSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist_cae3516af342fb3a35d3ff26ac4f830e import RsvpIngressRROSubObjectsList
        return RsvpIngressRROSubObjectsList(self)

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
    def AssociationId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Association ID of this LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssociationId']))

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
    def AutorouteTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Autoroute Traffic
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutorouteTraffic']))

    @property
    def BackupLspEnableEro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspEnableEro']))

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
    def BackupLspMaximumPacketSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Packet Size
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspMaximumPacketSize']))

    @property
    def BackupLspMinimumPolicedUnit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Policed Unit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspMinimumPolicedUnit']))

    @property
    def BackupLspNumberOfEroSubObjects(self):
        """
        Returns
        -------
        - number: Number Of ERO Sub-Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['BackupLspNumberOfEroSubObjects'])
    @BackupLspNumberOfEroSubObjects.setter
    def BackupLspNumberOfEroSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BackupLspNumberOfEroSubObjects'], value)

    @property
    def BackupLspPeakDataRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peak Data Rate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspPeakDataRate']))

    @property
    def BackupLspPrefixLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspPrefixLength']))

    @property
    def BackupLspPrependDutToEro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prepend DUT to ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspPrependDutToEro']))

    @property
    def BackupLspSessionId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup LSP Session Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspSessionId']))

    @property
    def BackupLspTokenBucketRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Token Bucket Rate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspTokenBucketRate']))

    @property
    def BackupLspTokenBucketSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Token Bucket Size
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspTokenBucketSize']))

    @property
    def Bandwidth(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth (bps)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bandwidth']))

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
    def ConfigureSyncLspObject(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Objects
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSyncLspObject']))

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
    def DoMBBOnApplyChanges(self):
        """
        Returns
        -------
        - bool: Do Make Before Break on Apply Changes
        """
        return self._get_attribute(self._SDM_ATT_MAP['DoMBBOnApplyChanges'])
    @DoMBBOnApplyChanges.setter
    def DoMBBOnApplyChanges(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DoMBBOnApplyChanges'], value)

    @property
    def EnableBfdMpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, BFD MPLS is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBfdMpls']))

    @property
    def EnableEro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableEro']))

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
    def EnableLspPing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LSP Ping is enabled for learned LSPs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLspPing']))

    @property
    def EnableLspSelfPing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, Ingress LSP will use LSP Self Ping procedure to verify that forwarding state has been installed on all downstream nodes.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLspSelfPing']))

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
    def EroSameAsPrimary(self):
        """
        Returns
        -------
        - bool: ERO Same As Primary
        """
        return self._get_attribute(self._SDM_ATT_MAP['EroSameAsPrimary'])
    @EroSameAsPrimary.setter
    def EroSameAsPrimary(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EroSameAsPrimary'], value)

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
    def IncludeAssociation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Association will be included in a RSVP Sync LSP. All other attributes in sub-tab-PPAG would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAssociation']))

    @property
    def InitialDelegation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initial Delegation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitialDelegation']))

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
    def IpDSCPofLspSelfPing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP DSCP of LSP Self Ping. IP DSCP classifies the way an IP packet is routed in a network.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpDSCPofLspSelfPing']))

    @property
    def IpTTLofLspSelfPing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP TTL of LSP Self Ping. IP TTL limits the lifespan or lifetime of IP Packet in a network.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpTTLofLspSelfPing']))

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
    def LspCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP#
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspCount']))

    @property
    def LspDelegationState(self):
        """
        Returns
        -------
        - list(str[delegated | delegationConfirmed | delegationRejected | delegationReturned | delegationRevoked | nonDelegated | none]): LSP Delegation State
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspDelegationState'])

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
    def LspOperativeMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mode of LSP in which it is currently behaving.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspOperativeMode']))

    @property
    def LspSelfPingRetryCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Self Ping Retry Count. Maximum number of times LSP Self Ping Message will be Transmitted.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspSelfPingRetryCount']))

    @property
    def LspSelfPingRetryInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Self Ping Retry Interval (ms).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspSelfPingRetryInterval']))

    @property
    def LspSelfPingSessionId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Self Ping Session Id.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspSelfPingSessionId']))

    @property
    def LspSelfPingStatus(self):
        """
        Returns
        -------
        - list(str[none | success | timedOut]): Logs additional information about the LSP Self Ping Status(Success/Timed Out)
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspSelfPingStatus'])

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
    def NumberOfEroSubObjects(self):
        """
        Returns
        -------
        - number: Number Of ERO Sub-Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfEroSubObjects'])
    @NumberOfEroSubObjects.setter
    def NumberOfEroSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfEroSubObjects'], value)

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
    def PccIp(self):
        """
        Returns
        -------
        - list(str): PCC IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['PccIp'])

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
    def PpagTLVType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PPAG TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PpagTLVType']))

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixLength']))

    @property
    def PrependDutToEro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prepend DUT to ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrependDutToEro']))

    @property
    def ProtectionLsp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Protection LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProtectionLsp']))

    @property
    def ReDelegationTimerStatus(self):
        """
        Returns
        -------
        - list(str[expired | none | notStarted | running | stopped]): Re-Delegation Timer Status
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReDelegationTimerStatus'])

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
    def RedelegationTimeoutInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The period of time a PCC waits for, when a PCEP session is terminated, before revoking LSP delegation to a PCE and attempting to redelegate LSPs associated with the terminated PCEP session to PCE.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedelegationTimeoutInterval']))

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
    def RemoteIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteIp']))

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
    def SessionInformation(self):
        """
        Returns
        -------
        - list(str[lastErrLSPAdmissionControlFailure | lastErrLSPBadAdSpecValue | lastErrLSPBadExplicitRoute | lastErrLSPBadFlowspecValue | lastErrLSPBadInitialSubobject | lastErrLSPBadLooseNode | lastErrLSPBadStrictNode | lastErrLSPBadTSpecValue | lastErrLSPDelayBoundNotMet | lastErrLSPMPLSAllocationFailure | lastErrLSPMTUTooBig | lastErrLSPNonRSVPRouter | lastErrLSPNoRouteAvailable | lastErrLSPPathErr | lastErrLSPPathTearSent | lastErrLSPRequestedBandwidthUnavailable | lastErrLSPReservationTearReceived | lastErrLSPReservationTearSent | lastErrLSPReservationTimeout | lastErrLSPRoutingLoops | lastErrLSPRoutingProblem | lastErrLSPRSVPSystemError | lastErrLSPServiceConflict | lastErrLSPServiceUnsupported | lastErrLSPTrafficControlError | lastErrLSPTrafficControlSystemError | lastErrLSPTrafficOrganizationError | lastErrLSPTrafficServiceError | lastErrLSPUnknownObjectClass | lastErrLSPUnknownObjectCType | lastErrLSPUnsupportedL3PID | lSPAdmissionControlFailure | lSPBadAdSpecValue | lSPBadExplicitRoute | lSPBadFlowspecValue | lSPBadInitialSubobject | lSPBadLooseNode | lSPBadStrictNode | lSPBadTSpecValue | lSPDelayBoundNotMet | lSPMPLSAllocationFailure | lSPMTUTooBig | lSPNonRSVPRouter | lSPNoRouteAvailable | lSPPathErr | lSPPathTearSent | lSPRequestedBandwidthUnavailable | lSPReservationNotReceived | lSPReservationTearReceived | lSPReservationTearSent | lSPReservationTimeout | lSPRoutingLoops | lSPRoutingProblem | lSPRSVPSystemError | lSPServiceConflict | lSPServiceUnsupported | lSPTrafficControlError | lSPTrafficControlSystemError | lSPTrafficOrganizationError | lSPTrafficServiceError | lSPUnknownObjectClass | lSPUnknownObjectCType | lSPUnsupportedL3PID | mbbCompleted | mbbTriggered | none | noPathReceived | pCRepReceived | pCReqSent]): Logs additional information about the RSVP session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInformation'])

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
    def SourceIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIp']))

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
    def StandbyMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Standby LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StandbyMode']))

    @property
    def State(self):
        """
        Returns
        -------
        - list(str[down | none | notStarted | up]): State
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def TSpecSameAsPrimary(self):
        """
        Returns
        -------
        - bool: TSpec Same As Primary
        """
        return self._get_attribute(self._SDM_ATT_MAP['TSpecSameAsPrimary'])
    @TSpecSameAsPrimary.setter
    def TSpecSameAsPrimary(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TSpecSameAsPrimary'], value)

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
    def UsingHeadendIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Using Headend IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UsingHeadendIp']))

    def update(self, BackupLspNumberOfEroSubObjects=None, DelayLspSwitchOver=None, DoMBBOnApplyChanges=None, EroSameAsPrimary=None, LspSwitchOverDelayTime=None, Name=None, NumberOfDetourSubObjects=None, NumberOfEroSubObjects=None, NumberOfRroSubObjects=None, TSpecSameAsPrimary=None):
        """Updates rsvpP2PIngressLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - BackupLspNumberOfEroSubObjects (number): Number Of ERO Sub-Objects
        - DelayLspSwitchOver (bool): Delay LSP switch over
        - DoMBBOnApplyChanges (bool): Do Make Before Break on Apply Changes
        - EroSameAsPrimary (bool): ERO Same As Primary
        - LspSwitchOverDelayTime (number): LSP Switch Over Delay timer (sec)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfDetourSubObjects (number): Number Of Detour Sub-Objects
        - NumberOfEroSubObjects (number): Number Of ERO Sub-Objects
        - NumberOfRroSubObjects (number): Number Of RRO Sub-Objects
        - TSpecSameAsPrimary (bool): TSpec Same As Primary

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AssociationId=None, AutoGenerateSessionName=None, AutorouteTraffic=None, BackupLspEnableEro=None, BackupLspId=None, BackupLspMaximumPacketSize=None, BackupLspMinimumPolicedUnit=None, BackupLspPeakDataRate=None, BackupLspPrefixLength=None, BackupLspPrependDutToEro=None, BackupLspSessionId=None, BackupLspTokenBucketRate=None, BackupLspTokenBucketSize=None, Bandwidth=None, BandwidthProtectionDesired=None, ConfigureSyncLspObject=None, EnableBfdMpls=None, EnableEro=None, EnableFastReroute=None, EnableLspPing=None, EnableLspSelfPing=None, EnablePathReOptimization=None, EnablePeriodicReEvaluationRequest=None, ExcludeAny=None, FacilityBackupDesired=None, FastRerouteBandwidth=None, FastRerouteExcludeAny=None, FastRerouteHoldingPriority=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteSetupPriority=None, HoldingPriority=None, HopLimit=None, IncludeAll=None, IncludeAny=None, IncludeAssociation=None, InitialDelegation=None, InsertIPv6ExplicitNull=None, IpDSCPofLspSelfPing=None, IpTTLofLspSelfPing=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspCount=None, LspId=None, LspOperativeMode=None, LspSelfPingRetryCount=None, LspSelfPingRetryInterval=None, LspSelfPingSessionId=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, OneToOneBackupDesired=None, PeakDataRate=None, PpagTLVType=None, PrefixLength=None, PrependDutToEro=None, ProtectionLsp=None, ReEvaluationRequestInterval=None, RedelegationTimeoutInterval=None, RefreshInterval=None, RemoteIp=None, ResourceAffinities=None, SeStyleDesired=None, SendDetour=None, SendRro=None, SessionName=None, SetupPriority=None, SourceIp=None, SourceIpv6=None, StandbyMode=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None, TunnelId=None, UsingHeadendIp=None):
        """Base class infrastructure that gets a list of rsvpP2PIngressLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AssociationId (str): optional regex of associationId
        - AutoGenerateSessionName (str): optional regex of autoGenerateSessionName
        - AutorouteTraffic (str): optional regex of autorouteTraffic
        - BackupLspEnableEro (str): optional regex of backupLspEnableEro
        - BackupLspId (str): optional regex of backupLspId
        - BackupLspMaximumPacketSize (str): optional regex of backupLspMaximumPacketSize
        - BackupLspMinimumPolicedUnit (str): optional regex of backupLspMinimumPolicedUnit
        - BackupLspPeakDataRate (str): optional regex of backupLspPeakDataRate
        - BackupLspPrefixLength (str): optional regex of backupLspPrefixLength
        - BackupLspPrependDutToEro (str): optional regex of backupLspPrependDutToEro
        - BackupLspSessionId (str): optional regex of backupLspSessionId
        - BackupLspTokenBucketRate (str): optional regex of backupLspTokenBucketRate
        - BackupLspTokenBucketSize (str): optional regex of backupLspTokenBucketSize
        - Bandwidth (str): optional regex of bandwidth
        - BandwidthProtectionDesired (str): optional regex of bandwidthProtectionDesired
        - ConfigureSyncLspObject (str): optional regex of configureSyncLspObject
        - EnableBfdMpls (str): optional regex of enableBfdMpls
        - EnableEro (str): optional regex of enableEro
        - EnableFastReroute (str): optional regex of enableFastReroute
        - EnableLspPing (str): optional regex of enableLspPing
        - EnableLspSelfPing (str): optional regex of enableLspSelfPing
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
        - IncludeAssociation (str): optional regex of includeAssociation
        - InitialDelegation (str): optional regex of initialDelegation
        - InsertIPv6ExplicitNull (str): optional regex of insertIPv6ExplicitNull
        - IpDSCPofLspSelfPing (str): optional regex of ipDSCPofLspSelfPing
        - IpTTLofLspSelfPing (str): optional regex of ipTTLofLspSelfPing
        - LabelRecordingDesired (str): optional regex of labelRecordingDesired
        - LocalProtectionDesired (str): optional regex of localProtectionDesired
        - LspCount (str): optional regex of lspCount
        - LspId (str): optional regex of lspId
        - LspOperativeMode (str): optional regex of lspOperativeMode
        - LspSelfPingRetryCount (str): optional regex of lspSelfPingRetryCount
        - LspSelfPingRetryInterval (str): optional regex of lspSelfPingRetryInterval
        - LspSelfPingSessionId (str): optional regex of lspSelfPingSessionId
        - MaximumPacketSize (str): optional regex of maximumPacketSize
        - MinimumPolicedUnit (str): optional regex of minimumPolicedUnit
        - NodeProtectionDesired (str): optional regex of nodeProtectionDesired
        - OneToOneBackupDesired (str): optional regex of oneToOneBackupDesired
        - PeakDataRate (str): optional regex of peakDataRate
        - PpagTLVType (str): optional regex of ppagTLVType
        - PrefixLength (str): optional regex of prefixLength
        - PrependDutToEro (str): optional regex of prependDutToEro
        - ProtectionLsp (str): optional regex of protectionLsp
        - ReEvaluationRequestInterval (str): optional regex of reEvaluationRequestInterval
        - RedelegationTimeoutInterval (str): optional regex of redelegationTimeoutInterval
        - RefreshInterval (str): optional regex of refreshInterval
        - RemoteIp (str): optional regex of remoteIp
        - ResourceAffinities (str): optional regex of resourceAffinities
        - SeStyleDesired (str): optional regex of seStyleDesired
        - SendDetour (str): optional regex of sendDetour
        - SendRro (str): optional regex of sendRro
        - SessionName (str): optional regex of sessionName
        - SetupPriority (str): optional regex of setupPriority
        - SourceIp (str): optional regex of sourceIp
        - SourceIpv6 (str): optional regex of sourceIpv6
        - StandbyMode (str): optional regex of standbyMode
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

    def InitiatePathReoptimization(self, *args, **kwargs):
        """Executes the initiatePathReoptimization operation on the server.

        Send Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        initiatePathReoptimization(SessionIndices=list)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        initiatePathReoptimization(SessionIndices=string)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        initiatePathReoptimization(Arg2=list)list
        -----------------------------------------
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
        return self._execute('initiatePathReoptimization', payload=payload, response_object=None)

    def MakeBeforeBreak(self, *args, **kwargs):
        """Executes the makeBeforeBreak operation on the server.

        Initiate Make Before Break for selected Head Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        makeBeforeBreak(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        makeBeforeBreak(SessionIndices=string)
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        makeBeforeBreak(Arg2=list)list
        ------------------------------
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
        return self._execute('makeBeforeBreak', payload=payload, response_object=None)

    def PcepDelegate(self, *args, **kwargs):
        """Executes the pcepDelegate operation on the server.

        Delegate the non-delegated LSPs among the selected RSVP-TE LSPs to PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pcepDelegate(SessionIndices=list)
        ---------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        pcepDelegate(SessionIndices=string)
        -----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        pcepDelegate(Arg2=list)list
        ---------------------------
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
        return self._execute('pcepDelegate', payload=payload, response_object=None)

    def PcepRevokeDelegation(self, *args, **kwargs):
        """Executes the pcepRevokeDelegation operation on the server.

        Revoke Delegation from PCE for delegated LSPs among the selected LSPs.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pcepRevokeDelegation(SessionIndices=list)
        -----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        pcepRevokeDelegation(SessionIndices=string)
        -------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        pcepRevokeDelegation(Arg2=list)list
        -----------------------------------
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
        return self._execute('pcepRevokeDelegation', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Activate/Enable Tunnel selected Head Ranges

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

        Deactivate/Disable selected Tunnel Head Ranges

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
