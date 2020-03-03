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


class StaticMacsec(Base):
    """Static MACsec
    The StaticMacsec class encapsulates a list of staticMacsec resources that is be managed by the user.
    A list of resources can be retrieved from the server using the StaticMacsec.find() method.
    The list can be managed by the user by using the StaticMacsec.add() and StaticMacsec.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'staticMacsec'

    def __init__(self, parent):
        super(StaticMacsec, self).__init__(parent)

    @property
    def Connector(self):
        """An instance of the Connector class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
        return Connector(self)

    @property
    def InnerVlanList(self):
        """An instance of the InnerVlanList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.innervlanlist.InnerVlanList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.innervlanlist import InnerVlanList
        return InnerVlanList(self)

    @property
    def Ipv4(self):
        """An instance of the Ipv4 class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4.Ipv4)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4 import Ipv4
        return Ipv4(self)

    @property
    def Ipv6(self):
        """An instance of the Ipv6 class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6.Ipv6)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6 import Ipv6
        return Ipv6(self)

    @property
    def RxSakPool(self):
        """An instance of the RxSakPool class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rxsakpool.RxSakPool)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rxsakpool import RxSakPool
        return RxSakPool(self)._select()

    @property
    def TxSakPool(self):
        """An instance of the TxSakPool class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.txsakpool.TxSakPool)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.txsakpool import TxSakPool
        return TxSakPool(self)._select()

    @property
    def ActiveDevice(self):
        """Determines whether a MACsec device is active or not. If disabled, MACsec will not be started on the device.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('activeDevice')

    @property
    def CipherSuite(self):
        """The type of cipher suite. Options include: 1) AES-128 2) AES-256

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cipherSuite')

    @property
    def ConfidentialityOffset(self):
        """Determines the confidentiality offset for both transmit and receive channel.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('confidentialityOffset')

    @property
    def ConnectedVia(self):
        """DEPRECATED List of layers this layer used to connect to the wire

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('connectedVia')
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute('connectedVia', value)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def DutMac(self):
        """MAC address of the connected interface of the DUT to be used as Gateway MAC for IP traffic.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dutMac')

    @property
    def DutSciMac(self):
        """MAC component of SCI with which MACsec traffic is expected from the DUT.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dutSciMac')

    @property
    def DutSciPortId(self):
        """Port ID component of SCI with which MACsec traffic is expected from the DUT.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dutSciPortId')

    @property
    def EnableConfidentiality(self):
        """Determines whether transmitted MACsec payload is encrypted or not.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableConfidentiality')

    @property
    def EncryptedVlanCount(self):
        """Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.

        Returns:
            number
        """
        return self._get_attribute('encryptedVlanCount')
    @EncryptedVlanCount.setter
    def EncryptedVlanCount(self, value):
        self._set_attribute('encryptedVlanCount', value)

    @property
    def EncryptionEngine(self):
        """Determines the set of MACsec functionalities supported by a Device Group. Hardware Based enables encryption of stateless L2-3 traffic at line rate, Software Based enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.

        Returns:
            str(softwareBased|hardwareBased)
        """
        return self._get_attribute('encryptionEngine')
    @EncryptionEngine.setter
    def EncryptionEngine(self, value):
        self._set_attribute('encryptionEngine', value)

    @property
    def Errors(self):
        """A list of errors that have occurred

        Returns:
            list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
        """
        return self._get_attribute('errors')

    @property
    def FixedPn(self):
        """Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.

        Returns:
            number
        """
        return self._get_attribute('fixedPn')
    @FixedPn.setter
    def FixedPn(self, value):
        self._set_attribute('fixedPn', value)

    @property
    def IncludeSci(self):
        """Determines whether SCI should be included in the SecTAG of the transmitted MACsec traffic.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeSci')

    @property
    def Multiplier(self):
        """Number of layer instances per parent instance (multiplier)

        Returns:
            number
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def OverrideTciSetting(self):
        """If enabled, the default TCI settings as per configuration will be allowed for overwriting. Used to simulate mal-configured SecTAG for negative testing.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('overrideTciSetting')

    @property
    def PeriodicRekeyAttempts(self):
        """Determines the number of times Rekey will happen after MACsec is started.

        Returns:
            number
        """
        return self._get_attribute('periodicRekeyAttempts')
    @PeriodicRekeyAttempts.setter
    def PeriodicRekeyAttempts(self, value):
        self._set_attribute('periodicRekeyAttempts', value)

    @property
    def PeriodicRekeyInterval(self):
        """Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.

        Returns:
            number
        """
        return self._get_attribute('periodicRekeyInterval')
    @PeriodicRekeyInterval.setter
    def PeriodicRekeyInterval(self, value):
        self._set_attribute('periodicRekeyInterval', value)

    @property
    def PortId(self):
        """Port ID component of SCI with which MACsec traffic is transmitted.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('portId')

    @property
    def RekeyBehaviour(self):
        """Determines the Rekey behavior.

        Returns:
            str(dontRekey|rekeyContinuous|rekeyFixedCount)
        """
        return self._get_attribute('rekeyBehaviour')
    @RekeyBehaviour.setter
    def RekeyBehaviour(self, value):
        self._set_attribute('rekeyBehaviour', value)

    @property
    def RxSakPoolSize(self):
        """Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.

        Returns:
            number
        """
        return self._get_attribute('rxSakPoolSize')
    @RxSakPoolSize.setter
    def RxSakPoolSize(self, value):
        self._set_attribute('rxSakPoolSize', value)

    @property
    def SendGratArp(self):
        """Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.

        Returns:
            bool
        """
        return self._get_attribute('sendGratArp')
    @SendGratArp.setter
    def SendGratArp(self, value):
        self._set_attribute('sendGratArp', value)

    @property
    def SessionStatus(self):
        """Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

        Returns:
            list(str[down|notStarted|up])
        """
        return self._get_attribute('sessionStatus')

    @property
    def SourceIp(self):
        """IP address of the MACsec device. Used as the source IP of the MACsec traffic generated by the device.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sourceIp')

    @property
    def SourceMac(self):
        """MAC address of the Ethernet devices configured in the Ethernet stack.

        Returns:
            list(str)
        """
        return self._get_attribute('sourceMac')

    @property
    def StackedLayers(self):
        """List of secondary (many to one) child layer protocols

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('stackedLayers')
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute('stackedLayers', value)

    @property
    def StateCounts(self):
        """A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

        Returns:
            dict(total:number,notStarted:number,down:number,up:number)
        """
        return self._get_attribute('stateCounts')

    @property
    def Status(self):
        """Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            str(configured|error|mixed|notStarted|started|starting|stopping)
        """
        return self._get_attribute('status')

    @property
    def SystemId(self):
        """System Identifier component of the SCI field with which MACsec traffic is transmitted.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('systemId')

    @property
    def TciCBit(self):
        """Determines the C bit in TCI field of SecTAG if Override TCI Settings is enabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tciCBit')

    @property
    def TciEBit(self):
        """Determines the E bit in TCI field of SecTAG if Override TCI Settings is enabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tciEBit')

    @property
    def TciEsBit(self):
        """Determines the ES bit in TCI field of SecTAG if Override TCI Settings is enabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tciEsBit')

    @property
    def TciScBit(self):
        """Determines the SC bit in TCI field of SecTAG if Override TCI Settings is enabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tciScBit')

    @property
    def TciScbBit(self):
        """Determines the SCB bit in TCI field of SecTAG if Override TCI Settings is enabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tciScbBit')

    @property
    def TxSakPoolSize(self):
        """Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Returns:
            number
        """
        return self._get_attribute('txSakPoolSize')
    @TxSakPoolSize.setter
    def TxSakPoolSize(self, value):
        self._set_attribute('txSakPoolSize', value)

    @property
    def Version(self):
        """Version bit in TCI field of SecTAG if Override TCI Settings is enabled.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('version')

    def update(self, ConnectedVia=None, EncryptedVlanCount=None, EncryptionEngine=None, FixedPn=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyBehaviour=None, RxSakPoolSize=None, SendGratArp=None, StackedLayers=None, TxSakPoolSize=None):
        """Updates a child instance of staticMacsec on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
            EncryptionEngine (str(softwareBased|hardwareBased)): Determines the set of MACsec functionalities supported by a Device Group. Hardware Based enables encryption of stateless L2-3 traffic at line rate, Software Based enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
            FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
            PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
            RekeyBehaviour (str(dontRekey|rekeyContinuous|rekeyFixedCount)): Determines the Rekey behavior.
            RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
            SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ConnectedVia=None, EncryptedVlanCount=None, EncryptionEngine=None, FixedPn=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyBehaviour=None, RxSakPoolSize=None, SendGratArp=None, StackedLayers=None, TxSakPoolSize=None):
        """Adds a new staticMacsec node on the server and retrieves it in this instance.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
            EncryptionEngine (str(softwareBased|hardwareBased)): Determines the set of MACsec functionalities supported by a Device Group. Hardware Based enables encryption of stateless L2-3 traffic at line rate, Software Based enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
            FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
            PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
            RekeyBehaviour (str(dontRekey|rekeyContinuous|rekeyFixedCount)): Determines the Rekey behavior.
            RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
            SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Returns:
            self: This instance with all currently retrieved staticMacsec data using find and the newly added staticMacsec data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the staticMacsec data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EncryptedVlanCount=None, EncryptionEngine=None, Errors=None, FixedPn=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyBehaviour=None, RxSakPoolSize=None, SendGratArp=None, SessionStatus=None, SourceMac=None, StackedLayers=None, StateCounts=None, Status=None, TxSakPoolSize=None):
        """Finds and retrieves staticMacsec data from the server.

        All named parameters support regex and can be used to selectively retrieve staticMacsec data from the server.
        By default the find method takes no parameters and will retrieve all staticMacsec data from the server.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
            EncryptionEngine (str(softwareBased|hardwareBased)): Determines the set of MACsec functionalities supported by a Device Group. Hardware Based enables encryption of stateless L2-3 traffic at line rate, Software Based enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
            Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
            FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
            PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
            RekeyBehaviour (str(dontRekey|rekeyContinuous|rekeyFixedCount)): Determines the Rekey behavior.
            RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
            SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
            SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
            SourceMac (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
            Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
            TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Returns:
            self: This instance with matching staticMacsec data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of staticMacsec data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the staticMacsec data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveDevice=None, CipherSuite=None, ConfidentialityOffset=None, DutMac=None, DutSciMac=None, DutSciPortId=None, EnableConfidentiality=None, IncludeSci=None, OverrideTciSetting=None, PortId=None, SourceIp=None, SystemId=None, TciCBit=None, TciEBit=None, TciEsBit=None, TciScBit=None, TciScbBit=None, Version=None):
        """Base class infrastructure that gets a list of staticMacsec device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            ActiveDevice (str): optional regex of activeDevice
            CipherSuite (str): optional regex of cipherSuite
            ConfidentialityOffset (str): optional regex of confidentialityOffset
            DutMac (str): optional regex of dutMac
            DutSciMac (str): optional regex of dutSciMac
            DutSciPortId (str): optional regex of dutSciPortId
            EnableConfidentiality (str): optional regex of enableConfidentiality
            IncludeSci (str): optional regex of includeSci
            OverrideTciSetting (str): optional regex of overrideTciSetting
            PortId (str): optional regex of portId
            SourceIp (str): optional regex of sourceIp
            SystemId (str): optional regex of systemId
            TciCBit (str): optional regex of tciCBit
            TciEBit (str): optional regex of tciEBit
            TciEsBit (str): optional regex of tciEsBit
            TciScBit (str): optional regex of tciScBit
            TciScbBit (str): optional regex of tciScbBit
            Version (str): optional regex of version

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        restartDown()

        restartDown(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        restartDown(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start selected protocols.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        start()

        start(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        start(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop selected protocols.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        stop()

        stop(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        stop(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
