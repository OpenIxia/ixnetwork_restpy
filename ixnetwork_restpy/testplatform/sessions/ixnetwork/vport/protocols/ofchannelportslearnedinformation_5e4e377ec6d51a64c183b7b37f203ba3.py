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


class OfChannelPortsLearnedInformation(Base):
    """Signifies the information learned from OF channel ports.
    The OfChannelPortsLearnedInformation class encapsulates a list of ofChannelPortsLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelPortsLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannelPortsLearnedInformation'
    _SDM_ATT_MAP = {
        'AdvertisedFeatures': 'advertisedFeatures',
        'Config': 'config',
        'CurrentFeatures': 'currentFeatures',
        'CurrentSpeed': 'currentSpeed',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'EthernetAddress': 'ethernetAddress',
        'LocalIp': 'localIp',
        'MaximumSpeed': 'maximumSpeed',
        'Name': 'name',
        'PeerAdvertisedFeatures': 'peerAdvertisedFeatures',
        'PortNumber': 'portNumber',
        'RemoteIp': 'remoteIp',
        'State': 'state',
        'SupportedFeatures': 'supportedFeatures',
    }

    def __init__(self, parent):
        super(OfChannelPortsLearnedInformation, self).__init__(parent)

    @property
    def AdvertisedFeatures(self):
        """
        Returns
        -------
        - str: Signifies the advertised features of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertisedFeatures'])

    @property
    def Config(self):
        """
        Returns
        -------
        - str: Signifies the configuration name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Config'])

    @property
    def CurrentFeatures(self):
        """
        Returns
        -------
        - str: Signifies the current features of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentFeatures'])

    @property
    def CurrentSpeed(self):
        """
        Returns
        -------
        - number: Indicates the current speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentSpeed'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - number: The Datapath identifier of the Open Flow channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: The Data Path identifier of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def EthernetAddress(self):
        """
        Returns
        -------
        - str: Signifies the Ethernet IP address of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetAddress'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Signifies the local IP of the switch that the OF Channel is connected to.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MaximumSpeed(self):
        """
        Returns
        -------
        - number: Indicates the maximum speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumSpeed'])

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Signifies the name of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def PeerAdvertisedFeatures(self):
        """
        Returns
        -------
        - str: Signifies the features advertised by the peer port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerAdvertisedFeatures'])

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - number: Indicates the port number used by the corresponding switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumber'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: Signifies the remote IP of the switch that the OF Channel is connected to.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def State(self):
        """
        Returns
        -------
        - str: Signifies the state of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def SupportedFeatures(self):
        """
        Returns
        -------
        - str: Signifies the features supported by the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedFeatures'])

    def find(self, AdvertisedFeatures=None, Config=None, CurrentFeatures=None, CurrentSpeed=None, DataPathId=None, DataPathIdAsHex=None, EthernetAddress=None, LocalIp=None, MaximumSpeed=None, Name=None, PeerAdvertisedFeatures=None, PortNumber=None, RemoteIp=None, State=None, SupportedFeatures=None):
        """Finds and retrieves ofChannelPortsLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofChannelPortsLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofChannelPortsLearnedInformation resources from the server.

        Args
        ----
        - AdvertisedFeatures (str): Signifies the advertised features of the port.
        - Config (str): Signifies the configuration name.
        - CurrentFeatures (str): Signifies the current features of the port.
        - CurrentSpeed (number): Indicates the current speed.
        - DataPathId (number): The Datapath identifier of the Open Flow channel.
        - DataPathIdAsHex (str): The Data Path identifier of the OpenFlow switch in hexadecimal format.
        - EthernetAddress (str): Signifies the Ethernet IP address of the switch.
        - LocalIp (str): Signifies the local IP of the switch that the OF Channel is connected to.
        - MaximumSpeed (number): Indicates the maximum speed.
        - Name (str): Signifies the name of the port.
        - PeerAdvertisedFeatures (str): Signifies the features advertised by the peer port.
        - PortNumber (number): Indicates the port number used by the corresponding switch.
        - RemoteIp (str): Signifies the remote IP of the switch that the OF Channel is connected to.
        - State (str): Signifies the state of the port.
        - SupportedFeatures (str): Signifies the features supported by the port.

        Returns
        -------
        - self: This instance with matching ofChannelPortsLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofChannelPortsLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofChannelPortsLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
