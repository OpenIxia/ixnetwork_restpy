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


class OpenFlow(Base):
    """OpenFlow is a Layer 2 communications protocol that gives access to the forwarding plane of a network switch or router over the network.
    The OpenFlow class encapsulates a required openFlow resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'openFlow'

    def __init__(self, parent):
        super(OpenFlow, self).__init__(parent)

    @property
    def Device(self):
        """An instance of the Device class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.device_4e16fa0ebc2bc8204e8e814618b4431d.Device)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.device_4e16fa0ebc2bc8204e8e814618b4431d import Device
        return Device(self)

    @property
    def EthernetTrafficEndPoint(self):
        """An instance of the EthernetTrafficEndPoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettrafficendpoint_ac7c5d4e1e9ff92e14a1ffb430b8be8b.EthernetTrafficEndPoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettrafficendpoint_ac7c5d4e1e9ff92e14a1ffb430b8be8b import EthernetTrafficEndPoint
        return EthernetTrafficEndPoint(self)

    @property
    def HostTopologyLearnedInformation(self):
        """An instance of the HostTopologyLearnedInformation class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hosttopologylearnedinformation_19bd395ad8fe429f3c1712e0d4281a89.HostTopologyLearnedInformation)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hosttopologylearnedinformation_19bd395ad8fe429f3c1712e0d4281a89 import HostTopologyLearnedInformation
        return HostTopologyLearnedInformation(self)._select()

    @property
    def Ipv4TrafficEndPoint(self):
        """An instance of the Ipv4TrafficEndPoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4trafficendpoint_5ac747be14640838fcd7db82a0483ee4.Ipv4TrafficEndPoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4trafficendpoint_5ac747be14640838fcd7db82a0483ee4 import Ipv4TrafficEndPoint
        return Ipv4TrafficEndPoint(self)

    @property
    def Ipv6TrafficEndPoint(self):
        """An instance of the Ipv6TrafficEndPoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6trafficendpoint_83227b0419e7cb1138d5bd325ead95f4.Ipv6TrafficEndPoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6trafficendpoint_83227b0419e7cb1138d5bd325ead95f4 import Ipv6TrafficEndPoint
        return Ipv6TrafficEndPoint(self)

    @property
    def LearnedInformation(self):
        """An instance of the LearnedInformation class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_27c59a01c678cebe3fc8be0ee2ac2d0a.LearnedInformation)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_27c59a01c678cebe3fc8be0ee2ac2d0a import LearnedInformation
        return LearnedInformation(self)._select()

    @property
    def MplsTrafficEndPoint(self):
        """An instance of the MplsTrafficEndPoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstrafficendpoint_913cb5e2d372d7495ef373a5d7cdb78b.MplsTrafficEndPoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstrafficendpoint_913cb5e2d372d7495ef373a5d7cdb78b import MplsTrafficEndPoint
        return MplsTrafficEndPoint(self)

    @property
    def OfTopologyLearnedInformation(self):
        """An instance of the OfTopologyLearnedInformation class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.oftopologylearnedinformation_9bf6428a9a54180238c749b7e07307d1.OfTopologyLearnedInformation)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.oftopologylearnedinformation_9bf6428a9a54180238c749b7e07307d1 import OfTopologyLearnedInformation
        return OfTopologyLearnedInformation(self)._select()

    @property
    def SwitchLearnedInformation(self):
        """An instance of the SwitchLearnedInformation class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchlearnedinformation_511299f091081f14d15eb7136e3d4e76.SwitchLearnedInformation)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchlearnedinformation_511299f091081f14d15eb7136e3d4e76 import SwitchLearnedInformation
        return SwitchLearnedInformation(self)._select()

    @property
    def TrafficEndPoint(self):
        """An instance of the TrafficEndPoint class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficendpoint_c20d895be4e76bf8d262400376eccbc6.TrafficEndPoint)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficendpoint_c20d895be4e76bf8d262400376eccbc6 import TrafficEndPoint
        return TrafficEndPoint(self)

    @property
    def Enabled(self):
        """If true, the openFlow object is enabled.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def PortRole(self):
        """Indicates the role of the port in the protocol configuration.

        Returns:
            str(control|traffic|controlAndTraffic)
        """
        return self._get_attribute('portRole')
    @PortRole.setter
    def PortRole(self, value):
        self._set_attribute('portRole', value)

    @property
    def RunningState(self):
        """Indicates the state of the OpenFlow protocol on the port.

        Returns:
            str(unknown|stopped|stopping|starting|started)
        """
        return self._get_attribute('runningState')

    def update(self, Enabled=None, PortRole=None):
        """Updates a child instance of openFlow on the server.

        Args:
            Enabled (bool): If true, the openFlow object is enabled.
            PortRole (str(control|traffic|controlAndTraffic)): Indicates the role of the port in the protocol configuration.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def Start(self):
        """Executes the start operation on the server.

        This describes the start value of the trigger settings.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        This describes the stop value of the trigger settings.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
