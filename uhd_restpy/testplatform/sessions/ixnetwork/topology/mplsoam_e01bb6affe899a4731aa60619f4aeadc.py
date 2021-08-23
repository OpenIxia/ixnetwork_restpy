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


class MplsOam(Base):
    """
    The MplsOam class encapsulates a list of mplsOam resources that are managed by the user.
    A list of resources can be retrieved from the server using the MplsOam.find() method.
    The list can be managed by using the MplsOam.add() and MplsOam.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'mplsOam'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BfdCvType': 'bfdCvType',
        'BfdDiscriminatorEnd': 'bfdDiscriminatorEnd',
        'BfdDiscriminatorStart': 'bfdDiscriminatorStart',
        'ConnectedVia': 'connectedVia',
        'ControlChannel': 'controlChannel',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestinationAddressIpv4': 'destinationAddressIpv4',
        'DownstreamAddressType': 'downstreamAddressType',
        'DownstreamInterfaceAddressNumbered': 'downstreamInterfaceAddressNumbered',
        'DownstreamInterfaceAddressUnnumbered': 'downstreamInterfaceAddressUnnumbered',
        'DownstreamIpAddress': 'downstreamIpAddress',
        'EchoRequestInterval': 'echoRequestInterval',
        'EchoResponseTimeout': 'echoResponseTimeout',
        'EnableDSIflag': 'enableDSIflag',
        'EnableDownstreamMappingTlv': 'enableDownstreamMappingTlv',
        'EnableDsNflag': 'enableDsNflag',
        'EnableFecValidation': 'enableFecValidation',
        'EnablePeriodicPing': 'enablePeriodicPing',
        'EnableSBfdResponder': 'enableSBfdResponder',
        'Errors': 'errors',
        'FlapTxIntervals': 'flapTxIntervals',
        'IncludePadTlv': 'includePadTlv',
        'IncludeVendorEnterpriseNumbeTlv': 'includeVendorEnterpriseNumbeTlv',
        'InitiatorSBFDSessionCount': 'initiatorSBFDSessionCount',
        'LocalRouterId': 'localRouterId',
        'MinRxInterval': 'minRxInterval',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'PadTlvFirstOctet': 'padTlvFirstOctet',
        'PadTlvLength': 'padTlvLength',
        'ReplyMode': 'replyMode',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TxInterval': 'txInterval',
        'VendorEnterpriseNumber': 'vendorEnterpriseNumber',
    }
    _SDM_ENUM_MAP = {
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(MplsOam, self).__init__(parent, list_op)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        if self._properties.get('LearnedInfo', None) is not None:
            return self._properties.get('LearnedInfo')
        else:
            return LearnedInfo(self)

    @property
    def LearnedInfoUpdate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_b6503122c0a4a58877467964920e27b5.LearnedInfoUpdate): An instance of the LearnedInfoUpdate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_b6503122c0a4a58877467964920e27b5 import LearnedInfoUpdate
        if self._properties.get('LearnedInfoUpdate', None) is not None:
            return self._properties.get('LearnedInfoUpdate')
        else:
            return LearnedInfoUpdate(self)

    @property
    def SbfdInitiator(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.sbfdinitiator_ef4ed37c4520e95225e35be31ea6dde4.SbfdInitiator): An instance of the SbfdInitiator class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.sbfdinitiator_ef4ed37c4520e95225e35be31ea6dde4 import SbfdInitiator
        if self._properties.get('SbfdInitiator', None) is not None:
            return self._properties.get('SbfdInitiator')
        else:
            return SbfdInitiator(self)._select()

    @property
    def SbfdResponder(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.sbfdresponder_e89a7c6cba0a1f66c71ecb217db4ccfd.SbfdResponder): An instance of the SbfdResponder class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.sbfdresponder_e89a7c6cba0a1f66c71ecb217db4ccfd import SbfdResponder
        if self._properties.get('SbfdResponder', None) is not None:
            return self._properties.get('SbfdResponder')
        else:
            return SbfdResponder(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def BfdCvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the BFD Connectivity Verification type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BfdCvType']))

    @property
    def BfdDiscriminatorEnd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the last BFD Discriminator value. This value should be greater than the BFD Discriminator Start value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BfdDiscriminatorEnd']))

    @property
    def BfdDiscriminatorStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the first BFD Discriminator value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BfdDiscriminatorStart']))

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def ControlChannel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the communication control channel
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ControlChannel']))

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
    def DestinationAddressIpv4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The destination IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationAddressIpv4']))

    @property
    def DownstreamAddressType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the address Type of the downstream traffic
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DownstreamAddressType']))

    @property
    def DownstreamInterfaceAddressNumbered(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the interface address of the downstream traffic in IPv4 format
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DownstreamInterfaceAddressNumbered']))

    @property
    def DownstreamInterfaceAddressUnnumbered(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the interface address of the downstream traffic
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DownstreamInterfaceAddressUnnumbered']))

    @property
    def DownstreamIpAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the IPv4/IPv6 address of the downstream traffic
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DownstreamIpAddress']))

    @property
    def EchoRequestInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the minimum interval, in milliseconds, between received Echo packets that this interface is capable of supporting
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoRequestInterval']))

    @property
    def EchoResponseTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the minimum timeout interval, in milliseconds, between received Echo packets
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoResponseTimeout']))

    @property
    def EnableDSIflag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the activation of the DS I Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDSIflag']))

    @property
    def EnableDownstreamMappingTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the enable of the downstream mapping TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDownstreamMappingTlv']))

    @property
    def EnableDsNflag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the activation of the DS N Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDsNflag']))

    @property
    def EnableFecValidation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Selection of the check box enables FEC validation
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFecValidation']))

    @property
    def EnablePeriodicPing(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If true, the router is pinged at regular intervals
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicPing']))

    @property
    def EnableSBfdResponder(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables S-BFD Responder
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSBfdResponder'])
    @EnableSBfdResponder.setter
    def EnableSBfdResponder(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableSBfdResponder'], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FlapTxIntervals(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the number of seconds between route flaps for BFD. A value of zero means no flapping
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapTxIntervals']))

    @property
    def IncludePadTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If true, includes Pad TLV in triggered ping
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludePadTlv']))

    @property
    def IncludeVendorEnterpriseNumbeTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If true, include the TLV number of the vendor, in triggered ping
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeVendorEnterpriseNumbeTlv']))

    @property
    def InitiatorSBFDSessionCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of configured S-BFD Initiator sessions with static MPLS labels per MPLS-OAM Interface. Labels should be configured as the actual label values (not SIDs) for SR-LSPs and should include list of labels learned by Ixia port and not the ones configured on the Tx Port itself.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitiatorSBFDSessionCount'])
    @InitiatorSBFDSessionCount.setter
    def InitiatorSBFDSessionCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InitiatorSBFDSessionCount'], value)

    @property
    def LocalRouterId(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The MPLOAM Router ID value, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

    @property
    def MinRxInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinRxInterval']))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

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
    def PadTlvFirstOctet(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the selection of the first octet of the Pad TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PadTlvFirstOctet']))

    @property
    def PadTlvLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the specification of the length of the Pad TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PadTlvLength']))

    @property
    def ReplyMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the selection of the mode of reply
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReplyMode']))

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
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
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def TimeoutMultiplier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the negotiated transmit interval, multiplied by this value, provides the detection time for the interface
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier']))

    @property
    def TxInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxInterval']))

    @property
    def VendorEnterpriseNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This signifies the specification of the enterprise number of the vendor
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VendorEnterpriseNumber']))

    def update(self, ConnectedVia=None, EnableSBfdResponder=None, InitiatorSBFDSessionCount=None, Multiplier=None, Name=None, StackedLayers=None):
        # type: (List[str], bool, int, int, str, List[str]) -> MplsOam
        """Updates mplsOam resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableSBfdResponder (bool): Enables S-BFD Responder
        - InitiatorSBFDSessionCount (number): Number of configured S-BFD Initiator sessions with static MPLS labels per MPLS-OAM Interface. Labels should be configured as the actual label values (not SIDs) for SR-LSPs and should include list of labels learned by Ixia port and not the ones configured on the Tx Port itself.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EnableSBfdResponder=None, InitiatorSBFDSessionCount=None, Multiplier=None, Name=None, StackedLayers=None):
        # type: (List[str], bool, int, int, str, List[str]) -> MplsOam
        """Adds a new mplsOam resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableSBfdResponder (bool): Enables S-BFD Responder
        - InitiatorSBFDSessionCount (number): Number of configured S-BFD Initiator sessions with static MPLS labels per MPLS-OAM Interface. Labels should be configured as the actual label values (not SIDs) for SR-LSPs and should include list of labels learned by Ixia port and not the ones configured on the Tx Port itself.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved mplsOam resources using find and the newly added mplsOam resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mplsOam resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EnableSBfdResponder=None, Errors=None, InitiatorSBFDSessionCount=None, LocalRouterId=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves mplsOam resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mplsOam resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mplsOam resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableSBfdResponder (bool): Enables S-BFD Responder
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - InitiatorSBFDSessionCount (number): Number of configured S-BFD Initiator sessions with static MPLS labels per MPLS-OAM Interface. Labels should be configured as the actual label values (not SIDs) for SR-LSPs and should include list of labels learned by Ixia port and not the ones configured on the Tx Port itself.
        - LocalRouterId (list(str)): The MPLOAM Router ID value, in IPv4 format.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching mplsOam resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mplsOam data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mplsOam resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def ClearAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearAllLearnedInfo operation on the server.

        Clears ALL Learned LSP Information By PCC Device.

        clearAllLearnedInfo(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
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
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def GetAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getAllLearnedInfo operation on the server.

        MPLSOAM learned Info

        getAllLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
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
        return self._execute('getAllLearnedInfo', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, DestinationAddressIpv4=None, DownstreamAddressType=None, DownstreamInterfaceAddressNumbered=None, DownstreamInterfaceAddressUnnumbered=None, DownstreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDSIflag=None, EnableDownstreamMappingTlv=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumbeTlv=None, MinRxInterval=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, TimeoutMultiplier=None, TxInterval=None, VendorEnterpriseNumber=None):
        """Base class infrastructure that gets a list of mplsOam device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BfdCvType (str): optional regex of bfdCvType
        - BfdDiscriminatorEnd (str): optional regex of bfdDiscriminatorEnd
        - BfdDiscriminatorStart (str): optional regex of bfdDiscriminatorStart
        - ControlChannel (str): optional regex of controlChannel
        - DestinationAddressIpv4 (str): optional regex of destinationAddressIpv4
        - DownstreamAddressType (str): optional regex of downstreamAddressType
        - DownstreamInterfaceAddressNumbered (str): optional regex of downstreamInterfaceAddressNumbered
        - DownstreamInterfaceAddressUnnumbered (str): optional regex of downstreamInterfaceAddressUnnumbered
        - DownstreamIpAddress (str): optional regex of downstreamIpAddress
        - EchoRequestInterval (str): optional regex of echoRequestInterval
        - EchoResponseTimeout (str): optional regex of echoResponseTimeout
        - EnableDSIflag (str): optional regex of enableDSIflag
        - EnableDownstreamMappingTlv (str): optional regex of enableDownstreamMappingTlv
        - EnableDsNflag (str): optional regex of enableDsNflag
        - EnableFecValidation (str): optional regex of enableFecValidation
        - EnablePeriodicPing (str): optional regex of enablePeriodicPing
        - FlapTxIntervals (str): optional regex of flapTxIntervals
        - IncludePadTlv (str): optional regex of includePadTlv
        - IncludeVendorEnterpriseNumbeTlv (str): optional regex of includeVendorEnterpriseNumbeTlv
        - MinRxInterval (str): optional regex of minRxInterval
        - PadTlvFirstOctet (str): optional regex of padTlvFirstOctet
        - PadTlvLength (str): optional regex of padTlvLength
        - ReplyMode (str): optional regex of replyMode
        - TimeoutMultiplier (str): optional regex of timeoutMultiplier
        - TxInterval (str): optional regex of txInterval
        - VendorEnterpriseNumber (str): optional regex of vendorEnterpriseNumber

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
