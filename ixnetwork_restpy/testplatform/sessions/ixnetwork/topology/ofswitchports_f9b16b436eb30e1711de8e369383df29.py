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


class OfSwitchPorts(Base):
    """Openflow Switch Ports level Configuration
    The OfSwitchPorts class encapsulates a required ofSwitchPorts resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ofSwitchPorts"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AdvertisedFeatures": "advertisedFeatures",
        "Config": "config",
        "Count": "count",
        "CurrentConnectionType": "currentConnectionType",
        "CurrentFeatures": "currentFeatures",
        "CurrentSpeed": "currentSpeed",
        "DescriptiveName": "descriptiveName",
        "EtherAddr": "etherAddr",
        "ForcedConnectionType": "forcedConnectionType",
        "MaxSpeed": "maxSpeed",
        "Name": "name",
        "NumQueueRange": "numQueueRange",
        "ParentSwitch": "parentSwitch",
        "PeerAdvertisedFeatures": "peerAdvertisedFeatures",
        "PortIndex": "portIndex",
        "PortLivenessSupport": "portLivenessSupport",
        "PortName": "portName",
        "PortNumber": "portNumber",
        "RemotePortIndex": "remotePortIndex",
        "RemoteSwitch": "remoteSwitch",
        "RemoteSwitchIndex": "remoteSwitchIndex",
        "RemoteSwitchPort": "remoteSwitchPort",
        "State": "state",
        "SupportedFeatures": "supportedFeatures",
        "SwitchIndex": "switchIndex",
        "TransmissionDelay": "transmissionDelay",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OfSwitchPorts, self).__init__(parent, list_op)

    @property
    def OfSwitchQueues(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchqueues_9037a6161291f813628ddfbefe3df8ed.OfSwitchQueues): An instance of the OfSwitchQueues class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchqueues_9037a6161291f813628ddfbefe3df8ed import (
            OfSwitchQueues,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OfSwitchQueues", None) is not None:
                return self._properties.get("OfSwitchQueues")
        return OfSwitchQueues(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AdvertisedFeatures(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the features (link modes, link types, and link features) from the list that will be advertised by the port
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertisedFeatures"])
        )

    @property
    def Config(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the port administrative settings to indicate the behavior of the physical port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Config"]))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def CurrentConnectionType(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[auto | externalSwitch | host | internalSwitch | noConnection]): Port Type calculated based on host topology assigned and forced type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentConnectionType"])

    @property
    def CurrentFeatures(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the current features (link modes, link types, and link features) from the list that the port will support
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CurrentFeatures"])
        )

    @property
    def CurrentSpeed(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The current bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the current capacity of the link.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CurrentSpeed"]))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def EtherAddr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Ethernet address for the OpenFlow switch port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EtherAddr"]))

    @property
    def ForcedConnectionType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Users override for connection type.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ForcedConnectionType"])
        )

    @property
    def MaxSpeed(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The maximum bit rate (raw transmission speed) of the link in kilobytes per second. This indicates the maximum configured capacity of the link.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxSpeed"]))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NumQueueRange(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the number of Queue ranges to be configured for this switch port
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumQueueRange"])

    @NumQueueRange.setter
    def NumQueueRange(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumQueueRange"], value)

    @property
    def ParentSwitch(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Parent Switch Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["ParentSwitch"])

    @property
    def PeerAdvertisedFeatures(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the features (link modes, link types, and link features) from the list that will be advertised by the peer
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PeerAdvertisedFeatures"])
        )

    @property
    def PortIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Index of port in particular OF Switch.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortIndex"]))

    @property
    def PortLivenessSupport(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, port liveness is supported in its port state. A port is considered live when it is not down or when its link is not down.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortLivenessSupport"])
        )

    @property
    def PortName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the name of the Port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortName"]))

    @property
    def PortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The OpenFlow pipeline receives and sends packets on ports.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortNumber"]))

    @property
    def RemotePortIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Index of the Remote Port. Please refer Port Index to enter value in this field.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemotePortIndex"])
        )

    @property
    def RemoteSwitch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The name of the remote Switch at the other end of the Switch OF Channel
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemoteSwitch"]))

    @property
    def RemoteSwitchIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Index of the Remote Switch. Please refer Switch Index to enter value in this field.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteSwitchIndex"])
        )

    @property
    def RemoteSwitchPort(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The remote Switch port number identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteSwitchPort"])
        )

    @property
    def State(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the port states
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["State"]))

    @property
    def SupportedFeatures(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the features (link modes, link types, and link features) from the list that will be supported by the port
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SupportedFeatures"])
        )

    @property
    def SwitchIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Index of the OF Switch.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SwitchIndex"]))

    @property
    def TransmissionDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The delay in milliseconds, between internal Switch ports
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TransmissionDelay"])
        )

    def update(self, Name=None, NumQueueRange=None):
        # type: (str, int) -> OfSwitchPorts
        """Updates ofSwitchPorts resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumQueueRange (number): Specify the number of Queue ranges to be configured for this switch port

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        CurrentConnectionType=None,
        DescriptiveName=None,
        Name=None,
        NumQueueRange=None,
        ParentSwitch=None,
    ):
        # type: (int, List[str], str, str, int, str) -> OfSwitchPorts
        """Finds and retrieves ofSwitchPorts resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofSwitchPorts resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofSwitchPorts resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - CurrentConnectionType (list(str[auto | externalSwitch | host | internalSwitch | noConnection])): Port Type calculated based on host topology assigned and forced type.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumQueueRange (number): Specify the number of Queue ranges to be configured for this switch port
        - ParentSwitch (str): Parent Switch Name

        Returns
        -------
        - self: This instance with matching ofSwitchPorts resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofSwitchPorts data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofSwitchPorts resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def SimulatePortUpDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the simulatePortUpDown operation on the server.

        Method to Simulate Port Up Down.

        simulatePortUpDown(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AdvertisedFeatures=None,
        Config=None,
        CurrentFeatures=None,
        CurrentSpeed=None,
        EtherAddr=None,
        ForcedConnectionType=None,
        MaxSpeed=None,
        PeerAdvertisedFeatures=None,
        PortIndex=None,
        PortLivenessSupport=None,
        PortName=None,
        PortNumber=None,
        RemotePortIndex=None,
        RemoteSwitch=None,
        RemoteSwitchIndex=None,
        RemoteSwitchPort=None,
        State=None,
        SupportedFeatures=None,
        SwitchIndex=None,
        TransmissionDelay=None,
    ):
        """Base class infrastructure that gets a list of ofSwitchPorts device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertisedFeatures (str): optional regex of advertisedFeatures
        - Config (str): optional regex of config
        - CurrentFeatures (str): optional regex of currentFeatures
        - CurrentSpeed (str): optional regex of currentSpeed
        - EtherAddr (str): optional regex of etherAddr
        - ForcedConnectionType (str): optional regex of forcedConnectionType
        - MaxSpeed (str): optional regex of maxSpeed
        - PeerAdvertisedFeatures (str): optional regex of peerAdvertisedFeatures
        - PortIndex (str): optional regex of portIndex
        - PortLivenessSupport (str): optional regex of portLivenessSupport
        - PortName (str): optional regex of portName
        - PortNumber (str): optional regex of portNumber
        - RemotePortIndex (str): optional regex of remotePortIndex
        - RemoteSwitch (str): optional regex of remoteSwitch
        - RemoteSwitchIndex (str): optional regex of remoteSwitchIndex
        - RemoteSwitchPort (str): optional regex of remoteSwitchPort
        - State (str): optional regex of state
        - SupportedFeatures (str): optional regex of supportedFeatures
        - SwitchIndex (str): optional regex of switchIndex
        - TransmissionDelay (str): optional regex of transmissionDelay

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
