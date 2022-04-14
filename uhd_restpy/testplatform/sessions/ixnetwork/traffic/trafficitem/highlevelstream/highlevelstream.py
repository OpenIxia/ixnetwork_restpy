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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class HighLevelStream(Base):
    """A Flow Group that is generated from the Traffic Item. Each Traffic Item generates one or more Flow Groups, which in turn map to hardware streams on the port.  Each Flow Group/highLevelStream picks up its QOS, Rate, Frame size properties/attributes from its corresponding configElement configuration under the Traffic Item.
    The HighLevelStream class encapsulates a list of highLevelStream resources that are managed by the system.
    A list of resources can be retrieved from the server using the HighLevelStream.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'highLevelStream'
    _SDM_ATT_MAP = {
        'AppliedFrameRate': 'appliedFrameRate',
        'AppliedFrameSize': 'appliedFrameSize',
        'AppliedPacketCount': 'appliedPacketCount',
        'Crc': 'crc',
        'CurrentPacketCount': 'currentPacketCount',
        'DestinationMacMode': 'destinationMacMode',
        'Distributions': 'distributions',
        'Enabled': 'enabled',
        'EncapsulationName': 'encapsulationName',
        'EndpointSetId': 'endpointSetId',
        'Name': 'name',
        'OverSubscribed': 'overSubscribed',
        'Pause': 'pause',
        'PreambleCustomSize': 'preambleCustomSize',
        'PreambleFrameSizeMode': 'preambleFrameSizeMode',
        'RxPortIds': 'rxPortIds',
        'RxPortNames': 'rxPortNames',
        'State': 'state',
        'Suspend': 'suspend',
        'TxPortId': 'txPortId',
        'TxPortName': 'txPortName',
    }
    _SDM_ENUM_MAP = {
        'crc': ['badCrc', 'goodCrc'],
        'destinationMacMode': ['arp', 'manual'],
        'preambleFrameSizeMode': ['auto', 'custom'],
    }

    def __init__(self, parent, list_op=False):
        super(HighLevelStream, self).__init__(parent, list_op)

    @property
    def FramePayload(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framepayload.framepayload.FramePayload): An instance of the FramePayload class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framepayload.framepayload import FramePayload
        if len(self._object_properties) > 0:
            if self._properties.get('FramePayload', None) is not None:
                return self._properties.get('FramePayload')
        return FramePayload(self)._select()

    @property
    def FramePreemption(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framepreemption.framepreemption.FramePreemption): An instance of the FramePreemption class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framepreemption.framepreemption import FramePreemption
        if len(self._object_properties) > 0:
            if self._properties.get('FramePreemption', None) is not None:
                return self._properties.get('FramePreemption')
        return FramePreemption(self)

    @property
    def FrameRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framerate.framerate.FrameRate): An instance of the FrameRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framerate.framerate import FrameRate
        if len(self._object_properties) > 0:
            if self._properties.get('FrameRate', None) is not None:
                return self._properties.get('FrameRate')
        return FrameRate(self)._select()

    @property
    def FrameSize(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framesize.framesize.FrameSize): An instance of the FrameSize class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.framesize.framesize import FrameSize
        if len(self._object_properties) > 0:
            if self._properties.get('FrameSize', None) is not None:
                return self._properties.get('FrameSize')
        return FrameSize(self)._select()

    @property
    def Stack(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.stack.stack.Stack): An instance of the Stack class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stack import Stack
        if len(self._object_properties) > 0:
            if self._properties.get('Stack', None) is not None:
                return self._properties.get('Stack')
        return Stack(self)

    @property
    def StackLink(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.stacklink.stacklink.StackLink): An instance of the StackLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.stacklink.stacklink import StackLink
        if len(self._object_properties) > 0:
            if self._properties.get('StackLink', None) is not None:
                return self._properties.get('StackLink')
        return StackLink(self)

    @property
    def TableUdf(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.tableudf.TableUdf): An instance of the TableUdf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.tableudf import TableUdf
        if len(self._object_properties) > 0:
            if self._properties.get('TableUdf', None) is not None:
                return self._properties.get('TableUdf')
        return TableUdf(self)

    @property
    def TransmissionControl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.transmissioncontrol.transmissioncontrol.TransmissionControl): An instance of the TransmissionControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.transmissioncontrol.transmissioncontrol import TransmissionControl
        if len(self._object_properties) > 0:
            if self._properties.get('TransmissionControl', None) is not None:
                return self._properties.get('TransmissionControl')
        return TransmissionControl(self)._select()

    @property
    def Udf(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.udf.Udf): An instance of the Udf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.udf import Udf
        if len(self._object_properties) > 0:
            if self._properties.get('Udf', None) is not None:
                return self._properties.get('Udf')
        return Udf(self)

    @property
    def AppliedFrameRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AppliedFrameRate'])

    @property
    def AppliedFrameSize(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read only) Indicates the applied frame size of the high level stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AppliedFrameSize'])

    @property
    def AppliedPacketCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read only) Indicates the aplied packet count of the high level stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AppliedPacketCount'])

    @property
    def Crc(self):
        # type: () -> str
        """
        Returns
        -------
        - str(badCrc | goodCrc): The Cyclic Redundancy Check frame of the configured high level stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Crc'])
    @Crc.setter
    def Crc(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Crc'], value)

    @property
    def CurrentPacketCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read only) Denotes the number of packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentPacketCount'])

    @property
    def DestinationMacMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(arp | manual): The mode in which the Destination MAC Address is configured, either manual or ARP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationMacMode'])
    @DestinationMacMode.setter
    def DestinationMacMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DestinationMacMode'], value)

    @property
    def Distributions(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str)): Denotes the distribution of the high level stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Distributions'])

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EncapsulationName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of the configured encapsulation type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EncapsulationName'])

    @property
    def EndpointSetId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The ID of the configured endpoint set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndpointSetId'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: An alphanumeric string that returns the name of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OverSubscribed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the rate is oversubscribed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverSubscribed'])

    @property
    def Pause(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then pause is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Pause'])
    @Pause.setter
    def Pause(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Pause'], value)

    @property
    def PreambleCustomSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Customizes the preamble size of the frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreambleCustomSize'])
    @PreambleCustomSize.setter
    def PreambleCustomSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PreambleCustomSize'], value)

    @property
    def PreambleFrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(auto | custom): The starting size of the frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreambleFrameSizeMode'])
    @PreambleFrameSizeMode.setter
    def PreambleFrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PreambleFrameSizeMode'], value)

    @property
    def RxPortIds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport]): A list of virtual ports that are the receiving ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxPortIds'])
    @RxPortIds.setter
    def RxPortIds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['RxPortIds'], value)

    @property
    def RxPortNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): A list of names from the receiving virtual ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxPortNames'])

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read only) Denotes the current state of the stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def Suspend(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Suspends all traffic on this high level stream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Suspend'])
    @Suspend.setter
    def Suspend(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Suspend'], value)

    @property
    def TxPortId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport): The virtual port that is the transmitting port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxPortId'])
    @TxPortId.setter
    def TxPortId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TxPortId'], value)

    @property
    def TxPortName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the virtual port that is the transmitting port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxPortName'])

    def update(self, Crc=None, DestinationMacMode=None, Enabled=None, Name=None, Pause=None, PreambleCustomSize=None, PreambleFrameSizeMode=None, RxPortIds=None, Suspend=None, TxPortId=None):
        # type: (str, str, bool, str, bool, int, str, List[str], bool, str) -> HighLevelStream
        """Updates highLevelStream resource on the server.

        Args
        ----
        - Crc (str(badCrc | goodCrc)): The Cyclic Redundancy Check frame of the configured high level stream.
        - DestinationMacMode (str(arp | manual)): The mode in which the Destination MAC Address is configured, either manual or ARP.
        - Enabled (bool): 
        - Name (str): An alphanumeric string that returns the name of the field.
        - Pause (bool): If true then pause is enabled.
        - PreambleCustomSize (number): Customizes the preamble size of the frame.
        - PreambleFrameSizeMode (str(auto | custom)): The starting size of the frame.
        - RxPortIds (list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport])): A list of virtual ports that are the receiving ports
        - Suspend (bool): Suspends all traffic on this high level stream.
        - TxPortId (str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport)): The virtual port that is the transmitting port.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Crc=None, DestinationMacMode=None, Enabled=None, Name=None, Pause=None, PreambleCustomSize=None, PreambleFrameSizeMode=None, RxPortIds=None, Suspend=None, TxPortId=None):
        # type: (str, str, bool, str, bool, int, str, List[str], bool, str) -> HighLevelStream
        """Adds a new highLevelStream resource on the json, only valid with batch add utility

        Args
        ----
        - Crc (str(badCrc | goodCrc)): The Cyclic Redundancy Check frame of the configured high level stream.
        - DestinationMacMode (str(arp | manual)): The mode in which the Destination MAC Address is configured, either manual or ARP.
        - Enabled (bool): 
        - Name (str): An alphanumeric string that returns the name of the field.
        - Pause (bool): If true then pause is enabled.
        - PreambleCustomSize (number): Customizes the preamble size of the frame.
        - PreambleFrameSizeMode (str(auto | custom)): The starting size of the frame.
        - RxPortIds (list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport])): A list of virtual ports that are the receiving ports
        - Suspend (bool): Suspends all traffic on this high level stream.
        - TxPortId (str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport)): The virtual port that is the transmitting port.

        Returns
        -------
        - self: This instance with all currently retrieved highLevelStream resources using find and the newly added highLevelStream resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AppliedFrameRate=None, AppliedFrameSize=None, AppliedPacketCount=None, Crc=None, CurrentPacketCount=None, DestinationMacMode=None, Distributions=None, Enabled=None, EncapsulationName=None, EndpointSetId=None, Name=None, OverSubscribed=None, Pause=None, PreambleCustomSize=None, PreambleFrameSizeMode=None, RxPortIds=None, RxPortNames=None, State=None, Suspend=None, TxPortId=None, TxPortName=None):
        """Finds and retrieves highLevelStream resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve highLevelStream resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all highLevelStream resources from the server.

        Args
        ----
        - AppliedFrameRate (str): 
        - AppliedFrameSize (str): (Read only) Indicates the applied frame size of the high level stream.
        - AppliedPacketCount (number): (Read only) Indicates the aplied packet count of the high level stream.
        - Crc (str(badCrc | goodCrc)): The Cyclic Redundancy Check frame of the configured high level stream.
        - CurrentPacketCount (number): (Read only) Denotes the number of packets.
        - DestinationMacMode (str(arp | manual)): The mode in which the Destination MAC Address is configured, either manual or ARP.
        - Distributions (list(dict(arg1:str,arg2:str))): Denotes the distribution of the high level stream.
        - Enabled (bool): 
        - EncapsulationName (str): Name of the configured encapsulation type.
        - EndpointSetId (number): The ID of the configured endpoint set.
        - Name (str): An alphanumeric string that returns the name of the field.
        - OverSubscribed (bool): If true, the rate is oversubscribed.
        - Pause (bool): If true then pause is enabled.
        - PreambleCustomSize (number): Customizes the preamble size of the frame.
        - PreambleFrameSizeMode (str(auto | custom)): The starting size of the frame.
        - RxPortIds (list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport])): A list of virtual ports that are the receiving ports
        - RxPortNames (list(str)): A list of names from the receiving virtual ports.
        - State (str): (Read only) Denotes the current state of the stream.
        - Suspend (bool): Suspends all traffic on this high level stream.
        - TxPortId (str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport)): The virtual port that is the transmitting port.
        - TxPortName (str): The name of the virtual port that is the transmitting port.

        Returns
        -------
        - self: This instance with matching highLevelStream resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of highLevelStream data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the highLevelStream resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def DeleteQuickFlowGroups(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the deleteQuickFlowGroups operation on the server.

        Deletes a list of quick flow groups.

        deleteQuickFlowGroups(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('deleteQuickFlowGroups', payload=payload, response_object=None)

    def DuplicateQuickFlowGroups(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the duplicateQuickFlowGroups operation on the server.

        Duplicate selected quick flows with the count provided.

        duplicateQuickFlowGroups(Arg2=number, async_operation=bool)
        -----------------------------------------------------------
        - Arg2 (number): Duplicate count
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('duplicateQuickFlowGroups', payload=payload, response_object=None)

    def GetPacketViewInHex(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getPacketViewInHex operation on the server.

        Gets packet in Hex format for selected highLevelstream and for the given packet index

        getPacketViewInHex(Arg2=number, async_operation=bool)string
        -----------------------------------------------------------
        - Arg2 (number): Packet Index (0 based)
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
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

    def PauseStatelessTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the pauseStatelessTraffic operation on the server.

        Pause or Resume stateless traffic.

        pauseStatelessTraffic(Arg2=bool, async_operation=bool)
        ------------------------------------------------------
        - Arg2 (bool): If true, it will pause running traffic. If false, it will resume previously paused traffic.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('pauseStatelessTraffic', payload=payload, response_object=None)

    def PreviewFlowPackets(self, *args, **kwargs):
        """Executes the previewFlowPackets operation on the server.

        Preview packets for selected highLevelstream

        previewFlowPackets(Arg2=number, Arg3=number, async_operation=bool)object
        ------------------------------------------------------------------------
        - Arg2 (number): 
        - Arg3 (number): 
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns dict(arg1:number,arg2:number,arg3:list[str],arg4:list[list[str]]): No return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('previewFlowPackets', payload=payload, response_object=None)

    def StartStatelessTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startStatelessTraffic operation on the server.

        Start the traffic configuration for stateless traffic items only.

        startStatelessTraffic(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startStatelessTraffic', payload=payload, response_object=None)

    def StartStatelessTrafficBlocking(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startStatelessTrafficBlocking operation on the server.

        Start the traffic configuration for stateless traffic items only. This will block until traffic is fully started.

        startStatelessTrafficBlocking(async_operation=bool)
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startStatelessTrafficBlocking', payload=payload, response_object=None)

    def StopStatelessTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopStatelessTraffic operation on the server.

        Stop the stateless traffic items.

        stopStatelessTraffic(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopStatelessTraffic', payload=payload, response_object=None)

    def StopStatelessTrafficBlocking(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopStatelessTrafficBlocking operation on the server.

        Stop the traffic configuration for stateless traffic items only. This will block until traffic is fully stopped.

        stopStatelessTrafficBlocking(async_operation=bool)
        --------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopStatelessTrafficBlocking', payload=payload, response_object=None)
