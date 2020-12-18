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


class TrafficItem(Base):
    """This object specifies the particular traffic item related properties.
    The TrafficItem class encapsulates a list of trafficItem resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficItem.find() method.
    The list can be managed by using the TrafficItem.add() and TrafficItem.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trafficItem'
    _SDM_ATT_MAP = {
        'AllowSelfDestined': 'allowSelfDestined',
        'BgpEpeOrdinalValue': 'bgpEpeOrdinalValue',
        'BgpEpeSidType': 'bgpEpeSidType',
        'BiDirectional': 'biDirectional',
        'EgressEnabled': 'egressEnabled',
        'EnableDynamicMplsLabelValues': 'enableDynamicMplsLabelValues',
        'EnableMacsecEgressOnlyAutoConfig': 'enableMacsecEgressOnlyAutoConfig',
        'Enabled': 'enabled',
        'Errors': 'errors',
        'EvpnNextHopOrdinalValue': 'evpnNextHopOrdinalValue',
        'FlowGroupCount': 'flowGroupCount',
        'FrerDuplicateElimination': 'frerDuplicateElimination',
        'HasOpenFlow': 'hasOpenFlow',
        'HostsPerNetwork': 'hostsPerNetwork',
        'InterAsBgpPreference': 'interAsBgpPreference',
        'InterAsLdpPreference': 'interAsLdpPreference',
        'LabelPreferences': 'labelPreferences',
        'MaxNumberOfVpnLabelStack': 'maxNumberOfVpnLabelStack',
        'MergeDestinations': 'mergeDestinations',
        'MulticastForwardingMode': 'multicastForwardingMode',
        'Name': 'name',
        'NumVlansForMulticastReplication': 'numVlansForMulticastReplication',
        'OrdinalNo': 'ordinalNo',
        'OriginatorType': 'originatorType',
        'RawTrafficRxPortsBehavior': 'rawTrafficRxPortsBehavior',
        'RegenerateCount': 'regenerateCount',
        'RoundRobinPacketOrdering': 'roundRobinPacketOrdering',
        'RouteMesh': 'routeMesh',
        'SrcDestMesh': 'srcDestMesh',
        'State': 'state',
        'Suspend': 'suspend',
        'TrafficItemType': 'trafficItemType',
        'TrafficType': 'trafficType',
        'TransmitMode': 'transmitMode',
        'TransportLdpPreference': 'transportLdpPreference',
        'TransportRsvpTePreference': 'transportRsvpTePreference',
        'UseControlPlaneFrameSize': 'useControlPlaneFrameSize',
        'UseControlPlaneRate': 'useControlPlaneRate',
        'Warnings': 'warnings',
    }

    def __init__(self, parent):
        super(TrafficItem, self).__init__(parent)

    @property
    def AppLibProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibprofile.AppLibProfile): An instance of the AppLibProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibprofile import AppLibProfile
        return AppLibProfile(self)

    @property
    def ConfigElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.configelement.ConfigElement): An instance of the ConfigElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.configelement import ConfigElement
        return ConfigElement(self)

    @property
    def DynamicUpdate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.dynamicupdate.dynamicupdate.DynamicUpdate): An instance of the DynamicUpdate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.dynamicupdate.dynamicupdate import DynamicUpdate
        return DynamicUpdate(self)

    @property
    def EgressTracking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.egresstracking.EgressTracking): An instance of the EgressTracking class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.egresstracking import EgressTracking
        return EgressTracking(self)

    @property
    def EndpointSet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.endpointset.endpointset.EndpointSet): An instance of the EndpointSet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.endpointset.endpointset import EndpointSet
        return EndpointSet(self)

    @property
    def HighLevelStream(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.highlevelstream.HighLevelStream): An instance of the HighLevelStream class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.highlevelstream import HighLevelStream
        return HighLevelStream(self)

    @property
    def Tracking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.tracking.Tracking): An instance of the Tracking class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.tracking import Tracking
        return Tracking(self)

    @property
    def TransmissionDistribution(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.transmissiondistribution.transmissiondistribution.TransmissionDistribution): An instance of the TransmissionDistribution class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.transmissiondistribution.transmissiondistribution import TransmissionDistribution
        return TransmissionDistribution(self)

    @property
    def AllowSelfDestined(self):
        """
        Returns
        -------
        - bool: If true, this helps to send traffic from routes on an Ixia port to other routes on the same Ixia port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowSelfDestined'])
    @AllowSelfDestined.setter
    def AllowSelfDestined(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllowSelfDestined'], value)

    @property
    def BgpEpeOrdinalValue(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BgpEpeOrdinalValue'])
    @BgpEpeOrdinalValue.setter
    def BgpEpeOrdinalValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BgpEpeOrdinalValue'], value)

    @property
    def BgpEpeSidType(self):
        """
        Returns
        -------
        - str(adjSID | nodeSID | setSID): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BgpEpeSidType'])
    @BgpEpeSidType.setter
    def BgpEpeSidType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BgpEpeSidType'], value)

    @property
    def BiDirectional(self):
        """
        Returns
        -------
        - bool: If true, this enables traffic to be sent in forward and reverse destination.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BiDirectional'])
    @BiDirectional.setter
    def BiDirectional(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BiDirectional'], value)

    @property
    def EgressEnabled(self):
        """
        Returns
        -------
        - bool: Enables the egress.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressEnabled'])
    @EgressEnabled.setter
    def EgressEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EgressEnabled'], value)

    @property
    def EnableDynamicMplsLabelValues(self):
        """
        Returns
        -------
        - bool: Enables the dynamic MPLS label values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDynamicMplsLabelValues'])
    @EnableDynamicMplsLabelValues.setter
    def EnableDynamicMplsLabelValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDynamicMplsLabelValues'], value)

    @property
    def EnableMacsecEgressOnlyAutoConfig(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMacsecEgressOnlyAutoConfig'])
    @EnableMacsecEgressOnlyAutoConfig.setter
    def EnableMacsecEgressOnlyAutoConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMacsecEgressOnlyAutoConfig'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, this enables the selected traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(str): Displays the errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def EvpnNextHopOrdinalValue(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvpnNextHopOrdinalValue'])
    @EvpnNextHopOrdinalValue.setter
    def EvpnNextHopOrdinalValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvpnNextHopOrdinalValue'], value)

    @property
    def FlowGroupCount(self):
        """
        Returns
        -------
        - number: Indicates the number of flow groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowGroupCount'])

    @property
    def FrerDuplicateElimination(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrerDuplicateElimination'])
    @FrerDuplicateElimination.setter
    def FrerDuplicateElimination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrerDuplicateElimination'], value)

    @property
    def HasOpenFlow(self):
        """
        Returns
        -------
        - bool: Indicates whether or not this trafficItem has openflow.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HasOpenFlow'])
    @HasOpenFlow.setter
    def HasOpenFlow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HasOpenFlow'], value)

    @property
    def HostsPerNetwork(self):
        """
        Returns
        -------
        - number: The number of emulated hosts for the traffic stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostsPerNetwork'])
    @HostsPerNetwork.setter
    def HostsPerNetwork(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostsPerNetwork'], value)

    @property
    def InterAsBgpPreference(self):
        """DEPRECATED 
        Returns
        -------
        - str(one | two): This attribute is deprecated. Use labelPreferences attribute instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterAsBgpPreference'])
    @InterAsBgpPreference.setter
    def InterAsBgpPreference(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterAsBgpPreference'], value)

    @property
    def InterAsLdpPreference(self):
        """DEPRECATED 
        Returns
        -------
        - str(one | two): This attribute is deprecated. Use labelPreferences attribute instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterAsLdpPreference'])
    @InterAsLdpPreference.setter
    def InterAsLdpPreference(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterAsLdpPreference'], value)

    @property
    def LabelPreferences(self):
        """
        Returns
        -------
        - list(dict(labelCategory:str[interAsRegionLsp | interAsRegionLspClassic | ipTransportLsp | transportLspClassic | vpnTransportLsp],labelPreferenceInput:str[auto | custom | none],labelProviderList:list[str[bgpLuSr | bgpLuSrInterAs | bgpv6LuSr | isisSr | ldp | ospfSr | ospfv3Sr | rsvp | targetedLdpInterAs]])): List of label preferences per Label Category defined as List[Label Category, Label Category input type, List of Label Providers in the preferred order]
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelPreferences'])
    @LabelPreferences.setter
    def LabelPreferences(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelPreferences'], value)

    @property
    def MaxNumberOfVpnLabelStack(self):
        """
        Returns
        -------
        - number: Signifies the maximum number of VPN label stack
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNumberOfVpnLabelStack'])
    @MaxNumberOfVpnLabelStack.setter
    def MaxNumberOfVpnLabelStack(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxNumberOfVpnLabelStack'], value)

    @property
    def MergeDestinations(self):
        """
        Returns
        -------
        - bool: If true, merges the traffic flow in the destination ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MergeDestinations'])
    @MergeDestinations.setter
    def MergeDestinations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MergeDestinations'], value)

    @property
    def MulticastForwardingMode(self):
        """
        Returns
        -------
        - str(loadBalancing | replication): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastForwardingMode'])
    @MulticastForwardingMode.setter
    def MulticastForwardingMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastForwardingMode'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NumVlansForMulticastReplication(self):
        """
        Returns
        -------
        - number: Set the number of vlans for multicast replication
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumVlansForMulticastReplication'])
    @NumVlansForMulticastReplication.setter
    def NumVlansForMulticastReplication(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumVlansForMulticastReplication'], value)

    @property
    def OrdinalNo(self):
        """
        Returns
        -------
        - number: Signifies the ordinal number
        """
        return self._get_attribute(self._SDM_ATT_MAP['OrdinalNo'])
    @OrdinalNo.setter
    def OrdinalNo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OrdinalNo'], value)

    @property
    def OriginatorType(self):
        """
        Returns
        -------
        - str(endUser | quickTest): Indicates who created this trafficItem.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatorType'])
    @OriginatorType.setter
    def OriginatorType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginatorType'], value)

    @property
    def RawTrafficRxPortsBehavior(self):
        """
        Returns
        -------
        - str(loadBalanced | replicated): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RawTrafficRxPortsBehavior'])
    @RawTrafficRxPortsBehavior.setter
    def RawTrafficRxPortsBehavior(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RawTrafficRxPortsBehavior'], value)

    @property
    def RegenerateCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RegenerateCount'])

    @property
    def RoundRobinPacketOrdering(self):
        """
        Returns
        -------
        - bool: This option enables Round Robin Packet Ordering within endpoints across Rx ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RoundRobinPacketOrdering'])
    @RoundRobinPacketOrdering.setter
    def RoundRobinPacketOrdering(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RoundRobinPacketOrdering'], value)

    @property
    def RouteMesh(self):
        """
        Returns
        -------
        - str(fullMesh | oneToOne): The traffic flow type between each pair of source route endpoint and destination route endpoint.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteMesh'])
    @RouteMesh.setter
    def RouteMesh(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteMesh'], value)

    @property
    def SrcDestMesh(self):
        """
        Returns
        -------
        - str(fullMesh | manyToMany | none | oneToOne): Select the options to set the traffic mesh type between the Source Endpoint and Destination endpoint.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrcDestMesh'])
    @SrcDestMesh.setter
    def SrcDestMesh(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrcDestMesh'], value)

    @property
    def State(self):
        """
        Returns
        -------
        - str: (Read only) A read-only field which indicates the current state of the traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def Suspend(self):
        """
        Returns
        -------
        - bool: Suspends all traffic on this stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Suspend'])
    @Suspend.setter
    def Suspend(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Suspend'], value)

    @property
    def TrafficItemType(self):
        """
        Returns
        -------
        - str(application | applicationLibrary | l2L3 | quick): Helps to configure and edit a traffic item that is sent across Ixia ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemType'])
    @TrafficItemType.setter
    def TrafficItemType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficItemType'], value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(atm | avb1722 | avbRaw | ethernetVlan | fc | fcoe | frameRelay | hdlc | ipv4 | ipv4ApplicationTraffic | ipv6 | ipv6ApplicationTraffic | ppp | raw): Helps to select the type of traffic endpoint to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficType'])
    @TrafficType.setter
    def TrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficType'], value)

    @property
    def TransmitMode(self):
        """
        Returns
        -------
        - str(interleaved | sequential): The transmit mode for this traffic item
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitMode'])
    @TransmitMode.setter
    def TransmitMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmitMode'], value)

    @property
    def TransportLdpPreference(self):
        """DEPRECATED 
        Returns
        -------
        - str(one | two): This attribute is deprecated. Use labelPreferences attribute instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportLdpPreference'])
    @TransportLdpPreference.setter
    def TransportLdpPreference(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportLdpPreference'], value)

    @property
    def TransportRsvpTePreference(self):
        """DEPRECATED 
        Returns
        -------
        - str(one | two): This attribute is deprecated. Use labelPreferences attribute instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportRsvpTePreference'])
    @TransportRsvpTePreference.setter
    def TransportRsvpTePreference(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportRsvpTePreference'], value)

    @property
    def UseControlPlaneFrameSize(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseControlPlaneFrameSize'])
    @UseControlPlaneFrameSize.setter
    def UseControlPlaneFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseControlPlaneFrameSize'], value)

    @property
    def UseControlPlaneRate(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseControlPlaneRate'])
    @UseControlPlaneRate.setter
    def UseControlPlaneRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseControlPlaneRate'], value)

    @property
    def Warnings(self):
        """
        Returns
        -------
        - list(str): Displays the warnings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Warnings'])

    def update(self, AllowSelfDestined=None, BgpEpeOrdinalValue=None, BgpEpeSidType=None, BiDirectional=None, EgressEnabled=None, EnableDynamicMplsLabelValues=None, EnableMacsecEgressOnlyAutoConfig=None, Enabled=None, EvpnNextHopOrdinalValue=None, FrerDuplicateElimination=None, HasOpenFlow=None, HostsPerNetwork=None, InterAsBgpPreference=None, InterAsLdpPreference=None, LabelPreferences=None, MaxNumberOfVpnLabelStack=None, MergeDestinations=None, MulticastForwardingMode=None, Name=None, NumVlansForMulticastReplication=None, OrdinalNo=None, OriginatorType=None, RawTrafficRxPortsBehavior=None, RoundRobinPacketOrdering=None, RouteMesh=None, SrcDestMesh=None, Suspend=None, TrafficItemType=None, TrafficType=None, TransmitMode=None, TransportLdpPreference=None, TransportRsvpTePreference=None, UseControlPlaneFrameSize=None, UseControlPlaneRate=None):
        """Updates trafficItem resource on the server.

        Args
        ----
        - AllowSelfDestined (bool): If true, this helps to send traffic from routes on an Ixia port to other routes on the same Ixia port.
        - BgpEpeOrdinalValue (number): 
        - BgpEpeSidType (str(adjSID | nodeSID | setSID)): 
        - BiDirectional (bool): If true, this enables traffic to be sent in forward and reverse destination.
        - EgressEnabled (bool): Enables the egress.
        - EnableDynamicMplsLabelValues (bool): Enables the dynamic MPLS label values.
        - EnableMacsecEgressOnlyAutoConfig (bool): 
        - Enabled (bool): If true, this enables the selected traffic item.
        - EvpnNextHopOrdinalValue (number): 
        - FrerDuplicateElimination (bool): 
        - HasOpenFlow (bool): Indicates whether or not this trafficItem has openflow.
        - HostsPerNetwork (number): The number of emulated hosts for the traffic stream.
        - InterAsBgpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - InterAsLdpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - LabelPreferences (list(dict(labelCategory:str[interAsRegionLsp | interAsRegionLspClassic | ipTransportLsp | transportLspClassic | vpnTransportLsp],labelPreferenceInput:str[auto | custom | none],labelProviderList:list[str[bgpLuSr | bgpLuSrInterAs | bgpv6LuSr | isisSr | ldp | ospfSr | ospfv3Sr | rsvp | targetedLdpInterAs]]))): List of label preferences per Label Category defined as List[Label Category, Label Category input type, List of Label Providers in the preferred order]
        - MaxNumberOfVpnLabelStack (number): Signifies the maximum number of VPN label stack
        - MergeDestinations (bool): If true, merges the traffic flow in the destination ranges.
        - MulticastForwardingMode (str(loadBalancing | replication)): 
        - Name (str): The name of the traffic item.
        - NumVlansForMulticastReplication (number): Set the number of vlans for multicast replication
        - OrdinalNo (number): Signifies the ordinal number
        - OriginatorType (str(endUser | quickTest)): Indicates who created this trafficItem.
        - RawTrafficRxPortsBehavior (str(loadBalanced | replicated)): 
        - RoundRobinPacketOrdering (bool): This option enables Round Robin Packet Ordering within endpoints across Rx ports.
        - RouteMesh (str(fullMesh | oneToOne)): The traffic flow type between each pair of source route endpoint and destination route endpoint.
        - SrcDestMesh (str(fullMesh | manyToMany | none | oneToOne)): Select the options to set the traffic mesh type between the Source Endpoint and Destination endpoint.
        - Suspend (bool): Suspends all traffic on this stream.
        - TrafficItemType (str(application | applicationLibrary | l2L3 | quick)): Helps to configure and edit a traffic item that is sent across Ixia ports.
        - TrafficType (str(atm | avb1722 | avbRaw | ethernetVlan | fc | fcoe | frameRelay | hdlc | ipv4 | ipv4ApplicationTraffic | ipv6 | ipv6ApplicationTraffic | ppp | raw)): Helps to select the type of traffic endpoint to be configured.
        - TransmitMode (str(interleaved | sequential)): The transmit mode for this traffic item
        - TransportLdpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - TransportRsvpTePreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - UseControlPlaneFrameSize (bool): 
        - UseControlPlaneRate (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AllowSelfDestined=None, BgpEpeOrdinalValue=None, BgpEpeSidType=None, BiDirectional=None, EgressEnabled=None, EnableDynamicMplsLabelValues=None, EnableMacsecEgressOnlyAutoConfig=None, Enabled=None, EvpnNextHopOrdinalValue=None, FrerDuplicateElimination=None, HasOpenFlow=None, HostsPerNetwork=None, InterAsBgpPreference=None, InterAsLdpPreference=None, LabelPreferences=None, MaxNumberOfVpnLabelStack=None, MergeDestinations=None, MulticastForwardingMode=None, Name=None, NumVlansForMulticastReplication=None, OrdinalNo=None, OriginatorType=None, RawTrafficRxPortsBehavior=None, RoundRobinPacketOrdering=None, RouteMesh=None, SrcDestMesh=None, Suspend=None, TrafficItemType=None, TrafficType=None, TransmitMode=None, TransportLdpPreference=None, TransportRsvpTePreference=None, UseControlPlaneFrameSize=None, UseControlPlaneRate=None):
        """Adds a new trafficItem resource on the server and adds it to the container.

        Args
        ----
        - AllowSelfDestined (bool): If true, this helps to send traffic from routes on an Ixia port to other routes on the same Ixia port.
        - BgpEpeOrdinalValue (number): 
        - BgpEpeSidType (str(adjSID | nodeSID | setSID)): 
        - BiDirectional (bool): If true, this enables traffic to be sent in forward and reverse destination.
        - EgressEnabled (bool): Enables the egress.
        - EnableDynamicMplsLabelValues (bool): Enables the dynamic MPLS label values.
        - EnableMacsecEgressOnlyAutoConfig (bool): 
        - Enabled (bool): If true, this enables the selected traffic item.
        - EvpnNextHopOrdinalValue (number): 
        - FrerDuplicateElimination (bool): 
        - HasOpenFlow (bool): Indicates whether or not this trafficItem has openflow.
        - HostsPerNetwork (number): The number of emulated hosts for the traffic stream.
        - InterAsBgpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - InterAsLdpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - LabelPreferences (list(dict(labelCategory:str[interAsRegionLsp | interAsRegionLspClassic | ipTransportLsp | transportLspClassic | vpnTransportLsp],labelPreferenceInput:str[auto | custom | none],labelProviderList:list[str[bgpLuSr | bgpLuSrInterAs | bgpv6LuSr | isisSr | ldp | ospfSr | ospfv3Sr | rsvp | targetedLdpInterAs]]))): List of label preferences per Label Category defined as List[Label Category, Label Category input type, List of Label Providers in the preferred order]
        - MaxNumberOfVpnLabelStack (number): Signifies the maximum number of VPN label stack
        - MergeDestinations (bool): If true, merges the traffic flow in the destination ranges.
        - MulticastForwardingMode (str(loadBalancing | replication)): 
        - Name (str): The name of the traffic item.
        - NumVlansForMulticastReplication (number): Set the number of vlans for multicast replication
        - OrdinalNo (number): Signifies the ordinal number
        - OriginatorType (str(endUser | quickTest)): Indicates who created this trafficItem.
        - RawTrafficRxPortsBehavior (str(loadBalanced | replicated)): 
        - RoundRobinPacketOrdering (bool): This option enables Round Robin Packet Ordering within endpoints across Rx ports.
        - RouteMesh (str(fullMesh | oneToOne)): The traffic flow type between each pair of source route endpoint and destination route endpoint.
        - SrcDestMesh (str(fullMesh | manyToMany | none | oneToOne)): Select the options to set the traffic mesh type between the Source Endpoint and Destination endpoint.
        - Suspend (bool): Suspends all traffic on this stream.
        - TrafficItemType (str(application | applicationLibrary | l2L3 | quick)): Helps to configure and edit a traffic item that is sent across Ixia ports.
        - TrafficType (str(atm | avb1722 | avbRaw | ethernetVlan | fc | fcoe | frameRelay | hdlc | ipv4 | ipv4ApplicationTraffic | ipv6 | ipv6ApplicationTraffic | ppp | raw)): Helps to select the type of traffic endpoint to be configured.
        - TransmitMode (str(interleaved | sequential)): The transmit mode for this traffic item
        - TransportLdpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - TransportRsvpTePreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - UseControlPlaneFrameSize (bool): 
        - UseControlPlaneRate (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved trafficItem resources using find and the newly added trafficItem resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trafficItem resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AllowSelfDestined=None, BgpEpeOrdinalValue=None, BgpEpeSidType=None, BiDirectional=None, EgressEnabled=None, EnableDynamicMplsLabelValues=None, EnableMacsecEgressOnlyAutoConfig=None, Enabled=None, Errors=None, EvpnNextHopOrdinalValue=None, FlowGroupCount=None, FrerDuplicateElimination=None, HasOpenFlow=None, HostsPerNetwork=None, InterAsBgpPreference=None, InterAsLdpPreference=None, LabelPreferences=None, MaxNumberOfVpnLabelStack=None, MergeDestinations=None, MulticastForwardingMode=None, Name=None, NumVlansForMulticastReplication=None, OrdinalNo=None, OriginatorType=None, RawTrafficRxPortsBehavior=None, RegenerateCount=None, RoundRobinPacketOrdering=None, RouteMesh=None, SrcDestMesh=None, State=None, Suspend=None, TrafficItemType=None, TrafficType=None, TransmitMode=None, TransportLdpPreference=None, TransportRsvpTePreference=None, UseControlPlaneFrameSize=None, UseControlPlaneRate=None, Warnings=None):
        """Finds and retrieves trafficItem resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficItem resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficItem resources from the server.

        Args
        ----
        - AllowSelfDestined (bool): If true, this helps to send traffic from routes on an Ixia port to other routes on the same Ixia port.
        - BgpEpeOrdinalValue (number): 
        - BgpEpeSidType (str(adjSID | nodeSID | setSID)): 
        - BiDirectional (bool): If true, this enables traffic to be sent in forward and reverse destination.
        - EgressEnabled (bool): Enables the egress.
        - EnableDynamicMplsLabelValues (bool): Enables the dynamic MPLS label values.
        - EnableMacsecEgressOnlyAutoConfig (bool): 
        - Enabled (bool): If true, this enables the selected traffic item.
        - Errors (list(str)): Displays the errors.
        - EvpnNextHopOrdinalValue (number): 
        - FlowGroupCount (number): Indicates the number of flow groups.
        - FrerDuplicateElimination (bool): 
        - HasOpenFlow (bool): Indicates whether or not this trafficItem has openflow.
        - HostsPerNetwork (number): The number of emulated hosts for the traffic stream.
        - InterAsBgpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - InterAsLdpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - LabelPreferences (list(dict(labelCategory:str[interAsRegionLsp | interAsRegionLspClassic | ipTransportLsp | transportLspClassic | vpnTransportLsp],labelPreferenceInput:str[auto | custom | none],labelProviderList:list[str[bgpLuSr | bgpLuSrInterAs | bgpv6LuSr | isisSr | ldp | ospfSr | ospfv3Sr | rsvp | targetedLdpInterAs]]))): List of label preferences per Label Category defined as List[Label Category, Label Category input type, List of Label Providers in the preferred order]
        - MaxNumberOfVpnLabelStack (number): Signifies the maximum number of VPN label stack
        - MergeDestinations (bool): If true, merges the traffic flow in the destination ranges.
        - MulticastForwardingMode (str(loadBalancing | replication)): 
        - Name (str): The name of the traffic item.
        - NumVlansForMulticastReplication (number): Set the number of vlans for multicast replication
        - OrdinalNo (number): Signifies the ordinal number
        - OriginatorType (str(endUser | quickTest)): Indicates who created this trafficItem.
        - RawTrafficRxPortsBehavior (str(loadBalanced | replicated)): 
        - RegenerateCount (number): 
        - RoundRobinPacketOrdering (bool): This option enables Round Robin Packet Ordering within endpoints across Rx ports.
        - RouteMesh (str(fullMesh | oneToOne)): The traffic flow type between each pair of source route endpoint and destination route endpoint.
        - SrcDestMesh (str(fullMesh | manyToMany | none | oneToOne)): Select the options to set the traffic mesh type between the Source Endpoint and Destination endpoint.
        - State (str): (Read only) A read-only field which indicates the current state of the traffic item.
        - Suspend (bool): Suspends all traffic on this stream.
        - TrafficItemType (str(application | applicationLibrary | l2L3 | quick)): Helps to configure and edit a traffic item that is sent across Ixia ports.
        - TrafficType (str(atm | avb1722 | avbRaw | ethernetVlan | fc | fcoe | frameRelay | hdlc | ipv4 | ipv4ApplicationTraffic | ipv6 | ipv6ApplicationTraffic | ppp | raw)): Helps to select the type of traffic endpoint to be configured.
        - TransmitMode (str(interleaved | sequential)): The transmit mode for this traffic item
        - TransportLdpPreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - TransportRsvpTePreference (str(one | two)): This attribute is deprecated. Use labelPreferences attribute instead.
        - UseControlPlaneFrameSize (bool): 
        - UseControlPlaneRate (bool): 
        - Warnings (list(str)): Displays the warnings.

        Returns
        -------
        - self: This instance with matching trafficItem resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trafficItem data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficItem resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ConvertToRaw(self):
        """Executes the convertToRaw operation on the server.

        Converts a non-raw traffic item to a raw traffic item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('convertToRaw', payload=payload, response_object=None)

    def Duplicate(self, *args, **kwargs):
        """Executes the duplicate operation on the server.

        Duplicates a specific traffic item.

        duplicate(Arg2=number)
        ----------------------
        - Arg2 (number): The number of times to duplicate the traffic item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('duplicate', payload=payload, response_object=None)

    def DuplicateItems(self):
        """Executes the duplicateItems operation on the server.

        Duplicates a list of traffic items.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('duplicateItems', payload=payload, response_object=None)

    def Generate(self):
        """Executes the generate operation on the server.

        Generate traffic for specific traffic items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('generate', payload=payload, response_object=None)

    def PauseStatelessTraffic(self, *args, **kwargs):
        """Executes the pauseStatelessTraffic operation on the server.

        Pause or Resume stateless traffic.

        pauseStatelessTraffic(Arg2=bool)
        --------------------------------
        - Arg2 (bool): If true, it will pause running traffic. If false, it will resume previously paused traffic.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('pauseStatelessTraffic', payload=payload, response_object=None)

    def ResolveAptixiaEndpoints(self):
        """Executes the resolveAptixiaEndpoints operation on the server.

        Resolves /vport/protocolStack/. endpoints being used by a specific traffic item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('resolveAptixiaEndpoints', payload=payload, response_object=None)

    def StartDefaultLearning(self):
        """Executes the startDefaultLearning operation on the server.

        Starts default learning for a list of traffic items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('startDefaultLearning', payload=payload, response_object=None)

    def StartLearning(self, *args, **kwargs):
        """Executes the startLearning operation on the server.

        Sends learning frames.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startLearning(Arg2=number, Arg3=number, Arg4=number)
        ----------------------------------------------------
        - Arg2 (number): The framesize of the learning frame.
        - Arg3 (number): The framecount of the learning frames.
        - Arg4 (number): The frames per second of the learning frames.

        startLearning(Arg2=number, Arg3=number, Arg4=number, Arg5=bool, Arg6=bool, Arg7=bool)
        -------------------------------------------------------------------------------------
        - Arg2 (number): The framesize of the learning frame.
        - Arg3 (number): The framecount of the learning frames.
        - Arg4 (number): The frames per second of the learning frames.
        - Arg5 (bool): Send gratuitous ARP frames.
        - Arg6 (bool): Send MAC frames.
        - Arg7 (bool): Send Fast Path frames.

        startLearning(Arg2=number, Arg3=number, Arg4=number, Arg5=bool, Arg6=bool, Arg7=bool, Arg8=bool)
        ------------------------------------------------------------------------------------------------
        - Arg2 (number): The framesize of the learning frame.
        - Arg3 (number): The framecount of the learning frames.
        - Arg4 (number): The frames per second of the learning frames.
        - Arg5 (bool): Send gratuitous ARP frames.
        - Arg6 (bool): Send MAC frames.
        - Arg7 (bool): Send Fast Path frames.
        - Arg8 (bool): Send full mesh.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startLearning', payload=payload, response_object=None)

    def StartStatelessTraffic(self):
        """Executes the startStatelessTraffic operation on the server.

        Start the traffic configuration for stateless traffic items only.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('startStatelessTraffic', payload=payload, response_object=None)

    def StartStatelessTrafficBlocking(self):
        """Executes the startStatelessTrafficBlocking operation on the server.

        Start the traffic configuration for stateless traffic items only. This will block until traffic is fully started.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('startStatelessTrafficBlocking', payload=payload, response_object=None)

    def StopStatelessTraffic(self):
        """Executes the stopStatelessTraffic operation on the server.

        Stop the stateless traffic items.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stopStatelessTraffic', payload=payload, response_object=None)

    def StopStatelessTrafficBlocking(self):
        """Executes the stopStatelessTrafficBlocking operation on the server.

        Stop the traffic configuration for stateless traffic items only. This will block until traffic is fully stopped.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stopStatelessTrafficBlocking', payload=payload, response_object=None)
