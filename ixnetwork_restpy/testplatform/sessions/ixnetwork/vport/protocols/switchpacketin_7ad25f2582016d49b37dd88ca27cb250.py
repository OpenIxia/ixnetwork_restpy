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


class SwitchPacketIn(Base):
    """This object allows to configure the packet-in message parameters of the switch.
    The SwitchPacketIn class encapsulates a list of switchPacketIn resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchPacketIn.find() method.
    The list can be managed by using the SwitchPacketIn.add() and SwitchPacketIn.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchPacketIn'
    _SDM_ATT_MAP = {
        'ConsultFlowTable': 'consultFlowTable',
        'Enabled': 'enabled',
        'InPort': 'inPort',
        'PacketIn': 'packetIn',
        'PacketInName': 'packetInName',
        'SendPacketIn': 'sendPacketIn',
    }

    def __init__(self, parent):
        super(SwitchPacketIn, self).__init__(parent)

    @property
    def PacketInHeaders(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinheaders_da8aa56801b2924bcf5b2a7f534aea6e.PacketInHeaders): An instance of the PacketInHeaders class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinheaders_da8aa56801b2924bcf5b2a7f534aea6e import PacketInHeaders
        return PacketInHeaders(self)._select()

    @property
    def ConsultFlowTable(self):
        """
        Returns
        -------
        - bool: If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConsultFlowTable'])
    @ConsultFlowTable.setter
    def ConsultFlowTable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConsultFlowTable'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables Packet-In Range for the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: Specifies the number of ports on which the switch receives the new packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPort'])
    @InPort.setter
    def InPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPort'], value)

    @property
    def PacketIn(self):
        """
        Returns
        -------
        - str: Specifies the contents of the new packet that will be sent via the Packet-In message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketIn'])
    @PacketIn.setter
    def PacketIn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketIn'], value)

    @property
    def PacketInName(self):
        """
        Returns
        -------
        - str: Indicates the packet-in Range identifier name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketInName'])
    @PacketInName.setter
    def PacketInName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketInName'], value)

    @property
    def SendPacketIn(self):
        """
        Returns
        -------
        - bool: If true, packet-in messages will be sent to the controller using this Packet-In range definitions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendPacketIn'])
    @SendPacketIn.setter
    def SendPacketIn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendPacketIn'], value)

    def update(self, ConsultFlowTable=None, Enabled=None, InPort=None, PacketIn=None, PacketInName=None, SendPacketIn=None):
        """Updates switchPacketIn resource on the server.

        Args
        ----
        - ConsultFlowTable (bool): If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.
        - Enabled (bool): If true, enables Packet-In Range for the switch.
        - InPort (str): Specifies the number of ports on which the switch receives the new packet.
        - PacketIn (str): Specifies the contents of the new packet that will be sent via the Packet-In message.
        - PacketInName (str): Indicates the packet-in Range identifier name.
        - SendPacketIn (bool): If true, packet-in messages will be sent to the controller using this Packet-In range definitions.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConsultFlowTable=None, Enabled=None, InPort=None, PacketIn=None, PacketInName=None, SendPacketIn=None):
        """Adds a new switchPacketIn resource on the server and adds it to the container.

        Args
        ----
        - ConsultFlowTable (bool): If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.
        - Enabled (bool): If true, enables Packet-In Range for the switch.
        - InPort (str): Specifies the number of ports on which the switch receives the new packet.
        - PacketIn (str): Specifies the contents of the new packet that will be sent via the Packet-In message.
        - PacketInName (str): Indicates the packet-in Range identifier name.
        - SendPacketIn (bool): If true, packet-in messages will be sent to the controller using this Packet-In range definitions.

        Returns
        -------
        - self: This instance with all currently retrieved switchPacketIn resources using find and the newly added switchPacketIn resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switchPacketIn resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConsultFlowTable=None, Enabled=None, InPort=None, PacketIn=None, PacketInName=None, SendPacketIn=None):
        """Finds and retrieves switchPacketIn resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchPacketIn resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchPacketIn resources from the server.

        Args
        ----
        - ConsultFlowTable (bool): If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.
        - Enabled (bool): If true, enables Packet-In Range for the switch.
        - InPort (str): Specifies the number of ports on which the switch receives the new packet.
        - PacketIn (str): Specifies the contents of the new packet that will be sent via the Packet-In message.
        - PacketInName (str): Indicates the packet-in Range identifier name.
        - SendPacketIn (bool): If true, packet-in messages will be sent to the controller using this Packet-In range definitions.

        Returns
        -------
        - self: This instance with matching switchPacketIn resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchPacketIn data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchPacketIn resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def SendSwitchPacketInOption(self, *args, **kwargs):
        """Executes the sendSwitchPacketInOption operation on the server.

        NOT DEFINED

        sendSwitchPacketInOption(Arg2=enum)bool
        ---------------------------------------
        - Arg2 (str(sendPause | sendStart | sendStop)): NOT DEFINED
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendSwitchPacketInOption', payload=payload, response_object=None)
