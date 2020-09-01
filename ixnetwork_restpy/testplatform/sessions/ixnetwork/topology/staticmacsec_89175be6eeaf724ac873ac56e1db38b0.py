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


class StaticMacsec(Base):
    """Static MACsec
    The StaticMacsec class encapsulates a list of staticMacsec resources that are managed by the user.
    A list of resources can be retrieved from the server using the StaticMacsec.find() method.
    The list can be managed by using the StaticMacsec.add() and StaticMacsec.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'staticMacsec'
    _SDM_ATT_MAP = {
        'ActiveDevice': 'activeDevice',
        'CipherSuite': 'cipherSuite',
        'ConfidentialityOffset': 'confidentialityOffset',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DutMac': 'dutMac',
        'DutMsbOfXpn': 'dutMsbOfXpn',
        'DutSciMac': 'dutSciMac',
        'DutSciPortId': 'dutSciPortId',
        'EnableConfidentiality': 'enableConfidentiality',
        'EnableEncryptedVlan': 'enableEncryptedVlan',
        'EnableEncryptedVlans': 'enableEncryptedVlans',
        'EncryptedTrafficType': 'encryptedTrafficType',
        'EncryptedVlanCount': 'encryptedVlanCount',
        'EncryptionEngine': 'encryptionEngine',
        'EndStation': 'endStation',
        'Errors': 'errors',
        'FixedPn': 'fixedPn',
        'IncludeSci': 'includeSci',
        'Multiplier': 'multiplier',
        'MvFixedXpn': 'mvFixedXpn',
        'Name': 'name',
        'OverrideTciSetting': 'overrideTciSetting',
        'PeriodicRekeyAttempts': 'periodicRekeyAttempts',
        'PeriodicRekeyInterval': 'periodicRekeyInterval',
        'PortId': 'portId',
        'RekeyBehaviour': 'rekeyBehaviour',
        'RxSakPoolSize': 'rxSakPoolSize',
        'SendGratArp': 'sendGratArp',
        'SessionStatus': 'sessionStatus',
        'SourceIp': 'sourceIp',
        'SourceMac': 'sourceMac',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SystemId': 'systemId',
        'TciCBit': 'tciCBit',
        'TciEBit': 'tciEBit',
        'TciEsBit': 'tciEsBit',
        'TciScBit': 'tciScBit',
        'TciScbBit': 'tciScbBit',
        'TxSakPoolSize': 'txSakPoolSize',
        'Version': 'version',
    }

    def __init__(self, parent):
        super(StaticMacsec, self).__init__(parent)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

    @property
    def InnerVlanList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.innervlanlist_e709d209ac3f7ec472b5b8b70db9e853.InnerVlanList): An instance of the InnerVlanList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.innervlanlist_e709d209ac3f7ec472b5b8b70db9e853 import InnerVlanList
        return InnerVlanList(self)

    @property
    def Ipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4_8cb960b62ae85a03e1b40a57bfaeb7bb.Ipv4): An instance of the Ipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4_8cb960b62ae85a03e1b40a57bfaeb7bb import Ipv4
        return Ipv4(self)

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6_abda0a2a4cac3d529994b093916059a4.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6_abda0a2a4cac3d529994b093916059a4 import Ipv6
        return Ipv6(self)

    @property
    def RxSakPool(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rxsakpool_22340fe5cb5d81664cab595d3e6d08ef.RxSakPool): An instance of the RxSakPool class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rxsakpool_22340fe5cb5d81664cab595d3e6d08ef import RxSakPool
        return RxSakPool(self)._select()

    @property
    def TxSakPool(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.txsakpool_7ab8c0a10359fbab4d0c5bd3dab1bfb2.TxSakPool): An instance of the TxSakPool class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.txsakpool_7ab8c0a10359fbab4d0c5bd3dab1bfb2 import TxSakPool
        return TxSakPool(self)._select()

    @property
    def ActiveDevice(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether a MACsec device is active or not. If disabled, MACsec will not be started on the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveDevice']))

    @property
    def CipherSuite(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of cipher suite. Options include: 1) GCM-AES-128 2) GCM-AES-256 3) GCM-AES-XPN-128 4) GCM-AES-XPN-256
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CipherSuite']))

    @property
    def ConfidentialityOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the confidentiality offset for both transmit and receive channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfidentialityOffset']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
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
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DutMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MAC address of the connected interface of the DUT to be used as Gateway MAC for IP traffic.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DutMac']))

    @property
    def DutMsbOfXpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 32 most significant bits of the XPN that DUT will be using to construct the 64 bits XPN value when test starts.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DutMsbOfXpn']))

    @property
    def DutSciMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MAC component of SCI with which MACsec traffic is expected from the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DutSciMac']))

    @property
    def DutSciPortId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Port ID component of SCI with which MACsec traffic is expected from the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DutSciPortId']))

    @property
    def EnableConfidentiality(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether transmitted MACsec payload is encrypted or not.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableConfidentiality']))

    @property
    def EnableEncryptedVlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines if VLAN data is to be encrypted or not.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableEncryptedVlan']))

    @property
    def EnableEncryptedVlans(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables VLANs for the sessions.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableEncryptedVlans']))

    @property
    def EncryptedTrafficType(self):
        """
        Returns
        -------
        - str(statefulL47 | statelessL23): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EncryptedTrafficType'])
    @EncryptedTrafficType.setter
    def EncryptedTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EncryptedTrafficType'], value)

    @property
    def EncryptedVlanCount(self):
        """
        Returns
        -------
        - number: Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EncryptedVlanCount'])
    @EncryptedVlanCount.setter
    def EncryptedVlanCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EncryptedVlanCount'], value)

    @property
    def EncryptionEngine(self):
        """DEPRECATED 
        Returns
        -------
        - str(softwareBased | hardwareBased): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EncryptionEngine'])
    @EncryptionEngine.setter
    def EncryptionEngine(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EncryptionEngine'], value)

    @property
    def EndStation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether this device should act as the End Station.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndStation']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FixedPn(self):
        """
        Returns
        -------
        - number: Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedPn'])
    @FixedPn.setter
    def FixedPn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedPn'], value)

    @property
    def IncludeSci(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether SCI should be included in the SecTAG of the transmitted MACsec traffic.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSci']))

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
    def MvFixedXpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 8 bytes PN with which all packets will be sent out.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvFixedXpn']))

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
    def OverrideTciSetting(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the default TCI settings as per configuration will be allowed for overwriting. Used to simulate mal-configured SecTAG for negative testing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverrideTciSetting']))

    @property
    def PeriodicRekeyAttempts(self):
        """
        Returns
        -------
        - number: Determines the number of times Rekey will happen after MACsec is started.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeriodicRekeyAttempts'])
    @PeriodicRekeyAttempts.setter
    def PeriodicRekeyAttempts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeriodicRekeyAttempts'], value)

    @property
    def PeriodicRekeyInterval(self):
        """
        Returns
        -------
        - number: Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeriodicRekeyInterval'])
    @PeriodicRekeyInterval.setter
    def PeriodicRekeyInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeriodicRekeyInterval'], value)

    @property
    def PortId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Port ID component of SCI with which MACsec traffic is transmitted.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortId']))

    @property
    def RekeyBehaviour(self):
        """
        Returns
        -------
        - str(dontRekey | rekeyContinuous | rekeyFixedCount): Determines the Rekey behavior.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RekeyBehaviour'])
    @RekeyBehaviour.setter
    def RekeyBehaviour(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RekeyBehaviour'], value)

    @property
    def RxSakPoolSize(self):
        """
        Returns
        -------
        - number: Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxSakPoolSize'])
    @RxSakPoolSize.setter
    def RxSakPoolSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RxSakPoolSize'], value)

    @property
    def SendGratArp(self):
        """
        Returns
        -------
        - bool: Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendGratArp'])
    @SendGratArp.setter
    def SendGratArp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendGratArp'], value)

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SourceIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP address of the MACsec device. Used as the source IP of the MACsec traffic generated by the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIp']))

    @property
    def SourceMac(self):
        """
        Returns
        -------
        - list(str): MAC address of the Ethernet devices configured in the Ethernet stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceMac'])

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
    def SystemId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): System Identifier component of the SCI field with which MACsec traffic is transmitted.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SystemId']))

    @property
    def TciCBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the C bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciCBit']))

    @property
    def TciEBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the E bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciEBit']))

    @property
    def TciEsBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the ES bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciEsBit']))

    @property
    def TciScBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the SC bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciScBit']))

    @property
    def TciScbBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the SCB bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciScbBit']))

    @property
    def TxSakPoolSize(self):
        """
        Returns
        -------
        - number: Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxSakPoolSize'])
    @TxSakPoolSize.setter
    def TxSakPoolSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxSakPoolSize'], value)

    @property
    def Version(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Version bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    def update(self, ConnectedVia=None, EncryptedTrafficType=None, EncryptedVlanCount=None, EncryptionEngine=None, FixedPn=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyBehaviour=None, RxSakPoolSize=None, SendGratArp=None, StackedLayers=None, TxSakPoolSize=None):
        """Updates staticMacsec resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EncryptedTrafficType (str(statefulL47 | statelessL23)): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        - EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
        - EncryptionEngine (str(softwareBased | hardwareBased)): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        - FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EncryptedTrafficType=None, EncryptedVlanCount=None, EncryptionEngine=None, FixedPn=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyBehaviour=None, RxSakPoolSize=None, SendGratArp=None, StackedLayers=None, TxSakPoolSize=None):
        """Adds a new staticMacsec resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EncryptedTrafficType (str(statefulL47 | statelessL23)): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        - EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
        - EncryptionEngine (str(softwareBased | hardwareBased)): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        - FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Returns
        -------
        - self: This instance with all currently retrieved staticMacsec resources using find and the newly added staticMacsec resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained staticMacsec resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EncryptedTrafficType=None, EncryptedVlanCount=None, EncryptionEngine=None, Errors=None, FixedPn=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyBehaviour=None, RxSakPoolSize=None, SendGratArp=None, SessionStatus=None, SourceMac=None, StackedLayers=None, StateCounts=None, Status=None, TxSakPoolSize=None):
        """Finds and retrieves staticMacsec resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve staticMacsec resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all staticMacsec resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EncryptedTrafficType (str(statefulL47 | statelessL23)): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        - EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
        - EncryptionEngine (str(softwareBased | hardwareBased)): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SourceMac (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Returns
        -------
        - self: This instance with matching staticMacsec resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of staticMacsec data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the staticMacsec resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveDevice=None, CipherSuite=None, ConfidentialityOffset=None, DutMac=None, DutMsbOfXpn=None, DutSciMac=None, DutSciPortId=None, EnableConfidentiality=None, EnableEncryptedVlan=None, EnableEncryptedVlans=None, EndStation=None, IncludeSci=None, MvFixedXpn=None, OverrideTciSetting=None, PortId=None, SourceIp=None, SystemId=None, TciCBit=None, TciEBit=None, TciEsBit=None, TciScBit=None, TciScbBit=None, Version=None):
        """Base class infrastructure that gets a list of staticMacsec device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveDevice (str): optional regex of activeDevice
        - CipherSuite (str): optional regex of cipherSuite
        - ConfidentialityOffset (str): optional regex of confidentialityOffset
        - DutMac (str): optional regex of dutMac
        - DutMsbOfXpn (str): optional regex of dutMsbOfXpn
        - DutSciMac (str): optional regex of dutSciMac
        - DutSciPortId (str): optional regex of dutSciPortId
        - EnableConfidentiality (str): optional regex of enableConfidentiality
        - EnableEncryptedVlan (str): optional regex of enableEncryptedVlan
        - EnableEncryptedVlans (str): optional regex of enableEncryptedVlans
        - EndStation (str): optional regex of endStation
        - IncludeSci (str): optional regex of includeSci
        - MvFixedXpn (str): optional regex of mvFixedXpn
        - OverrideTciSetting (str): optional regex of overrideTciSetting
        - PortId (str): optional regex of portId
        - SourceIp (str): optional regex of sourceIp
        - SystemId (str): optional regex of systemId
        - TciCBit (str): optional regex of tciCBit
        - TciEBit (str): optional regex of tciEBit
        - TciEsBit (str): optional regex of tciEsBit
        - TciScBit (str): optional regex of tciScBit
        - TciScbBit (str): optional regex of tciScbBit
        - Version (str): optional regex of version

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
