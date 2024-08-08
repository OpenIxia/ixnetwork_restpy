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


class StaticMacsec(Base):
    """Static MACsec
    The StaticMacsec class encapsulates a list of staticMacsec resources that are managed by the user.
    A list of resources can be retrieved from the server using the StaticMacsec.find() method.
    The list can be managed by using the StaticMacsec.add() and StaticMacsec.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "staticMacsec"
    _SDM_ATT_MAP = {
        "ActiveDevice": "activeDevice",
        "CipherSuite": "cipherSuite",
        "ConfidentialityOffset": "confidentialityOffset",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DutMac": "dutMac",
        "DutMsbOfXpn": "dutMsbOfXpn",
        "DutSciMac": "dutSciMac",
        "DutSciPortId": "dutSciPortId",
        "EnableClearTextVlans": "enableClearTextVlans",
        "EnableConfidentiality": "enableConfidentiality",
        "EnableEncryptedVlan": "enableEncryptedVlan",
        "EnableEncryptedVlans": "enableEncryptedVlans",
        "EncryptedTrafficType": "encryptedTrafficType",
        "EncryptedVlanCount": "encryptedVlanCount",
        "EncryptionEngine": "encryptionEngine",
        "EndStation": "endStation",
        "Errors": "errors",
        "ExcludedProtocols": "excludedProtocols",
        "FirstPn": "firstPn",
        "FixedPn": "fixedPn",
        "IncludeSci": "includeSci",
        "IncrementingPn": "incrementingPn",
        "LastPn": "lastPn",
        "Multiplier": "multiplier",
        "MvFirstXpn": "mvFirstXpn",
        "MvFixedXpn": "mvFixedXpn",
        "MvLastXpn": "mvLastXpn",
        "Name": "name",
        "OverrideTciSetting": "overrideTciSetting",
        "PacketCountPn": "packetCountPn",
        "PeriodicRekeyAttempts": "periodicRekeyAttempts",
        "PeriodicRekeyInterval": "periodicRekeyInterval",
        "PortId": "portId",
        "RekeyBehaviour": "rekeyBehaviour",
        "RxSakPoolSize": "rxSakPoolSize",
        "SendGratArp": "sendGratArp",
        "SessionStatus": "sessionStatus",
        "SourceIp": "sourceIp",
        "SourceMac": "sourceMac",
        "StackedLayers": "stackedLayers",
        "StartingPn": "startingPn",
        "StartingXpn": "startingXpn",
        "StateCounts": "stateCounts",
        "Status": "status",
        "SystemId": "systemId",
        "TciCBit": "tciCBit",
        "TciEBit": "tciEBit",
        "TciEsBit": "tciEsBit",
        "TciScBit": "tciScBit",
        "TciScbBit": "tciScbBit",
        "TxSakPoolSize": "txSakPoolSize",
        "Version": "version",
    }
    _SDM_ENUM_MAP = {
        "encryptedTrafficType": ["statefulL47", "statelessL23"],
        "encryptionEngine": ["softwareBased", "hardwareBased"],
        "rekeyBehaviour": ["dontRekey", "rekeyContinuous", "rekeyFixedCount"],
        "status": [
            "configured",
            "error",
            "mixed",
            "notStarted",
            "started",
            "starting",
            "stopping",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(StaticMacsec, self).__init__(parent, list_op)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import (
            Connector,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Connector", None) is not None:
                return self._properties.get("Connector")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.innervlanlist_e709d209ac3f7ec472b5b8b70db9e853 import (
            InnerVlanList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InnerVlanList", None) is not None:
                return self._properties.get("InnerVlanList")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4_8cb960b62ae85a03e1b40a57bfaeb7bb import (
            Ipv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4", None) is not None:
                return self._properties.get("Ipv4")
        return Ipv4(self)

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6_b40789fa49420009901a46b8dc683afc.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6_b40789fa49420009901a46b8dc683afc import (
            Ipv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6", None) is not None:
                return self._properties.get("Ipv6")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rxsakpool_22340fe5cb5d81664cab595d3e6d08ef import (
            RxSakPool,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RxSakPool", None) is not None:
                return self._properties.get("RxSakPool")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.txsakpool_7ab8c0a10359fbab4d0c5bd3dab1bfb2 import (
            TxSakPool,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TxSakPool", None) is not None:
                return self._properties.get("TxSakPool")
        return TxSakPool(self)._select()

    @property
    def ActiveDevice(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether a MACsec device is active or not. If disabled, MACsec will not be started on the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActiveDevice"]))

    @property
    def CipherSuite(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of cipher suite. Options include: 1) GCM-AES-128 2) GCM-AES-256 3) GCM-AES-XPN-128 4) GCM-AES-XPN-256
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CipherSuite"]))

    @property
    def ConfidentialityOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the confidentiality offset for both transmit and receive channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfidentialityOffset"])
        )

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedVia"])

    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedVia"], value)

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
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DutMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MAC address of the connected interface of the DUT to be used as Gateway MAC for IP traffic.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DutMac"]))

    @property
    def DutMsbOfXpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 32 most significant bits of the XPN that DUT will be using to construct the 64 bits XPN value when test starts.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DutMsbOfXpn"]))

    @property
    def DutSciMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MAC component of SCI with which MACsec traffic is expected from the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DutSciMac"]))

    @property
    def DutSciPortId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Port ID component of SCI with which MACsec traffic is expected from the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DutSciPortId"]))

    @property
    def EnableClearTextVlans(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Determines whether the VLANs configured on the parent Ethernet layer are sent as clear text VLANs (before secTAG) or as encrypted VLANs (after secTAG). By default this is disabled and the VLANs configured on the parent Ethernet layer are copied to MACsec layer and sent as encrypted VLANs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableClearTextVlans"])

    @EnableClearTextVlans.setter
    def EnableClearTextVlans(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableClearTextVlans"], value)

    @property
    def EnableConfidentiality(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether transmitted MACsec payload is encrypted or not.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableConfidentiality"])
        )

    @property
    def EnableEncryptedVlan(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines if VLAN data is to be encrypted or not.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableEncryptedVlan"])
        )

    @property
    def EnableEncryptedVlans(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether configured encrypted VLANs are included in MACsec packets or not. It can be configured per device.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableEncryptedVlans"])
        )

    @property
    def EncryptedTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(statefulL47 | statelessL23): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncryptedTrafficType"])

    @EncryptedTrafficType.setter
    def EncryptedTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncryptedTrafficType"], value)

    @property
    def EncryptedVlanCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Denotes the number of VLANs to be sent as encrypted VLANs. Maximum 6 VLANs can be configured as encrypted VLANs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncryptedVlanCount"])

    @EncryptedVlanCount.setter
    def EncryptedVlanCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncryptedVlanCount"], value)

    @property
    def EncryptionEngine(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(softwareBased | hardwareBased): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncryptionEngine"])

    @EncryptionEngine.setter
    def EncryptionEngine(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncryptionEngine"], value)

    @property
    def EndStation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether this device should act as the End Station.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EndStation"]))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def ExcludedProtocols(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Excluded Protocol
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExcludedProtocols"])
        )

    @property
    def FirstPn(self):
        # type: () -> int
        """
        Returns
        -------
        - number: First Packet Number of defined PN range with which MACsec packets will be sent out by single device of the Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstPn"])

    @FirstPn.setter
    def FirstPn(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstPn"], value)

    @property
    def FixedPn(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedPn"])

    @FixedPn.setter
    def FixedPn(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedPn"], value)

    @property
    def IncludeSci(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether SCI should be included in the SecTAG of the transmitted MACsec traffic.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeSci"]))

    @property
    def IncrementingPn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Determines whether MACsec packets will be sent out by single device with an incrementing PN or XPN. If Incrementing PN-XPN, is disabled then all MACsec packets will be sent out with the configured Fixed PN or lower half of configured Fixed XPN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementingPn"])

    @IncrementingPn.setter
    def IncrementingPn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementingPn"], value)

    @property
    def LastPn(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Last Packet Number of defined PN range with which MACsec packets will be sent out by single device of the Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastPn"])

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def MvFirstXpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): First 8 bytes PN of the PN range with which first MACsec packet of single device of the device group will be sent out.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MvFirstXpn"]))

    @property
    def MvFixedXpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 8 bytes PN with which all packets will be sent out.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MvFixedXpn"]))

    @property
    def MvLastXpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Last 8 bytes PN of the PN range with which last MACsec packet of single device of the device group will be sent out.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MvLastXpn"]))

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
    def OverrideTciSetting(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the default TCI settings as per configuration will be allowed for overwriting. Used to simulate mal-configured SecTAG for negative testing.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OverrideTciSetting"])
        )

    @property
    def PacketCountPn(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Packets of defined PN range which MACsec packets will be sent out by single device of the Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketCountPn"])

    @PacketCountPn.setter
    def PacketCountPn(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketCountPn"], value)

    @property
    def PeriodicRekeyAttempts(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Determines the number of times Rekey will happen after MACsec is started.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeriodicRekeyAttempts"])

    @PeriodicRekeyAttempts.setter
    def PeriodicRekeyAttempts(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeriodicRekeyAttempts"], value)

    @property
    def PeriodicRekeyInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeriodicRekeyInterval"])

    @PeriodicRekeyInterval.setter
    def PeriodicRekeyInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeriodicRekeyInterval"], value)

    @property
    def PortId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Port ID component of SCI with which MACsec traffic is transmitted.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortId"]))

    @property
    def RekeyBehaviour(self):
        # type: () -> str
        """
        Returns
        -------
        - str(dontRekey | rekeyContinuous | rekeyFixedCount): Determines the Rekey behavior.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RekeyBehaviour"])

    @RekeyBehaviour.setter
    def RekeyBehaviour(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RekeyBehaviour"], value)

    @property
    def RxSakPoolSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxSakPoolSize"])

    @RxSakPoolSize.setter
    def RxSakPoolSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxSakPoolSize"], value)

    @property
    def SendGratArp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendGratArp"])

    @SendGratArp.setter
    def SendGratArp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendGratArp"], value)

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def SourceIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP address of the MACsec device. Used as the source IP of the MACsec traffic generated by the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SourceIp"]))

    @property
    def SourceMac(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): MAC address of the Ethernet devices configured in the Ethernet stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceMac"])

    @SourceMac.setter
    def SourceMac(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceMac"], value)

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StartingPn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PN value with which MACsec packet transmission starts both for the first time as well as after Rekey.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StartingPn"]))

    @property
    def StartingXpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): XPN value with which MACsec packet transmission starts.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StartingXpn"]))

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateCounts"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @property
    def SystemId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): System Identifier component of the SCI field with which MACsec traffic is transmitted.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SystemId"]))

    @property
    def TciCBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the C bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciCBit"]))

    @property
    def TciEBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the E bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciEBit"]))

    @property
    def TciEsBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the ES bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciEsBit"]))

    @property
    def TciScBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the SC bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciScBit"]))

    @property
    def TciScbBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the SCB bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciScbBit"]))

    @property
    def TxSakPoolSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxSakPoolSize"])

    @TxSakPoolSize.setter
    def TxSakPoolSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxSakPoolSize"], value)

    @property
    def Version(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Version bit in TCI field of SecTAG if Override TCI Settings is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    def update(
        self,
        ConnectedVia=None,
        EnableClearTextVlans=None,
        EncryptedTrafficType=None,
        EncryptedVlanCount=None,
        EncryptionEngine=None,
        FirstPn=None,
        FixedPn=None,
        IncrementingPn=None,
        Multiplier=None,
        Name=None,
        PacketCountPn=None,
        PeriodicRekeyAttempts=None,
        PeriodicRekeyInterval=None,
        RekeyBehaviour=None,
        RxSakPoolSize=None,
        SendGratArp=None,
        SourceMac=None,
        StackedLayers=None,
        TxSakPoolSize=None,
    ):
        # type: (List[str], bool, str, int, str, int, int, bool, int, str, int, int, int, str, int, bool, List[str], List[str], int) -> StaticMacsec
        """Updates staticMacsec resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableClearTextVlans (bool): Determines whether the VLANs configured on the parent Ethernet layer are sent as clear text VLANs (before secTAG) or as encrypted VLANs (after secTAG). By default this is disabled and the VLANs configured on the parent Ethernet layer are copied to MACsec layer and sent as encrypted VLANs.
        - EncryptedTrafficType (str(statefulL47 | statelessL23)): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        - EncryptedVlanCount (number): Denotes the number of VLANs to be sent as encrypted VLANs. Maximum 6 VLANs can be configured as encrypted VLANs.
        - EncryptionEngine (str(softwareBased | hardwareBased)): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        - FirstPn (number): First Packet Number of defined PN range with which MACsec packets will be sent out by single device of the Device Group.
        - FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        - IncrementingPn (bool): Determines whether MACsec packets will be sent out by single device with an incrementing PN or XPN. If Incrementing PN-XPN, is disabled then all MACsec packets will be sent out with the configured Fixed PN or lower half of configured Fixed XPN.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PacketCountPn (number): Number of Packets of defined PN range which MACsec packets will be sent out by single device of the Device Group.
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        - SourceMac (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - TxSakPoolSize (number): Determines the number of SAKs configured for each device for the Tx secure channel. Multiple SAKs are needed if Rekey scenario is to be simulated.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        EnableClearTextVlans=None,
        EncryptedTrafficType=None,
        EncryptedVlanCount=None,
        EncryptionEngine=None,
        FirstPn=None,
        FixedPn=None,
        IncrementingPn=None,
        Multiplier=None,
        Name=None,
        PacketCountPn=None,
        PeriodicRekeyAttempts=None,
        PeriodicRekeyInterval=None,
        RekeyBehaviour=None,
        RxSakPoolSize=None,
        SendGratArp=None,
        SourceMac=None,
        StackedLayers=None,
        TxSakPoolSize=None,
    ):
        # type: (List[str], bool, str, int, str, int, int, bool, int, str, int, int, int, str, int, bool, List[str], List[str], int) -> StaticMacsec
        """Adds a new staticMacsec resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableClearTextVlans (bool): Determines whether the VLANs configured on the parent Ethernet layer are sent as clear text VLANs (before secTAG) or as encrypted VLANs (after secTAG). By default this is disabled and the VLANs configured on the parent Ethernet layer are copied to MACsec layer and sent as encrypted VLANs.
        - EncryptedTrafficType (str(statefulL47 | statelessL23)): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        - EncryptedVlanCount (number): Denotes the number of VLANs to be sent as encrypted VLANs. Maximum 6 VLANs can be configured as encrypted VLANs.
        - EncryptionEngine (str(softwareBased | hardwareBased)): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        - FirstPn (number): First Packet Number of defined PN range with which MACsec packets will be sent out by single device of the Device Group.
        - FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        - IncrementingPn (bool): Determines whether MACsec packets will be sent out by single device with an incrementing PN or XPN. If Incrementing PN-XPN, is disabled then all MACsec packets will be sent out with the configured Fixed PN or lower half of configured Fixed XPN.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PacketCountPn (number): Number of Packets of defined PN range which MACsec packets will be sent out by single device of the Device Group.
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        - SourceMac (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
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

    def find(
        self,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        EnableClearTextVlans=None,
        EncryptedTrafficType=None,
        EncryptedVlanCount=None,
        EncryptionEngine=None,
        Errors=None,
        FirstPn=None,
        FixedPn=None,
        IncrementingPn=None,
        LastPn=None,
        Multiplier=None,
        Name=None,
        PacketCountPn=None,
        PeriodicRekeyAttempts=None,
        PeriodicRekeyInterval=None,
        RekeyBehaviour=None,
        RxSakPoolSize=None,
        SendGratArp=None,
        SessionStatus=None,
        SourceMac=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        TxSakPoolSize=None,
    ):
        """Finds and retrieves staticMacsec resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve staticMacsec resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all staticMacsec resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableClearTextVlans (bool): Determines whether the VLANs configured on the parent Ethernet layer are sent as clear text VLANs (before secTAG) or as encrypted VLANs (after secTAG). By default this is disabled and the VLANs configured on the parent Ethernet layer are copied to MACsec layer and sent as encrypted VLANs.
        - EncryptedTrafficType (str(statefulL47 | statelessL23)): Determines the set of MACsec functionalities supported by a Device Group. Stateless L2-3 enables encryption of stateless L2-3 traffic at line rate, Stateful L4-7 enables encryption and live decryption of stateful L4-7 traffic at lower throughput. Separate Device Groups need to be configured to get both the options on the same port.
        - EncryptedVlanCount (number): Denotes the number of VLANs to be sent as encrypted VLANs. Maximum 6 VLANs can be configured as encrypted VLANs.
        - EncryptionEngine (str(softwareBased | hardwareBased)): Obsolete field. Replaced by Encrypted Traffic Type. Value is always same as Encrypted Traffic Type.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - FirstPn (number): First Packet Number of defined PN range with which MACsec packets will be sent out by single device of the Device Group.
        - FixedPn (number): Packet Number with which all MACsec packets will be sent out by all the devices of the Device Group.
        - IncrementingPn (bool): Determines whether MACsec packets will be sent out by single device with an incrementing PN or XPN. If Incrementing PN-XPN, is disabled then all MACsec packets will be sent out with the configured Fixed PN or lower half of configured Fixed XPN.
        - LastPn (number): Last Packet Number of defined PN range with which MACsec packets will be sent out by single device of the Device Group.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PacketCountPn (number): Number of Packets of defined PN range which MACsec packets will be sent out by single device of the Device Group.
        - PeriodicRekeyAttempts (number): Determines the number of times Rekey will happen after MACsec is started.
        - PeriodicRekeyInterval (number): Determines the time interval between two subsequent Rekey events. The timer starts with the first MACsec packet transmission from a device.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RxSakPoolSize (number): Determines the number of SAKs configured for each device for the Rx secure channel. Multiple SAKs are needed if DUT is expected to trigger Rekey during the test.
        - SendGratArp (bool): Determines whether Grat ARP should be sent out by each device with the configured MAC-IP mapping if encryption engine is Hardware Based. If Grap ARP is disabled then static ARP entries need to be created at the DUT to avoid traffic loss.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SourceMac (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("restartDown", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        ActiveDevice=None,
        CipherSuite=None,
        ConfidentialityOffset=None,
        DutMac=None,
        DutMsbOfXpn=None,
        DutSciMac=None,
        DutSciPortId=None,
        EnableConfidentiality=None,
        EnableEncryptedVlan=None,
        EnableEncryptedVlans=None,
        EndStation=None,
        ExcludedProtocols=None,
        IncludeSci=None,
        MvFirstXpn=None,
        MvFixedXpn=None,
        MvLastXpn=None,
        OverrideTciSetting=None,
        PortId=None,
        SourceIp=None,
        StartingPn=None,
        StartingXpn=None,
        SystemId=None,
        TciCBit=None,
        TciEBit=None,
        TciEsBit=None,
        TciScBit=None,
        TciScbBit=None,
        Version=None,
    ):
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
        - ExcludedProtocols (str): optional regex of excludedProtocols
        - IncludeSci (str): optional regex of includeSci
        - MvFirstXpn (str): optional regex of mvFirstXpn
        - MvFixedXpn (str): optional regex of mvFixedXpn
        - MvLastXpn (str): optional regex of mvLastXpn
        - OverrideTciSetting (str): optional regex of overrideTciSetting
        - PortId (str): optional regex of portId
        - SourceIp (str): optional regex of sourceIp
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
