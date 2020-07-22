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


class OfChannelPortsSwitchLearnedInfo(Base):
    """This object allows to configure the OF Channel Port Switch learned information parameters.
    The OfChannelPortsSwitchLearnedInfo class encapsulates a list of ofChannelPortsSwitchLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the OfChannelPortsSwitchLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannelPortsSwitchLearnedInfo'
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
        super(OfChannelPortsSwitchLearnedInfo, self).__init__(parent)

    @property
    def AdvertisedFeatures(self):
        """
        Returns
        -------
        - str: This describes the advertised features of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertisedFeatures'])

    @property
    def Config(self):
        """
        Returns
        -------
        - str: This describes the current configuration of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Config'])

    @property
    def CurrentFeatures(self):
        """
        Returns
        -------
        - str: This describes the current features of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentFeatures'])

    @property
    def CurrentSpeed(self):
        """
        Returns
        -------
        - number: This describes the current speed of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentSpeed'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: This describes the datapath ID of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: This describes the datapath ID, in hexadecimal format, of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def EthernetAddress(self):
        """
        Returns
        -------
        - str: This describes the hardware address of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetAddress'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: This describes the local IP of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MaximumSpeed(self):
        """
        Returns
        -------
        - number: This describes the maximum speed of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumSpeed'])

    @property
    def Name(self):
        """
        Returns
        -------
        - str: This describes the name of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def PeerAdvertisedFeatures(self):
        """
        Returns
        -------
        - str: This describes the peer advertised features of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerAdvertisedFeatures'])

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - number: This describes the port number of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumber'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: This describes the IP address of the remote end of the OF channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def State(self):
        """
        Returns
        -------
        - str: This describes the current state of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def SupportedFeatures(self):
        """
        Returns
        -------
        - str: This describes the supported features of the physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedFeatures'])

    def find(self, AdvertisedFeatures=None, Config=None, CurrentFeatures=None, CurrentSpeed=None, DataPathId=None, DataPathIdAsHex=None, EthernetAddress=None, LocalIp=None, MaximumSpeed=None, Name=None, PeerAdvertisedFeatures=None, PortNumber=None, RemoteIp=None, State=None, SupportedFeatures=None):
        """Finds and retrieves ofChannelPortsSwitchLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofChannelPortsSwitchLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofChannelPortsSwitchLearnedInfo resources from the server.

        Args
        ----
        - AdvertisedFeatures (str): This describes the advertised features of the physical port.
        - Config (str): This describes the current configuration of the physical port.
        - CurrentFeatures (str): This describes the current features of the physical port.
        - CurrentSpeed (number): This describes the current speed of the port.
        - DataPathId (str): This describes the datapath ID of the switch.
        - DataPathIdAsHex (str): This describes the datapath ID, in hexadecimal format, of the switch.
        - EthernetAddress (str): This describes the hardware address of the physical port.
        - LocalIp (str): This describes the local IP of the switch.
        - MaximumSpeed (number): This describes the maximum speed of the port.
        - Name (str): This describes the name of the physical port.
        - PeerAdvertisedFeatures (str): This describes the peer advertised features of the physical port.
        - PortNumber (number): This describes the port number of the physical port.
        - RemoteIp (str): This describes the IP address of the remote end of the OF channel.
        - State (str): This describes the current state of the physical port.
        - SupportedFeatures (str): This describes the supported features of the physical port.

        Returns
        -------
        - self: This instance with matching ofChannelPortsSwitchLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofChannelPortsSwitchLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofChannelPortsSwitchLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
