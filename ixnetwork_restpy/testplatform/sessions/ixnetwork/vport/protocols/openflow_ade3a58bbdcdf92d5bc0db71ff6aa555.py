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


class OpenFlow(Base):
    """OpenFlow is a Layer 2 communications protocol that gives access to the forwarding plane of a network switch or router over the network.
    The OpenFlow class encapsulates a required openFlow resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'openFlow'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'PortRole': 'portRole',
        'RunningState': 'runningState',
    }

    def __init__(self, parent):
        super(OpenFlow, self).__init__(parent)

    @property
    def Device(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.device_74c871c7b5db2ab8dd9f7511062c7165.Device): An instance of the Device class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.device_74c871c7b5db2ab8dd9f7511062c7165 import Device
        return Device(self)

    @property
    def EthernetTrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettrafficendpoint_b36a9e037b1c239f5e5bff7ddc302d29.EthernetTrafficEndPoint): An instance of the EthernetTrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettrafficendpoint_b36a9e037b1c239f5e5bff7ddc302d29 import EthernetTrafficEndPoint
        return EthernetTrafficEndPoint(self)

    @property
    def HostTopologyLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hosttopologylearnedinformation_315566f37c38fa9a23fdcf2331e54847.HostTopologyLearnedInformation): An instance of the HostTopologyLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hosttopologylearnedinformation_315566f37c38fa9a23fdcf2331e54847 import HostTopologyLearnedInformation
        return HostTopologyLearnedInformation(self)._select()

    @property
    def Ipv4TrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4trafficendpoint_5010de30aa90277034ff453bd1d391ef.Ipv4TrafficEndPoint): An instance of the Ipv4TrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4trafficendpoint_5010de30aa90277034ff453bd1d391ef import Ipv4TrafficEndPoint
        return Ipv4TrafficEndPoint(self)

    @property
    def Ipv6TrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6trafficendpoint_ca75aa14dfb2c06578dfc94f9ed6678d.Ipv6TrafficEndPoint): An instance of the Ipv6TrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6trafficendpoint_ca75aa14dfb2c06578dfc94f9ed6678d import Ipv6TrafficEndPoint
        return Ipv6TrafficEndPoint(self)

    @property
    def LearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_b7766cf6772040f87ed6db0e089eca27.LearnedInformation): An instance of the LearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_b7766cf6772040f87ed6db0e089eca27 import LearnedInformation
        return LearnedInformation(self)._select()

    @property
    def MplsTrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstrafficendpoint_2ff77b0f3263566e5f590f66b022a983.MplsTrafficEndPoint): An instance of the MplsTrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstrafficendpoint_2ff77b0f3263566e5f590f66b022a983 import MplsTrafficEndPoint
        return MplsTrafficEndPoint(self)

    @property
    def OfTopologyLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.oftopologylearnedinformation_258c8097854561963aea00d96c712047.OfTopologyLearnedInformation): An instance of the OfTopologyLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.oftopologylearnedinformation_258c8097854561963aea00d96c712047 import OfTopologyLearnedInformation
        return OfTopologyLearnedInformation(self)._select()

    @property
    def SwitchLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchlearnedinformation_29489f049b9adc4205fc457bfd194309.SwitchLearnedInformation): An instance of the SwitchLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchlearnedinformation_29489f049b9adc4205fc457bfd194309 import SwitchLearnedInformation
        return SwitchLearnedInformation(self)._select()

    @property
    def TrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficendpoint_2a9ee9d883512c1a5bdd5b6b068836f5.TrafficEndPoint): An instance of the TrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficendpoint_2a9ee9d883512c1a5bdd5b6b068836f5 import TrafficEndPoint
        return TrafficEndPoint(self)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the openFlow object is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def PortRole(self):
        """
        Returns
        -------
        - str(control | traffic | controlAndTraffic): Indicates the role of the port in the protocol configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortRole'])
    @PortRole.setter
    def PortRole(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortRole'], value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): Indicates the state of the OpenFlow protocol on the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    def update(self, Enabled=None, PortRole=None):
        """Updates openFlow resource on the server.

        Args
        ----
        - Enabled (bool): If true, the openFlow object is enabled.
        - PortRole (str(control | traffic | controlAndTraffic)): Indicates the role of the port in the protocol configuration.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Start(self):
        """Executes the start operation on the server.

        This describes the start value of the trigger settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        This describes the stop value of the trigger settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
