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


class SwitchPorts(Base):
    """This object allows to define the attributes for the physical Switch Ports.
    The SwitchPorts class encapsulates a list of switchPorts resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchPorts.find() method.
    The list can be managed by using the SwitchPorts.add() and SwitchPorts.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "switchPorts"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "EthernetAddress": "ethernetAddress",
        "NumberOfPorts": "numberOfPorts",
        "PortName": "portName",
        "PortNumber": "portNumber",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SwitchPorts, self).__init__(parent, list_op)

    @property
    def AdvertisedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_cc9bc55beca4c93e502db79a52a9d8e1.AdvertisedFeatures): An instance of the AdvertisedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_cc9bc55beca4c93e502db79a52a9d8e1 import (
            AdvertisedFeatures,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AdvertisedFeatures", None) is not None:
                return self._properties.get("AdvertisedFeatures")
        return AdvertisedFeatures(self)._select()

    @property
    def Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_6e49c0b3f524c23bb670180305a48807.Config): An instance of the Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_6e49c0b3f524c23bb670180305a48807 import (
            Config,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Config", None) is not None:
                return self._properties.get("Config")
        return Config(self)._select()

    @property
    def CurrentFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_42185161180e45e15d9936f9f341eb2d.CurrentFeatures): An instance of the CurrentFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_42185161180e45e15d9936f9f341eb2d import (
            CurrentFeatures,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CurrentFeatures", None) is not None:
                return self._properties.get("CurrentFeatures")
        return CurrentFeatures(self)._select()

    @property
    def PeerAdvertisedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_fb6d7682a9aed018ab02944d64968cc4.PeerAdvertisedFeatures): An instance of the PeerAdvertisedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_fb6d7682a9aed018ab02944d64968cc4 import (
            PeerAdvertisedFeatures,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PeerAdvertisedFeatures", None) is not None:
                return self._properties.get("PeerAdvertisedFeatures")
        return PeerAdvertisedFeatures(self)._select()

    @property
    def State(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_587063f3d328642794be16a898bab140.State): An instance of the State class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_587063f3d328642794be16a898bab140 import (
            State,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("State", None) is not None:
                return self._properties.get("State")
        return State(self)._select()

    @property
    def SupportedFeatures(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_12ce664a571508519b7508c8c6cc3e98.SupportedFeatures): An instance of the SupportedFeatures class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_12ce664a571508519b7508c8c6cc3e98 import (
            SupportedFeatures,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SupportedFeatures", None) is not None:
                return self._properties.get("SupportedFeatures")
        return SupportedFeatures(self)._select()

    @property
    def SwitchPortQueues(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_daba470e1df112e54556817cbc544b15.SwitchPortQueues): An instance of the SwitchPortQueues class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_daba470e1df112e54556817cbc544b15 import (
            SwitchPortQueues,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchPortQueues", None) is not None:
                return self._properties.get("SwitchPortQueues")
        return SwitchPortQueues(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the ports in the selected port range are added to the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def EthernetAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the hardware address of the ports in the port range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetAddress"])

    @EthernetAddress.setter
    def EthernetAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetAddress"], value)

    @property
    def NumberOfPorts(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of ports in a port range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfPorts"])

    @NumberOfPorts.setter
    def NumberOfPorts(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfPorts"], value)

    @property
    def PortName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the name for the switch port interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortName"])

    @PortName.setter
    def PortName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortName"], value)

    @property
    def PortNumber(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates a value that the datapath associates with a physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortNumber"])

    @PortNumber.setter
    def PortNumber(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortNumber"], value)

    def update(
        self,
        Enabled=None,
        EthernetAddress=None,
        NumberOfPorts=None,
        PortName=None,
        PortNumber=None,
    ):
        # type: (bool, str, int, str, str) -> SwitchPorts
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
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        EthernetAddress=None,
        NumberOfPorts=None,
        PortName=None,
        PortNumber=None,
    ):
        # type: (bool, str, int, str, str) -> SwitchPorts
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
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switchPorts resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        EthernetAddress=None,
        NumberOfPorts=None,
        PortName=None,
        PortNumber=None,
    ):
        # type: (bool, str, int, str, str) -> SwitchPorts
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

    def SimulatePortUpDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the simulatePortUpDown operation on the server.

        Exec to simulate port up and down.

        simulatePortUpDown(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute(
            "simulatePortUpDown", payload=payload, response_object=None
        )
