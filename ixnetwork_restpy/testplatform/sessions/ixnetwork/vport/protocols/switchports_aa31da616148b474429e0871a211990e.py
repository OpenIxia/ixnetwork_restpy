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


class SwitchPorts(Base):
    """A high level object that allows you to define the Switch Port configuration.
    The SwitchPorts class encapsulates a list of switchPorts resources that is be managed by the user.
    A list of resources can be retrieved from the server using the SwitchPorts.find() method.
    The list can be managed by the user by using the SwitchPorts.add() and SwitchPorts.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchPorts'

    def __init__(self, parent):
        super(SwitchPorts, self).__init__(parent)

    @property
    def AdvertisedFeatures(self):
        """An instance of the AdvertisedFeatures class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_1ba99e59bcf769c96d4394c34f351c93.AdvertisedFeatures)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_1ba99e59bcf769c96d4394c34f351c93 import AdvertisedFeatures
        return AdvertisedFeatures(self)._select()

    @property
    def Config(self):
        """An instance of the Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_876ec3b8cee8c538a22228629f05a6af.Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_876ec3b8cee8c538a22228629f05a6af import Config
        return Config(self)._select()

    @property
    def CurrentFeatures(self):
        """An instance of the CurrentFeatures class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_63508dd721c71267919bf746711b566a.CurrentFeatures)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_63508dd721c71267919bf746711b566a import CurrentFeatures
        return CurrentFeatures(self)._select()

    @property
    def PeerAdvertisedFeatures(self):
        """An instance of the PeerAdvertisedFeatures class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_5adb220885fb08a29a1ab647e9125b75.PeerAdvertisedFeatures)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_5adb220885fb08a29a1ab647e9125b75 import PeerAdvertisedFeatures
        return PeerAdvertisedFeatures(self)._select()

    @property
    def State(self):
        """An instance of the State class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_16239ce84d9e9faf3ade88301204c790.State)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_16239ce84d9e9faf3ade88301204c790 import State
        return State(self)._select()

    @property
    def SupportedFeatures(self):
        """An instance of the SupportedFeatures class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_5e336d65c5a7703f82f7e0726a22340e.SupportedFeatures)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_5e336d65c5a7703f82f7e0726a22340e import SupportedFeatures
        return SupportedFeatures(self)._select()

    @property
    def SwitchHostRanges(self):
        """An instance of the SwitchHostRanges class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostranges_d052c5ab2034986ea69ce58342f23523.SwitchHostRanges)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostranges_d052c5ab2034986ea69ce58342f23523 import SwitchHostRanges
        return SwitchHostRanges(self)

    @property
    def SwitchPortQueues(self):
        """An instance of the SwitchPortQueues class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_061655acfadc2b93c7bef86e60611f73.SwitchPortQueues)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_061655acfadc2b93c7bef86e60611f73 import SwitchPortQueues
        return SwitchPortQueues(self)

    @property
    def ConnectionType(self):
        """Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)

        Returns:
            str(internalSwitch|externalSwitch|noConnection|host)
        """
        return self._get_attribute('connectionType')
    @ConnectionType.setter
    def ConnectionType(self, value):
        self._set_attribute('connectionType', value)

    @property
    def CurrentSpeed(self):
        """The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.

        Returns:
            str
        """
        return self._get_attribute('currentSpeed')
    @CurrentSpeed.setter
    def CurrentSpeed(self, value):
        self._set_attribute('currentSpeed', value)

    @property
    def Enabled(self):
        """If true, indicates that the object is enabled.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def EthernetAddress(self):
        """The Ethernet address for the OpenFlow switch port.

        Returns:
            str
        """
        return self._get_attribute('ethernetAddress')
    @EthernetAddress.setter
    def EthernetAddress(self, value):
        self._set_attribute('ethernetAddress', value)

    @property
    def MaxSpeed(self):
        """The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.

        Returns:
            str
        """
        return self._get_attribute('maxSpeed')
    @MaxSpeed.setter
    def MaxSpeed(self, value):
        self._set_attribute('maxSpeed', value)

    @property
    def NumberOfPorts(self):
        """Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.

        Returns:
            number
        """
        return self._get_attribute('numberOfPorts')
    @NumberOfPorts.setter
    def NumberOfPorts(self, value):
        self._set_attribute('numberOfPorts', value)

    @property
    def PortLivenessSupport(self):
        """If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.

        Returns:
            bool
        """
        return self._get_attribute('portLivenessSupport')
    @PortLivenessSupport.setter
    def PortLivenessSupport(self, value):
        self._set_attribute('portLivenessSupport', value)

    @property
    def PortName(self):
        """The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.

        Returns:
            str
        """
        return self._get_attribute('portName')
    @PortName.setter
    def PortName(self, value):
        self._set_attribute('portName', value)

    @property
    def PortNumber(self):
        """Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.

        Returns:
            str
        """
        return self._get_attribute('portNumber')
    @PortNumber.setter
    def PortNumber(self, value):
        self._set_attribute('portNumber', value)

    @property
    def RemoteSwitch(self):
        """Specifies the internal remote Switch to which this port is connected

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switch)
        """
        return self._get_attribute('remoteSwitch')
    @RemoteSwitch.setter
    def RemoteSwitch(self, value):
        self._set_attribute('remoteSwitch', value)

    @property
    def RemoteSwitchPort(self):
        """Specifies the switchPort (of the internal remote switch) to which this switch port is connected

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switchPorts)
        """
        return self._get_attribute('remoteSwitchPort')
    @RemoteSwitchPort.setter
    def RemoteSwitchPort(self, value):
        self._set_attribute('remoteSwitchPort', value)

    @property
    def TransmissionDelay(self):
        """Specifies the time required in transmitting packets through link

        Returns:
            number
        """
        return self._get_attribute('transmissionDelay')
    @TransmissionDelay.setter
    def TransmissionDelay(self, value):
        self._set_attribute('transmissionDelay', value)

    def update(self, ConnectionType=None, CurrentSpeed=None, Enabled=None, EthernetAddress=None, MaxSpeed=None, NumberOfPorts=None, PortLivenessSupport=None, PortName=None, PortNumber=None, RemoteSwitch=None, RemoteSwitchPort=None, TransmissionDelay=None):
        """Updates a child instance of switchPorts on the server.

        Args:
            ConnectionType (str(internalSwitch|externalSwitch|noConnection|host)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
            CurrentSpeed (str): The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
            Enabled (bool): If true, indicates that the object is enabled.
            EthernetAddress (str): The Ethernet address for the OpenFlow switch port.
            MaxSpeed (str): The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.
            NumberOfPorts (number): Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.
            PortLivenessSupport (bool): If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
            PortName (str): The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.
            PortNumber (str): Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.
            RemoteSwitch (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switch)): Specifies the internal remote Switch to which this port is connected
            RemoteSwitchPort (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switchPorts)): Specifies the switchPort (of the internal remote switch) to which this switch port is connected
            TransmissionDelay (number): Specifies the time required in transmitting packets through link

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ConnectionType=None, CurrentSpeed=None, Enabled=None, EthernetAddress=None, MaxSpeed=None, NumberOfPorts=None, PortLivenessSupport=None, PortName=None, PortNumber=None, RemoteSwitch=None, RemoteSwitchPort=None, TransmissionDelay=None):
        """Adds a new switchPorts node on the server and retrieves it in this instance.

        Args:
            ConnectionType (str(internalSwitch|externalSwitch|noConnection|host)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
            CurrentSpeed (str): The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
            Enabled (bool): If true, indicates that the object is enabled.
            EthernetAddress (str): The Ethernet address for the OpenFlow switch port.
            MaxSpeed (str): The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.
            NumberOfPorts (number): Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.
            PortLivenessSupport (bool): If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
            PortName (str): The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.
            PortNumber (str): Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.
            RemoteSwitch (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switch)): Specifies the internal remote Switch to which this port is connected
            RemoteSwitchPort (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switchPorts)): Specifies the switchPort (of the internal remote switch) to which this switch port is connected
            TransmissionDelay (number): Specifies the time required in transmitting packets through link

        Returns:
            self: This instance with all currently retrieved switchPorts data using find and the newly added switchPorts data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the switchPorts data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectionType=None, CurrentSpeed=None, Enabled=None, EthernetAddress=None, MaxSpeed=None, NumberOfPorts=None, PortLivenessSupport=None, PortName=None, PortNumber=None, RemoteSwitch=None, RemoteSwitchPort=None, TransmissionDelay=None):
        """Finds and retrieves switchPorts data from the server.

        All named parameters support regex and can be used to selectively retrieve switchPorts data from the server.
        By default the find method takes no parameters and will retrieve all switchPorts data from the server.

        Args:
            ConnectionType (str(internalSwitch|externalSwitch|noConnection|host)): Specifies how this switchPort is connected to another switch (internal/external) or host or there is no connection (noConnection)
            CurrentSpeed (str): The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
            Enabled (bool): If true, indicates that the object is enabled.
            EthernetAddress (str): The Ethernet address for the OpenFlow switch port.
            MaxSpeed (str): The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link. The default value is 1000 kbps.
            NumberOfPorts (number): Specify the number of ports to be configured. The default value is 1. This can be modified only when the Connection Type is specified as No Connection.
            PortLivenessSupport (bool): If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
            PortName (str): The description of the port. For an assigned port, the format is - (Chassis name) (card no.): (port no.) - (type). For an unassigned port configuration, the format is - (Port type) Port 00x.
            PortNumber (str): Specify the port number for this OpenFlow Channel. The OpenFlow pipeline receives and sends packets on ports.
            RemoteSwitch (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switch)): Specifies the internal remote Switch to which this port is connected
            RemoteSwitchPort (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=switchPorts)): Specifies the switchPort (of the internal remote switch) to which this switch port is connected
            TransmissionDelay (number): Specifies the time required in transmitting packets through link

        Returns:
            self: This instance with matching switchPorts data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of switchPorts data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the switchPorts data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def SimulatePortUpDown(self):
        """Executes the simulatePortUpDown operation on the server.

        NOT DEFINED

            Returns:
                bool: NOT DEFINED

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('simulatePortUpDown', payload=payload, response_object=None)
