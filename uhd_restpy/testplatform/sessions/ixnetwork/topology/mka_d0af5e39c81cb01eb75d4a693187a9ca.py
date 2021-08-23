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
from typing import List, Any, Union


class Mka(Base):
    """Mka Configuration
    The Mka class encapsulates a list of mka resources that are managed by the user.
    A list of resources can be retrieved from the server using the Mka.find() method.
    The list can be managed by using the Mka.add() and Mka.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'mka'
    _SDM_ATT_MAP = {
        'ActiveDevice': 'activeDevice',
        'AssociationNumber': 'associationNumber',
        'CakCount': 'cakCount',
        'CipherSuite': 'cipherSuite',
        'ConfidentialityOffset': 'confidentialityOffset',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DataPlaneParameters': 'dataPlaneParameters',
        'DelayProtect': 'delayProtect',
        'DescriptiveName': 'descriptiveName',
        'ElectedKeyServer': 'electedKeyServer',
        'Errors': 'errors',
        'KeyServerPriority': 'keyServerPriority',
        'KeyType': 'keyType',
        'LlpnStep': 'llpnStep',
        'MacsecCapability': 'macsecCapability',
        'MacsecDesired': 'macsecDesired',
        'MemberIdentifier': 'memberIdentifier',
        'MirroredMacAddr': 'mirroredMacAddr',
        'MkaHelloTime': 'mkaHelloTime',
        'MkaLifeTime': 'mkaLifeTime',
        'MkaVersion': 'mkaVersion',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'OlpnStep': 'olpnStep',
        'RandomizeMemberIdentifier': 'randomizeMemberIdentifier',
        'RekeyThresholdPN': 'rekeyThresholdPN',
        'RekeyThresholdXPN': 'rekeyThresholdXPN',
        'Sak': 'sak',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StartingDistributedAN': 'startingDistributedAN',
        'StartingKeyNumber': 'startingKeyNumber',
        'StartingLLPN': 'startingLLPN',
        'StartingOLPN': 'startingOLPN',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TxChannelCount': 'txChannelCount',
    }
    _SDM_ENUM_MAP = {
        'keyType': ['psk'],
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(Mka, self).__init__(parent, list_op)

    @property
    def CakCache(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.cakcache_9d23d3bf0d5a4d71a4e75ece8ff0a1ea.CakCache): An instance of the CakCache class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.cakcache_9d23d3bf0d5a4d71a4e75ece8ff0a1ea import CakCache
        if self._properties.get('CakCache', None) is not None:
            return self._properties.get('CakCache')
        else:
            return CakCache(self)._select()

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        if self._properties.get('LearnedInfo', None) is not None:
            return self._properties.get('LearnedInfo')
        else:
            return LearnedInfo(self)

    @property
    def TxChannels(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.txchannels_a961f7f036af2edebf4e1957fed8ab53.TxChannels): An instance of the TxChannels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.txchannels_a961f7f036af2edebf4e1957fed8ab53 import TxChannels
        if self._properties.get('TxChannels', None) is not None:
            return self._properties.get('TxChannels')
        else:
            return TxChannels(self)._select()

    @property
    def ActiveDevice(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines whether a MKA device is active or not. If disabled, MKA will not be started on the device.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveDevice']))

    @property
    def AssociationNumber(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Displays the Association Number for the received SAK.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AssociationNumber'])

    @property
    def CakCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: CAK Cache Size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CakCount'])

    @property
    def CipherSuite(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the type of cipher suite.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CipherSuite']))

    @property
    def ConfidentialityOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the confidentiality offset.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfidentialityOffset']))

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DataPlaneParameters(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): By default MACsec data plane parameters (eg. LLPN, OLPN, LRX, ORX, LTX, OTX) will be learned from the underlying MAC layer as per MACSec data traffic Tx/Rx status. If MACSec traffic is not running (User is only doing MKA conformance test w/o MACSec traffic), then these variables need to be configured manually. Such variables are grouped into the page Data Plane Parameters, so it can be either Learned or Simulated.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataPlaneParameters']))

    @property
    def DelayProtect(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Delay Protect behavior of the device.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayProtect']))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def ElectedKeyServer(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Denotes whether this device has been elected as a Key Server or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ElectedKeyServer'])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def KeyServerPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the Key Server Priority.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['KeyServerPriority']))

    @property
    def KeyType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(psk): Indicates the source of CAK.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyType'])
    @KeyType.setter
    def KeyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['KeyType'], value)

    @property
    def LlpnStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the LLPN Step.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LlpnStep']))

    @property
    def MacsecCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates MACsec capabilities.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacsecCapability']))

    @property
    def MacsecDesired(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines whether MACsec is desired or not. It is advertised in periodic hellos.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacsecDesired']))

    @property
    def MemberIdentifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - list(obj(uhd_restpy.multivalue.Multivalue)): Displays the Member Identifier calculated by the state machine.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MemberIdentifier']))

    @property
    def MirroredMacAddr(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): MAC address of the Ethernet devices configured in the Ethernet stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MirroredMacAddr'])

    @property
    def MkaHelloTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates MKA Hello Time.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MkaHelloTime']))

    @property
    def MkaLifeTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates MKA Life Time of a Peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MkaLifeTime'])
    @MkaLifeTime.setter
    def MkaLifeTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MkaLifeTime'], value)

    @property
    def MkaVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates the version of MKA.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MkaVersion']))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OlpnStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the OLPN Step.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OlpnStep']))

    @property
    def RandomizeMemberIdentifier(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomizeMemberIdentifier'])
    @RandomizeMemberIdentifier.setter
    def RandomizeMemberIdentifier(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['RandomizeMemberIdentifier'], value)

    @property
    def RekeyThresholdPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the PN rekey threshold.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RekeyThresholdPN']))

    @property
    def RekeyThresholdXPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the XPN rekey threshold.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RekeyThresholdXPN']))

    @property
    def Sak(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Displays the SAK received from the Key Server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Sak'])

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StartingDistributedAN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines starting distributed AN.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingDistributedAN']))

    @property
    def StartingKeyNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Determines the starting key number.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingKeyNumber']))

    @property
    def StartingLLPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates the starting LLPN.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingLLPN']))

    @property
    def StartingOLPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates the starting OLPN.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingOLPN']))

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def TxChannelCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Determines the number of Tx Channels configured for each device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxChannelCount'])

    def update(self, ConnectedVia=None, KeyType=None, MkaLifeTime=None, Multiplier=None, Name=None, RandomizeMemberIdentifier=None, StackedLayers=None):
        # type: (List[str], str, int, int, str, bool, List[str]) -> Mka
        """Updates mka resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - KeyType (str(psk)): Indicates the source of CAK.
        - MkaLifeTime (number): Indicates MKA Life Time of a Peer.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RandomizeMemberIdentifier (bool): If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, KeyType=None, MkaLifeTime=None, Multiplier=None, Name=None, RandomizeMemberIdentifier=None, StackedLayers=None):
        # type: (List[str], str, int, int, str, bool, List[str]) -> Mka
        """Adds a new mka resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - KeyType (str(psk)): Indicates the source of CAK.
        - MkaLifeTime (number): Indicates MKA Life Time of a Peer.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RandomizeMemberIdentifier (bool): If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved mka resources using find and the newly added mka resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mka resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AssociationNumber=None, CakCount=None, ConnectedVia=None, Count=None, DescriptiveName=None, ElectedKeyServer=None, Errors=None, KeyType=None, MirroredMacAddr=None, MkaLifeTime=None, Multiplier=None, Name=None, RandomizeMemberIdentifier=None, Sak=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, TxChannelCount=None):
        """Finds and retrieves mka resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mka resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mka resources from the server.

        Args
        ----
        - AssociationNumber (list(str)): Displays the Association Number for the received SAK.
        - CakCount (number): CAK Cache Size.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - ElectedKeyServer (list(str)): Denotes whether this device has been elected as a Key Server or not.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - KeyType (str(psk)): Indicates the source of CAK.
        - MirroredMacAddr (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
        - MkaLifeTime (number): Indicates MKA Life Time of a Peer.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RandomizeMemberIdentifier (bool): If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        - Sak (list(str)): Displays the SAK received from the Key Server.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TxChannelCount (number): Determines the number of Tx Channels configured for each device.

        Returns
        -------
        - self: This instance with matching mka resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mka data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mka resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def ClearAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedInfo(async_operation=bool)
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedInfo(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedInfo(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedInfo(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def GetLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getLearnedInfo operation on the server.

        Get Learned Info.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLearnedInfo(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getLearnedInfo', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, ActiveDevice=None, CipherSuite=None, ConfidentialityOffset=None, DataPlaneParameters=None, DelayProtect=None, KeyServerPriority=None, LlpnStep=None, MacsecCapability=None, MacsecDesired=None, MemberIdentifier=None, MkaHelloTime=None, MkaVersion=None, OlpnStep=None, RekeyThresholdPN=None, RekeyThresholdXPN=None, StartingDistributedAN=None, StartingKeyNumber=None, StartingLLPN=None, StartingOLPN=None):
        """Base class infrastructure that gets a list of mka device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveDevice (str): optional regex of activeDevice
        - CipherSuite (str): optional regex of cipherSuite
        - ConfidentialityOffset (str): optional regex of confidentialityOffset
        - DataPlaneParameters (str): optional regex of dataPlaneParameters
        - DelayProtect (str): optional regex of delayProtect
        - KeyServerPriority (str): optional regex of keyServerPriority
        - LlpnStep (str): optional regex of llpnStep
        - MacsecCapability (str): optional regex of macsecCapability
        - MacsecDesired (str): optional regex of macsecDesired
        - MemberIdentifier (str): optional regex of memberIdentifier
        - MkaHelloTime (str): optional regex of mkaHelloTime
        - MkaVersion (str): optional regex of mkaVersion
        - OlpnStep (str): optional regex of olpnStep
        - RekeyThresholdPN (str): optional regex of rekeyThresholdPN
        - RekeyThresholdXPN (str): optional regex of rekeyThresholdXPN
        - StartingDistributedAN (str): optional regex of startingDistributedAN
        - StartingKeyNumber (str): optional regex of startingKeyNumber
        - StartingLLPN (str): optional regex of startingLLPN
        - StartingOLPN (str): optional regex of startingOLPN

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
