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


class Router(Base):
    """The router object represents a simulated router. In addition to some identifying options, it holds four lists for the router: (1) Advertise FEC Range-FECs to be advertised by the simulated router. (2)  Interfaces-router interface. (3) L2 VPN Interfaces-Layer 2 VPN interfaces used in establishing VPNs. (4) Explicit Include List-an optional list of IP FECs used to filter received FECs. This allows the simulated router to ignore all other FECs.
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def AdvFecRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advfecrange_50f11fb9eb8ad4bc46efad7d30a63633.AdvFecRange): An instance of the AdvFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advfecrange_50f11fb9eb8ad4bc46efad7d30a63633 import AdvFecRange
        return AdvFecRange(self)

    @property
    def IncludeIpFecRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.includeipfecrange_750dabbfe0009db3bf98162eea4c204f.IncludeIpFecRange): An instance of the IncludeIpFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.includeipfecrange_750dabbfe0009db3bf98162eea4c204f import IncludeIpFecRange
        return IncludeIpFecRange(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_847309e242b54314e1aa3949ea7dd4f1.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_847309e242b54314e1aa3949ea7dd4f1 import Interface
        return Interface(self)

    @property
    def L2Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2interface_2a8f8081f52d9fd29002b831306fb174.L2Interface): An instance of the L2Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2interface_2a8f8081f52d9fd29002b831306fb174 import L2Interface
        return L2Interface(self)

    @property
    def LearnedBgpAdVplsLabels(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbgpadvplslabels_108c1f9bcdd67c9d81b15d480ace9a80.LearnedBgpAdVplsLabels): An instance of the LearnedBgpAdVplsLabels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbgpadvplslabels_108c1f9bcdd67c9d81b15d480ace9a80 import LearnedBgpAdVplsLabels
        return LearnedBgpAdVplsLabels(self)

    @property
    def MulticastLeafRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastleafrange_abe2fac8e0af633b10c62244f4af9590.MulticastLeafRange): An instance of the MulticastLeafRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastleafrange_abe2fac8e0af633b10c62244f4af9590 import MulticastLeafRange
        return MulticastLeafRange(self)

    @property
    def MulticastRootRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastrootrange_e0141048589686ae12b6c24346c70f75.MulticastRootRange): An instance of the MulticastRootRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastrootrange_e0141048589686ae12b6c24346c70f75 import MulticastRootRange
        return MulticastRootRange(self)

    @property
    def ReqFecRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.reqfecrange_905da777a9209c53b5fa9272916aef18.ReqFecRange): An instance of the ReqFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.reqfecrange_905da777a9209c53b5fa9272916aef18 import ReqFecRange
        return ReqFecRange(self)

    @property
    def EnableBfdMplsLearnedLsp(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableBfdMplsLearnedLsp')
    @EnableBfdMplsLearnedLsp.setter
    def EnableBfdMplsLearnedLsp(self, value):
        self._set_attribute('enableBfdMplsLearnedLsp', value)

    @property
    def EnableFilterFec(self):
        """
        Returns
        -------
        - bool: Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        """
        return self._get_attribute('enableFilterFec')
    @EnableFilterFec.setter
    def EnableFilterFec(self, value):
        self._set_attribute('enableFilterFec', value)

    @property
    def EnableGracefulRestart(self):
        """
        Returns
        -------
        - bool: If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        """
        return self._get_attribute('enableGracefulRestart')
    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        self._set_attribute('enableGracefulRestart', value)

    @property
    def EnableLspPingLearnedLsp(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableLspPingLearnedLsp')
    @EnableLspPingLearnedLsp.setter
    def EnableLspPingLearnedLsp(self, value):
        self._set_attribute('enableLspPingLearnedLsp', value)

    @property
    def EnableOverrideRbit(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableOverrideRbit')
    @EnableOverrideRbit.setter
    def EnableOverrideRbit(self, value):
        self._set_attribute('enableOverrideRbit', value)

    @property
    def EnableP2mpCapabilty(self):
        """
        Returns
        -------
        - bool: If true, enables P2MP capability.
        """
        return self._get_attribute('enableP2mpCapabilty')
    @EnableP2mpCapabilty.setter
    def EnableP2mpCapabilty(self, value):
        self._set_attribute('enableP2mpCapabilty', value)

    @property
    def EnablePduRateControl(self):
        """
        Returns
        -------
        - bool: Enables the PDU Rate Control feature.
        """
        return self._get_attribute('enablePduRateControl')
    @EnablePduRateControl.setter
    def EnablePduRateControl(self, value):
        self._set_attribute('enablePduRateControl', value)

    @property
    def EnableVcFecs(self):
        """
        Returns
        -------
        - bool: Enables the use of Layer 2 Virtual Circuit FECs.
        """
        return self._get_attribute('enableVcFecs')
    @EnableVcFecs.setter
    def EnableVcFecs(self, value):
        self._set_attribute('enableVcFecs', value)

    @property
    def EnableVcGroupMatch(self):
        """
        Returns
        -------
        - bool: If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        """
        return self._get_attribute('enableVcGroupMatch')
    @EnableVcGroupMatch.setter
    def EnableVcGroupMatch(self, value):
        self._set_attribute('enableVcGroupMatch', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the simulated router.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def InterPduGap(self):
        """
        Returns
        -------
        - number: The user-specified gap time between PDUs, in milliseconds (ms).
        """
        return self._get_attribute('interPduGap')
    @InterPduGap.setter
    def InterPduGap(self, value):
        self._set_attribute('interPduGap', value)

    @property
    def IsBgpAdVplsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: Refreshes the AD VPLS Learned Info.
        """
        return self._get_attribute('isBgpAdVplsLearnedInfoRefreshed')

    @property
    def ReconnectTime(self):
        """
        Returns
        -------
        - number: This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        """
        return self._get_attribute('reconnectTime')
    @ReconnectTime.setter
    def ReconnectTime(self, value):
        self._set_attribute('reconnectTime', value)

    @property
    def RecoveryTime(self):
        """
        Returns
        -------
        - number: The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        """
        return self._get_attribute('recoveryTime')
    @RecoveryTime.setter
    def RecoveryTime(self, value):
        self._set_attribute('recoveryTime', value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: The ID of the simulated router, expressed as an IP address.
        """
        return self._get_attribute('routerId')
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute('routerId', value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute('trafficGroupId')
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute('trafficGroupId', value)

    @property
    def TransportAddress(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The string interface description for the transport address.
        """
        return self._get_attribute('transportAddress')
    @TransportAddress.setter
    def TransportAddress(self, value):
        self._set_attribute('transportAddress', value)

    @property
    def UseTransportAddress(self):
        """
        Returns
        -------
        - bool: The boolean value for the transport address.
        """
        return self._get_attribute('useTransportAddress')
    @UseTransportAddress.setter
    def UseTransportAddress(self, value):
        self._set_attribute('useTransportAddress', value)

    def update(self, EnableBfdMplsLearnedLsp=None, EnableFilterFec=None, EnableGracefulRestart=None, EnableLspPingLearnedLsp=None, EnableOverrideRbit=None, EnableP2mpCapabilty=None, EnablePduRateControl=None, EnableVcFecs=None, EnableVcGroupMatch=None, Enabled=None, InterPduGap=None, ReconnectTime=None, RecoveryTime=None, RouterId=None, TrafficGroupId=None, TransportAddress=None, UseTransportAddress=None):
        """Updates router resource on the server.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): NOT DEFINED
        - EnableFilterFec (bool): Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        - EnableGracefulRestart (bool): If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        - EnableLspPingLearnedLsp (bool): NOT DEFINED
        - EnableOverrideRbit (bool): NOT DEFINED
        - EnableP2mpCapabilty (bool): If true, enables P2MP capability.
        - EnablePduRateControl (bool): Enables the PDU Rate Control feature.
        - EnableVcFecs (bool): Enables the use of Layer 2 Virtual Circuit FECs.
        - EnableVcGroupMatch (bool): If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        - Enabled (bool): Enables or disables the simulated router.
        - InterPduGap (number): The user-specified gap time between PDUs, in milliseconds (ms).
        - ReconnectTime (number): This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        - RecoveryTime (number): The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        - RouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The string interface description for the transport address.
        - UseTransportAddress (bool): The boolean value for the transport address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, EnableBfdMplsLearnedLsp=None, EnableFilterFec=None, EnableGracefulRestart=None, EnableLspPingLearnedLsp=None, EnableOverrideRbit=None, EnableP2mpCapabilty=None, EnablePduRateControl=None, EnableVcFecs=None, EnableVcGroupMatch=None, Enabled=None, InterPduGap=None, ReconnectTime=None, RecoveryTime=None, RouterId=None, TrafficGroupId=None, TransportAddress=None, UseTransportAddress=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): NOT DEFINED
        - EnableFilterFec (bool): Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        - EnableGracefulRestart (bool): If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        - EnableLspPingLearnedLsp (bool): NOT DEFINED
        - EnableOverrideRbit (bool): NOT DEFINED
        - EnableP2mpCapabilty (bool): If true, enables P2MP capability.
        - EnablePduRateControl (bool): Enables the PDU Rate Control feature.
        - EnableVcFecs (bool): Enables the use of Layer 2 Virtual Circuit FECs.
        - EnableVcGroupMatch (bool): If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        - Enabled (bool): Enables or disables the simulated router.
        - InterPduGap (number): The user-specified gap time between PDUs, in milliseconds (ms).
        - ReconnectTime (number): This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        - RecoveryTime (number): The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        - RouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The string interface description for the transport address.
        - UseTransportAddress (bool): The boolean value for the transport address.

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableBfdMplsLearnedLsp=None, EnableFilterFec=None, EnableGracefulRestart=None, EnableLspPingLearnedLsp=None, EnableOverrideRbit=None, EnableP2mpCapabilty=None, EnablePduRateControl=None, EnableVcFecs=None, EnableVcGroupMatch=None, Enabled=None, InterPduGap=None, IsBgpAdVplsLearnedInfoRefreshed=None, ReconnectTime=None, RecoveryTime=None, RouterId=None, TrafficGroupId=None, TransportAddress=None, UseTransportAddress=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): NOT DEFINED
        - EnableFilterFec (bool): Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        - EnableGracefulRestart (bool): If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        - EnableLspPingLearnedLsp (bool): NOT DEFINED
        - EnableOverrideRbit (bool): NOT DEFINED
        - EnableP2mpCapabilty (bool): If true, enables P2MP capability.
        - EnablePduRateControl (bool): Enables the PDU Rate Control feature.
        - EnableVcFecs (bool): Enables the use of Layer 2 Virtual Circuit FECs.
        - EnableVcGroupMatch (bool): If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        - Enabled (bool): Enables or disables the simulated router.
        - InterPduGap (number): The user-specified gap time between PDUs, in milliseconds (ms).
        - IsBgpAdVplsLearnedInfoRefreshed (bool): Refreshes the AD VPLS Learned Info.
        - ReconnectTime (number): This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        - RecoveryTime (number): The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        - RouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The string interface description for the transport address.
        - UseTransportAddress (bool): The boolean value for the transport address.

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshBgpAdVplsLearnedInfo(self):
        """Executes the refreshBgpAdVplsLearnedInfo operation on the server.

        If enabled, it refreshes BGP advanced LSP learned information.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshBgpAdVplsLearnedInfo', payload=payload, response_object=None)
