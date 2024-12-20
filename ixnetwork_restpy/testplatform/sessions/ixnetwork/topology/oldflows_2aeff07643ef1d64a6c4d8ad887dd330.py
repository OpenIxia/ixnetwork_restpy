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


class Oldflows(Base):
    """DEPRECATED RoCE Flow settings
    The Oldflows class encapsulates a list of oldflows resources that are managed by the user.
    A list of resources can be retrieved from the server using the Oldflows.find() method.
    The list can be managed by using the Oldflows.add() and Oldflows.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "oldflows"
    _SDM_ATT_MAP = {
        "AllPeersAdded": "allPeersAdded",
        "BufferSize": "bufferSize",
        "BufferSizeRemote": "bufferSizeRemote",
        "BufferSizeUnit": "bufferSizeUnit",
        "BufferSizeUnitRemote": "bufferSizeUnitRemote",
        "Count": "count",
        "CustomQP": "customQP",
        "CustomizeQP": "customizeQP",
        "DescriptiveName": "descriptiveName",
        "Dscp": "dscp",
        "DscpRemote": "dscpRemote",
        "EcnVal": "ecnVal",
        "EcnValRemote": "ecnValRemote",
        "ExecuteCommands": "executeCommands",
        "ExecuteCommandsRemote": "executeCommandsRemote",
        "FlowLoaded": "flowLoaded",
        "FlowType": "flowType",
        "ImmidtData": "immidtData",
        "ImmidtDataRemote": "immidtDataRemote",
        "InitialPSN": "initialPSN",
        "InitialPSNRemote": "initialPSNRemote",
        "LocalPeer": "localPeer",
        "LocalPeerRemote": "localPeerRemote",
        "LocalPeerRemoteList": "localPeerRemoteList",
        "MessageSize": "messageSize",
        "MessageSizeRemote": "messageSizeRemote",
        "MessageSizeUnit": "messageSizeUnit",
        "MessageSizeUnitRemote": "messageSizeUnitRemote",
        "Name": "name",
        "PeerNameList": "peerNameList",
        "QPNumber": "qPNumber",
        "RemoteEndPoint": "remoteEndPoint",
        "RemoteKey": "remoteKey",
        "RemotePeer": "remotePeer",
        "RemotePeerList": "remotePeerList",
        "RemotePeerRemote": "remotePeerRemote",
        "RemoteQP": "remoteQP",
        "RemoteVA": "remoteVA",
        "UdpSourcePort": "udpSourcePort",
        "UdpSourcePortRemote": "udpSourcePortRemote",
    }
    _SDM_ENUM_MAP = {
        "flowType": ["twoArm", "oneArm"],
    }

    def __init__(self, parent, list_op=False):
        super(Oldflows, self).__init__(parent, list_op)

    @property
    def AllPeersAdded(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ResourceManager usage only - clear before adding to peerNameList, set to true once peerNameList is populated
        """
        return self._get_attribute(self._SDM_ATT_MAP["AllPeersAdded"])

    @AllPeersAdded.setter
    def AllPeersAdded(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AllPeersAdded"], value)

    @property
    def BufferSize(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Length of Buffer that needs to be transmitted to the remote end-point
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BufferSize"]))

    @property
    def BufferSizeRemote(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Length of Buffer that needs to be transmitted to the remote end-point
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BufferSizeRemote"])
        )

    @property
    def BufferSizeUnit(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Buffer Size Unit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BufferSizeUnit"])
        )

    @property
    def BufferSizeUnitRemote(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Buffer Size Unit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BufferSizeUnitRemote"])
        )

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
    def CustomQP(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allow users to configure custom QP for this flow.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CustomQP"]))

    @property
    def CustomizeQP(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Allow users to configure custom QP for this flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomizeQP"])

    @CustomizeQP.setter
    def CustomizeQP(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomizeQP"], value)

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
    def Dscp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSCP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Dscp"]))

    @property
    def DscpRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSCP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DscpRemote"]))

    @property
    def EcnVal(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ECN
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EcnVal"]))

    @property
    def EcnValRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ECN
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EcnValRemote"]))

    @property
    def ExecuteCommands(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Execute Commands
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExecuteCommands"])
        )

    @property
    def ExecuteCommandsRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Execute Commands
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExecuteCommandsRemote"])
        )

    @property
    def FlowLoaded(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To detect end of flow load through scriptgen.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlowLoaded"]))

    @property
    def FlowType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(twoArm | oneArm): Flow Type
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowType"])

    @FlowType.setter
    def FlowType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowType"], value)

    @property
    def ImmidtData(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Immediate Data field required for SEND/WRITE with Immediate verb
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ImmidtData"]))

    @property
    def ImmidtDataRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Immediate Data field required for SEND/WRITE with Immediate verb
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ImmidtDataRemote"])
        )

    @property
    def InitialPSN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initial PSN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["InitialPSN"]))

    @property
    def InitialPSNRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initial PSN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InitialPSNRemote"])
        )

    @property
    def LocalPeer(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Local Peer Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPeer"])

    @property
    def LocalPeerRemote(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Local Peer Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPeerRemote"])

    @property
    def LocalPeerRemoteList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Local Peer Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPeerRemoteList"])

    @property
    def MessageSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Length of Message that needs to be transmitted to the remote end-point
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MessageSize"]))

    @property
    def MessageSizeRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Length of Message that needs to be transmitted to the remote end-point
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageSizeRemote"])
        )

    @property
    def MessageSizeUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Message Size Unit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageSizeUnit"])
        )

    @property
    def MessageSizeUnitRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Message Size Unit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageSizeUnitRemote"])
        )

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
    def PeerNameList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str):
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerNameList"])

    @PeerNameList.setter
    def PeerNameList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeerNameList"], value)

    @property
    def QPNumber(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Auto Assigned QP Number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QPNumber"])

    @property
    def RemoteEndPoint(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Name of Remote RoCE protocol stack
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteEndPoint"])

    @RemoteEndPoint.setter
    def RemoteEndPoint(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteEndPoint"], value)

    @property
    def RemoteKey(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote Key.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemoteKey"]))

    @property
    def RemotePeer(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Remote Peer Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemotePeer"])

    @property
    def RemotePeerList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Remote Peer Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemotePeerList"])

    @property
    def RemotePeerRemote(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Remote Peer Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemotePeerRemote"])

    @property
    def RemoteQP(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote QP Number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemoteQP"]))

    @property
    def RemoteVA(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote Virtual Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemoteVA"]))

    @property
    def UdpSourcePort(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP Source Port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UdpSourcePort"]))

    @property
    def UdpSourcePortRemote(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP Source Port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UdpSourcePortRemote"])
        )

    def update(
        self,
        AllPeersAdded=None,
        CustomizeQP=None,
        FlowType=None,
        Name=None,
        PeerNameList=None,
        RemoteEndPoint=None,
    ):
        # type: (bool, bool, str, str, List[str], str) -> Oldflows
        """Updates oldflows resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AllPeersAdded (bool): ResourceManager usage only - clear before adding to peerNameList, set to true once peerNameList is populated
        - CustomizeQP (bool): Allow users to configure custom QP for this flow.
        - FlowType (str(twoArm | oneArm)): Flow Type
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerNameList (list(str)):
        - RemoteEndPoint (str): Name of Remote RoCE protocol stack

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AllPeersAdded=None,
        CustomizeQP=None,
        FlowType=None,
        Name=None,
        PeerNameList=None,
        RemoteEndPoint=None,
    ):
        # type: (bool, bool, str, str, List[str], str) -> Oldflows
        """Adds a new oldflows resource on the server and adds it to the container.

        Args
        ----
        - AllPeersAdded (bool): ResourceManager usage only - clear before adding to peerNameList, set to true once peerNameList is populated
        - CustomizeQP (bool): Allow users to configure custom QP for this flow.
        - FlowType (str(twoArm | oneArm)): Flow Type
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerNameList (list(str)):
        - RemoteEndPoint (str): Name of Remote RoCE protocol stack

        Returns
        -------
        - self: This instance with all currently retrieved oldflows resources using find and the newly added oldflows resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained oldflows resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AllPeersAdded=None,
        Count=None,
        CustomizeQP=None,
        DescriptiveName=None,
        FlowType=None,
        LocalPeer=None,
        LocalPeerRemote=None,
        LocalPeerRemoteList=None,
        Name=None,
        PeerNameList=None,
        QPNumber=None,
        RemoteEndPoint=None,
        RemotePeer=None,
        RemotePeerList=None,
        RemotePeerRemote=None,
    ):
        # type: (bool, int, bool, str, str, str, str, List[str], str, List[str], List[str], str, str, List[str], str) -> Oldflows
        """Finds and retrieves oldflows resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve oldflows resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all oldflows resources from the server.

        Args
        ----
        - AllPeersAdded (bool): ResourceManager usage only - clear before adding to peerNameList, set to true once peerNameList is populated
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - CustomizeQP (bool): Allow users to configure custom QP for this flow.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - FlowType (str(twoArm | oneArm)): Flow Type
        - LocalPeer (str): Local Peer Name.
        - LocalPeerRemote (str): Local Peer Name.
        - LocalPeerRemoteList (list(str)): Local Peer Name.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerNameList (list(str)):
        - QPNumber (list(str)): Auto Assigned QP Number.
        - RemoteEndPoint (str): Name of Remote RoCE protocol stack
        - RemotePeer (str): Remote Peer Name.
        - RemotePeerList (list(str)): Remote Peer Name.
        - RemotePeerRemote (str): Remote Peer Name.

        Returns
        -------
        - self: This instance with matching oldflows resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of oldflows data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the oldflows resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        DEPRECATED addDeleteTags(Arg2=bool, async_operation=bool)
        ---------------------------------------------------------
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

    def get_device_ids(
        self,
        PortNames=None,
        BufferSize=None,
        BufferSizeRemote=None,
        BufferSizeUnit=None,
        BufferSizeUnitRemote=None,
        CustomQP=None,
        Dscp=None,
        DscpRemote=None,
        EcnVal=None,
        EcnValRemote=None,
        ExecuteCommands=None,
        ExecuteCommandsRemote=None,
        FlowLoaded=None,
        ImmidtData=None,
        ImmidtDataRemote=None,
        InitialPSN=None,
        InitialPSNRemote=None,
        MessageSize=None,
        MessageSizeRemote=None,
        MessageSizeUnit=None,
        MessageSizeUnitRemote=None,
        RemoteKey=None,
        RemoteQP=None,
        RemoteVA=None,
        UdpSourcePort=None,
        UdpSourcePortRemote=None,
    ):
        """Base class infrastructure that gets a list of oldflows device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BufferSize (str): optional regex of bufferSize
        - BufferSizeRemote (str): optional regex of bufferSizeRemote
        - BufferSizeUnit (str): optional regex of bufferSizeUnit
        - BufferSizeUnitRemote (str): optional regex of bufferSizeUnitRemote
        - CustomQP (str): optional regex of customQP
        - Dscp (str): optional regex of dscp
        - DscpRemote (str): optional regex of dscpRemote
        - EcnVal (str): optional regex of ecnVal
        - EcnValRemote (str): optional regex of ecnValRemote
        - ExecuteCommands (str): optional regex of executeCommands
        - ExecuteCommandsRemote (str): optional regex of executeCommandsRemote
        - FlowLoaded (str): optional regex of flowLoaded
        - ImmidtData (str): optional regex of immidtData
        - ImmidtDataRemote (str): optional regex of immidtDataRemote
        - InitialPSN (str): optional regex of initialPSN
        - InitialPSNRemote (str): optional regex of initialPSNRemote
        - MessageSize (str): optional regex of messageSize
        - MessageSizeRemote (str): optional regex of messageSizeRemote
        - MessageSizeUnit (str): optional regex of messageSizeUnit
        - MessageSizeUnitRemote (str): optional regex of messageSizeUnitRemote
        - RemoteKey (str): optional regex of remoteKey
        - RemoteQP (str): optional regex of remoteQP
        - RemoteVA (str): optional regex of remoteVA
        - UdpSourcePort (str): optional regex of udpSourcePort
        - UdpSourcePortRemote (str): optional regex of udpSourcePortRemote

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
