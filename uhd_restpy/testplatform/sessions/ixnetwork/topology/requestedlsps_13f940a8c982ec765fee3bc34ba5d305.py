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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class RequestedLsps(Base):
    """Requested LSPs
    The RequestedLsps class encapsulates a required requestedLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'requestedLsps'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ActiveDataTrafficEndPoints': 'activeDataTrafficEndPoints',
        'Bandwidth': 'bandwidth',
        'BiDirectional': 'biDirectional',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestinationIpv4Address': 'destinationIpv4Address',
        'DestinationIpv6Address': 'destinationIpv6Address',
        'ExcludeAny': 'excludeAny',
        'FailBit': 'failBit',
        'HoldingPriority': 'holdingPriority',
        'IncludeAll': 'includeAll',
        'IncludeAny': 'includeAny',
        'IncludeBandwidth': 'includeBandwidth',
        'IncludeEndPoints': 'includeEndPoints',
        'IncludeIro': 'includeIro',
        'IncludeLsp': 'includeLsp',
        'IncludeLspa': 'includeLspa',
        'IncludeMetric': 'includeMetric',
        'IncludeRp': 'includeRp',
        'IncludeSymbolicPathNameTlv': 'includeSymbolicPathNameTlv',
        'IncludeXro': 'includeXro',
        'InitialDelegation': 'initialDelegation',
        'InsertIpv6ExplicitNull': 'insertIpv6ExplicitNull',
        'IpVersion': 'ipVersion',
        'LocalProtection': 'localProtection',
        'Loose': 'loose',
        'LspDelegationState': 'lspDelegationState',
        'MaxExpectedSegmentCount': 'maxExpectedSegmentCount',
        'MaxNoOfIroSubObjects': 'maxNoOfIroSubObjects',
        'MaxNoOfXroSubObjects': 'maxNoOfXroSubObjects',
        'MaxNumberOfMetrics': 'maxNumberOfMetrics',
        'Name': 'name',
        'OverridePlspId': 'overridePlspId',
        'OverrideRequestId': 'overrideRequestId',
        'OverrideSourceAddress': 'overrideSourceAddress',
        'PFlagBandwidth': 'pFlagBandwidth',
        'PFlagIro': 'pFlagIro',
        'PFlagLsp': 'pFlagLsp',
        'PFlagLspa': 'pFlagLspa',
        'PFlagRp': 'pFlagRp',
        'PFlagXro': 'pFlagXro',
        'PflagEndpoints': 'pflagEndpoints',
        'PlspId': 'plspId',
        'Priority': 'priority',
        'ReDelegationTimerStatus': 'reDelegationTimerStatus',
        'ReOptimization': 'reOptimization',
        'RedelegationTimeoutInterval': 'redelegationTimeoutInterval',
        'RequestId': 'requestId',
        'SetupPriority': 'setupPriority',
        'SourceEndPointIPv4': 'sourceEndPointIPv4',
        'SourceEndPointIPv6': 'sourceEndPointIPv6',
        'SourceIpv4Address': 'sourceIpv4Address',
        'SourceIpv6Address': 'sourceIpv6Address',
        'SymbolicPathName': 'symbolicPathName',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(RequestedLsps, self).__init__(parent, list_op)

    @property
    def PccRequestedMetricSubObjectsList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pccrequestedmetricsubobjectslist_c24616543d14c4003121b08785bb4446.PccRequestedMetricSubObjectsList): An instance of the PccRequestedMetricSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pccrequestedmetricsubobjectslist_c24616543d14c4003121b08785bb4446 import PccRequestedMetricSubObjectsList
        if self._properties.get('PccRequestedMetricSubObjectsList', None) is not None:
            return self._properties.get('PccRequestedMetricSubObjectsList')
        else:
            return PccRequestedMetricSubObjectsList(self)

    @property
    def PcepIroSubObjectsList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pcepirosubobjectslist_9817af6d0e89111784eda2c3b9333ff5.PcepIroSubObjectsList): An instance of the PcepIroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pcepirosubobjectslist_9817af6d0e89111784eda2c3b9333ff5 import PcepIroSubObjectsList
        if self._properties.get('PcepIroSubObjectsList', None) is not None:
            return self._properties.get('PcepIroSubObjectsList')
        else:
            return PcepIroSubObjectsList(self)

    @property
    def PcepXroSubObjectsList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pcepxrosubobjectslist_a61cc0ded9b5e7cc900bb16a43234a56.PcepXroSubObjectsList): An instance of the PcepXroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pcepxrosubobjectslist_a61cc0ded9b5e7cc900bb16a43234a56 import PcepXroSubObjectsList
        if self._properties.get('PcepXroSubObjectsList', None) is not None:
            return self._properties.get('PcepXroSubObjectsList')
        else:
            return PcepXroSubObjectsList(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        if self._properties.get('Tag', None) is not None:
            return self._properties.get('Tag')
        else:
            return Tag(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ActiveDataTrafficEndPoints(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies whether that specific Data Traffic Endpoint will generate data traffic
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveDataTrafficEndPoints']))

    @property
    def Bandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth (bits/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bandwidth']))

    @property
    def BiDirectional(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bi-directional
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BiDirectional']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DestinationIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationIpv4Address']))

    @property
    def DestinationIpv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination IPv6 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationIpv6Address']))

    @property
    def ExcludeAny(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Exclude Any
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAny']))

    @property
    def FailBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Fail Bit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FailBit']))

    @property
    def HoldingPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Holding Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HoldingPriority']))

    @property
    def IncludeAll(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include All
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAll']))

    @property
    def IncludeAny(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Any
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAny']))

    @property
    def IncludeBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Bandwidth
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeBandwidth']))

    @property
    def IncludeEndPoints(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include End Points
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeEndPoints']))

    @property
    def IncludeIro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include IRO
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeIro']))

    @property
    def IncludeLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeLsp']))

    @property
    def IncludeLspa(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include LSPA
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeLspa']))

    @property
    def IncludeMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMetric']))

    @property
    def IncludeRp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include RP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeRp']))

    @property
    def IncludeSymbolicPathNameTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Symbolic Path Name TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSymbolicPathNameTlv']))

    @property
    def IncludeXro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include XRO
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeXro']))

    @property
    def InitialDelegation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Initial Delegation
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitialDelegation']))

    @property
    def InsertIpv6ExplicitNull(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        """
        return self._get_attribute(self._SDM_ATT_MAP['InsertIpv6ExplicitNull'])
    @InsertIpv6ExplicitNull.setter
    def InsertIpv6ExplicitNull(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['InsertIpv6ExplicitNull'], value)

    @property
    def IpVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IP Version
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpVersion']))

    @property
    def LocalProtection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local Protection
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalProtection']))

    @property
    def Loose(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Loose
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Loose']))

    @property
    def LspDelegationState(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[delegated | delegationConfirmed | delegationRejected | delegationReturned | delegationRevoked | nonDelegated | none]): LSP Delegation State
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspDelegationState'])

    @property
    def MaxExpectedSegmentCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This control is used to set the maximum Segment count/ MPLS labels that would be present in the generted traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxExpectedSegmentCount'])
    @MaxExpectedSegmentCount.setter
    def MaxExpectedSegmentCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxExpectedSegmentCount'], value)

    @property
    def MaxNoOfIroSubObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Max Number of IRO Sub Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNoOfIroSubObjects'])
    @MaxNoOfIroSubObjects.setter
    def MaxNoOfIroSubObjects(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxNoOfIroSubObjects'], value)

    @property
    def MaxNoOfXroSubObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Max Number of XRO Sub Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNoOfXroSubObjects'])
    @MaxNoOfXroSubObjects.setter
    def MaxNoOfXroSubObjects(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxNoOfXroSubObjects'], value)

    @property
    def MaxNumberOfMetrics(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Max Number of Metrics
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNumberOfMetrics'])
    @MaxNumberOfMetrics.setter
    def MaxNumberOfMetrics(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxNumberOfMetrics'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OverridePlspId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Override PLSP-ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverridePlspId'])
    @OverridePlspId.setter
    def OverridePlspId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['OverridePlspId'], value)

    @property
    def OverrideRequestId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Override Request ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideRequestId'])
    @OverrideRequestId.setter
    def OverrideRequestId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['OverrideRequestId'], value)

    @property
    def OverrideSourceAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Override Source Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverrideSourceAddress']))

    @property
    def PFlagBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagBandwidth']))

    @property
    def PFlagIro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IRO P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagIro']))

    @property
    def PFlagLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): LSP P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagLsp']))

    @property
    def PFlagLspa(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): LSPA P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagLspa']))

    @property
    def PFlagRp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RP P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagRp']))

    @property
    def PFlagXro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): XRO P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagXro']))

    @property
    def PflagEndpoints(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): End Points P Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PflagEndpoints']))

    @property
    def PlspId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PlspId']))

    @property
    def Priority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    @property
    def ReDelegationTimerStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[expired | none | notStarted | running | stopped]): Re-Delegation Timer Status
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReDelegationTimerStatus'])

    @property
    def ReOptimization(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Re-optimization
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReOptimization']))

    @property
    def RedelegationTimeoutInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The period of time a PCC waits for, when a PCEP session is terminated, before revoking LSP delegation to a PCE and attempting to redelegate LSPs associated with the terminated PCEP session to PCE.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedelegationTimeoutInterval']))

    @property
    def RequestId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Request ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RequestId']))

    @property
    def SetupPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Setup Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetupPriority']))

    @property
    def SourceEndPointIPv4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceEndPointIPv4']))

    @property
    def SourceEndPointIPv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv6 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceEndPointIPv6']))

    @property
    def SourceIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIpv4Address']))

    @property
    def SourceIpv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv6 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIpv6Address']))

    @property
    def SymbolicPathName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Symbolic Path Name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SymbolicPathName']))

    def update(self, InsertIpv6ExplicitNull=None, MaxExpectedSegmentCount=None, MaxNoOfIroSubObjects=None, MaxNoOfXroSubObjects=None, MaxNumberOfMetrics=None, Name=None, OverridePlspId=None, OverrideRequestId=None):
        # type: (bool, int, int, int, int, str, bool, bool) -> RequestedLsps
        """Updates requestedLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - InsertIpv6ExplicitNull (bool): Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        - MaxExpectedSegmentCount (number): This control is used to set the maximum Segment count/ MPLS labels that would be present in the generted traffic.
        - MaxNoOfIroSubObjects (number): Max Number of IRO Sub Objects
        - MaxNoOfXroSubObjects (number): Max Number of XRO Sub Objects
        - MaxNumberOfMetrics (number): Max Number of Metrics
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OverridePlspId (bool): Override PLSP-ID
        - OverrideRequestId (bool): Override Request ID

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Delegate(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the delegate operation on the server.

        Delegate

        delegate(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('delegate', payload=payload, response_object=None)

    def RevokeDelegation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the revokeDelegation operation on the server.

        Revoke Delegation

        revokeDelegation(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('revokeDelegation', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, ActiveDataTrafficEndPoints=None, Bandwidth=None, BiDirectional=None, DestinationIpv4Address=None, DestinationIpv6Address=None, ExcludeAny=None, FailBit=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeBandwidth=None, IncludeEndPoints=None, IncludeIro=None, IncludeLsp=None, IncludeLspa=None, IncludeMetric=None, IncludeRp=None, IncludeSymbolicPathNameTlv=None, IncludeXro=None, InitialDelegation=None, IpVersion=None, LocalProtection=None, Loose=None, OverrideSourceAddress=None, PFlagBandwidth=None, PFlagIro=None, PFlagLsp=None, PFlagLspa=None, PFlagRp=None, PFlagXro=None, PflagEndpoints=None, PlspId=None, Priority=None, ReOptimization=None, RedelegationTimeoutInterval=None, RequestId=None, SetupPriority=None, SourceEndPointIPv4=None, SourceEndPointIPv6=None, SourceIpv4Address=None, SourceIpv6Address=None, SymbolicPathName=None):
        """Base class infrastructure that gets a list of requestedLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveDataTrafficEndPoints (str): optional regex of activeDataTrafficEndPoints
        - Bandwidth (str): optional regex of bandwidth
        - BiDirectional (str): optional regex of biDirectional
        - DestinationIpv4Address (str): optional regex of destinationIpv4Address
        - DestinationIpv6Address (str): optional regex of destinationIpv6Address
        - ExcludeAny (str): optional regex of excludeAny
        - FailBit (str): optional regex of failBit
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeBandwidth (str): optional regex of includeBandwidth
        - IncludeEndPoints (str): optional regex of includeEndPoints
        - IncludeIro (str): optional regex of includeIro
        - IncludeLsp (str): optional regex of includeLsp
        - IncludeLspa (str): optional regex of includeLspa
        - IncludeMetric (str): optional regex of includeMetric
        - IncludeRp (str): optional regex of includeRp
        - IncludeSymbolicPathNameTlv (str): optional regex of includeSymbolicPathNameTlv
        - IncludeXro (str): optional regex of includeXro
        - InitialDelegation (str): optional regex of initialDelegation
        - IpVersion (str): optional regex of ipVersion
        - LocalProtection (str): optional regex of localProtection
        - Loose (str): optional regex of loose
        - OverrideSourceAddress (str): optional regex of overrideSourceAddress
        - PFlagBandwidth (str): optional regex of pFlagBandwidth
        - PFlagIro (str): optional regex of pFlagIro
        - PFlagLsp (str): optional regex of pFlagLsp
        - PFlagLspa (str): optional regex of pFlagLspa
        - PFlagRp (str): optional regex of pFlagRp
        - PFlagXro (str): optional regex of pFlagXro
        - PflagEndpoints (str): optional regex of pflagEndpoints
        - PlspId (str): optional regex of plspId
        - Priority (str): optional regex of priority
        - ReOptimization (str): optional regex of reOptimization
        - RedelegationTimeoutInterval (str): optional regex of redelegationTimeoutInterval
        - RequestId (str): optional regex of requestId
        - SetupPriority (str): optional regex of setupPriority
        - SourceEndPointIPv4 (str): optional regex of sourceEndPointIPv4
        - SourceEndPointIPv6 (str): optional regex of sourceEndPointIPv6
        - SourceIpv4Address (str): optional regex of sourceIpv4Address
        - SourceIpv6Address (str): optional regex of sourceIpv6Address
        - SymbolicPathName (str): optional regex of symbolicPathName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
