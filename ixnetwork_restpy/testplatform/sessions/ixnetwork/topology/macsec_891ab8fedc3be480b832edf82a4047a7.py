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


class Macsec(Base):
    """MACsec
    The Macsec class encapsulates a list of macsec resources that are managed by the user.
    A list of resources can be retrieved from the server using the Macsec.find() method.
    The list can be managed by using the Macsec.add() and Macsec.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'macsec'
    _SDM_ATT_MAP = {
        'ActiveDevice': 'activeDevice',
        'BadIcv': 'badIcv',
        'CipherSuite': 'cipherSuite',
        'ConfidentialityOffset': 'confidentialityOffset',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DutMsbOfXpn': 'dutMsbOfXpn',
        'DutSciMac': 'dutSciMac',
        'DutSciPortId': 'dutSciPortId',
        'EnableConfidentiality': 'enableConfidentiality',
        'EnableEncryptedVlans': 'enableEncryptedVlans',
        'EnableOutOfWindowPn': 'enableOutOfWindowPn',
        'EncryptedVlanCount': 'encryptedVlanCount',
        'EndStation': 'endStation',
        'Errors': 'errors',
        'IncludeSci': 'includeSci',
        'InterleaveDuration': 'interleaveDuration',
        'InterleaveOldSak': 'interleaveOldSak',
        'MalformedPktPercent': 'malformedPktPercent',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'OverrideTciSetting': 'overrideTciSetting',
        'PeriodicRekeyAttempts': 'periodicRekeyAttempts',
        'PeriodicRekeyInterval': 'periodicRekeyInterval',
        'PnExhaustionBehaviour': 'pnExhaustionBehaviour',
        'PortId': 'portId',
        'RekeyMode': 'rekeyMode',
        'ReplayWindowSize': 'replayWindowSize',
        'RxSakPoolSize': 'rxSakPoolSize',
        'SessionStatus': 'sessionStatus',
        'SourceMac': 'sourceMac',
        'StackedLayers': 'stackedLayers',
        'StartingPn': 'startingPn',
        'StartingXpn': 'startingXpn',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SystemId': 'systemId',
        'TciCBit': 'tciCBit',
        'TciEBit': 'tciEBit',
        'TciEsBit': 'tciEsBit',
        'TciScBit': 'tciScBit',
        'TciScbBit': 'tciScbBit',
        'TimerBasedRekeyBehaviour': 'timerBasedRekeyBehaviour',
        'TxSakPoolSize': 'txSakPoolSize',
        'Version': 'version',
    }

    def __init__(self, parent):
        super(Macsec, self).__init__(parent)

    @property
    def BondedGRE(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bondedgre_09eda4ea678bfaf1026122797df45443.BondedGRE): An instance of the BondedGRE class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bondedgre_09eda4ea678bfaf1026122797df45443 import BondedGRE
        return BondedGRE(self)

    @property
    def CfmBridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge_0d1f83a1e9fee8ee7d444b2a33a0e03b.CfmBridge): An instance of the CfmBridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge_0d1f83a1e9fee8ee7d444b2a33a0e03b import CfmBridge
        return CfmBridge(self)

    @property
    def Dhcpv4client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client_cfcdda8db5004b679a441f92193405ea.Dhcpv4client): An instance of the Dhcpv4client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client_cfcdda8db5004b679a441f92193405ea import Dhcpv4client
        return Dhcpv4client(self)

    @property
    def Dhcpv6client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client_355391ba11ab3c1555c827e2e4ac3c4c.Dhcpv6client): An instance of the Dhcpv6client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client_355391ba11ab3c1555c827e2e4ac3c4c import Dhcpv6client
        return Dhcpv6client(self)

    @property
    def ECpriRe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011.ECpriRe): An instance of the ECpriRe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011 import ECpriRe
        return ECpriRe(self)

    @property
    def ECpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255.ECpriRec): An instance of the ECpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255 import ECpriRec
        return ECpriRec(self)

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
    def Ipv6Autoconfiguration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration_b065cceda7a3517cca0451a09d81d989.Ipv6Autoconfiguration): An instance of the Ipv6Autoconfiguration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration_b065cceda7a3517cca0451a09d81d989 import Ipv6Autoconfiguration
        return Ipv6Autoconfiguration(self)

    @property
    def IsisDceSimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter_92c9662fb6421c6639f138f508faf4d4.IsisDceSimRouter): An instance of the IsisDceSimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter_92c9662fb6421c6639f138f508faf4d4 import IsisDceSimRouter
        return IsisDceSimRouter(self)

    @property
    def IsisFabricPath(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath_49ed8317c28295615f21a4a8362c2b95.IsisFabricPath): An instance of the IsisFabricPath class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath_49ed8317c28295615f21a4a8362c2b95 import IsisFabricPath
        return IsisFabricPath(self)

    @property
    def IsisL3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3_dd64c602d4f484ff78cfcd9dc64c9599.IsisL3): An instance of the IsisL3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3_dd64c602d4f484ff78cfcd9dc64c9599 import IsisL3
        return IsisL3(self)

    @property
    def IsisSpbBcb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb_d576c38717539c1b1768a3a9f8ab5670.IsisSpbBcb): An instance of the IsisSpbBcb class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb_d576c38717539c1b1768a3a9f8ab5670 import IsisSpbBcb
        return IsisSpbBcb(self)

    @property
    def IsisSpbBeb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb_82771ae7e9ec8dfc9848a0c0aa078da2.IsisSpbBeb): An instance of the IsisSpbBeb class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb_82771ae7e9ec8dfc9848a0c0aa078da2 import IsisSpbBeb
        return IsisSpbBeb(self)

    @property
    def IsisSpbSimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter_4d8d2b3596c2f006afcd75a76b6934ff.IsisSpbSimRouter): An instance of the IsisSpbSimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter_4d8d2b3596c2f006afcd75a76b6934ff import IsisSpbSimRouter
        return IsisSpbSimRouter(self)

    @property
    def IsisTrill(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill_e1cc1866688f861871e06513525d235b.IsisTrill): An instance of the IsisTrill class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill_e1cc1866688f861871e06513525d235b import IsisTrill
        return IsisTrill(self)

    @property
    def IsisTrillSimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter_7f0721f1a50df44db865ccea96c8f735.IsisTrillSimRouter): An instance of the IsisTrillSimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter_7f0721f1a50df44db865ccea96c8f735 import IsisTrillSimRouter
        return IsisTrillSimRouter(self)

    @property
    def Lacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp_b6b488f98125e4a7318076cb1375941b.Lacp): An instance of the Lacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp_b6b488f98125e4a7318076cb1375941b import Lacp
        return Lacp(self)

    @property
    def Lagportlacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportlacp_ed42d76e076cab1a6c2369b757a5d616.Lagportlacp): An instance of the Lagportlacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportlacp_ed42d76e076cab1a6c2369b757a5d616 import Lagportlacp
        return Lagportlacp(self)

    @property
    def Lagportstaticlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportstaticlag_f67759421ceee90b665b41bf19b8202d.Lagportstaticlag): An instance of the Lagportstaticlag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportstaticlag_f67759421ceee90b665b41bf19b8202d import Lagportstaticlag
        return Lagportstaticlag(self)

    @property
    def Mka(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mka_d0af5e39c81cb01eb75d4a693187a9ca.Mka): An instance of the Mka class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mka_d0af5e39c81cb01eb75d4a693187a9ca import Mka
        return Mka(self)

    @property
    def MsrpListener(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener_e4c5ef0942a99c83ab955893f78633c0.MsrpListener): An instance of the MsrpListener class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener_e4c5ef0942a99c83ab955893f78633c0 import MsrpListener
        return MsrpListener(self)

    @property
    def MsrpTalker(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker_ac4e61374b0b4d8500aef7076a2cda89.MsrpTalker): An instance of the MsrpTalker class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker_ac4e61374b0b4d8500aef7076a2cda89 import MsrpTalker
        return MsrpTalker(self)

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
    def StaticLag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag_d16a8997708d466db9c9f007ce04724e.StaticLag): An instance of the StaticLag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag_d16a8997708d466db9c9f007ce04724e import StaticLag
        return StaticLag(self)

    @property
    def Streams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams_dcd5bdb9e0099c6354f7bed1be55d8f6.Streams): An instance of the Streams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams_dcd5bdb9e0099c6354f7bed1be55d8f6 import Streams
        return Streams(self)

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
    def BadIcv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Checkbox to insert Bad ICV in the packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BadIcv']))

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
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

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
    def EnableEncryptedVlans(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables VLANs for the sessions.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableEncryptedVlans']))

    @property
    def EnableOutOfWindowPn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Used for -ve testing to include a packet with PN = (HPN-W) within the set of packets as configured.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOutOfWindowPn']))

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
    def IncludeSci(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether SCI should be included in the SecTAG of the transmitted MACsec traffic.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSci']))

    @property
    def InterleaveDuration(self):
        """
        Returns
        -------
        - number: Determines how long the Old and New SAKs should be interleaved.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterleaveDuration'])
    @InterleaveDuration.setter
    def InterleaveDuration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterleaveDuration'], value)

    @property
    def InterleaveOldSak(self):
        """
        Returns
        -------
        - bool: Determines whether Ixia interleaves Old and New SAKs after Rekey is triggered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterleaveOldSak'])
    @InterleaveOldSak.setter
    def InterleaveOldSak(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterleaveOldSak'], value)

    @property
    def MalformedPktPercent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This value will determine how much of the packets will have malformed TCI settings. 100% means all packets will be sent with the negative configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MalformedPktPercent']))

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
    def PnExhaustionBehaviour(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): What should Ixia tx port do if PN has exhausted but no new SAK is available from MKA or Rekey Timer has not expired.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PnExhaustionBehaviour']))

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
    def RekeyMode(self):
        """
        Returns
        -------
        - str(timerBased | pnBased): Rekey criteria, either PN based or Timer based.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RekeyMode'])
    @RekeyMode.setter
    def RekeyMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RekeyMode'], value)

    @property
    def ReplayWindowSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Window size required for calculating LAPN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReplayWindowSize']))

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
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

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
    def StartingPn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PN value with which packet transmission will begin.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingPn']))

    @property
    def StartingXpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PN value with which packet transmission will begin.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingXpn']))

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
    def TimerBasedRekeyBehaviour(self):
        """
        Returns
        -------
        - str(dontRekey | rekeyContinuous | rekeyFixedCount): Control to do timer based Rekey.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimerBasedRekeyBehaviour'])
    @TimerBasedRekeyBehaviour.setter
    def TimerBasedRekeyBehaviour(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimerBasedRekeyBehaviour'], value)

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

    def update(self, ConnectedVia=None, EncryptedVlanCount=None, InterleaveDuration=None, InterleaveOldSak=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyMode=None, RxSakPoolSize=None, StackedLayers=None, TimerBasedRekeyBehaviour=None, TxSakPoolSize=None):
        """Updates macsec resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
        - InterleaveDuration (number): Determines how long the Old and New SAKs should be interleaved.
        - InterleaveOldSak (bool): Determines whether Ixia interleaves Old and New SAKs after Rekey is triggered.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyMode (str(timerBased | pnBased)): Rekey criteria, either PN based or Timer based.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TimerBasedRekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Control to do timer based Rekey.
        - TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EncryptedVlanCount=None, InterleaveDuration=None, InterleaveOldSak=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyMode=None, RxSakPoolSize=None, StackedLayers=None, TimerBasedRekeyBehaviour=None, TxSakPoolSize=None):
        """Adds a new macsec resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
        - InterleaveDuration (number): Determines how long the Old and New SAKs should be interleaved.
        - InterleaveOldSak (bool): Determines whether Ixia interleaves Old and New SAKs after Rekey is triggered.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyMode (str(timerBased | pnBased)): Rekey criteria, either PN based or Timer based.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TimerBasedRekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Control to do timer based Rekey.
        - TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Returns
        -------
        - self: This instance with all currently retrieved macsec resources using find and the newly added macsec resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained macsec resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EncryptedVlanCount=None, Errors=None, InterleaveDuration=None, InterleaveOldSak=None, Multiplier=None, Name=None, PeriodicRekeyAttempts=None, PeriodicRekeyInterval=None, RekeyMode=None, RxSakPoolSize=None, SessionStatus=None, SourceMac=None, StackedLayers=None, StateCounts=None, Status=None, TimerBasedRekeyBehaviour=None, TxSakPoolSize=None):
        """Finds and retrieves macsec resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macsec resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macsec resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - EncryptedVlanCount (number): Determines if VLAN information to be encrypted or not. Maximum 6 VLANs can be added in the encrypted payload.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - InterleaveDuration (number): Determines how long the Old and New SAKs should be interleaved.
        - InterleaveOldSak (bool): Determines whether Ixia interleaves Old and New SAKs after Rekey is triggered.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyMode (str(timerBased | pnBased)): Rekey criteria, either PN based or Timer based.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SourceMac (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TimerBasedRekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Control to do timer based Rekey.
        - TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Returns
        -------
        - self: This instance with matching macsec resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macsec data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macsec resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveDevice=None, BadIcv=None, CipherSuite=None, ConfidentialityOffset=None, DutMsbOfXpn=None, DutSciMac=None, DutSciPortId=None, EnableConfidentiality=None, EnableEncryptedVlans=None, EnableOutOfWindowPn=None, EndStation=None, IncludeSci=None, MalformedPktPercent=None, OverrideTciSetting=None, PnExhaustionBehaviour=None, PortId=None, ReplayWindowSize=None, StartingPn=None, StartingXpn=None, SystemId=None, TciCBit=None, TciEBit=None, TciEsBit=None, TciScBit=None, TciScbBit=None, Version=None):
        """Base class infrastructure that gets a list of macsec device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveDevice (str): optional regex of activeDevice
        - BadIcv (str): optional regex of badIcv
        - CipherSuite (str): optional regex of cipherSuite
        - ConfidentialityOffset (str): optional regex of confidentialityOffset
        - DutMsbOfXpn (str): optional regex of dutMsbOfXpn
        - DutSciMac (str): optional regex of dutSciMac
        - DutSciPortId (str): optional regex of dutSciPortId
        - EnableConfidentiality (str): optional regex of enableConfidentiality
        - EnableEncryptedVlans (str): optional regex of enableEncryptedVlans
        - EnableOutOfWindowPn (str): optional regex of enableOutOfWindowPn
        - EndStation (str): optional regex of endStation
        - IncludeSci (str): optional regex of includeSci
        - MalformedPktPercent (str): optional regex of malformedPktPercent
        - OverrideTciSetting (str): optional regex of overrideTciSetting
        - PnExhaustionBehaviour (str): optional regex of pnExhaustionBehaviour
        - PortId (str): optional regex of portId
        - ReplayWindowSize (str): optional regex of replayWindowSize
        - StartingPn (str): optional regex of startingPn
        - StartingXpn (str): optional regex of startingXpn
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
