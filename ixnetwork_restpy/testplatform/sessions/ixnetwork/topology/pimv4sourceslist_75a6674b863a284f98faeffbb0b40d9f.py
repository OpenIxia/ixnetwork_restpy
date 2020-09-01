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


class PimV4SourcesList(Base):
    """PIMv4 Sources Data
    The PimV4SourcesList class encapsulates a required pimV4SourcesList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pimV4SourcesList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DiscardSgJoinStates': 'discardSgJoinStates',
        'GroupAddress': 'groupAddress',
        'GroupCount': 'groupCount',
        'LocalRouterId': 'localRouterId',
        'MulticastDataLength': 'multicastDataLength',
        'Name': 'name',
        'RegisterProbeTime': 'registerProbeTime',
        'RpAddress': 'rpAddress',
        'SendNullRegAtBegin': 'sendNullRegAtBegin',
        'SourceAddress': 'sourceAddress',
        'SourceCount': 'sourceCount',
        'Status': 'status',
        'SupressionTime': 'supressionTime',
        'SwitchOverInterval': 'switchOverInterval',
        'TxIterationGap': 'txIterationGap',
        'UdpDestinationPort': 'udpDestinationPort',
        'UdpSourcePort': 'udpSourcePort',
    }

    def __init__(self, parent):
        super(PimV4SourcesList, self).__init__(parent)

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
    def DiscardSgJoinStates(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Learned Join States sent by the RP (DUT) in response to this specific Register Message will be discarded-and will not be displayed in the table of the Register Range window.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DiscardSgJoinStates']))

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The first IPv4 multicast group address in the range of group addresses included in this Register message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddress']))

    @property
    def GroupCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of group addresses to be included in this register message
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupCount']))

    @property
    def LocalRouterId(self):
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

    @property
    def MulticastDataLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (in bytes) This field indicates the length of the UDP packet (the payload) within the IPv4 packet that is encapsulated in the PIM-SM Register Message sent from the DR to the DUT. The default is 64 bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastDataLength']))

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
    def RegisterProbeTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (In seconds) Part of the Register-Stop Timer (RST (S,G). Used to control the time intervals for the transmission of Null-Register messages from the Source's DR to the RP. Prior to expiration of the Register Suppression Time of the RST, a Null-Register message is sent to probe the RP, as a reminder to the RP to send a new Register-Stop message and maintain the state. If the RP does not respond with a new Register-Stop message, the Source's DR will start sending Register-encapsulated data again. The default is 5 seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RegisterProbeTime']))

    @property
    def RpAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the Rendezvous Point (RP) router-the root of the RPT (Rendezvous Point Tree).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RpAddress']))

    @property
    def SendNullRegAtBegin(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, a Null Register packet will be sent by the Ixia-emulated Designated Router (DR)/Source Range to the RP to start the message exchange. (A Null Register packet contains no data.) Regardless of whether or not the box is selected-in addition-a Null Register packet will be sent to the RP every time (just before) the Register Stop timer is about to expire on the RP. This will trigger the RP to restart the timer so it will continue sending Register Stop packets to the Ixia-emulated DR/Source Range.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendNullRegAtBegin']))

    @property
    def SourceAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The first IPv4 source address to be included in this Register message. (IPv4 Multicast addresses are not valid for sources.)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddress']))

    @property
    def SourceCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of source addresses to be included in this register message
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceCount']))

    @property
    def Status(self):
        """
        Returns
        -------
        - list(str[none | notStarted | started]): Status
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def SupressionTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (In seconds) Part of the Register-Stop Timer (RST (S,G). The amount of time, following receipt of a Register-Stop message, that the DR will NOT send Register-encapsulated data to the Rendezvous Point (RP). The default is 60 seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupressionTime']))

    @property
    def SwitchOverInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*, G) to (S,G). The default value is 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SwitchOverInterval']))

    @property
    def TxIterationGap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (in milliseconds) The gap between each iteration of the Register Range. The default is 60,000 ms (= 60 seconds). (Does not apply to NULL Registers, which contain no data.)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxIterationGap']))

    @property
    def UdpDestinationPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of UDP Destination Ports in the receiving Multicast Group. The default is 3000 UDP Destination Ports.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UdpDestinationPort']))

    @property
    def UdpSourcePort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of UDP Source Ports sending encapsulated UDP packets to MultiCast Groups (through Register Messages to the RP). The default is 3000 UDP Source Ports.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UdpSourcePort']))

    def update(self, Name=None):
        """Updates pimV4SourcesList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, DiscardSgJoinStates=None, GroupAddress=None, GroupCount=None, MulticastDataLength=None, RegisterProbeTime=None, RpAddress=None, SendNullRegAtBegin=None, SourceAddress=None, SourceCount=None, SupressionTime=None, SwitchOverInterval=None, TxIterationGap=None, UdpDestinationPort=None, UdpSourcePort=None):
        """Base class infrastructure that gets a list of pimV4SourcesList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - DiscardSgJoinStates (str): optional regex of discardSgJoinStates
        - GroupAddress (str): optional regex of groupAddress
        - GroupCount (str): optional regex of groupCount
        - MulticastDataLength (str): optional regex of multicastDataLength
        - RegisterProbeTime (str): optional regex of registerProbeTime
        - RpAddress (str): optional regex of rpAddress
        - SendNullRegAtBegin (str): optional regex of sendNullRegAtBegin
        - SourceAddress (str): optional regex of sourceAddress
        - SourceCount (str): optional regex of sourceCount
        - SupressionTime (str): optional regex of supressionTime
        - SwitchOverInterval (str): optional regex of switchOverInterval
        - TxIterationGap (str): optional regex of txIterationGap
        - UdpDestinationPort (str): optional regex of udpDestinationPort
        - UdpSourcePort (str): optional regex of udpSourcePort

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

        Activate Source

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

        Deactivate Source

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
