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


class Link(Base):
    """This object holds the LACP link configuration.
    The Link class encapsulates a list of link resources that are managed by the user.
    A list of resources can be retrieved from the server using the Link.find() method.
    The list can be managed by using the Link.add() and Link.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'link'
    _SDM_ATT_MAP = {
        'ActorKey': 'actorKey',
        'ActorPortNumber': 'actorPortNumber',
        'ActorPortPriority': 'actorPortPriority',
        'ActorSystemId': 'actorSystemId',
        'ActorSystemPriority': 'actorSystemPriority',
        'AdministrativeKey': 'administrativeKey',
        'AggregationFlagState': 'aggregationFlagState',
        'AutoPickPortMac': 'autoPickPortMac',
        'CollectingFlag': 'collectingFlag',
        'CollectorMaxDelay': 'collectorMaxDelay',
        'DistributingFlag': 'distributingFlag',
        'Enabled': 'enabled',
        'InterMarkerPduDelay': 'interMarkerPduDelay',
        'LacpActivity': 'lacpActivity',
        'LacpTimeout': 'lacpTimeout',
        'LacpduPeriodicTimeInterval': 'lacpduPeriodicTimeInterval',
        'MarkerRequestMode': 'markerRequestMode',
        'MarkerResponseWaitTime': 'markerResponseWaitTime',
        'PortMac': 'portMac',
        'SendMarkerRequestOnLagChange': 'sendMarkerRequestOnLagChange',
        'SendPeriodicMarkerRequest': 'sendPeriodicMarkerRequest',
        'SupportRespondingToMarker': 'supportRespondingToMarker',
        'SyncFlag': 'syncFlag',
        'UpdateRequired': 'updateRequired',
    }

    def __init__(self, parent):
        super(Link, self).__init__(parent)

    @property
    def ActorKey(self):
        """
        Returns
        -------
        - number: The operational Key value assigned to the port by the Actor. This is a 2 byte field with a default of 1. Minimum value is 0, maximum value is 65535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorKey'])
    @ActorKey.setter
    def ActorKey(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorKey'], value)

    @property
    def ActorPortNumber(self):
        """
        Returns
        -------
        - number: The port number assigned to the port by the Actor (the System sending the PDU). It is a 2 byte field with a default of 1. Min: 0, Max: 65535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorPortNumber'])
    @ActorPortNumber.setter
    def ActorPortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorPortNumber'], value)

    @property
    def ActorPortPriority(self):
        """
        Returns
        -------
        - number: This field specifies the port priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorPortPriority'])
    @ActorPortPriority.setter
    def ActorPortPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorPortPriority'], value)

    @property
    def ActorSystemId(self):
        """
        Returns
        -------
        - str: This field specifies the system identifier for the link Actor. It is a 6 byte field, with a default of 00-00-00-00-00-01. Min: 00-00-00-00-00-00, Max: FF-FF-FF-FF-FF-FF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorSystemId'])
    @ActorSystemId.setter
    def ActorSystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorSystemId'], value)

    @property
    def ActorSystemPriority(self):
        """
        Returns
        -------
        - number: This field specifies the system priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorSystemPriority'])
    @ActorSystemPriority.setter
    def ActorSystemPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActorSystemPriority'], value)

    @property
    def AdministrativeKey(self):
        """
        Returns
        -------
        - number: This field controls the aggregation of ports of the same system with similar Actor Key.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdministrativeKey'])
    @AdministrativeKey.setter
    def AdministrativeKey(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdministrativeKey'], value)

    @property
    def AggregationFlagState(self):
        """
        Returns
        -------
        - str(disable | auto): If enabled, sets the port status to automatically allow aggregation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregationFlagState'])
    @AggregationFlagState.setter
    def AggregationFlagState(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregationFlagState'], value)

    @property
    def AutoPickPortMac(self):
        """
        Returns
        -------
        - bool: If true the source MAC is the interface MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoPickPortMac'])
    @AutoPickPortMac.setter
    def AutoPickPortMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoPickPortMac'], value)

    @property
    def CollectingFlag(self):
        """
        Returns
        -------
        - bool: If true, the actor port state Collecting is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent
        """
        return self._get_attribute(self._SDM_ATT_MAP['CollectingFlag'])
    @CollectingFlag.setter
    def CollectingFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CollectingFlag'], value)

    @property
    def CollectorMaxDelay(self):
        """
        Returns
        -------
        - number: The maximum time in microseconds that the Frame Collector may delay the delivery of a frame received from an Aggregator to its MAC client. This is a 2 byte field with a default 0. Min: 0, Max: 65535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CollectorMaxDelay'])
    @CollectorMaxDelay.setter
    def CollectorMaxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CollectorMaxDelay'], value)

    @property
    def DistributingFlag(self):
        """
        Returns
        -------
        - bool: If true, the actor port state Distributing is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DistributingFlag'])
    @DistributingFlag.setter
    def DistributingFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DistributingFlag'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the link is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterMarkerPduDelay(self):
        """
        Returns
        -------
        - str: The time gap in seconds between two consecutive Marker PDUs when transmitted periodically.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterMarkerPduDelay'])
    @InterMarkerPduDelay.setter
    def InterMarkerPduDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterMarkerPduDelay'], value)

    @property
    def LacpActivity(self):
        """
        Returns
        -------
        - str(active | passive): Sets the value of LACPs Actor activity, either passive or active.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacpActivity'])
    @LacpActivity.setter
    def LacpActivity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacpActivity'], value)

    @property
    def LacpTimeout(self):
        """
        Returns
        -------
        - number: This timer is used to detect whether received protocol information has expired. The user can provide a custom value from 1 to 65535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacpTimeout'])
    @LacpTimeout.setter
    def LacpTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacpTimeout'], value)

    @property
    def LacpduPeriodicTimeInterval(self):
        """
        Returns
        -------
        - number: This field defines how frequently LACPDUs are sent to the link partner. The user can provide a custom values from 1 to 65535, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacpduPeriodicTimeInterval'])
    @LacpduPeriodicTimeInterval.setter
    def LacpduPeriodicTimeInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacpduPeriodicTimeInterval'], value)

    @property
    def MarkerRequestMode(self):
        """
        Returns
        -------
        - str(fixed | random): Sets the marker request mode for the Actor link.In either case, the mode parameters are specified in Marker Request Frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MarkerRequestMode'])
    @MarkerRequestMode.setter
    def MarkerRequestMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MarkerRequestMode'], value)

    @property
    def MarkerResponseWaitTime(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for Marker Response after sending a Marker Request. After this time, the Marker Response Timeout Count is incremented. If a marker response does arrive for the request after this timeout, it is not considered as a legitimate response.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MarkerResponseWaitTime'])
    @MarkerResponseWaitTime.setter
    def MarkerResponseWaitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MarkerResponseWaitTime'], value)

    @property
    def PortMac(self):
        """
        Returns
        -------
        - str: specifies the port MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortMac'])
    @PortMac.setter
    def PortMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortMac'], value)

    @property
    def SendMarkerRequestOnLagChange(self):
        """
        Returns
        -------
        - bool: If true, this checkbox causes LACP to send a Marker PDU on the following situations: 1) System Priority has been modified; 2) System Id has been modified; 3) Actor Key has been modified; 4) Port Number/Port Priority has been modified while we are in Individual mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendMarkerRequestOnLagChange'])
    @SendMarkerRequestOnLagChange.setter
    def SendMarkerRequestOnLagChange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendMarkerRequestOnLagChange'], value)

    @property
    def SendPeriodicMarkerRequest(self):
        """
        Returns
        -------
        - bool: If true, Marker Request PDUs are periodically after both actor and partner are IN SYNC and our state is aggregated. The moment we come out of this state, the periodic sending of Marker will be stopped.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendPeriodicMarkerRequest'])
    @SendPeriodicMarkerRequest.setter
    def SendPeriodicMarkerRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendPeriodicMarkerRequest'], value)

    @property
    def SupportRespondingToMarker(self):
        """
        Returns
        -------
        - bool: If true, LACP doesn't respond to MARKER request PDUs from the partner.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportRespondingToMarker'])
    @SupportRespondingToMarker.setter
    def SupportRespondingToMarker(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportRespondingToMarker'], value)

    @property
    def SyncFlag(self):
        """
        Returns
        -------
        - str(disable | auto): If enabled, the actor port state is set to True based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SyncFlag'])
    @SyncFlag.setter
    def SyncFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SyncFlag'], value)

    @property
    def UpdateRequired(self):
        """
        Returns
        -------
        - bool: (read only) If true, an update LAPDU is required for the link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateRequired'])

    def update(self, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, AutoPickPortMac=None, CollectingFlag=None, CollectorMaxDelay=None, DistributingFlag=None, Enabled=None, InterMarkerPduDelay=None, LacpActivity=None, LacpTimeout=None, LacpduPeriodicTimeInterval=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, PortMac=None, SendMarkerRequestOnLagChange=None, SendPeriodicMarkerRequest=None, SupportRespondingToMarker=None, SyncFlag=None):
        """Updates link resource on the server.

        Args
        ----
        - ActorKey (number): The operational Key value assigned to the port by the Actor. This is a 2 byte field with a default of 1. Minimum value is 0, maximum value is 65535.
        - ActorPortNumber (number): The port number assigned to the port by the Actor (the System sending the PDU). It is a 2 byte field with a default of 1. Min: 0, Max: 65535.
        - ActorPortPriority (number): This field specifies the port priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        - ActorSystemId (str): This field specifies the system identifier for the link Actor. It is a 6 byte field, with a default of 00-00-00-00-00-01. Min: 00-00-00-00-00-00, Max: FF-FF-FF-FF-FF-FF.
        - ActorSystemPriority (number): This field specifies the system priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        - AdministrativeKey (number): This field controls the aggregation of ports of the same system with similar Actor Key.
        - AggregationFlagState (str(disable | auto)): If enabled, sets the port status to automatically allow aggregation.
        - AutoPickPortMac (bool): If true the source MAC is the interface MAC address.
        - CollectingFlag (bool): If true, the actor port state Collecting is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent
        - CollectorMaxDelay (number): The maximum time in microseconds that the Frame Collector may delay the delivery of a frame received from an Aggregator to its MAC client. This is a 2 byte field with a default 0. Min: 0, Max: 65535.
        - DistributingFlag (bool): If true, the actor port state Distributing is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.
        - Enabled (bool): If true, the link is enabled.
        - InterMarkerPduDelay (str): The time gap in seconds between two consecutive Marker PDUs when transmitted periodically.
        - LacpActivity (str(active | passive)): Sets the value of LACPs Actor activity, either passive or active.
        - LacpTimeout (number): This timer is used to detect whether received protocol information has expired. The user can provide a custom value from 1 to 65535.
        - LacpduPeriodicTimeInterval (number): This field defines how frequently LACPDUs are sent to the link partner. The user can provide a custom values from 1 to 65535, in seconds
        - MarkerRequestMode (str(fixed | random)): Sets the marker request mode for the Actor link.In either case, the mode parameters are specified in Marker Request Frequency.
        - MarkerResponseWaitTime (number): The number of seconds to wait for Marker Response after sending a Marker Request. After this time, the Marker Response Timeout Count is incremented. If a marker response does arrive for the request after this timeout, it is not considered as a legitimate response.
        - PortMac (str): specifies the port MAC address.
        - SendMarkerRequestOnLagChange (bool): If true, this checkbox causes LACP to send a Marker PDU on the following situations: 1) System Priority has been modified; 2) System Id has been modified; 3) Actor Key has been modified; 4) Port Number/Port Priority has been modified while we are in Individual mode.
        - SendPeriodicMarkerRequest (bool): If true, Marker Request PDUs are periodically after both actor and partner are IN SYNC and our state is aggregated. The moment we come out of this state, the periodic sending of Marker will be stopped.
        - SupportRespondingToMarker (bool): If true, LACP doesn't respond to MARKER request PDUs from the partner.
        - SyncFlag (str(disable | auto)): If enabled, the actor port state is set to True based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, AutoPickPortMac=None, CollectingFlag=None, CollectorMaxDelay=None, DistributingFlag=None, Enabled=None, InterMarkerPduDelay=None, LacpActivity=None, LacpTimeout=None, LacpduPeriodicTimeInterval=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, PortMac=None, SendMarkerRequestOnLagChange=None, SendPeriodicMarkerRequest=None, SupportRespondingToMarker=None, SyncFlag=None):
        """Adds a new link resource on the server and adds it to the container.

        Args
        ----
        - ActorKey (number): The operational Key value assigned to the port by the Actor. This is a 2 byte field with a default of 1. Minimum value is 0, maximum value is 65535.
        - ActorPortNumber (number): The port number assigned to the port by the Actor (the System sending the PDU). It is a 2 byte field with a default of 1. Min: 0, Max: 65535.
        - ActorPortPriority (number): This field specifies the port priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        - ActorSystemId (str): This field specifies the system identifier for the link Actor. It is a 6 byte field, with a default of 00-00-00-00-00-01. Min: 00-00-00-00-00-00, Max: FF-FF-FF-FF-FF-FF.
        - ActorSystemPriority (number): This field specifies the system priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        - AdministrativeKey (number): This field controls the aggregation of ports of the same system with similar Actor Key.
        - AggregationFlagState (str(disable | auto)): If enabled, sets the port status to automatically allow aggregation.
        - AutoPickPortMac (bool): If true the source MAC is the interface MAC address.
        - CollectingFlag (bool): If true, the actor port state Collecting is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent
        - CollectorMaxDelay (number): The maximum time in microseconds that the Frame Collector may delay the delivery of a frame received from an Aggregator to its MAC client. This is a 2 byte field with a default 0. Min: 0, Max: 65535.
        - DistributingFlag (bool): If true, the actor port state Distributing is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.
        - Enabled (bool): If true, the link is enabled.
        - InterMarkerPduDelay (str): The time gap in seconds between two consecutive Marker PDUs when transmitted periodically.
        - LacpActivity (str(active | passive)): Sets the value of LACPs Actor activity, either passive or active.
        - LacpTimeout (number): This timer is used to detect whether received protocol information has expired. The user can provide a custom value from 1 to 65535.
        - LacpduPeriodicTimeInterval (number): This field defines how frequently LACPDUs are sent to the link partner. The user can provide a custom values from 1 to 65535, in seconds
        - MarkerRequestMode (str(fixed | random)): Sets the marker request mode for the Actor link.In either case, the mode parameters are specified in Marker Request Frequency.
        - MarkerResponseWaitTime (number): The number of seconds to wait for Marker Response after sending a Marker Request. After this time, the Marker Response Timeout Count is incremented. If a marker response does arrive for the request after this timeout, it is not considered as a legitimate response.
        - PortMac (str): specifies the port MAC address.
        - SendMarkerRequestOnLagChange (bool): If true, this checkbox causes LACP to send a Marker PDU on the following situations: 1) System Priority has been modified; 2) System Id has been modified; 3) Actor Key has been modified; 4) Port Number/Port Priority has been modified while we are in Individual mode.
        - SendPeriodicMarkerRequest (bool): If true, Marker Request PDUs are periodically after both actor and partner are IN SYNC and our state is aggregated. The moment we come out of this state, the periodic sending of Marker will be stopped.
        - SupportRespondingToMarker (bool): If true, LACP doesn't respond to MARKER request PDUs from the partner.
        - SyncFlag (str(disable | auto)): If enabled, the actor port state is set to True based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.

        Returns
        -------
        - self: This instance with all currently retrieved link resources using find and the newly added link resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained link resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, AutoPickPortMac=None, CollectingFlag=None, CollectorMaxDelay=None, DistributingFlag=None, Enabled=None, InterMarkerPduDelay=None, LacpActivity=None, LacpTimeout=None, LacpduPeriodicTimeInterval=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, PortMac=None, SendMarkerRequestOnLagChange=None, SendPeriodicMarkerRequest=None, SupportRespondingToMarker=None, SyncFlag=None, UpdateRequired=None):
        """Finds and retrieves link resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve link resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all link resources from the server.

        Args
        ----
        - ActorKey (number): The operational Key value assigned to the port by the Actor. This is a 2 byte field with a default of 1. Minimum value is 0, maximum value is 65535.
        - ActorPortNumber (number): The port number assigned to the port by the Actor (the System sending the PDU). It is a 2 byte field with a default of 1. Min: 0, Max: 65535.
        - ActorPortPriority (number): This field specifies the port priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        - ActorSystemId (str): This field specifies the system identifier for the link Actor. It is a 6 byte field, with a default of 00-00-00-00-00-01. Min: 00-00-00-00-00-00, Max: FF-FF-FF-FF-FF-FF.
        - ActorSystemPriority (number): This field specifies the system priority of the link Actor. It is a 2 byte field, with a default or 1. Min: 0, Max: 65535.
        - AdministrativeKey (number): This field controls the aggregation of ports of the same system with similar Actor Key.
        - AggregationFlagState (str(disable | auto)): If enabled, sets the port status to automatically allow aggregation.
        - AutoPickPortMac (bool): If true the source MAC is the interface MAC address.
        - CollectingFlag (bool): If true, the actor port state Collecting is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent
        - CollectorMaxDelay (number): The maximum time in microseconds that the Frame Collector may delay the delivery of a frame received from an Aggregator to its MAC client. This is a 2 byte field with a default 0. Min: 0, Max: 65535.
        - DistributingFlag (bool): If true, the actor port state Distributing is set to true based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.
        - Enabled (bool): If true, the link is enabled.
        - InterMarkerPduDelay (str): The time gap in seconds between two consecutive Marker PDUs when transmitted periodically.
        - LacpActivity (str(active | passive)): Sets the value of LACPs Actor activity, either passive or active.
        - LacpTimeout (number): This timer is used to detect whether received protocol information has expired. The user can provide a custom value from 1 to 65535.
        - LacpduPeriodicTimeInterval (number): This field defines how frequently LACPDUs are sent to the link partner. The user can provide a custom values from 1 to 65535, in seconds
        - MarkerRequestMode (str(fixed | random)): Sets the marker request mode for the Actor link.In either case, the mode parameters are specified in Marker Request Frequency.
        - MarkerResponseWaitTime (number): The number of seconds to wait for Marker Response after sending a Marker Request. After this time, the Marker Response Timeout Count is incremented. If a marker response does arrive for the request after this timeout, it is not considered as a legitimate response.
        - PortMac (str): specifies the port MAC address.
        - SendMarkerRequestOnLagChange (bool): If true, this checkbox causes LACP to send a Marker PDU on the following situations: 1) System Priority has been modified; 2) System Id has been modified; 3) Actor Key has been modified; 4) Port Number/Port Priority has been modified while we are in Individual mode.
        - SendPeriodicMarkerRequest (bool): If true, Marker Request PDUs are periodically after both actor and partner are IN SYNC and our state is aggregated. The moment we come out of this state, the periodic sending of Marker will be stopped.
        - SupportRespondingToMarker (bool): If true, LACP doesn't respond to MARKER request PDUs from the partner.
        - SyncFlag (str(disable | auto)): If enabled, the actor port state is set to True based on Tx and Rx state machines. Otherwise, the flag in LACPDU remains reset for all packets sent.
        - UpdateRequired (bool): (read only) If true, an update LAPDU is required for the link.

        Returns
        -------
        - self: This instance with matching link resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of link data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the link resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
