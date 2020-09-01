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


class BgpMVpnReceiverSitesIpv4(Base):
    """Bgp MVPN Receiver Sites Properties
    The BgpMVpnReceiverSitesIpv4 class encapsulates a list of bgpMVpnReceiverSitesIpv4 resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpMVpnReceiverSitesIpv4.find() method.
    The list can be managed by using the BgpMVpnReceiverSitesIpv4.add() and BgpMVpnReceiverSitesIpv4.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpMVpnReceiverSitesIpv4'
    _SDM_ATT_MAP = {
        'BFRId': 'BFRId',
        'BFRIpv4Prefix': 'BFRIpv4Prefix',
        'BFRIpv6Prefix': 'BFRIpv6Prefix',
        'BFRPrefixType': 'BFRPrefixType',
        'SubDomainId': 'SubDomainId',
        'UseAutoSubDomainId': 'UseAutoSubDomainId',
        'Active': 'active',
        'CMulticastRouteType': 'cMulticastRouteType',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DownstreamLabel': 'downstreamLabel',
        'EnableNextHop': 'enableNextHop',
        'GroupAddressCount': 'groupAddressCount',
        'GroupMaskWidth': 'groupMaskWidth',
        'IncludeBierPtainLeafAd': 'includeBierPtainLeafAd',
        'Ipv4NextHop': 'ipv4NextHop',
        'Ipv6NextHop': 'ipv6NextHop',
        'Name': 'name',
        'SendTriggeredMulticastRoute': 'sendTriggeredMulticastRoute',
        'SetNextHop': 'setNextHop',
        'SetNextHopIpType': 'setNextHopIpType',
        'SourceAddressCount': 'sourceAddressCount',
        'SourceGroupMapping': 'sourceGroupMapping',
        'SourceMaskWidth': 'sourceMaskWidth',
        'StartGroupAddressIpv4': 'startGroupAddressIpv4',
        'StartSourceAddressIpv4': 'startSourceAddressIpv4',
        'StartSourceOrCrpAddressIpv4': 'startSourceOrCrpAddressIpv4',
        'SupportLeafADRoutesSending': 'supportLeafADRoutesSending',
        'WildCardLeafAdForBierPta': 'wildCardLeafAdForBierPta',
    }

    def __init__(self, parent):
        super(BgpMVpnReceiverSitesIpv4, self).__init__(parent)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        return EvpnIPv6PrefixRange(self)

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
    def BFRId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR-Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRId']))

    @property
    def BFRIpv4Prefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR IPv4 Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRIpv4Prefix']))

    @property
    def BFRIpv6Prefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR IPv6 Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRIpv6Prefix']))

    @property
    def BFRPrefixType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR Prefix Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRPrefixType']))

    @property
    def SubDomainId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub-Domain Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubDomainId']))

    @property
    def UseAutoSubDomainId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Auto Sub-Domain Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseAutoSubDomainId']))

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def CMulticastRouteType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-Multicast Route Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CMulticastRouteType']))

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
    def DownstreamLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Downstream Assigned Label in Leaf A-D route when tunnel type is Ingress Replication
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DownstreamLabel']))

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNextHop']))

    @property
    def GroupAddressCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddressCount']))

    @property
    def GroupMaskWidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Mask Width
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupMaskWidth']))

    @property
    def IncludeBierPtainLeafAd(self):
        """
        Returns
        -------
        - bool: Include Bier PTA in Leaf A-D
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeBierPtainLeafAd'])
    @IncludeBierPtainLeafAd.setter
    def IncludeBierPtainLeafAd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeBierPtainLeafAd'], value)

    @property
    def Ipv4NextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NextHop']))

    @property
    def Ipv6NextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NextHop']))

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
    def SendTriggeredMulticastRoute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send Triggered Multicast Route
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendTriggeredMulticastRoute']))

    @property
    def SetNextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetNextHop']))

    @property
    def SetNextHopIpType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetNextHopIpType']))

    @property
    def SourceAddressCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddressCount']))

    @property
    def SourceGroupMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Group Mapping
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceGroupMapping']))

    @property
    def SourceMaskWidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Mask Width
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceMaskWidth']))

    @property
    def StartGroupAddressIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartGroupAddressIpv4']))

    @property
    def StartSourceAddressIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start Source Address IPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartSourceAddressIpv4']))

    @property
    def StartSourceOrCrpAddressIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-RP Address IPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartSourceOrCrpAddressIpv4']))

    @property
    def SupportLeafADRoutesSending(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Leaf A-D Routes Sending
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportLeafADRoutesSending']))

    @property
    def WildCardLeafAdForBierPta(self):
        """
        Returns
        -------
        - bool: Wildcard Leaf A-D For Bier PTA
        """
        return self._get_attribute(self._SDM_ATT_MAP['WildCardLeafAdForBierPta'])
    @WildCardLeafAdForBierPta.setter
    def WildCardLeafAdForBierPta(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WildCardLeafAdForBierPta'], value)

    def update(self, IncludeBierPtainLeafAd=None, Name=None, WildCardLeafAdForBierPta=None):
        """Updates bgpMVpnReceiverSitesIpv4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - IncludeBierPtainLeafAd (bool): Include Bier PTA in Leaf A-D
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - WildCardLeafAdForBierPta (bool): Wildcard Leaf A-D For Bier PTA

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeBierPtainLeafAd=None, Name=None, WildCardLeafAdForBierPta=None):
        """Adds a new bgpMVpnReceiverSitesIpv4 resource on the server and adds it to the container.

        Args
        ----
        - IncludeBierPtainLeafAd (bool): Include Bier PTA in Leaf A-D
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - WildCardLeafAdForBierPta (bool): Wildcard Leaf A-D For Bier PTA

        Returns
        -------
        - self: This instance with all currently retrieved bgpMVpnReceiverSitesIpv4 resources using find and the newly added bgpMVpnReceiverSitesIpv4 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpMVpnReceiverSitesIpv4 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, IncludeBierPtainLeafAd=None, Name=None, WildCardLeafAdForBierPta=None):
        """Finds and retrieves bgpMVpnReceiverSitesIpv4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpMVpnReceiverSitesIpv4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpMVpnReceiverSitesIpv4 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - IncludeBierPtainLeafAd (bool): Include Bier PTA in Leaf A-D
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - WildCardLeafAdForBierPta (bool): Wildcard Leaf A-D For Bier PTA

        Returns
        -------
        - self: This instance with matching bgpMVpnReceiverSitesIpv4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpMVpnReceiverSitesIpv4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpMVpnReceiverSitesIpv4 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BFRId=None, BFRIpv4Prefix=None, BFRIpv6Prefix=None, BFRPrefixType=None, SubDomainId=None, UseAutoSubDomainId=None, Active=None, CMulticastRouteType=None, DownstreamLabel=None, EnableNextHop=None, GroupAddressCount=None, GroupMaskWidth=None, Ipv4NextHop=None, Ipv6NextHop=None, SendTriggeredMulticastRoute=None, SetNextHop=None, SetNextHopIpType=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddressIpv4=None, StartSourceAddressIpv4=None, StartSourceOrCrpAddressIpv4=None, SupportLeafADRoutesSending=None):
        """Base class infrastructure that gets a list of bgpMVpnReceiverSitesIpv4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BFRId (str): optional regex of BFRId
        - BFRIpv4Prefix (str): optional regex of BFRIpv4Prefix
        - BFRIpv6Prefix (str): optional regex of BFRIpv6Prefix
        - BFRPrefixType (str): optional regex of BFRPrefixType
        - SubDomainId (str): optional regex of SubDomainId
        - UseAutoSubDomainId (str): optional regex of UseAutoSubDomainId
        - Active (str): optional regex of active
        - CMulticastRouteType (str): optional regex of cMulticastRouteType
        - DownstreamLabel (str): optional regex of downstreamLabel
        - EnableNextHop (str): optional regex of enableNextHop
        - GroupAddressCount (str): optional regex of groupAddressCount
        - GroupMaskWidth (str): optional regex of groupMaskWidth
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - SendTriggeredMulticastRoute (str): optional regex of sendTriggeredMulticastRoute
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - SourceAddressCount (str): optional regex of sourceAddressCount
        - SourceGroupMapping (str): optional regex of sourceGroupMapping
        - SourceMaskWidth (str): optional regex of sourceMaskWidth
        - StartGroupAddressIpv4 (str): optional regex of startGroupAddressIpv4
        - StartSourceAddressIpv4 (str): optional regex of startSourceAddressIpv4
        - StartSourceOrCrpAddressIpv4 (str): optional regex of startSourceOrCrpAddressIpv4
        - SupportLeafADRoutesSending (str): optional regex of supportLeafADRoutesSending

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

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

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
