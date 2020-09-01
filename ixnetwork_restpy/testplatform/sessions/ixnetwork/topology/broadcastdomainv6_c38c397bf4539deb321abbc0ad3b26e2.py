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


class BroadcastDomainV6(Base):
    """BGP V6 Broadcast Domain Configuration
    The BroadcastDomainV6 class encapsulates a required broadcastDomainV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'broadcastDomainV6'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdRouteLabel': 'adRouteLabel',
        'AdvSrv6SidInIgp': 'advSrv6SidInIgp',
        'AdvertiseSRv6SID': 'advertiseSRv6SID',
        'BVlanId': 'bVlanId',
        'BVlanPriority': 'bVlanPriority',
        'BVlanTpid': 'bVlanTpid',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableVlanAwareService': 'enableVlanAwareService',
        'EthernetTagId': 'ethernetTagId',
        'GroupAddress': 'groupAddress',
        'Name': 'name',
        'NoOfMacPools': 'noOfMacPools',
        'RootAddress': 'rootAddress',
        'RsvpP2mpId': 'rsvpP2mpId',
        'RsvpP2mpIdAsNumber': 'rsvpP2mpIdAsNumber',
        'RsvpTunnelId': 'rsvpTunnelId',
        'SendSRv6SIDOptionalInfo': 'sendSRv6SIDOptionalInfo',
        'SenderAddressPRootNodeAddress': 'senderAddressPRootNodeAddress',
        'Srv6EndpointBehavior': 'srv6EndpointBehavior',
        'Srv6SIDOptionalInformation': 'srv6SIDOptionalInformation',
        'Srv6SidFlags': 'srv6SidFlags',
        'Srv6SidLoc': 'srv6SidLoc',
        'Srv6SidLocLen': 'srv6SidLocLen',
        'Srv6SidLocMetric': 'srv6SidLocMetric',
        'Srv6SidReserved': 'srv6SidReserved',
        'Srv6SidReserved1': 'srv6SidReserved1',
        'Srv6SidReserved2': 'srv6SidReserved2',
        'UsebVlan': 'usebVlan',
    }

    def __init__(self, parent):
        super(BroadcastDomainV6, self).__init__(parent)

    @property
    def PnTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57.PnTLVList): An instance of the PnTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57 import PnTLVList
        return PnTLVList(self)

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
    def AdRouteLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AD Route Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdRouteLabel']))

    @property
    def AdvSrv6SidInIgp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvSrv6SidInIgp']))

    @property
    def AdvertiseSRv6SID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseSRv6SID']))

    @property
    def BVlanId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BVlanId']))

    @property
    def BVlanPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BVlanPriority']))

    @property
    def BVlanTpid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BVlanTpid']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableVlanAwareService(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable VLAN Aware Service
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableVlanAwareService']))

    @property
    def EthernetTagId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ethernet Tag ID. For VPWS, this acts as VPWS Service ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EthernetTagId']))

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddress']))

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
    def NoOfMacPools(self):
        """
        Returns
        -------
        - number: Number of Mac Pools
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfMacPools'])
    @NoOfMacPools.setter
    def NoOfMacPools(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfMacPools'], value)

    @property
    def RootAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddress']))

    @property
    def RsvpP2mpId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpId']))

    @property
    def RsvpP2mpIdAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID as Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpIdAsNumber']))

    @property
    def RsvpTunnelId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvpTunnelId']))

    @property
    def SendSRv6SIDOptionalInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If we need to advertise SRv6 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendSRv6SIDOptionalInfo']))

    @property
    def SenderAddressPRootNodeAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SenderAddressPRootNodeAddress']))

    @property
    def Srv6EndpointBehavior(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Endpoint Behavior field Value for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6EndpointBehavior']))

    @property
    def Srv6SIDOptionalInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SIDOptionalInformation']))

    @property
    def Srv6SidFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Flags Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidFlags']))

    @property
    def Srv6SidLoc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLoc']))

    @property
    def Srv6SidLocLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLocLen']))

    @property
    def Srv6SidLocMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLocMetric']))

    @property
    def Srv6SidReserved(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved']))

    @property
    def Srv6SidReserved1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved1 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved1']))

    @property
    def Srv6SidReserved2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved2 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved2']))

    @property
    def UsebVlan(self):
        """
        Returns
        -------
        - bool: Use B-VLAN
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsebVlan'])
    @UsebVlan.setter
    def UsebVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsebVlan'], value)

    def update(self, Name=None, NoOfMacPools=None, UsebVlan=None):
        """Updates broadcastDomainV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMacPools (number): Number of Mac Pools
        - UsebVlan (bool): Use B-VLAN

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AdRouteLabel=None, AdvSrv6SidInIgp=None, AdvertiseSRv6SID=None, BVlanId=None, BVlanPriority=None, BVlanTpid=None, EnableVlanAwareService=None, EthernetTagId=None, GroupAddress=None, RootAddress=None, RsvpP2mpId=None, RsvpP2mpIdAsNumber=None, RsvpTunnelId=None, SendSRv6SIDOptionalInfo=None, SenderAddressPRootNodeAddress=None, Srv6EndpointBehavior=None, Srv6SIDOptionalInformation=None, Srv6SidFlags=None, Srv6SidLoc=None, Srv6SidLocLen=None, Srv6SidLocMetric=None, Srv6SidReserved=None, Srv6SidReserved1=None, Srv6SidReserved2=None):
        """Base class infrastructure that gets a list of broadcastDomainV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdRouteLabel (str): optional regex of adRouteLabel
        - AdvSrv6SidInIgp (str): optional regex of advSrv6SidInIgp
        - AdvertiseSRv6SID (str): optional regex of advertiseSRv6SID
        - BVlanId (str): optional regex of bVlanId
        - BVlanPriority (str): optional regex of bVlanPriority
        - BVlanTpid (str): optional regex of bVlanTpid
        - EnableVlanAwareService (str): optional regex of enableVlanAwareService
        - EthernetTagId (str): optional regex of ethernetTagId
        - GroupAddress (str): optional regex of groupAddress
        - RootAddress (str): optional regex of rootAddress
        - RsvpP2mpId (str): optional regex of rsvpP2mpId
        - RsvpP2mpIdAsNumber (str): optional regex of rsvpP2mpIdAsNumber
        - RsvpTunnelId (str): optional regex of rsvpTunnelId
        - SendSRv6SIDOptionalInfo (str): optional regex of sendSRv6SIDOptionalInfo
        - SenderAddressPRootNodeAddress (str): optional regex of senderAddressPRootNodeAddress
        - Srv6EndpointBehavior (str): optional regex of srv6EndpointBehavior
        - Srv6SIDOptionalInformation (str): optional regex of srv6SIDOptionalInformation
        - Srv6SidFlags (str): optional regex of srv6SidFlags
        - Srv6SidLoc (str): optional regex of srv6SidLoc
        - Srv6SidLocLen (str): optional regex of srv6SidLocLen
        - Srv6SidLocMetric (str): optional regex of srv6SidLocMetric
        - Srv6SidReserved (str): optional regex of srv6SidReserved
        - Srv6SidReserved1 (str): optional regex of srv6SidReserved1
        - Srv6SidReserved2 (str): optional regex of srv6SidReserved2

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def AdvertiseAliasing(self, *args, **kwargs):
        """Executes the advertiseAliasing operation on the server.

        Advertise Aliasing Per Broadcast Domain.

        advertiseAliasing(Arg2=list)list
        --------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('advertiseAliasing', payload=payload, response_object=None)

    def AdvertiseAliasingPerBroadcastDomain(self, *args, **kwargs):
        """Executes the advertiseAliasingPerBroadcastDomain operation on the server.

        Advertise Aliasing Per Broadcast Domain

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        advertiseAliasingPerBroadcastDomain(SessionIndices=list)
        --------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        advertiseAliasingPerBroadcastDomain(SessionIndices=string)
        ----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('advertiseAliasingPerBroadcastDomain', payload=payload, response_object=None)

    def WithdrawAliasing(self, *args, **kwargs):
        """Executes the withdrawAliasing operation on the server.

        Withdraw Aliasing Per Broadcast Domain.

        withdrawAliasing(Arg2=list)list
        -------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('withdrawAliasing', payload=payload, response_object=None)

    def WithdrawAliasingPerBroadcastDomain(self, *args, **kwargs):
        """Executes the withdrawAliasingPerBroadcastDomain operation on the server.

        Advertise Aliasing Per Broadcast Domain

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        withdrawAliasingPerBroadcastDomain(SessionIndices=list)
        -------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        withdrawAliasingPerBroadcastDomain(SessionIndices=string)
        ---------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('withdrawAliasingPerBroadcastDomain', payload=payload, response_object=None)
