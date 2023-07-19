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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class OpenFlow(Base):
    """OpenFlow is a Layer 2 communications protocol that gives access to the forwarding plane of a network switch or router over the network.
    The OpenFlow class encapsulates a required openFlow resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "openFlow"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "PortRole": "portRole",
        "RunningState": "runningState",
    }
    _SDM_ENUM_MAP = {
        "portRole": ["control", "traffic", "controlAndTraffic"],
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(OpenFlow, self).__init__(parent, list_op)

    @property
    def Device(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.device_4586a4936a98f79a4eb811335e8b0199.Device): An instance of the Device class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.device_4586a4936a98f79a4eb811335e8b0199 import (
            Device,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Device", None) is not None:
                return self._properties.get("Device")
        return Device(self)

    @property
    def EthernetTrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettrafficendpoint_399c5a8996b8d783c5205ec4f1afc1a9.EthernetTrafficEndPoint): An instance of the EthernetTrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernettrafficendpoint_399c5a8996b8d783c5205ec4f1afc1a9 import (
            EthernetTrafficEndPoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EthernetTrafficEndPoint", None) is not None:
                return self._properties.get("EthernetTrafficEndPoint")
        return EthernetTrafficEndPoint(self)

    @property
    def HostTopologyLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hosttopologylearnedinformation_a15e8f019af7bb51517582abe5420f9e.HostTopologyLearnedInformation): An instance of the HostTopologyLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hosttopologylearnedinformation_a15e8f019af7bb51517582abe5420f9e import (
            HostTopologyLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("HostTopologyLearnedInformation", None) is not None:
                return self._properties.get("HostTopologyLearnedInformation")
        return HostTopologyLearnedInformation(self)._select()

    @property
    def Ipv4TrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4trafficendpoint_ccf0ac687ab3e96bf323237e4242c33d.Ipv4TrafficEndPoint): An instance of the Ipv4TrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4trafficendpoint_ccf0ac687ab3e96bf323237e4242c33d import (
            Ipv4TrafficEndPoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4TrafficEndPoint", None) is not None:
                return self._properties.get("Ipv4TrafficEndPoint")
        return Ipv4TrafficEndPoint(self)

    @property
    def Ipv6TrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6trafficendpoint_5ba047ad864d88c7c789f996fb9125d8.Ipv6TrafficEndPoint): An instance of the Ipv6TrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6trafficendpoint_5ba047ad864d88c7c789f996fb9125d8 import (
            Ipv6TrafficEndPoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6TrafficEndPoint", None) is not None:
                return self._properties.get("Ipv6TrafficEndPoint")
        return Ipv6TrafficEndPoint(self)

    @property
    def LearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_5ae2c6e302466a4ce0ccf9b15b6452d6.LearnedInformation): An instance of the LearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_5ae2c6e302466a4ce0ccf9b15b6452d6 import (
            LearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInformation", None) is not None:
                return self._properties.get("LearnedInformation")
        return LearnedInformation(self)._select()

    @property
    def MplsTrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstrafficendpoint_9c9576354d6d254197b269b117417591.MplsTrafficEndPoint): An instance of the MplsTrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstrafficendpoint_9c9576354d6d254197b269b117417591 import (
            MplsTrafficEndPoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MplsTrafficEndPoint", None) is not None:
                return self._properties.get("MplsTrafficEndPoint")
        return MplsTrafficEndPoint(self)

    @property
    def OfTopologyLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.oftopologylearnedinformation_87be98fe03804b7931f394eeeb6ce91e.OfTopologyLearnedInformation): An instance of the OfTopologyLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.oftopologylearnedinformation_87be98fe03804b7931f394eeeb6ce91e import (
            OfTopologyLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OfTopologyLearnedInformation", None) is not None:
                return self._properties.get("OfTopologyLearnedInformation")
        return OfTopologyLearnedInformation(self)._select()

    @property
    def SwitchLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchlearnedinformation_229c33dcb7a8e23f875f8a6acf5d4f8a.SwitchLearnedInformation): An instance of the SwitchLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchlearnedinformation_229c33dcb7a8e23f875f8a6acf5d4f8a import (
            SwitchLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchLearnedInformation", None) is not None:
                return self._properties.get("SwitchLearnedInformation")
        return SwitchLearnedInformation(self)._select()

    @property
    def TrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficendpoint_3120038095a42c08bd61e91959198aa0.TrafficEndPoint): An instance of the TrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficendpoint_3120038095a42c08bd61e91959198aa0 import (
            TrafficEndPoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficEndPoint", None) is not None:
                return self._properties.get("TrafficEndPoint")
        return TrafficEndPoint(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the openFlow object is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def PortRole(self):
        # type: () -> str
        """
        Returns
        -------
        - str(control | traffic | controlAndTraffic): Indicates the role of the port in the protocol configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortRole"])

    @PortRole.setter
    def PortRole(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortRole"], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): Indicates the state of the OpenFlow protocol on the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    def update(self, Enabled=None, PortRole=None):
        # type: (bool, str) -> OpenFlow
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

    def find(self, Enabled=None, PortRole=None, RunningState=None):
        # type: (bool, str, str) -> OpenFlow
        """Finds and retrieves openFlow resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openFlow resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openFlow resources from the server.

        Args
        ----
        - Enabled (bool): If true, the openFlow object is enabled.
        - PortRole (str(control | traffic | controlAndTraffic)): Indicates the role of the port in the protocol configuration.
        - RunningState (str(unknown | stopped | stopping | starting | started)): Indicates the state of the OpenFlow protocol on the port.

        Returns
        -------
        - self: This instance with matching openFlow resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of openFlow data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openFlow resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        This describes the start value of the trigger settings.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        This describes the stop value of the trigger settings.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)
