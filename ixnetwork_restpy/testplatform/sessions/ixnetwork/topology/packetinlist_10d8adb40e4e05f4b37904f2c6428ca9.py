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


class PacketInList(Base):
    """Openflow Switch PacketIn Configuration
    The PacketInList class encapsulates a list of packetInList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PacketInList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'packetInList'
    _SDM_ATT_MAP = {
        'AuxiliaryId': 'auxiliaryId',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'FlowTable': 'flowTable',
        'InPort': 'inPort',
        'Name': 'name',
        'PacketInName': 'packetInName',
        'PhysicalInPort': 'physicalInPort',
        'SendPacketIn': 'sendPacketIn',
        'SwitchName': 'switchName',
    }

    def __init__(self, parent):
        super(PacketInList, self).__init__(parent)

    @property
    def AuxiliaryId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The identifier for auxiliary connections.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuxiliaryId']))

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
    def FlowTable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Switch looks up for each PacketIn configured in the Flow Table.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlowTable']))

    @property
    def InPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Switch Port on which, this Packet has come.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InPort']))

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
    def PacketInName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The description of the packet-in.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PacketInName']))

    @property
    def PhysicalInPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The physical In port value for this PacketIn range. It is the underlying physical port when packet is received on a logical port.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PhysicalInPort']))

    @property
    def SendPacketIn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Switch starts sending PacketIn messages when the session comes up.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendPacketIn']))

    @property
    def SwitchName(self):
        """
        Returns
        -------
        - str: Parent Switch Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchName'])

    def update(self, Name=None):
        """Updates packetInList resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None, SwitchName=None):
        """Finds and retrieves packetInList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve packetInList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all packetInList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SwitchName (str): Parent Switch Name

        Returns
        -------
        - self: This instance with matching packetInList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of packetInList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the packetInList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, AuxiliaryId=None, FlowTable=None, InPort=None, PacketInName=None, PhysicalInPort=None, SendPacketIn=None):
        """Base class infrastructure that gets a list of packetInList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AuxiliaryId (str): optional regex of auxiliaryId
        - FlowTable (str): optional regex of flowTable
        - InPort (str): optional regex of inPort
        - PacketInName (str): optional regex of packetInName
        - PhysicalInPort (str): optional regex of physicalInPort
        - SendPacketIn (str): optional regex of sendPacketIn

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def SendPause(self, *args, **kwargs):
        """Executes the sendPause operation on the server.

        Pause Sending PacketIn

        sendPause(Arg2=list)list
        ------------------------
        - Arg2 (list(number)): List of PacketIn.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPause', payload=payload, response_object=None)

    def SendStart(self, *args, **kwargs):
        """Executes the sendStart operation on the server.

        Start Sending PacketIn

        sendStart(Arg2=list)list
        ------------------------
        - Arg2 (list(number)): List of PacketIn.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendStart', payload=payload, response_object=None)

    def SendStop(self, *args, **kwargs):
        """Executes the sendStop operation on the server.

        Stop Sending PacketIn

        sendStop(Arg2=list)list
        -----------------------
        - Arg2 (list(number)): List of PacketIn.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendStop', payload=payload, response_object=None)
