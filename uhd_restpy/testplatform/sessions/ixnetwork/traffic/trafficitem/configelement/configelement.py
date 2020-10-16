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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class ConfigElement(Base):
    """A grouping of endpoints under the Traffic Item per unique encapsulation/packet structure. The user sees each configElement as rows in the Pages of the wizard after the first page of the Wizard and also on the First Page under Endpoint sets as below. The user can then configure QOS, Frame Size, Rate etc per configElement. The configElements control the rate/frame size/qos properties of one or more flowGroups/highLevelStreams that are generated from the Traffic Item.
    The ConfigElement class encapsulates a list of configElement resources that are managed by the system.
    A list of resources can be retrieved from the server using the ConfigElement.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'configElement'
    _SDM_ATT_MAP = {
        'Crc': 'crc',
        'DestinationMacMode': 'destinationMacMode',
        'EnableDisparityError': 'enableDisparityError',
        'EncapsulationName': 'encapsulationName',
        'EndpointSetId': 'endpointSetId',
        'PreambleCustomSize': 'preambleCustomSize',
        'PreambleFrameSizeMode': 'preambleFrameSizeMode',
    }

    def __init__(self, parent):
        super(ConfigElement, self).__init__(parent)

    @property
    def FramePayload(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.framepayload.framepayload.FramePayload): An instance of the FramePayload class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.framepayload.framepayload import FramePayload
        return FramePayload(self)._select()

    @property
    def FrameRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.framerate.framerate.FrameRate): An instance of the FrameRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.framerate.framerate import FrameRate
        return FrameRate(self)._select()

    @property
    def FrameRateDistribution(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.frameratedistribution.frameratedistribution.FrameRateDistribution): An instance of the FrameRateDistribution class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.frameratedistribution.frameratedistribution import FrameRateDistribution
        return FrameRateDistribution(self)._select()

    @property
    def FrameSize(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.framesize.framesize.FrameSize): An instance of the FrameSize class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.framesize.framesize import FrameSize
        return FrameSize(self)._select()

    @property
    def Stack(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stack.Stack): An instance of the Stack class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stack import Stack
        return Stack(self)

    @property
    def StackLink(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stacklink.stacklink.StackLink): An instance of the StackLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stacklink.stacklink import StackLink
        return StackLink(self)

    @property
    def TransmissionControl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.transmissioncontrol.transmissioncontrol.TransmissionControl): An instance of the TransmissionControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.transmissioncontrol.transmissioncontrol import TransmissionControl
        return TransmissionControl(self)._select()

    @property
    def TransmissionDistribution(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.transmissiondistribution.transmissiondistribution.TransmissionDistribution): An instance of the TransmissionDistribution class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.transmissiondistribution.transmissiondistribution import TransmissionDistribution
        return TransmissionDistribution(self)

    @property
    def Crc(self):
        """
        Returns
        -------
        - str(badCrc | goodCrc): The Cyclic Redundancy Check frame of the configured encapsulation set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Crc'])
    @Crc.setter
    def Crc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Crc'], value)

    @property
    def DestinationMacMode(self):
        """
        Returns
        -------
        - str(arp | manual): The destination MAC address that is to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationMacMode'])
    @DestinationMacMode.setter
    def DestinationMacMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationMacMode'], value)

    @property
    def EnableDisparityError(self):
        """
        Returns
        -------
        - bool: If true, enables disparity error
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDisparityError'])
    @EnableDisparityError.setter
    def EnableDisparityError(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDisparityError'], value)

    @property
    def EncapsulationName(self):
        """
        Returns
        -------
        - str: Indicates the name of the encapsulation set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EncapsulationName'])

    @property
    def EndpointSetId(self):
        """
        Returns
        -------
        - number: Indicates the identification of the endpoint set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndpointSetId'])

    @property
    def PreambleCustomSize(self):
        """
        Returns
        -------
        - number: Indicates the customized preamble size of the frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreambleCustomSize'])
    @PreambleCustomSize.setter
    def PreambleCustomSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PreambleCustomSize'], value)

    @property
    def PreambleFrameSizeMode(self):
        """
        Returns
        -------
        - str(auto | custom): The preamble size to synchronize sender and receiver of the configured encapsulation set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreambleFrameSizeMode'])
    @PreambleFrameSizeMode.setter
    def PreambleFrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PreambleFrameSizeMode'], value)

    def update(self, Crc=None, DestinationMacMode=None, EnableDisparityError=None, PreambleCustomSize=None, PreambleFrameSizeMode=None):
        """Updates configElement resource on the server.

        Args
        ----
        - Crc (str(badCrc | goodCrc)): The Cyclic Redundancy Check frame of the configured encapsulation set.
        - DestinationMacMode (str(arp | manual)): The destination MAC address that is to be configured.
        - EnableDisparityError (bool): If true, enables disparity error
        - PreambleCustomSize (number): Indicates the customized preamble size of the frame.
        - PreambleFrameSizeMode (str(auto | custom)): The preamble size to synchronize sender and receiver of the configured encapsulation set.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Crc=None, DestinationMacMode=None, EnableDisparityError=None, EncapsulationName=None, EndpointSetId=None, PreambleCustomSize=None, PreambleFrameSizeMode=None):
        """Finds and retrieves configElement resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve configElement resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all configElement resources from the server.

        Args
        ----
        - Crc (str(badCrc | goodCrc)): The Cyclic Redundancy Check frame of the configured encapsulation set.
        - DestinationMacMode (str(arp | manual)): The destination MAC address that is to be configured.
        - EnableDisparityError (bool): If true, enables disparity error
        - EncapsulationName (str): Indicates the name of the encapsulation set.
        - EndpointSetId (number): Indicates the identification of the endpoint set.
        - PreambleCustomSize (number): Indicates the customized preamble size of the frame.
        - PreambleFrameSizeMode (str(auto | custom)): The preamble size to synchronize sender and receiver of the configured encapsulation set.

        Returns
        -------
        - self: This instance with matching configElement resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of configElement data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the configElement resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetPacketViewInHex(self, *args, **kwargs):
        """Executes the getPacketViewInHex operation on the server.

        Gets packet in Hex format for selected configElement and for the given packet index

        getPacketViewInHex(Arg2=number)string
        -------------------------------------
        - Arg2 (number): Packet Index (0 based)
        - Returns str: Packet in Hex format

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPacketViewInHex', payload=payload, response_object=None)
