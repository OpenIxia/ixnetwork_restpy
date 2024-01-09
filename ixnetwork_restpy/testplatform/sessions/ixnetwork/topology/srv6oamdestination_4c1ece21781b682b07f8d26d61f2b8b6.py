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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Srv6OamDestination(Base):
    """SRv6 Destination Address
    The Srv6OamDestination class encapsulates a required srv6OamDestination resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "srv6OamDestination"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AutoGenSegmentLeftValue": "autoGenSegmentLeftValue",
        "BfdDiscriminator": "bfdDiscriminator",
        "BfdEchoInterval": "bfdEchoInterval",
        "BfdEnCtrlPlaneIndependent": "bfdEnCtrlPlaneIndependent",
        "BfdEnPeerDiscriminatorLearned": "bfdEnPeerDiscriminatorLearned",
        "BfdHopLimit": "bfdHopLimit",
        "BfdMinRxInterval": "bfdMinRxInterval",
        "BfdMode": "bfdMode",
        "BfdPeerDiscriminator": "bfdPeerDiscriminator",
        "BfdSessionInfo": "bfdSessionInfo",
        "BfdTimeoutMultiplier": "bfdTimeoutMultiplier",
        "BfdTxInterval": "bfdTxInterval",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnReducedSRH": "enReducedSRH",
        "EnableBfd": "enableBfd",
        "EnableSBfdInitiator": "enableSBfdInitiator",
        "MaxTtlForTR": "maxTtlForTR",
        "MyDiscriminator": "myDiscriminator",
        "Name": "name",
        "NumPingRequest": "numPingRequest",
        "NumSegments": "numSegments",
        "OFlag": "oFlag",
        "PayloadLen": "payloadLen",
        "PeerDiscriminator": "peerDiscriminator",
        "PingInterval": "pingInterval",
        "PingTriggerType": "pingTriggerType",
        "ResponseTimeout": "responseTimeout",
        "SegmentLeftValue": "segmentLeftValue",
        "SessionInfo": "sessionInfo",
        "SiIndex": "siIndex",
        "Srv6DestAddress": "srv6DestAddress",
        "Srv6DstName": "srv6DstName",
        "TimeoutMultiplier": "timeoutMultiplier",
        "Ttl": "ttl",
        "TxCfgSrcAddrFlag": "txCfgSrcAddrFlag",
        "TxInterval": "txInterval",
        "TxSrcAddr": "txSrcAddr",
        "UseGSRv6SI": "useGSRv6SI",
        "ValidateDestination": "validateDestination",
    }
    _SDM_ENUM_MAP = {
        "pingTriggerType": ["singlePing", "periodicPing", "continuosPing"],
    }

    def __init__(self, parent, list_op=False):
        super(Srv6OamDestination, self).__init__(parent, list_op)

    @property
    def Srv6oamSegmentNode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamsegmentnode_d3b3fcd80f1d1cbaba726b72e946acc7.Srv6oamSegmentNode): An instance of the Srv6oamSegmentNode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamsegmentnode_d3b3fcd80f1d1cbaba726b72e946acc7 import (
            Srv6oamSegmentNode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Srv6oamSegmentNode", None) is not None:
                return self._properties.get("Srv6oamSegmentNode")
        return Srv6oamSegmentNode(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AutoGenSegmentLeftValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled then Segment Left field value will be auto generated.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoGenSegmentLeftValue"])
        )

    @property
    def BfdDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be used for My Discriminator in BFD packets sent by this BFD session.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BfdDiscriminator"])
        )

    @property
    def BfdEchoInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Echo Interval in Milli Seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BfdEchoInterval"])
        )

    @property
    def BfdEnCtrlPlaneIndependent(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it enables the Control Plane Independent flag BFD packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BfdEnCtrlPlaneIndependent"])
        )

    @property
    def BfdEnPeerDiscriminatorLearned(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it enables BFD session to learn peer discriminator.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BfdEnPeerDiscriminatorLearned"]),
        )

    @property
    def BfdHopLimit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hop Limit to be set in IPv6 header in BFD packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BfdHopLimit"]))

    @property
    def BfdMinRxInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The minimum interval, in milliseconds, between received BFD packets that this session is capable of supporting.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BfdMinRxInterval"])
        )

    @property
    def BfdMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mode of BFD session.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BfdMode"]))

    @property
    def BfdPeerDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be used for Your Discriminator in BFD packets sent by this BFD session.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BfdPeerDiscriminator"])
        )

    @property
    def BfdSessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[adminDown | down | errorDupDisc | up]): Current state of the BFD Session.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BfdSessionInfo"])

    @property
    def BfdTimeoutMultiplier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If reply packets are not recieved within Timeout Multiplier times Negotiated Transmit Interval, then session is brought down and Flap Count is increased in statistics.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BfdTimeoutMultiplier"])
        )

    @property
    def BfdTxInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The minimum inter, in milliseconds, thst the session would like to use when transmitting BFD packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BfdTxInterval"]))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def EnReducedSRH(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If Enabled the First Segment will not be added to SRH. If Enabled and Number of Segments are 0 then no SRH header i.e Best Effort case.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnReducedSRH"]))

    @property
    def EnableBfd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it enables the BFD.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBfd"]))

    @property
    def EnableSBfdInitiator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it enables the S-BFD Initiator.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSBfdInitiator"])
        )

    @property
    def MaxTtlForTR(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum TTL for Trace Route request packets. Once hop count reaches max ttl, it will be considered destination unreachable and no further requests sent.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxTtlForTR"]))

    @property
    def MyDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be used for My Discriminator in S-BFD packets sent to the Responder by this Initiator. Should be unique in sessions from a single Initiator.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MyDiscriminator"])
        )

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NumPingRequest(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Mention number of ping request message to send.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumPingRequest"])

    @NumPingRequest.setter
    def NumPingRequest(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumPingRequest"], value)

    @property
    def NumSegments(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Total Number Segments/Trasit addresses present to reach destination. This count is excluding the actual Destination Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumSegments"])

    @NumSegments.setter
    def NumSegments(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumSegments"], value)

    @property
    def OFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): O-flag in Segment Routing Header.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OFlag"]))

    @property
    def PayloadLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ICMPv6/UDP payload length, min 0 and max 8900 bytes. Message size must be less than or equal to MTU size including payload.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PayloadLen"]))

    @property
    def PeerDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configured Peer Discriminator which should match the configured Local or My Discriminator on the target Responder.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PeerDiscriminator"])
        )

    @property
    def PingInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Delay between each ping request message in ms.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PingInterval"])

    @PingInterval.setter
    def PingInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PingInterval"], value)

    @property
    def PingTriggerType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(singlePing | periodicPing | continuosPing): Select Single or Periodic or Continuous Ping Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PingTriggerType"])

    @PingTriggerType.setter
    def PingTriggerType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PingTriggerType"], value)

    @property
    def ResponseTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Threshold time for Response for Request packets. After this Timeout, it will be treated as Ping Failure.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ResponseTimeout"])
        )

    @property
    def SegmentLeftValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment Left value to be used in SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentLeftValue"])
        )

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[adminDown | down | up]): Current state of the S-BFD Initiator Session. It is normally Up or Down depending on whether Responder is responding correctly or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionInfo"])

    @property
    def SiIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment Index to be filled in argument field of IPv6 Destination Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SiIndex"]))

    @property
    def Srv6DestAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination address to be used for ping/SBFD request.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6DestAddress"])
        )

    @property
    def Srv6DstName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination Address Name For Reference.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6DstName"]))

    @property
    def TimeoutMultiplier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If reply packets are not recieved within Timeout Multiplier times Negotiated Transmit Interval, then session is brought down and Flap Count is increased in statistics.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeoutMultiplier"])
        )

    @property
    def Ttl(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TTL to be used in IPv6 Header for Ping Packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ttl"]))

    @property
    def TxCfgSrcAddrFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, configured Source Address will be considered as Source Address of Ipv6. If Disabled, Source Address of IPv6 will be taken from the Interface on which this destination is learned (emulated/loopback interfaces).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TxCfgSrcAddrFlag"])
        )

    @property
    def TxInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tx Interval in Milli Seconds. Initial transmission interval is set to maximum of 1 second and configured Tx Interval. Once session comes up, the timer auto-transitions to the negotiated value, that is maximum of local Tx Interval and recieved Rx Interval from Responder.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TxInterval"]))

    @property
    def TxSrcAddr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Source address to be used in Ping Requests.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TxSrcAddr"]))

    @property
    def UseGSRv6SI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use G SRv6 SI in SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UseGSRv6SI"]))

    @property
    def ValidateDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If Enabled, then Ping/SBFD request will be sent only if this destination is learned either from IGP (ISIS/OSPFv2/v3) or BGP. If Disabled, then Ping/SBFD request will be sent for this destination without failure even if it is not learnt from IGP/BGP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidateDestination"])

    @ValidateDestination.setter
    def ValidateDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ValidateDestination"], value)

    def update(
        self,
        Name=None,
        NumPingRequest=None,
        NumSegments=None,
        PingInterval=None,
        PingTriggerType=None,
        ValidateDestination=None,
    ):
        # type: (str, int, int, int, str, bool) -> Srv6OamDestination
        """Updates srv6OamDestination resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumPingRequest (number): Mention number of ping request message to send.
        - NumSegments (number): Total Number Segments/Trasit addresses present to reach destination. This count is excluding the actual Destination Address.
        - PingInterval (number): Delay between each ping request message in ms.
        - PingTriggerType (str(singlePing | periodicPing | continuosPing)): Select Single or Periodic or Continuous Ping Type.
        - ValidateDestination (bool): If Enabled, then Ping/SBFD request will be sent only if this destination is learned either from IGP (ISIS/OSPFv2/v3) or BGP. If Disabled, then Ping/SBFD request will be sent for this destination without failure even if it is not learnt from IGP/BGP.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BfdSessionInfo=None,
        Count=None,
        DescriptiveName=None,
        Name=None,
        NumPingRequest=None,
        NumSegments=None,
        PingInterval=None,
        PingTriggerType=None,
        SessionInfo=None,
        ValidateDestination=None,
    ):
        # type: (List[str], int, str, str, int, int, int, str, List[str], bool) -> Srv6OamDestination
        """Finds and retrieves srv6OamDestination resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve srv6OamDestination resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all srv6OamDestination resources from the server.

        Args
        ----
        - BfdSessionInfo (list(str[adminDown | down | errorDupDisc | up])): Current state of the BFD Session.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumPingRequest (number): Mention number of ping request message to send.
        - NumSegments (number): Total Number Segments/Trasit addresses present to reach destination. This count is excluding the actual Destination Address.
        - PingInterval (number): Delay between each ping request message in ms.
        - PingTriggerType (str(singlePing | periodicPing | continuosPing)): Select Single or Periodic or Continuous Ping Type.
        - SessionInfo (list(str[adminDown | down | up])): Current state of the S-BFD Initiator Session. It is normally Up or Down depending on whether Responder is responding correctly or not.
        - ValidateDestination (bool): If Enabled, then Ping/SBFD request will be sent only if this destination is learned either from IGP (ISIS/OSPFv2/v3) or BGP. If Disabled, then Ping/SBFD request will be sent for this destination without failure even if it is not learnt from IGP/BGP.

        Returns
        -------
        - self: This instance with matching srv6OamDestination resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of srv6OamDestination data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the srv6OamDestination resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearAllLearnedInfo", payload=payload, response_object=None
        )

    def GetBfdSessionLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getBfdSessionLearnedInfo operation on the server.

        Fetch BFD Session Learned Information.

        getBfdSessionLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getBfdSessionLearnedInfo", payload=payload, response_object=None
        )

    def GetPeriodicOrContLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPeriodicOrContLearnedInfo operation on the server.

        Fetch periodic or continuos learned Info

        getPeriodicOrContLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getPeriodicOrContLearnedInfo", payload=payload, response_object=None
        )

    def GetSbfdInitiatorLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getSbfdInitiatorLearnedInfo operation on the server.

        Fetch SBFD Initiator Learned Information.

        getSbfdInitiatorLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getSbfdInitiatorLearnedInfo", payload=payload, response_object=None
        )

    def SendPingRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendPingRequest operation on the server.

        Trigger to send ping request message.

        sendPingRequest(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("sendPingRequest", payload=payload, response_object=None)

    def SendTraceRouteRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendTraceRouteRequest operation on the server.

        Trigger to send trace route request message.

        sendTraceRouteRequest(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "sendTraceRouteRequest", payload=payload, response_object=None
        )

    def StartBfd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the startBfd operation on the server.

        Trigger to start sending BFD packets.

        startBfd(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("startBfd", payload=payload, response_object=None)

    def StartSbfd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the startSbfd operation on the server.

        Trigger to start sending S-BFD initiator message.

        startSbfd(Arg2=list, async_operation=bool)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("startSbfd", payload=payload, response_object=None)

    def StopBfd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopBfd operation on the server.

        Trigger to stop sending BFD packets.

        stopBfd(Arg2=list, async_operation=bool)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopBfd", payload=payload, response_object=None)

    def StopPing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopPing operation on the server.

        Trigger to stop ping request message.

        stopPing(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopPing", payload=payload, response_object=None)

    def StopSbfd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopSbfd operation on the server.

        Trigger to stop sending S-BFD initiator message.

        stopSbfd(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopSbfd", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AutoGenSegmentLeftValue=None,
        BfdDiscriminator=None,
        BfdEchoInterval=None,
        BfdEnCtrlPlaneIndependent=None,
        BfdEnPeerDiscriminatorLearned=None,
        BfdHopLimit=None,
        BfdMinRxInterval=None,
        BfdMode=None,
        BfdPeerDiscriminator=None,
        BfdTimeoutMultiplier=None,
        BfdTxInterval=None,
        EnReducedSRH=None,
        EnableBfd=None,
        EnableSBfdInitiator=None,
        MaxTtlForTR=None,
        MyDiscriminator=None,
        OFlag=None,
        PayloadLen=None,
        PeerDiscriminator=None,
        ResponseTimeout=None,
        SegmentLeftValue=None,
        SiIndex=None,
        Srv6DestAddress=None,
        Srv6DstName=None,
        TimeoutMultiplier=None,
        Ttl=None,
        TxCfgSrcAddrFlag=None,
        TxInterval=None,
        TxSrcAddr=None,
        UseGSRv6SI=None,
    ):
        """Base class infrastructure that gets a list of srv6OamDestination device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AutoGenSegmentLeftValue (str): optional regex of autoGenSegmentLeftValue
        - BfdDiscriminator (str): optional regex of bfdDiscriminator
        - BfdEchoInterval (str): optional regex of bfdEchoInterval
        - BfdEnCtrlPlaneIndependent (str): optional regex of bfdEnCtrlPlaneIndependent
        - BfdEnPeerDiscriminatorLearned (str): optional regex of bfdEnPeerDiscriminatorLearned
        - BfdHopLimit (str): optional regex of bfdHopLimit
        - BfdMinRxInterval (str): optional regex of bfdMinRxInterval
        - BfdMode (str): optional regex of bfdMode
        - BfdPeerDiscriminator (str): optional regex of bfdPeerDiscriminator
        - BfdTimeoutMultiplier (str): optional regex of bfdTimeoutMultiplier
        - BfdTxInterval (str): optional regex of bfdTxInterval
        - EnReducedSRH (str): optional regex of enReducedSRH
        - EnableBfd (str): optional regex of enableBfd
        - EnableSBfdInitiator (str): optional regex of enableSBfdInitiator
        - MaxTtlForTR (str): optional regex of maxTtlForTR
        - MyDiscriminator (str): optional regex of myDiscriminator
        - OFlag (str): optional regex of oFlag
        - PayloadLen (str): optional regex of payloadLen
        - PeerDiscriminator (str): optional regex of peerDiscriminator
        - ResponseTimeout (str): optional regex of responseTimeout
        - SegmentLeftValue (str): optional regex of segmentLeftValue
        - SiIndex (str): optional regex of siIndex
        - Srv6DestAddress (str): optional regex of srv6DestAddress
        - Srv6DstName (str): optional regex of srv6DstName
        - TimeoutMultiplier (str): optional regex of timeoutMultiplier
        - Ttl (str): optional regex of ttl
        - TxCfgSrcAddrFlag (str): optional regex of txCfgSrcAddrFlag
        - TxInterval (str): optional regex of txInterval
        - TxSrcAddr (str): optional regex of txSrcAddr
        - UseGSRv6SI (str): optional regex of useGSRv6SI

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
