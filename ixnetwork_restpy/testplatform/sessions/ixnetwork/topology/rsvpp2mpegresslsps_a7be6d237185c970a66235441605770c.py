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


class RsvpP2mpEgressLsps(Base):
    """RSVP-TE P2MP Tail (Egress) Tunnels
    The RsvpP2mpEgressLsps class encapsulates a required rsvpP2mpEgressLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvpP2mpEgressLsps'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestinationIpv4GroupAddress': 'destinationIpv4GroupAddress',
        'EnableFixedLabelForReservations': 'enableFixedLabelForReservations',
        'EndPointIpv6': 'endPointIpv6',
        'IncludeConnectedIpOnTop': 'includeConnectedIpOnTop',
        'IncludeLeafIpAtBottom': 'includeLeafIpAtBottom',
        'LabelValue': 'labelValue',
        'LocalIp': 'localIp',
        'Name': 'name',
        'NumberOfRroSubObjects': 'numberOfRroSubObjects',
        'P2mpIdAsNumber': 'p2mpIdAsNumber',
        'P2mpIdIp': 'p2mpIdIp',
        'ReflectRro': 'reflectRro',
        'RefreshInterval': 'refreshInterval',
        'ReservationStyle': 'reservationStyle',
        'SendAsRro': 'sendAsRro',
        'SendAsSrro': 'sendAsSrro',
        'SendReservationConfirmation': 'sendReservationConfirmation',
        'State': 'state',
        'SubLspsDown': 'subLspsDown',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TypeP2mpId': 'typeP2mpId',
    }

    def __init__(self, parent):
        super(RsvpP2mpEgressLsps, self).__init__(parent)

    @property
    def RsvpRroSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvprrosubobjectslist_b3619f826be3c6dc7d602fee61c4c981.RsvpRroSubObjectsList): An instance of the RsvpRroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvprrosubobjectslist_b3619f826be3c6dc7d602fee61c4c981 import RsvpRroSubObjectsList
        return RsvpRroSubObjectsList(self)

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
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
    def DestinationIpv4GroupAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination IPv4 Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationIpv4GroupAddress']))

    @property
    def EnableFixedLabelForReservations(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Fixed Label For Reservations
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFixedLabelForReservations']))

    @property
    def EndPointIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination IPv6 Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndPointIpv6']))

    @property
    def IncludeConnectedIpOnTop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include connected IP on top
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeConnectedIpOnTop']))

    @property
    def IncludeLeafIpAtBottom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Leaf IP at bottom
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeLeafIpAtBottom']))

    @property
    def LabelValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
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
    def P2mpIdAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P2MP ID displayed in Integer format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['P2mpIdAsNumber']))

    @property
    def P2mpIdIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P2MP ID displayed in IP Address format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['P2mpIdIp']))

    @property
    def ReflectRro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reflect RRO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReflectRro']))

    @property
    def RefreshInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Refresh Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RefreshInterval']))

    @property
    def ReservationStyle(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reservation Style
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservationStyle']))

    @property
    def SendAsRro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send As RRO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendAsRro']))

    @property
    def SendAsSrro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send As SRRO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendAsSrro']))

    @property
    def SendReservationConfirmation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send Reservation Confirmation
        """
        from ixnetwork_restpy.multivalue import Multivalue
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
    def SubLspsDown(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub LSPs Down
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubLspsDown']))

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout Multiplier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier']))

    @property
    def TypeP2mpId(self):
        """
        Returns
        -------
        - str(p2MPId | iP): P2MP ID Type
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeP2mpId'])
    @TypeP2mpId.setter
    def TypeP2mpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeP2mpId'], value)

    def update(self, Name=None, NumberOfRroSubObjects=None, TypeP2mpId=None):
        """Updates rsvpP2mpEgressLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfRroSubObjects (number): Number Of RRO Sub-Objects
        - TypeP2mpId (str(p2MPId | iP)): P2MP ID Type

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, DestinationIpv4GroupAddress=None, EnableFixedLabelForReservations=None, EndPointIpv6=None, IncludeConnectedIpOnTop=None, IncludeLeafIpAtBottom=None, LabelValue=None, P2mpIdAsNumber=None, P2mpIdIp=None, ReflectRro=None, RefreshInterval=None, ReservationStyle=None, SendAsRro=None, SendAsSrro=None, SendReservationConfirmation=None, SubLspsDown=None, TimeoutMultiplier=None):
        """Base class infrastructure that gets a list of rsvpP2mpEgressLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - DestinationIpv4GroupAddress (str): optional regex of destinationIpv4GroupAddress
        - EnableFixedLabelForReservations (str): optional regex of enableFixedLabelForReservations
        - EndPointIpv6 (str): optional regex of endPointIpv6
        - IncludeConnectedIpOnTop (str): optional regex of includeConnectedIpOnTop
        - IncludeLeafIpAtBottom (str): optional regex of includeLeafIpAtBottom
        - LabelValue (str): optional regex of labelValue
        - P2mpIdAsNumber (str): optional regex of p2mpIdAsNumber
        - P2mpIdIp (str): optional regex of p2mpIdIp
        - ReflectRro (str): optional regex of reflectRro
        - RefreshInterval (str): optional regex of refreshInterval
        - ReservationStyle (str): optional regex of reservationStyle
        - SendAsRro (str): optional regex of sendAsRro
        - SendAsSrro (str): optional regex of sendAsSrro
        - SendReservationConfirmation (str): optional regex of sendReservationConfirmation
        - SubLspsDown (str): optional regex of subLspsDown
        - TimeoutMultiplier (str): optional regex of timeoutMultiplier

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def GraftSubLsp(self, *args, **kwargs):
        """Executes the graftSubLsp operation on the server.

        Activate/Enable Tunnel selected SubLsp Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        graftSubLsp(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        graftSubLsp(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        graftSubLsp(Arg2=list)list
        --------------------------
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
        return self._execute('graftSubLsp', payload=payload, response_object=None)

    def PruneSubLsp(self, *args, **kwargs):
        """Executes the pruneSubLsp operation on the server.

        Deactivate/Disable selected Tunnel SubLsp Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pruneSubLsp(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        pruneSubLsp(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        pruneSubLsp(Arg2=list)list
        --------------------------
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
        return self._execute('pruneSubLsp', payload=payload, response_object=None)

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
