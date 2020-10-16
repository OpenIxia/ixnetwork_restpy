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


class RsvpP2PEgressLsps(Base):
    """RSVP-TE p2p Tail (Egress) LSPs
    The RsvpP2PEgressLsps class encapsulates a required rsvpP2PEgressLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvpP2PEgressLsps'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableFixedLabelForReservations': 'enableFixedLabelForReservations',
        'EnableReplyingLspPing': 'enableReplyingLspPing',
        'EndPointIpv6': 'endPointIpv6',
        'ForwardLspSelfPing': 'forwardLspSelfPing',
        'InitialLspSelfPingDropCount': 'initialLspSelfPingDropCount',
        'IpTTLDecrementCount': 'ipTTLDecrementCount',
        'LabelValue': 'labelValue',
        'LocalIp': 'localIp',
        'LspSelfPingIPDSCP': 'lspSelfPingIPDSCP',
        'Name': 'name',
        'NumberOfRroSubObjects': 'numberOfRroSubObjects',
        'ReflectRro': 'reflectRro',
        'RefreshInterval': 'refreshInterval',
        'ReservationStyle': 'reservationStyle',
        'RetainLspSelfPingDSCP': 'retainLspSelfPingDSCP',
        'SendReservationConfirmation': 'sendReservationConfirmation',
        'State': 'state',
        'TimeoutMultiplier': 'timeoutMultiplier',
    }

    def __init__(self, parent):
        super(RsvpP2PEgressLsps, self).__init__(parent)

    @property
    def RsvpRROSubObjectsList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.rsvprrosubobjectslist_77057ceebebb20e47d2ca898582fad61.RsvpRROSubObjectsList): An instance of the RsvpRROSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.rsvprrosubobjectslist_77057ceebebb20e47d2ca898582fad61 import RsvpRROSubObjectsList
        return RsvpRROSubObjectsList(self)

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
        return Tag(self)

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
    def EnableFixedLabelForReservations(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Fixed Label For Reservations
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFixedLabelForReservations']))

    @property
    def EnableReplyingLspPing(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Replying To Lsp Ping
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableReplyingLspPing']))

    @property
    def EndPointIpv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination IPv6
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndPointIpv6']))

    @property
    def ForwardLspSelfPing(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Forward LSP Self Ping
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ForwardLspSelfPing']))

    @property
    def InitialLspSelfPingDropCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Initial LSP Self Ping Drop Count. Number of times Egress LSP will drop LSP Self Ping Message before forwarding it back.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitialLspSelfPingDropCount']))

    @property
    def IpTTLDecrementCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IP TTL Decrement Count. IP TTL limits the lifespan or lifetime of IP Packet in a network.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpTTLDecrementCount']))

    @property
    def LabelValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Label Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelValue']))

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def LspSelfPingIPDSCP(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): LSP Self Ping IP DSCP. IP DSCP classifies the way an IP packet is routed in a network.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspSelfPingIPDSCP']))

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
    def ReflectRro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reflect RRO
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReflectRro']))

    @property
    def RefreshInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Refresh Interval (ms)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RefreshInterval']))

    @property
    def ReservationStyle(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reservation Style
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservationStyle']))

    @property
    def RetainLspSelfPingDSCP(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Retain LSP Self Ping DSCP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RetainLspSelfPingDSCP']))

    @property
    def SendReservationConfirmation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Send Reservation Confirmation
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendReservationConfirmation']))

    @property
    def State(self):
        """
        Returns
        -------
        - list(str[down | none | notStarted | up]): State
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Timeout Multiplier
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier']))

    def update(self, Name=None, NumberOfRroSubObjects=None):
        """Updates rsvpP2PEgressLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfRroSubObjects (number): Number Of RRO Sub-Objects

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, EnableFixedLabelForReservations=None, EnableReplyingLspPing=None, EndPointIpv6=None, ForwardLspSelfPing=None, InitialLspSelfPingDropCount=None, IpTTLDecrementCount=None, LabelValue=None, LspSelfPingIPDSCP=None, ReflectRro=None, RefreshInterval=None, ReservationStyle=None, RetainLspSelfPingDSCP=None, SendReservationConfirmation=None, TimeoutMultiplier=None):
        """Base class infrastructure that gets a list of rsvpP2PEgressLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableFixedLabelForReservations (str): optional regex of enableFixedLabelForReservations
        - EnableReplyingLspPing (str): optional regex of enableReplyingLspPing
        - EndPointIpv6 (str): optional regex of endPointIpv6
        - ForwardLspSelfPing (str): optional regex of forwardLspSelfPing
        - InitialLspSelfPingDropCount (str): optional regex of initialLspSelfPingDropCount
        - IpTTLDecrementCount (str): optional regex of ipTTLDecrementCount
        - LabelValue (str): optional regex of labelValue
        - LspSelfPingIPDSCP (str): optional regex of lspSelfPingIPDSCP
        - ReflectRro (str): optional regex of reflectRro
        - RefreshInterval (str): optional regex of refreshInterval
        - ReservationStyle (str): optional regex of reservationStyle
        - RetainLspSelfPingDSCP (str): optional regex of retainLspSelfPingDSCP
        - SendReservationConfirmation (str): optional regex of sendReservationConfirmation
        - TimeoutMultiplier (str): optional regex of timeoutMultiplier

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Activate/Enable selected Tunnel Tail Ranges

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

        Deactivate/Disable selected Tunnel Tail Ranges

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
