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

    def __init__(self, parent):
        super(Mka, self).__init__(parent)

    @property
    def CakCache(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cakcache_9d23d3bf0d5a4d71a4e75ece8ff0a1ea.CakCache): An instance of the CakCache class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cakcache_9d23d3bf0d5a4d71a4e75ece8ff0a1ea import CakCache
        return CakCache(self)._select()

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        return LearnedInfo(self)

    @property
    def TxChannels(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.txchannels_a961f7f036af2edebf4e1957fed8ab53.TxChannels): An instance of the TxChannels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.txchannels_a961f7f036af2edebf4e1957fed8ab53 import TxChannels
        return TxChannels(self)._select()

    @property
    def ActiveDevice(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether a MKA device is active or not. If disabled, MKA will not be started on the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveDevice']))

    @property
    def AssociationNumber(self):
        """
        Returns
        -------
        - list(str): Displays the Association Number for the received SAK.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AssociationNumber'])

    @property
    def CakCount(self):
        """
        Returns
        -------
        - number: CAK Cache Size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CakCount'])

    @property
    def CipherSuite(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the type of cipher suite.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CipherSuite']))

    @property
    def ConfidentialityOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the confidentiality offset.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfidentialityOffset']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DataPlaneParameters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): By default MACsec data plane parameters (eg. LLPN, OLPN, LRX, ORX, LTX, OTX) will be learned from the underlying MAC layer as per MACSec data traffic Tx/Rx status. If MACSec traffic is not running (User is only doing MKA conformance test w/o MACSec traffic), then these variables need to be configured manually. Such variables are grouped into the page Data Plane Parameters, so it can be either Learned or Simulated.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataPlaneParameters']))

    @property
    def DelayProtect(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay Protect behavior of the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayProtect']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def ElectedKeyServer(self):
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
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the Key Server Priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['KeyServerPriority']))

    @property
    def KeyType(self):
        """
        Returns
        -------
        - str(psk): Indicates the source of CAK.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyType'])
    @KeyType.setter
    def KeyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeyType'], value)

    @property
    def LlpnStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the LLPN Step.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LlpnStep']))

    @property
    def MacsecCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates MACsec capabilities.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacsecCapability']))

    @property
    def MacsecDesired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether MACsec is desired or not. It is advertised in periodic hellos.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacsecDesired']))

    @property
    def MemberIdentifier(self):
        """
        Returns
        -------
        - list(obj(ixnetwork_restpy.multivalue.Multivalue)): Displays the Member Identifier calculated by the state machine.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MemberIdentifier']))

    @property
    def MirroredMacAddr(self):
        """
        Returns
        -------
        - list(str): MAC address of the Ethernet devices configured in the Ethernet stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MirroredMacAddr'])

    @property
    def MkaHelloTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates MKA Hello Time.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MkaHelloTime']))

    @property
    def MkaLifeTime(self):
        """
        Returns
        -------
        - number: Indicates MKA Life Time of a Peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MkaLifeTime'])
    @MkaLifeTime.setter
    def MkaLifeTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MkaLifeTime'], value)

    @property
    def MkaVersion(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the version of MKA.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MkaVersion']))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OlpnStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the OLPN Step.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OlpnStep']))

    @property
    def RandomizeMemberIdentifier(self):
        """
        Returns
        -------
        - bool: If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomizeMemberIdentifier'])
    @RandomizeMemberIdentifier.setter
    def RandomizeMemberIdentifier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RandomizeMemberIdentifier'], value)

    @property
    def RekeyThresholdPN(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the PN rekey threshold.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RekeyThresholdPN']))

    @property
    def RekeyThresholdXPN(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the XPN rekey threshold.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RekeyThresholdXPN']))

    @property
    def Sak(self):
        """
        Returns
        -------
        - list(str): Displays the SAK received from the Key Server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Sak'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StartingDistributedAN(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines starting distributed AN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingDistributedAN']))

    @property
    def StartingKeyNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the starting key number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingKeyNumber']))

    @property
    def StartingLLPN(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the starting LLPN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingLLPN']))

    @property
    def StartingOLPN(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the starting OLPN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
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
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def TxChannelCount(self):
        """
        Returns
        -------
        - number: Determines the number of Tx Channels configured for each device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxChannelCount'])

    def update(self, ConnectedVia=None, KeyType=None, MkaLifeTime=None, Multiplier=None, Name=None, RandomizeMemberIdentifier=None, StackedLayers=None):
        """Updates mka resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
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
        """Adds a new mka resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
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
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
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

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

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
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedInfo(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        clearAllLearnedInfo(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        clearAllLearnedInfo(Arg2=list)list
        ----------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        """Executes the getLearnedInfo operation on the server.

        Get Learned Info.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLearnedInfo(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getLearnedInfo(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getLearnedInfo(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

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
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

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
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
