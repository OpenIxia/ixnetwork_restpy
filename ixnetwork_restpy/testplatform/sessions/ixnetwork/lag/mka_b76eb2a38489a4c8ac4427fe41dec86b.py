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


class Mka(Base):
    """Mka
    The Mka class encapsulates a list of mka resources that are managed by the user.
    A list of resources can be retrieved from the server using the Mka.find() method.
    The list can be managed by using the Mka.add() and Mka.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "mka"
    _SDM_ATT_MAP = {
        "ActiveDevice": "activeDevice",
        "AssociationNumber": "associationNumber",
        "CakCount": "cakCount",
        "CipherSuite": "cipherSuite",
        "ConfidentialityOffset": "confidentialityOffset",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DelayProtect": "delayProtect",
        "DelayProtectSimulation": "delayProtectSimulation",
        "DescriptiveName": "descriptiveName",
        "DistributedCipherSuite": "distributedCipherSuite",
        "DistributedConfidentialityOffset": "distributedConfidentialityOffset",
        "ElectedKeyServer": "electedKeyServer",
        "Errors": "errors",
        "KeyDerivationFunction": "keyDerivationFunction",
        "KeyServerPriority": "keyServerPriority",
        "KeyServerSCI": "keyServerSCI",
        "KeyType": "keyType",
        "LlpnStep": "llpnStep",
        "MacsecCapability": "macsecCapability",
        "MacsecDesired": "macsecDesired",
        "MemberIdentifier": "memberIdentifier",
        "MirroredMacAddr": "mirroredMacAddr",
        "MkaHelloTime": "mkaHelloTime",
        "MkaLifeTime": "mkaLifeTime",
        "MkaVersion": "mkaVersion",
        "Multiplier": "multiplier",
        "Name": "name",
        "OlpnStep": "olpnStep",
        "PeerPN": "peerPN",
        "PeriodicRekeyAttempts": "periodicRekeyAttempts",
        "PeriodicRekeyInterval": "periodicRekeyInterval",
        "RandomizeMemberIdentifier": "randomizeMemberIdentifier",
        "RekeyBehaviour": "rekeyBehaviour",
        "RekeyMode": "rekeyMode",
        "RekeyThresholdPN": "rekeyThresholdPN",
        "RekeyThresholdXPN": "rekeyThresholdXPN",
        "Sak": "sak",
        "SendICVIndicator": "sendICVIndicator",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StartingDistributedAN": "startingDistributedAN",
        "StartingKeyNumber": "startingKeyNumber",
        "StartingLLPN": "startingLLPN",
        "StartingOLPN": "startingOLPN",
        "StateCounts": "stateCounts",
        "Status": "status",
        "SupportedCipherSuites": "supportedCipherSuites",
        "TxChannelCount": "txChannelCount",
    }
    _SDM_ENUM_MAP = {
        "keyType": ["psk"],
        "rekeyBehaviour": ["dontRekey", "rekeyContinuous", "rekeyFixedCount"],
        "rekeyMode": ["timerBased", "pNBased"],
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
        super(Mka, self).__init__(parent, list_op)

    @property
    def CakCache(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.cakcache_dfe6ea26428ccbc879e70415c02b2ccd.CakCache): An instance of the CakCache class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.cakcache_dfe6ea26428ccbc879e70415c02b2ccd import (
            CakCache,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CakCache", None) is not None:
                return self._properties.get("CakCache")
        return CakCache(self)._select()

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.learnedinfo_e3842fc998f50863a80ad08bc75a2de8.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.learnedinfo_e3842fc998f50863a80ad08bc75a2de8 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

    @property
    def TxChannels(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.txchannels_b00cc0f5ee44e7e1276269692ddc248a.TxChannels): An instance of the TxChannels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.txchannels_b00cc0f5ee44e7e1276269692ddc248a import (
            TxChannels,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TxChannels", None) is not None:
                return self._properties.get("TxChannels")
        return TxChannels(self)._select()

    @property
    def ActiveDevice(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether an MKA device is active or not. If disabled, MKA will not be started on the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActiveDevice"]))

    @property
    def AssociationNumber(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Displays the Association Number for the received SAK.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssociationNumber"])

    @property
    def CakCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: PSK Chain Size (Min 1, Max 10).
        """
        return self._get_attribute(self._SDM_ATT_MAP["CakCount"])

    @CakCount.setter
    def CakCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CakCount"], value)

    @property
    def CipherSuite(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the type of cipher suite.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CipherSuite"]))

    @property
    def ConfidentialityOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the confidentiality offset.
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
        - list(str[None | /api/v1/sessions/1/ixnetwork/lag]): List of layers this layer is used to connect with to the wire.
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
    def DelayProtect(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay Protect behavior of the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DelayProtect"]))

    @property
    def DelayProtectSimulation(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Displays the actual PN, simulated PN and the MKPDU message number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayProtectSimulation"])

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
    def DistributedCipherSuite(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[aes128 | aes256 | aesXpn128 | aesXpn256 | none]): Displays the cipher suite of the SAK distributed by the Key Server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistributedCipherSuite"])

    @property
    def DistributedConfidentialityOffset(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[confidentialityOffset30Octets | confidentialityOffset50Octets | noConfidentiality | noConfidentialityOffset | none]): Displays the Confidentiality Offset for the received SAK.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DistributedConfidentialityOffset"]
        )

    @property
    def ElectedKeyServer(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Denotes whether this device has been elected as a Key Server or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElectedKeyServer"])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def KeyDerivationFunction(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the KDF used to generate keys used by MKA.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyDerivationFunction"])
        )

    @property
    def KeyServerPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the Key Server Priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyServerPriority"])
        )

    @property
    def KeyServerSCI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - list(obj(ixnetwork_restpy.multivalue.Multivalue)): Key Server SCI.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyServerSCI"]))

    @property
    def KeyType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(psk): Indicates the source of CAK.
        """
        return self._get_attribute(self._SDM_ATT_MAP["KeyType"])

    @KeyType.setter
    def KeyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["KeyType"], value)

    @property
    def LlpnStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the LLPN Step.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LlpnStep"]))

    @property
    def MacsecCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates MACsec capabilities.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacsecCapability"])
        )

    @property
    def MacsecDesired(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether MACsec is desired or not. It is advertised in periodic hellos.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MacsecDesired"]))

    @property
    def MemberIdentifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - list(obj(ixnetwork_restpy.multivalue.Multivalue)): Displays the Member Identifier calculated by the state machine.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MemberIdentifier"])
        )

    @property
    def MirroredMacAddr(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): MAC address of the Ethernet devices configured in the Ethernet stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MirroredMacAddr"])

    @property
    def MkaHelloTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates MKA Hello Time.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MkaHelloTime"]))

    @property
    def MkaLifeTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates MKA Life Time of a Peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MkaLifeTime"])

    @MkaLifeTime.setter
    def MkaLifeTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MkaLifeTime"], value)

    @property
    def MkaVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the version of MKA.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MkaVersion"]))

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
    def OlpnStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the OLPN Step.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OlpnStep"]))

    @property
    def PeerPN(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Displays the PN advertised by the peer's PN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerPN"])

    @property
    def PeriodicRekeyAttempts(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of times Rekey should be triggered.
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
        - number: Time interval between two Rekey triggers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeriodicRekeyInterval"])

    @PeriodicRekeyInterval.setter
    def PeriodicRekeyInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeriodicRekeyInterval"], value)

    @property
    def RandomizeMemberIdentifier(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RandomizeMemberIdentifier"])

    @RandomizeMemberIdentifier.setter
    def RandomizeMemberIdentifier(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RandomizeMemberIdentifier"], value)

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
    def RekeyMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(timerBased | pNBased): Rekey criteria.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RekeyMode"])

    @RekeyMode.setter
    def RekeyMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RekeyMode"], value)

    @property
    def RekeyThresholdPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the PN rekey threshold.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RekeyThresholdPN"])
        )

    @property
    def RekeyThresholdXPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the XPN rekey threshold.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RekeyThresholdXPN"])
        )

    @property
    def Sak(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Displays the SAK received from the Key Server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Sak"])

    @property
    def SendICVIndicator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send ICV Indicator in MKPDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendICVIndicator"])
        )

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
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/lag]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StartingDistributedAN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines starting distributed AN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartingDistributedAN"])
        )

    @property
    def StartingKeyNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the starting key number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartingKeyNumber"])
        )

    @property
    def StartingLLPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the starting LLPN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StartingLLPN"]))

    @property
    def StartingOLPN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the starting OLPN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StartingOLPN"]))

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
    def SupportedCipherSuites(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The list of cipher suites supported by the device. All options are selected by default.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SupportedCipherSuites"])
        )

    @property
    def TxChannelCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Determines the number of Tx Channels configured for each device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxChannelCount"])

    def update(
        self,
        CakCount=None,
        ConnectedVia=None,
        KeyType=None,
        MkaLifeTime=None,
        Multiplier=None,
        Name=None,
        PeriodicRekeyAttempts=None,
        PeriodicRekeyInterval=None,
        RandomizeMemberIdentifier=None,
        RekeyBehaviour=None,
        RekeyMode=None,
        StackedLayers=None,
    ):
        # type: (int, List[str], str, int, int, str, int, int, bool, str, str, List[str]) -> Mka
        """Updates mka resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - CakCount (number): PSK Chain Size (Min 1, Max 10).
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/lag])): List of layers this layer is used to connect with to the wire.
        - KeyType (str(psk)): Indicates the source of CAK.
        - MkaLifeTime (number): Indicates MKA Life Time of a Peer.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Number of times Rekey should be triggered.
        - PeriodicRekeyInterval (number): Time interval between two Rekey triggers.
        - RandomizeMemberIdentifier (bool): If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RekeyMode (str(timerBased | pNBased)): Rekey criteria.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/lag])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        CakCount=None,
        ConnectedVia=None,
        KeyType=None,
        MkaLifeTime=None,
        Multiplier=None,
        Name=None,
        PeriodicRekeyAttempts=None,
        PeriodicRekeyInterval=None,
        RandomizeMemberIdentifier=None,
        RekeyBehaviour=None,
        RekeyMode=None,
        StackedLayers=None,
    ):
        # type: (int, List[str], str, int, int, str, int, int, bool, str, str, List[str]) -> Mka
        """Adds a new mka resource on the server and adds it to the container.

        Args
        ----
        - CakCount (number): PSK Chain Size (Min 1, Max 10).
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/lag])): List of layers this layer is used to connect with to the wire.
        - KeyType (str(psk)): Indicates the source of CAK.
        - MkaLifeTime (number): Indicates MKA Life Time of a Peer.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeriodicRekeyAttempts (number): Number of times Rekey should be triggered.
        - PeriodicRekeyInterval (number): Time interval between two Rekey triggers.
        - RandomizeMemberIdentifier (bool): If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RekeyMode (str(timerBased | pNBased)): Rekey criteria.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/lag])): List of secondary (many to one) child layer protocols

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

    def find(
        self,
        AssociationNumber=None,
        CakCount=None,
        ConnectedVia=None,
        Count=None,
        DelayProtectSimulation=None,
        DescriptiveName=None,
        DistributedCipherSuite=None,
        DistributedConfidentialityOffset=None,
        ElectedKeyServer=None,
        Errors=None,
        KeyType=None,
        MirroredMacAddr=None,
        MkaLifeTime=None,
        Multiplier=None,
        Name=None,
        PeerPN=None,
        PeriodicRekeyAttempts=None,
        PeriodicRekeyInterval=None,
        RandomizeMemberIdentifier=None,
        RekeyBehaviour=None,
        RekeyMode=None,
        Sak=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        TxChannelCount=None,
    ):
        """Finds and retrieves mka resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mka resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mka resources from the server.

        Args
        ----
        - AssociationNumber (list(str)): Displays the Association Number for the received SAK.
        - CakCount (number): PSK Chain Size (Min 1, Max 10).
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/lag])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DelayProtectSimulation (list(str)): Displays the actual PN, simulated PN and the MKPDU message number.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DistributedCipherSuite (list(str[aes128 | aes256 | aesXpn128 | aesXpn256 | none])): Displays the cipher suite of the SAK distributed by the Key Server.
        - DistributedConfidentialityOffset (list(str[confidentialityOffset30Octets | confidentialityOffset50Octets | noConfidentiality | noConfidentialityOffset | none])): Displays the Confidentiality Offset for the received SAK.
        - ElectedKeyServer (list(str)): Denotes whether this device has been elected as a Key Server or not.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - KeyType (str(psk)): Indicates the source of CAK.
        - MirroredMacAddr (list(str)): MAC address of the Ethernet devices configured in the Ethernet stack.
        - MkaLifeTime (number): Indicates MKA Life Time of a Peer.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerPN (list(number)): Displays the PN advertised by the peer's PN.
        - PeriodicRekeyAttempts (number): Number of times Rekey should be triggered.
        - PeriodicRekeyInterval (number): Time interval between two Rekey triggers.
        - RandomizeMemberIdentifier (bool): If this box is checked, then Ixia MKA devices will generate random member identifiers. Otherwise member identifiers of the form MAC Address-Counter will be generated to aid in debugging.
        - RekeyBehaviour (str(dontRekey | rekeyContinuous | rekeyFixedCount)): Determines the Rekey behavior.
        - RekeyMode (str(timerBased | pNBased)): Rekey criteria.
        - Sak (list(str)): Displays the SAK received from the Key Server.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/lag])): List of secondary (many to one) child layer protocols
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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearAllLearnedInfo", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getLearnedInfo", payload=payload, response_object=None)

    def PauseMKPDUTransmission(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the pauseMKPDUTransmission operation on the server.

        Pause MKPDU Transmission.

        pauseMKPDUTransmission(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
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
            "pauseMKPDUTransmission", payload=payload, response_object=None
        )

    def PausePeriodicRekey(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the PausePeriodicRekey operation on the server.

        Pause the periodic rekey timer if it is running.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        PausePeriodicRekey(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        PausePeriodicRekey(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        PausePeriodicRekey(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
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
        return self._execute(
            "PausePeriodicRekey", payload=payload, response_object=None
        )

    def PausePeriodicRekey(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the pausePeriodicRekey operation on the server.

        Pause the periodic rekey timer if it is running.

        pausePeriodicRekey(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
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
            "pausePeriodicRekey", payload=payload, response_object=None
        )

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

    def RestartPeriodicRekey(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the RestartPeriodicRekey operation on the server.

        Restart the periodic rekey timer if it was stopped.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        RestartPeriodicRekey(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        RestartPeriodicRekey(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        RestartPeriodicRekey(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------
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
        return self._execute(
            "RestartPeriodicRekey", payload=payload, response_object=None
        )

    def RestartPeriodicRekey(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the restartPeriodicRekey operation on the server.

        Restart the periodic rekey timer if it was stopped.

        restartPeriodicRekey(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
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
            "restartPeriodicRekey", payload=payload, response_object=None
        )

    def ResumeMKPDUTransmission(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumeMKPDUTransmission operation on the server.

        Resume MKPDU Transmission.

        resumeMKPDUTransmission(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
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
            "resumeMKPDUTransmission", payload=payload, response_object=None
        )

    def SimulateDelayedMACsecPacketsStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the simulateDelayedMACsecPacketsStart operation on the server.

        Start delay protect simulation.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        simulateDelayedMACsecPacketsStart(async_operation=bool)
        -------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        simulateDelayedMACsecPacketsStart(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        simulateDelayedMACsecPacketsStart(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        simulateDelayedMACsecPacketsStart(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "simulateDelayedMACsecPacketsStart", payload=payload, response_object=None
        )

    def SimulateDelayedMACsecPacketsStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the simulateDelayedMACsecPacketsStop operation on the server.

        Stop delay protect simulation.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        simulateDelayedMACsecPacketsStop(async_operation=bool)
        ------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        simulateDelayedMACsecPacketsStop(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        simulateDelayedMACsecPacketsStop(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        simulateDelayedMACsecPacketsStop(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "simulateDelayedMACsecPacketsStop", payload=payload, response_object=None
        )

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

    def TriggerRekey(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the triggerRekey operation on the server.

        Trigger a Rekey Event from Keysight emulated KeyServer.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        triggerRekey(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        triggerRekey(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        triggerRekey(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        triggerRekey(Arg2=list, async_operation=bool)list
        -------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("triggerRekey", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        ActiveDevice=None,
        CipherSuite=None,
        ConfidentialityOffset=None,
        DelayProtect=None,
        KeyDerivationFunction=None,
        KeyServerPriority=None,
        KeyServerSCI=None,
        LlpnStep=None,
        MacsecCapability=None,
        MacsecDesired=None,
        MemberIdentifier=None,
        MkaHelloTime=None,
        MkaVersion=None,
        OlpnStep=None,
        RekeyThresholdPN=None,
        RekeyThresholdXPN=None,
        SendICVIndicator=None,
        StartingDistributedAN=None,
        StartingKeyNumber=None,
        StartingLLPN=None,
        StartingOLPN=None,
        SupportedCipherSuites=None,
    ):
        """Base class infrastructure that gets a list of mka device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveDevice (str): optional regex of activeDevice
        - CipherSuite (str): optional regex of cipherSuite
        - ConfidentialityOffset (str): optional regex of confidentialityOffset
        - DelayProtect (str): optional regex of delayProtect
        - KeyDerivationFunction (str): optional regex of keyDerivationFunction
        - KeyServerPriority (str): optional regex of keyServerPriority
        - KeyServerSCI (str): optional regex of keyServerSCI
        - LlpnStep (str): optional regex of llpnStep
        - MacsecCapability (str): optional regex of macsecCapability
        - MacsecDesired (str): optional regex of macsecDesired
        - MemberIdentifier (str): optional regex of memberIdentifier
        - MkaHelloTime (str): optional regex of mkaHelloTime
        - MkaVersion (str): optional regex of mkaVersion
        - OlpnStep (str): optional regex of olpnStep
        - RekeyThresholdPN (str): optional regex of rekeyThresholdPN
        - RekeyThresholdXPN (str): optional regex of rekeyThresholdXPN
        - SendICVIndicator (str): optional regex of sendICVIndicator
        - StartingDistributedAN (str): optional regex of startingDistributedAN
        - StartingKeyNumber (str): optional regex of startingKeyNumber
        - StartingLLPN (str): optional regex of startingLLPN
        - StartingOLPN (str): optional regex of startingOLPN
        - SupportedCipherSuites (str): optional regex of supportedCipherSuites

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
