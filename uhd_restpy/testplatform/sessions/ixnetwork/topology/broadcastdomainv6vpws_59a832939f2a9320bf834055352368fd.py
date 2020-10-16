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


class BroadcastDomainV6Vpws(Base):
    """BGP V6 Broadcast Domain Configuration
    The BroadcastDomainV6Vpws class encapsulates a required broadcastDomainV6Vpws resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'broadcastDomainV6Vpws'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdRouteLabel': 'adRouteLabel',
        'AdvSrv6SidInIgp': 'advSrv6SidInIgp',
        'AdvertiseSRv6SID': 'advertiseSRv6SID',
        'ArgumentLength': 'argumentLength',
        'BVlanId': 'bVlanId',
        'BVlanPriority': 'bVlanPriority',
        'BVlanTpid': 'bVlanTpid',
        'BackupFlag': 'backupFlag',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableVlanAwareService': 'enableVlanAwareService',
        'EthernetTagId': 'ethernetTagId',
        'FunctionLength': 'functionLength',
        'FxcType': 'fxcType',
        'GroupAddress': 'groupAddress',
        'IncludeVpwsL2AttrExtComm': 'includeVpwsL2AttrExtComm',
        'L2Mtu': 'l2Mtu',
        'LocBlockLength': 'locBlockLength',
        'LocNodeLength': 'locNodeLength',
        'MvEnableTransposition': 'mvEnableTransposition',
        'MvIncSrv6SidStructSsTlv': 'mvIncSrv6SidStructSsTlv',
        'Name': 'name',
        'NoOfMacPools': 'noOfMacPools',
        'PrimaryPE': 'primaryPE',
        'RemoteServiceId': 'remoteServiceId',
        'RequireCW': 'requireCW',
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
        'TranpositionLength': 'tranpositionLength',
        'TranpositionOffset': 'tranpositionOffset',
        'UsebVlan': 'usebVlan',
        'VidNormalization': 'vidNormalization',
    }

    def __init__(self, parent):
        super(BroadcastDomainV6Vpws, self).__init__(parent)

    @property
    def PnTLVList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57.PnTLVList): An instance of the PnTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57 import PnTLVList
        return PnTLVList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdRouteLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AD Route Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdRouteLabel']))

    @property
    def AdvSrv6SidInIgp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise SRv6 SID in IGP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvSrv6SidInIgp']))

    @property
    def AdvertiseSRv6SID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise SRv6 SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseSRv6SID']))

    @property
    def ArgumentLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Argument Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ArgumentLength']))

    @property
    def BVlanId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B VLAN ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BVlanId']))

    @property
    def BVlanPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B VLAN Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BVlanPriority']))

    @property
    def BVlanTpid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B VLAN TPID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BVlanTpid']))

    @property
    def BackupFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Backup Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupFlag']))

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
        - obj(uhd_restpy.multivalue.Multivalue): Enable VLAN Aware Service
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableVlanAwareService']))

    @property
    def EthernetTagId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Ethernet Tag ID. For VPWS, this acts as VPWS Service ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EthernetTagId']))

    @property
    def FunctionLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Function Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FunctionLength']))

    @property
    def FxcType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): FXC Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FxcType']))

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddress']))

    @property
    def IncludeVpwsL2AttrExtComm(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include VPWS Layer 2 Attributes Extended Community
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeVpwsL2AttrExtComm']))

    @property
    def L2Mtu(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): L2 MTU
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['L2Mtu']))

    @property
    def LocBlockLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Block Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocBlockLength']))

    @property
    def LocNodeLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Node Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocNodeLength']))

    @property
    def MvEnableTransposition(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Transposition
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvEnableTransposition']))

    @property
    def MvIncSrv6SidStructSsTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include SRv6 SID Structure Sub-Sub TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvIncSrv6SidStructSsTlv']))

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
    def PrimaryPE(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Primary PE
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrimaryPE']))

    @property
    def RemoteServiceId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Remote Service ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteServiceId']))

    @property
    def RequireCW(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Require CW
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RequireCW']))

    @property
    def RootAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Root Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddress']))

    @property
    def RsvpP2mpId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RSVP P2MP ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpId']))

    @property
    def RsvpP2mpIdAsNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RSVP P2MP ID as Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpIdAsNumber']))

    @property
    def RsvpTunnelId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RSVP Tunnel ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvpTunnelId']))

    @property
    def SendSRv6SIDOptionalInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If we need to advertise SRv6 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendSRv6SIDOptionalInfo']))

    @property
    def SenderAddressPRootNodeAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SenderAddressPRootNodeAddress']))

    @property
    def Srv6EndpointBehavior(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 Endpoint Behavior field Value for all routes in this Route Range
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6EndpointBehavior']))

    @property
    def Srv6SIDOptionalInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SIDOptionalInformation']))

    @property
    def Srv6SidFlags(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Flags Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidFlags']))

    @property
    def Srv6SidLoc(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID. It consists of Locator, Func and Args
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLoc']))

    @property
    def Srv6SidLocLen(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Locator Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLocLen']))

    @property
    def Srv6SidLocMetric(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Locator Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLocMetric']))

    @property
    def Srv6SidReserved(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved']))

    @property
    def Srv6SidReserved1(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Reserved1 Field for Service Information sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved1']))

    @property
    def Srv6SidReserved2(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Reserved2 Field for Service Information sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved2']))

    @property
    def TranpositionLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Transposition Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TranpositionLength']))

    @property
    def TranpositionOffset(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Transposition Offset
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TranpositionOffset']))

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

    @property
    def VidNormalization(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VID Normalization
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VidNormalization']))

    def update(self, Name=None, NoOfMacPools=None, UsebVlan=None):
        """Updates broadcastDomainV6Vpws resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, AdRouteLabel=None, AdvSrv6SidInIgp=None, AdvertiseSRv6SID=None, ArgumentLength=None, BVlanId=None, BVlanPriority=None, BVlanTpid=None, BackupFlag=None, EnableVlanAwareService=None, EthernetTagId=None, FunctionLength=None, FxcType=None, GroupAddress=None, IncludeVpwsL2AttrExtComm=None, L2Mtu=None, LocBlockLength=None, LocNodeLength=None, MvEnableTransposition=None, MvIncSrv6SidStructSsTlv=None, PrimaryPE=None, RemoteServiceId=None, RequireCW=None, RootAddress=None, RsvpP2mpId=None, RsvpP2mpIdAsNumber=None, RsvpTunnelId=None, SendSRv6SIDOptionalInfo=None, SenderAddressPRootNodeAddress=None, Srv6EndpointBehavior=None, Srv6SIDOptionalInformation=None, Srv6SidFlags=None, Srv6SidLoc=None, Srv6SidLocLen=None, Srv6SidLocMetric=None, Srv6SidReserved=None, Srv6SidReserved1=None, Srv6SidReserved2=None, TranpositionLength=None, TranpositionOffset=None, VidNormalization=None):
        """Base class infrastructure that gets a list of broadcastDomainV6Vpws device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdRouteLabel (str): optional regex of adRouteLabel
        - AdvSrv6SidInIgp (str): optional regex of advSrv6SidInIgp
        - AdvertiseSRv6SID (str): optional regex of advertiseSRv6SID
        - ArgumentLength (str): optional regex of argumentLength
        - BVlanId (str): optional regex of bVlanId
        - BVlanPriority (str): optional regex of bVlanPriority
        - BVlanTpid (str): optional regex of bVlanTpid
        - BackupFlag (str): optional regex of backupFlag
        - EnableVlanAwareService (str): optional regex of enableVlanAwareService
        - EthernetTagId (str): optional regex of ethernetTagId
        - FunctionLength (str): optional regex of functionLength
        - FxcType (str): optional regex of fxcType
        - GroupAddress (str): optional regex of groupAddress
        - IncludeVpwsL2AttrExtComm (str): optional regex of includeVpwsL2AttrExtComm
        - L2Mtu (str): optional regex of l2Mtu
        - LocBlockLength (str): optional regex of locBlockLength
        - LocNodeLength (str): optional regex of locNodeLength
        - MvEnableTransposition (str): optional regex of mvEnableTransposition
        - MvIncSrv6SidStructSsTlv (str): optional regex of mvIncSrv6SidStructSsTlv
        - PrimaryPE (str): optional regex of primaryPE
        - RemoteServiceId (str): optional regex of remoteServiceId
        - RequireCW (str): optional regex of requireCW
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
        - TranpositionLength (str): optional regex of tranpositionLength
        - TranpositionOffset (str): optional regex of tranpositionOffset
        - VidNormalization (str): optional regex of vidNormalization

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
