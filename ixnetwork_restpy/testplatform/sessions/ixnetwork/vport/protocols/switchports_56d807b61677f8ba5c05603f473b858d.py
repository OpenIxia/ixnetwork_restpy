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
    """This object allows to define the attributes for the physical Switch Ports.
    The SwitchPorts class encapsulates a list of switchPorts resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchPorts.find() method.
    The list can be managed by using the SwitchPorts.add() and SwitchPorts.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchPorts'

    def __init__(self, parent):
        super(SwitchPorts, self).__init__(parent)

    @property
    def AdvertisedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_0ef3ac1db9aa8bc64320a687d88e4d79.AdvertisedFeatures): An instance of the AdvertisedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_0ef3ac1db9aa8bc64320a687d88e4d79 import AdvertisedFeatures
        return AdvertisedFeatures(self)._select()

    @property
    def Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_5d9001581cadd18c65bab3c03d435f1b.Config): An instance of the Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_5d9001581cadd18c65bab3c03d435f1b import Config
        return Config(self)._select()

    @property
    def CurrentFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_31297c16efe904c634c9858877cc1c59.CurrentFeatures): An instance of the CurrentFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_31297c16efe904c634c9858877cc1c59 import CurrentFeatures
        return CurrentFeatures(self)._select()

    @property
    def PeerAdvertisedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_10a7fab22b63d8a00b89ffb54a0deeb6.PeerAdvertisedFeatures): An instance of the PeerAdvertisedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_10a7fab22b63d8a00b89ffb54a0deeb6 import PeerAdvertisedFeatures
        return PeerAdvertisedFeatures(self)._select()

    @property
    def State(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_e30ab3660676f38743eb4e51da8e15ea.State): An instance of the State class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_e30ab3660676f38743eb4e51da8e15ea import State
        return State(self)._select()

    @property
    def SupportedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_c04ef4f1e7a49f46a80f8f5920f7b2ab.SupportedFeatures): An instance of the SupportedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_c04ef4f1e7a49f46a80f8f5920f7b2ab import SupportedFeatures
        return SupportedFeatures(self)._select()

    @property
    def SwitchPortQueues(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_df3f97cd2355d3c90f1061f6bfa87ae0.SwitchPortQueues): An instance of the SwitchPortQueues class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_df3f97cd2355d3c90f1061f6bfa87ae0 import SwitchPortQueues
        return SwitchPortQueues(self)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the ports in the selected port range are added to the switch.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def EthernetAddress(self):
        """
        Returns
        -------
        - str: Indicates the hardware address of the ports in the port range.
        """
        return self._get_attribute('ethernetAddress')
    @EthernetAddress.setter
    def EthernetAddress(self, value):
        self._set_attribute('ethernetAddress', value)

    @property
    def NumberOfPorts(self):
        """
        Returns
        -------
        - number: Specifies the number of ports in a port range.
        """
        return self._get_attribute('numberOfPorts')
    @NumberOfPorts.setter
    def NumberOfPorts(self, value):
        self._set_attribute('numberOfPorts', value)

    @property
    def PortName(self):
        """
        Returns
        -------
        - str: Indicates the name for the switch port interface.
        """
        return self._get_attribute('portName')
    @PortName.setter
    def PortName(self, value):
        self._set_attribute('portName', value)

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - str: Indicates a value that the datapath associates with a physical port.
        """
        return self._get_attribute('portNumber')
    @PortNumber.setter
    def PortNumber(self, value):
        self._set_attribute('portNumber', value)

    def update(self, Enabled=None, EthernetAddress=None, NumberOfPorts=None, PortName=None, PortNumber=None):
        """Updates switchPorts resource on the server.

        Args
        ----
        - Enabled (bool): If true, the ports in the selected port range are added to the switch.
        - EthernetAddress (str): Indicates the hardware address of the ports in the port range.
        - NumberOfPorts (number): Specifies the number of ports in a port range.
        - PortName (str): Indicates the name for the switch port interface.
        - PortNumber (str): Indicates a value that the datapath associates with a physical port.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, Enabled=None, EthernetAddress=None, NumberOfPorts=None, PortName=None, PortNumber=None):
        """Adds a new switchPorts resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, the ports in the selected port range are added to the switch.
        - EthernetAddress (str): Indicates the hardware address of the ports in the port range.
        - NumberOfPorts (number): Specifies the number of ports in a port range.
        - PortName (str): Indicates the name for the switch port interface.
        - PortNumber (str): Indicates a value that the datapath associates with a physical port.

        Returns
        -------
        - self: This instance with all currently retrieved switchPorts resources using find and the newly added switchPorts resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained switchPorts resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, EthernetAddress=None, NumberOfPorts=None, PortName=None, PortNumber=None):
        """Finds and retrieves switchPorts resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchPorts resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchPorts resources from the server.

        Args
        ----
        - Enabled (bool): If true, the ports in the selected port range are added to the switch.
        - EthernetAddress (str): Indicates the hardware address of the ports in the port range.
        - NumberOfPorts (number): Specifies the number of ports in a port range.
        - PortName (str): Indicates the name for the switch port interface.
        - PortNumber (str): Indicates a value that the datapath associates with a physical port.

        Returns
        -------
        - self: This instance with matching switchPorts resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

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

        Exec to simulate port up and down.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('simulatePortUpDown', payload=payload, response_object=None)
