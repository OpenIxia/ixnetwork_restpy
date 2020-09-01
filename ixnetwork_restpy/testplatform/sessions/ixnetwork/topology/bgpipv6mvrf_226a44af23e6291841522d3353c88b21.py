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


class BgpIpv6MVrf(Base):
    """BGP IPv6 Peer mVRF Configuration
    The BgpIpv6MVrf class encapsulates a list of bgpIpv6MVrf resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpIpv6MVrf.find() method.
    The list can be managed by using the BgpIpv6MVrf.add() and BgpIpv6MVrf.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpIpv6MVrf'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DutIpv6': 'dutIpv6',
        'Errors': 'errors',
        'ImportRtListSameAsExportRtList': 'importRtListSameAsExportRtList',
        'IncludePmsiTunnelAttribute': 'includePmsiTunnelAttribute',
        'LocalIpv6': 'localIpv6',
        'LocalRouterID': 'localRouterID',
        'MulticastDistinguisherAs4Number': 'multicastDistinguisherAs4Number',
        'MulticastDistinguisherAsNumber': 'multicastDistinguisherAsNumber',
        'MulticastDistinguisherAssignedNumber': 'multicastDistinguisherAssignedNumber',
        'MulticastDistinguisherIpAddress': 'multicastDistinguisherIpAddress',
        'MulticastDistinguisherType': 'multicastDistinguisherType',
        'MulticastTunnelType': 'multicastTunnelType',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumRtInExportRouteTargetList': 'numRtInExportRouteTargetList',
        'NumRtInImportRouteTargetList': 'numRtInImportRouteTargetList',
        'NumRtInUmhExportRouteTargetList': 'numRtInUmhExportRouteTargetList',
        'NumRtInUmhImportRouteTargetList': 'numRtInUmhImportRouteTargetList',
        'RootAddress': 'rootAddress',
        'RsvpP2mpId': 'rsvpP2mpId',
        'RsvpP2mpIdAsNumber': 'rsvpP2mpIdAsNumber',
        'RsvpTunnelId': 'rsvpTunnelId',
        'SameAsExportRT': 'sameAsExportRT',
        'SameAsImportRT': 'sameAsImportRT',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'UpOrDownStreamAssignedLabel': 'upOrDownStreamAssignedLabel',
        'UseUpOrDownStreamAssigneLabel': 'useUpOrDownStreamAssigneLabel',
    }

    def __init__(self, parent):
        super(BgpIpv6MVrf, self).__init__(parent)

    @property
    def BgpExportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist_ce93ce056c01eaf7643c31a7fd67768c.BgpExportRouteTargetList): An instance of the BgpExportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist_ce93ce056c01eaf7643c31a7fd67768c import BgpExportRouteTargetList
        return BgpExportRouteTargetList(self)

    @property
    def BgpImportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist_99470595cc13238e15b19c07b8af6021.BgpImportRouteTargetList): An instance of the BgpImportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist_99470595cc13238e15b19c07b8af6021 import BgpImportRouteTargetList
        return BgpImportRouteTargetList(self)

    @property
    def BgpUmhExportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhexportroutetargetlist_536e8a485efae5ffcda5cfc4f848255b.BgpUmhExportRouteTargetList): An instance of the BgpUmhExportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhexportroutetargetlist_536e8a485efae5ffcda5cfc4f848255b import BgpUmhExportRouteTargetList
        return BgpUmhExportRouteTargetList(self)

    @property
    def BgpUmhImportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhimportroutetargetlist_02ef98778defb99b99d0de435c533ff0.BgpUmhImportRouteTargetList): An instance of the BgpUmhImportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhimportroutetargetlist_02ef98778defb99b99d0de435c533ff0 import BgpUmhImportRouteTargetList
        return BgpUmhImportRouteTargetList(self)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

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
    def DutIpv6(self):
        """
        Returns
        -------
        - list(str): DUT IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutIpv6'])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def ImportRtListSameAsExportRtList(self):
        """
        Returns
        -------
        - bool: Import RT List Same As Export RT List
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImportRtListSameAsExportRtList'])
    @ImportRtListSameAsExportRtList.setter
    def ImportRtListSameAsExportRtList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImportRtListSameAsExportRtList'], value)

    @property
    def IncludePmsiTunnelAttribute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include PMSI Tunnel Attribute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludePmsiTunnelAttribute']))

    @property
    def LocalIpv6(self):
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIpv6'])

    @property
    def LocalRouterID(self):
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterID'])

    @property
    def MulticastDistinguisherAs4Number(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VMulticast Distinguisher AS4 Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastDistinguisherAs4Number']))

    @property
    def MulticastDistinguisherAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VMulticast Distinguisher AS Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastDistinguisherAsNumber']))

    @property
    def MulticastDistinguisherAssignedNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Distinguisher Assigned Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastDistinguisherAssignedNumber']))

    @property
    def MulticastDistinguisherIpAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Distinguisher IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastDistinguisherIpAddress']))

    @property
    def MulticastDistinguisherType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Distinguisher Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastDistinguisherType']))

    @property
    def MulticastTunnelType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Tunnel Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastTunnelType']))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

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
    def NumRtInExportRouteTargetList(self):
        """
        Returns
        -------
        - number: Number of RTs in Export Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumRtInExportRouteTargetList'])
    @NumRtInExportRouteTargetList.setter
    def NumRtInExportRouteTargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumRtInExportRouteTargetList'], value)

    @property
    def NumRtInImportRouteTargetList(self):
        """
        Returns
        -------
        - number: Number of RTs in Import Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumRtInImportRouteTargetList'])
    @NumRtInImportRouteTargetList.setter
    def NumRtInImportRouteTargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumRtInImportRouteTargetList'], value)

    @property
    def NumRtInUmhExportRouteTargetList(self):
        """
        Returns
        -------
        - number: Number of RTs in Export Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumRtInUmhExportRouteTargetList'])
    @NumRtInUmhExportRouteTargetList.setter
    def NumRtInUmhExportRouteTargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumRtInUmhExportRouteTargetList'], value)

    @property
    def NumRtInUmhImportRouteTargetList(self):
        """
        Returns
        -------
        - number: Number of RTs in Import Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumRtInUmhImportRouteTargetList'])
    @NumRtInUmhImportRouteTargetList.setter
    def NumRtInUmhImportRouteTargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumRtInUmhImportRouteTargetList'], value)

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
    def SameAsExportRT(self):
        """
        Returns
        -------
        - bool: Same As Export RT Attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP['SameAsExportRT'])
    @SameAsExportRT.setter
    def SameAsExportRT(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SameAsExportRT'], value)

    @property
    def SameAsImportRT(self):
        """
        Returns
        -------
        - bool: Same As Import RT Attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP['SameAsImportRT'])
    @SameAsImportRT.setter
    def SameAsImportRT(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SameAsImportRT'], value)

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def UpOrDownStreamAssignedLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upstream/Downstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UpOrDownStreamAssignedLabel']))

    @property
    def UseUpOrDownStreamAssigneLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Upstream/Downstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseUpOrDownStreamAssigneLabel']))

    def update(self, ConnectedVia=None, ImportRtListSameAsExportRtList=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, SameAsExportRT=None, SameAsImportRT=None, StackedLayers=None):
        """Updates bgpIpv6MVrf resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - SameAsExportRT (bool): Same As Export RT Attribute
        - SameAsImportRT (bool): Same As Import RT Attribute
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, ImportRtListSameAsExportRtList=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, SameAsExportRT=None, SameAsImportRT=None, StackedLayers=None):
        """Adds a new bgpIpv6MVrf resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - SameAsExportRT (bool): Same As Export RT Attribute
        - SameAsImportRT (bool): Same As Import RT Attribute
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved bgpIpv6MVrf resources using find and the newly added bgpIpv6MVrf resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpIpv6MVrf resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, DutIpv6=None, Errors=None, ImportRtListSameAsExportRtList=None, LocalIpv6=None, LocalRouterID=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, SameAsExportRT=None, SameAsImportRT=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves bgpIpv6MVrf resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpIpv6MVrf resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpIpv6MVrf resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DutIpv6 (list(str)): DUT IP
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - LocalIpv6 (list(str)): Local IP
        - LocalRouterID (list(str)): Router ID
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - SameAsExportRT (bool): Same As Export RT Attribute
        - SameAsImportRT (bool): Same As Import RT Attribute
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching bgpIpv6MVrf resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpIpv6MVrf data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpIpv6MVrf resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, IncludePmsiTunnelAttribute=None, MulticastDistinguisherAs4Number=None, MulticastDistinguisherAsNumber=None, MulticastDistinguisherAssignedNumber=None, MulticastDistinguisherIpAddress=None, MulticastDistinguisherType=None, MulticastTunnelType=None, RootAddress=None, RsvpP2mpId=None, RsvpP2mpIdAsNumber=None, RsvpTunnelId=None, UpOrDownStreamAssignedLabel=None, UseUpOrDownStreamAssigneLabel=None):
        """Base class infrastructure that gets a list of bgpIpv6MVrf device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - IncludePmsiTunnelAttribute (str): optional regex of includePmsiTunnelAttribute
        - MulticastDistinguisherAs4Number (str): optional regex of multicastDistinguisherAs4Number
        - MulticastDistinguisherAsNumber (str): optional regex of multicastDistinguisherAsNumber
        - MulticastDistinguisherAssignedNumber (str): optional regex of multicastDistinguisherAssignedNumber
        - MulticastDistinguisherIpAddress (str): optional regex of multicastDistinguisherIpAddress
        - MulticastDistinguisherType (str): optional regex of multicastDistinguisherType
        - MulticastTunnelType (str): optional regex of multicastTunnelType
        - RootAddress (str): optional regex of rootAddress
        - RsvpP2mpId (str): optional regex of rsvpP2mpId
        - RsvpP2mpIdAsNumber (str): optional regex of rsvpP2mpIdAsNumber
        - RsvpTunnelId (str): optional regex of rsvpTunnelId
        - UpOrDownStreamAssignedLabel (str): optional regex of upOrDownStreamAssignedLabel
        - UseUpOrDownStreamAssigneLabel (str): optional regex of useUpOrDownStreamAssigneLabel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
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
        return self._execute('abort', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

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
