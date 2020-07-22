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


class SwitchPorts(Base):
    """A high level object that allows you to define the Switch Port configuration.
    The SwitchPorts class encapsulates a list of switchPorts resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchPorts.find() method.
    The list can be managed by using the SwitchPorts.add() and SwitchPorts.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchPorts'
    _SDM_ATT_MAP = {
        'ConnectionType': 'connectionType',
        'CurrentSpeed': 'currentSpeed',
        'Enabled': 'enabled',
        'EthernetAddress': 'ethernetAddress',
        'MaxSpeed': 'maxSpeed',
        'NumberOfPorts': 'numberOfPorts',
        'PortLivenessSupport': 'portLivenessSupport',
        'PortName': 'portName',
        'PortNumber': 'portNumber',
        'RemoteSwitch': 'remoteSwitch',
        'RemoteSwitchPort': 'remoteSwitchPort',
        'TransmissionDelay': 'transmissionDelay',
    }

    def __init__(self, parent):
        super(SwitchPorts, self).__init__(parent)

    @property
    def AdvertisedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_56a04904a51fcb5b140ef5c5da7017e7.AdvertisedFeatures): An instance of the AdvertisedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_56a04904a51fcb5b140ef5c5da7017e7 import AdvertisedFeatures
        return AdvertisedFeatures(self)._select()

    @property
    def Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_62b7c65bc219bf58bd290f568c5c62cd.Config): An instance of the Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_62b7c65bc219bf58bd290f568c5c62cd import Config
        return Config(self)._select()

    @property
    def CurrentFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_9c597885128022b128b87f0d21ccab4e.CurrentFeatures): An instance of the CurrentFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_9c597885128022b128b87f0d21ccab4e import CurrentFeatures
        return CurrentFeatures(self)._select()

    @property
    def PeerAdvertisedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_c03cc0e79fa52dad924f6e97622a6060.PeerAdvertisedFeatures): An instance of the PeerAdvertisedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_c03cc0e79fa52dad924f6e97622a6060 import PeerAdvertisedFeatures
        return PeerAdvertisedFeatures(self)._select()

    @property
    def State(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_4b77e3f7e07a0d6bb28ad071368e0adc.State): An instance of the State class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_4b77e3f7e07a0d6bb28ad071368e0adc import State
        return State(self)._select()

    @property
    def SupportedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_f52d2e6f6faa02edea055b4cd6274a79.SupportedFeatures): An instance of the SupportedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_f52d2e6f6faa02edea055b4cd6274a79 import SupportedFeatures
        return SupportedFeatures(self)._select()

    @property
    def SwitchHostRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostranges_5d2115168a5da6fa79eb866056d9b27b.SwitchHostRanges): An instance of the SwitchHostRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostranges_5d2115168a5da6fa79eb866056d9b27b import SwitchHostRanges
        return SwitchHostRanges(self)

    @property
    def SwitchPortQueues(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_bde30bebca869fc45ea70a1a9c152aa7.SwitchPortQueues): An instance of the SwitchPortQueues class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_bde30bebca869fc45ea70a1a9c152aa7 import SwitchPortQueues
        return SwitchPortQueues(self)

    @property
    def ConnectionType(self):
        """
        Returns
        -------
        - str(internalSwitch | externalSwitch | noConnection | host): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionType'])
    @ConnectionType.setter
    def ConnectionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectionType'], value)

    @property
    def CurrentSpeed(self):
        """
        Returns
        -------
        - str: The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentSpeed'])
    @CurrentSpeed.setter
    def CurrentSpeed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CurrentSpeed'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, indicates that the object is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EthernetAddress(self):
        """
        Returns
        -------
        - str: The Ethernet address for the OpenFlow switch port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetAddress'])
    @EthernetAddress.setter
    def EthernetAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetAddress'], value)

    @property
    def MaxSpeed(self):
        """
        Returns
        -------
        - str: The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxSpeed'])
    @MaxSpeed.setter
    def MaxSpeed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxSpeed'], value)

    @property
    def NumberOfPorts(self):
        """
        Returns
        -------
        - number: Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfPorts'])
    @NumberOfPorts.setter
    def NumberOfPorts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfPorts'], value)

    @property
    def PortLivenessSupport(self):
        """
        Returns
        -------
        - bool: If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortLivenessSupport'])
    @PortLivenessSupport.setter
    def PortLivenessSupport(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortLivenessSupport'], value)

    @property
    def PortName(self):
        """
        Returns
        -------
        - str: The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortName'])
    @PortName.setter
    def PortName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortName'], value)

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - str: Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumber'])
    @PortNumber.setter
    def PortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortNumber'], value)

    @property
    def RemoteSwitch(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../switch): Specifies the internal remote Switch to which this port is connected
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteSwitch'])
    @RemoteSwitch.setter
    def RemoteSwitch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemoteSwitch'], value)

    @property
    def RemoteSwitchPort(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../switchPorts): Specifies the switchPort (of the internal remote switch) to which this switch port is connected
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteSwitchPort'])
    @RemoteSwitchPort.setter
    def RemoteSwitchPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RemoteSwitchPort'], value)

    @property
    def TransmissionDelay(self):
        """
        Returns
        -------
        - number: Specifies the time required in transmitting packets through link
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmissionDelay'])
    @TransmissionDelay.setter
    def TransmissionDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmissionDelay'], value)

    def update(self, ConnectionType=None, CurrentSpeed=None, Enabled=None, EthernetAddress=None, MaxSpeed=None, NumberOfPorts=None, PortLivenessSupport=None, PortName=None, PortNumber=None, RemoteSwitch=None, RemoteSwitchPort=None, TransmissionDelay=None):
        """Updates switchPorts resource on the server.

        Args
        ----
        - ConnectionType (str(internalSwitch | externalSwitch | noConnection | host)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        - CurrentSpeed (str): The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
        - Enabled (bool): If true, indicates that the object is enabled.
        - EthernetAddress (str): The Ethernet address for the OpenFlow switch port.
        - MaxSpeed (str): The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.
        - NumberOfPorts (number): Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.
        - PortLivenessSupport (bool): If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
        - PortName (str): The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.
        - PortNumber (str): Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.
        - RemoteSwitch (str(None | /api/v1/sessions/1/ixnetwork/vport/.../switch)): Specifies the internal remote Switch to which this port is connected
        - RemoteSwitchPort (str(None | /api/v1/sessions/1/ixnetwork/vport/.../switchPorts)): Specifies the switchPort (of the internal remote switch) to which this switch port is connected
        - TransmissionDelay (number): Specifies the time required in transmitting packets through link

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectionType=None, CurrentSpeed=None, Enabled=None, EthernetAddress=None, MaxSpeed=None, NumberOfPorts=None, PortLivenessSupport=None, PortName=None, PortNumber=None, RemoteSwitch=None, RemoteSwitchPort=None, TransmissionDelay=None):
        """Adds a new switchPorts resource on the server and adds it to the container.

        Args
        ----
        - ConnectionType (str(internalSwitch | externalSwitch | noConnection | host)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        - CurrentSpeed (str): The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
        - Enabled (bool): If true, indicates that the object is enabled.
        - EthernetAddress (str): The Ethernet address for the OpenFlow switch port.
        - MaxSpeed (str): The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.
        - NumberOfPorts (number): Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.
        - PortLivenessSupport (bool): If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
        - PortName (str): The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.
        - PortNumber (str): Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.
        - RemoteSwitch (str(None | /api/v1/sessions/1/ixnetwork/vport/.../switch)): Specifies the internal remote Switch to which this port is connected
        - RemoteSwitchPort (str(None | /api/v1/sessions/1/ixnetwork/vport/.../switchPorts)): Specifies the switchPort (of the internal remote switch) to which this switch port is connected
        - TransmissionDelay (number): Specifies the time required in transmitting packets through link

        Returns
        -------
        - self: This instance with all currently retrieved switchPorts resources using find and the newly added switchPorts resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switchPorts resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectionType=None, CurrentSpeed=None, Enabled=None, EthernetAddress=None, MaxSpeed=None, NumberOfPorts=None, PortLivenessSupport=None, PortName=None, PortNumber=None, RemoteSwitch=None, RemoteSwitchPort=None, TransmissionDelay=None):
        """Finds and retrieves switchPorts resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchPorts resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchPorts resources from the server.

        Args
        ----
        - ConnectionType (str(internalSwitch | externalSwitch | noConnection | host)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
        - CurrentSpeed (str): The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
        - Enabled (bool): If true, indicates that the object is enabled.
        - EthernetAddress (str): The Ethernet address for the OpenFlow switch port.
        - MaxSpeed (str): The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.
        - NumberOfPorts (number): Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.
        - PortLivenessSupport (bool): If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
        - PortName (str): The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.
        - PortNumber (str): Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.
        - RemoteSwitch (str(None | /api/v1/sessions/1/ixnetwork/vport/.../switch)): Specifies the internal remote Switch to which this port is connected
        - RemoteSwitchPort (str(None | /api/v1/sessions/1/ixnetwork/vport/.../switchPorts)): Specifies the switchPort (of the internal remote switch) to which this switch port is connected
        - TransmissionDelay (number): Specifies the time required in transmitting packets through link

        Returns
        -------
        - self: This instance with matching switchPorts resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchPorts data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchPorts resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def SimulatePortUpDown(self):
        """Executes the simulatePortUpDown operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('simulatePortUpDown', payload=payload, response_object=None)
