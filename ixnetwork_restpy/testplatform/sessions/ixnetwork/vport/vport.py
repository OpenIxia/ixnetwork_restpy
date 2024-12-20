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


class Vport(Base):
    """This is the virtual port hierarchy, which is used to configure IxNetwork.
    The Vport class encapsulates a list of vport resources that are managed by the user.
    A list of resources can be retrieved from the server using the Vport.find() method.
    The list can be managed by using the Vport.add() and Vport.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "vport"
    _SDM_ATT_MAP = {
        "ActualSpeed": "actualSpeed",
        "AdminMode": "adminMode",
        "AssignedTo": "assignedTo",
        "AssignedToDisplayName": "assignedToDisplayName",
        "CaptureSupported": "captureSupported",
        "ConnectedTo": "connectedTo",
        "ConnectionInfo": "connectionInfo",
        "ConnectionState": "connectionState",
        "ConnectionStatus": "connectionStatus",
        "ConnectionStatusDisplayName": "connectionStatusDisplayName",
        "DelayCompensation": "delayCompensation",
        "DpdkPerformanceAcceleration": "dpdkPerformanceAcceleration",
        "InternalId": "internalId",
        "IsAvailable": "isAvailable",
        "IsConnected": "isConnected",
        "IsFramePreemptionSupported": "isFramePreemptionSupported",
        "IsMapped": "isMapped",
        "IsPullOnly": "isPullOnly",
        "IsVMPort": "isVMPort",
        "IxnChassisVersion": "ixnChassisVersion",
        "IxnClientVersion": "ixnClientVersion",
        "IxosChassisVersion": "ixosChassisVersion",
        "LastLinkStateChangeEventTimestamp": "lastLinkStateChangeEventTimestamp",
        "Licenses": "licenses",
        "Location": "location",
        "MacsecEnabled": "macsecEnabled",
        "MaxStreamsSupported": "maxStreamsSupported",
        "Name": "name",
        "ResourceMode": "resourceMode",
        "RxMode": "rxMode",
        "State": "state",
        "StateDetail": "stateDetail",
        "TraceEnabled": "traceEnabled",
        "TraceLevel": "traceLevel",
        "TraceTag": "traceTag",
        "TransmitIgnoreLinkStatus": "transmitIgnoreLinkStatus",
        "TxGapControlMode": "txGapControlMode",
        "TxMode": "txMode",
        "Type": "type",
        "UseGlobalSettings": "useGlobalSettings",
        "ValidTxModes": "validTxModes",
    }
    _SDM_ENUM_MAP = {
        "captureSupported": ["data", "control", "dataAndControl", "none"],
        "connectionState": [
            "assignedInUseByOther",
            "assignedUnconnected",
            "connectedLinkDown",
            "connectedLinkUp",
            "connecting",
            "unassigned",
        ],
        "rxMode": ["capture", "measure", "captureAndMeasure", "packetImpairment"],
        "state": ["busy", "down", "unassigned", "up", "versionMismatch"],
        "stateDetail": [
            "busy",
            "cpuNotReady",
            "idle",
            "inActive",
            "l1ConfigFailed",
            "protocolsNotSupported",
            "versionMismatched",
            "waitingForCPUStatus",
        ],
        "traceLevel": [
            "kCritical",
            "kDebug",
            "kError",
            "kInfo",
            "kNote",
            "kTrace",
            "kWarning",
        ],
        "txGapControlMode": ["fixedMode", "averageMode"],
        "txMode": [
            "sequential",
            "interleaved",
            "sequentialCoarse",
            "interleavedCoarse",
            "packetImpairment",
        ],
        "type": [
            "ethernet",
            "ethernetvm",
            "ethernetcm",
            "novusmini",
            "novusminipro",
            "ethernetFcoe",
            "atm",
            "pos",
            "tenGigLan",
            "tenGigLanFcoe",
            "fortyGigLan",
            "fortyGigLanFcoe",
            "tenGigWan",
            "tenGigWanFcoe",
            "hundredGigLan",
            "hundredGigLanFcoe",
            "tenFortyHundredGigLan",
            "tenFortyHundredGigLanFcoe",
            "fc",
            "ethernetImpairment",
            "novusHundredGigLan",
            "novusHundredGigLanFcoe",
            "novusTenGigLan",
            "novusTenGigLanFcoe",
            "krakenFourHundredGigLan",
            "krakenFourHundredGigLanFcoe",
            "aresOneFourHundredGigLan",
            "aresOneFourHundredGigLanFcoe",
            "uhdOneHundredGigLan",
            "novus5GTenTwentyFiveGigLan",
            "novus5GTenTwentyFiveGigLanFcoe",
            "starFourHundredGigLan",
            "starFourHundredGigLanFcoe",
            "ravenEightHundredGigLan",
            "ravenEightHundredGigLanFcoe",
            "aresOneEightHundredGigLanQddC",
            "aresOneEightHundredGigLanQddCFcoe",
            "sertHundredGigLan",
            "aresOneEightHundredGigLanOsfpC",
            "aresOneEightHundredGigLanOsfpCFcoe",
            "aresOneM",
            "aresOneMFcoe",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Vport, self).__init__(parent, list_op)

    @property
    def Capture(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.capture.Capture): An instance of the Capture class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.capture import (
            Capture,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Capture", None) is not None:
                return self._properties.get("Capture")
        return Capture(self)._select()

    @property
    def DiscoveredNeighbor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.discoveredneighbor.discoveredneighbor.DiscoveredNeighbor): An instance of the DiscoveredNeighbor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.discoveredneighbor.discoveredneighbor import (
            DiscoveredNeighbor,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DiscoveredNeighbor", None) is not None:
                return self._properties.get("DiscoveredNeighbor")
        return DiscoveredNeighbor(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.interface.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.interface import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def InterfaceDiscoveredAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interfacediscoveredaddress.interfacediscoveredaddress.InterfaceDiscoveredAddress): An instance of the InterfaceDiscoveredAddress class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interfacediscoveredaddress.interfacediscoveredaddress import (
            InterfaceDiscoveredAddress,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InterfaceDiscoveredAddress", None) is not None:
                return self._properties.get("InterfaceDiscoveredAddress")
        return InterfaceDiscoveredAddress(self)._select()

    @property
    def L1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.l1config.L1Config): An instance of the L1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.l1config import (
            L1Config,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L1Config", None) is not None:
                return self._properties.get("L1Config")
        return L1Config(self)._select()

    @property
    def ProtocolStack(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.protocolstack.ProtocolStack): An instance of the ProtocolStack class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.protocolstack import (
            ProtocolStack,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ProtocolStack", None) is not None:
                return self._properties.get("ProtocolStack")
        return ProtocolStack(self)._select()

    @property
    def Protocols(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.protocols.Protocols): An instance of the Protocols class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.protocols import (
            Protocols,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Protocols", None) is not None:
                return self._properties.get("Protocols")
        return Protocols(self)

    @property
    def RateControlParameters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ratecontrolparameters.ratecontrolparameters.RateControlParameters): An instance of the RateControlParameters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ratecontrolparameters.ratecontrolparameters import (
            RateControlParameters,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RateControlParameters", None) is not None:
                return self._properties.get("RateControlParameters")
        return RateControlParameters(self)._select()

    @property
    def TapSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.tapsettings.tapsettings.TapSettings): An instance of the TapSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.tapsettings.tapsettings import (
            TapSettings,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TapSettings", None) is not None:
                return self._properties.get("TapSettings")
        return TapSettings(self)

    @property
    def ActualSpeed(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The actual speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActualSpeed"])

    @property
    def AdminMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdminMode"])

    @property
    def AssignedTo(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: (Deprecated, Read Only) A new port is assigned with this option.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignedTo"])

    @property
    def AssignedToDisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignedToDisplayName"])

    @property
    def CaptureSupported(self):
        # type: () -> str
        """
        Returns
        -------
        - str(data | control | dataAndControl | none):
        """
        return self._get_attribute(self._SDM_ATT_MAP["CaptureSupported"])

    @property
    def ConnectedTo(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port): The physical port to which the unassigned port is assigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedTo"])

    @ConnectedTo.setter
    def ConnectedTo(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedTo"], value)

    @property
    def ConnectionInfo(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Detailed information about location of the physical port that is assigned to this port configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectionInfo"])

    @property
    def ConnectionState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(assignedInUseByOther | assignedUnconnected | connectedLinkDown | connectedLinkUp | connecting | unassigned): Consolidated state of the vport. This combines the connection state with link state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectionState"])

    @property
    def ConnectionStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A string describing the status of the hardware connected to this vport
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectionStatus"])

    @property
    def ConnectionStatusDisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectionStatusDisplayName"])

    @property
    def DelayCompensation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Delay compensation value for transceiver and cable length in nano seconds(ns).
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayCompensation"])

    @DelayCompensation.setter
    def DelayCompensation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayCompensation"], value)

    @property
    def DpdkPerformanceAcceleration(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DpdkPerformanceAcceleration"])

    @property
    def InternalId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: For internal use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InternalId"])

    @property
    def IsAvailable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this virtual port is available for assigning to a physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsAvailable"])

    @property
    def IsConnected(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, indicates that the port is connected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsConnected"])

    @property
    def IsFramePreemptionSupported(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsFramePreemptionSupported"])

    @property
    def IsMapped(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this virtual port is mapped.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsMapped"])

    @property
    def IsPullOnly(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (This action only affects assigned ports.) This action will temporarily set the port as an Unassigned Port. This function is used to pull the configuration set by a Tcl script or an IxExplorer port file into the IxNetwork configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPullOnly"])

    @IsPullOnly.setter
    def IsPullOnly(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsPullOnly"], value)

    @property
    def IsVMPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the hardware connected to this vport is a virtual machine port
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsVMPort"])

    @property
    def IxnChassisVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read Only) If true, the installer installs the same resources as installed by the IxNetwork Full installer/IxNetwork Chassis installer on chassis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IxnChassisVersion"])

    @property
    def IxnClientVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read Only) If true, this installs full client side IxNetwork or IxNetwork-FT components.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IxnClientVersion"])

    @property
    def IxosChassisVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read Only) If true, the installer installs the same resources as installed by IxOS on a chassis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IxosChassisVersion"])

    @property
    def LastLinkStateChangeEventTimestamp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A string describing the last link status change client timestamp for the port.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["LastLinkStateChangeEventTimestamp"]
        )

    @property
    def Licenses(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Number of licenses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Licenses"])

    @property
    def Location(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems. This would attempt and wait for chassis/port connection.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Location"])

    @Location.setter
    def Location(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Location"], value)

    @property
    def MacsecEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacsecEnabled"])

    @property
    def MaxStreamsSupported(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxStreamsSupported"])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The description of the port: (1) For an assigned port, the format is: (Port type) (card no.): (port no.) - (chassis name or IP). (2) For an (unassigned) port configuration, the format is: (Port type) Port 00x.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ResourceMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResourceMode"])

    @property
    def RxMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(capture | measure | captureAndMeasure | packetImpairment): The receive mode of the virtual port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxMode"])

    @RxMode.setter
    def RxMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxMode"], value)

    @property
    def State(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(busy | down | unassigned | up | versionMismatch): The virtual port state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["State"])

    @property
    def StateDetail(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(busy | cpuNotReady | idle | inActive | l1ConfigFailed | protocolsNotSupported | versionMismatched | waitingForCPUStatus): This attribute describes the state of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateDetail"])

    @property
    def TraceEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables/Disables rpf port trace for this port
        """
        return self._get_attribute(self._SDM_ATT_MAP["TraceEnabled"])

    @TraceEnabled.setter
    def TraceEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TraceEnabled"], value)

    @property
    def TraceLevel(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kCritical | kDebug | kError | kInfo | kNote | kTrace | kWarning): PCPU Trace level
        """
        return self._get_attribute(self._SDM_ATT_MAP["TraceLevel"])

    @TraceLevel.setter
    def TraceLevel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TraceLevel"], value)

    @property
    def TraceTag(self):
        # type: () -> str
        """
        Returns
        -------
        - str: PCPU Trace Tag
        """
        return self._get_attribute(self._SDM_ATT_MAP["TraceTag"])

    @TraceTag.setter
    def TraceTag(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TraceTag"], value)

    @property
    def TransmitIgnoreLinkStatus(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the port ingores the link status when transmitting data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitIgnoreLinkStatus"])

    @TransmitIgnoreLinkStatus.setter
    def TransmitIgnoreLinkStatus(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitIgnoreLinkStatus"], value)

    @property
    def TxGapControlMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixedMode | averageMode): This object controls the Gap Control mode of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxGapControlMode"])

    @TxGapControlMode.setter
    def TxGapControlMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxGapControlMode"], value)

    @property
    def TxMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(sequential | interleaved | sequentialCoarse | interleavedCoarse | packetImpairment): The transmit mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxMode"])

    @TxMode.setter
    def TxMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxMode"], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ethernet | ethernetvm | ethernetcm | novusmini | novusminipro | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan | novus5GTenTwentyFiveGigLan | novus5GTenTwentyFiveGigLanFcoe | starFourHundredGigLan | starFourHundredGigLanFcoe | ravenEightHundredGigLan | ravenEightHundredGigLanFcoe | aresOneEightHundredGigLanQddC | aresOneEightHundredGigLanQddCFcoe | sertHundredGigLan | aresOneEightHundredGigLanOsfpC | aresOneEightHundredGigLanOsfpCFcoe | aresOneM | aresOneMFcoe): The type of port selection.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    @property
    def UseGlobalSettings(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables/Disables use of global settings instead of local settings on port
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseGlobalSettings"])

    @UseGlobalSettings.setter
    def UseGlobalSettings(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseGlobalSettings"], value)

    @property
    def ValidTxModes(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[interleaved | interleavedCoarse | packetImpairment | sequential | sequentialCoarse]):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidTxModes"])

    def update(
        self,
        ConnectedTo=None,
        DelayCompensation=None,
        IsPullOnly=None,
        Location=None,
        Name=None,
        RxMode=None,
        TraceEnabled=None,
        TraceLevel=None,
        TraceTag=None,
        TransmitIgnoreLinkStatus=None,
        TxGapControlMode=None,
        TxMode=None,
        Type=None,
        UseGlobalSettings=None,
    ):
        # type: (str, str, bool, str, str, str, bool, str, str, bool, str, str, str, bool) -> Vport
        """Updates vport resource on the server.

        Args
        ----
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port)): The physical port to which the unassigned port is assigned.
        - DelayCompensation (str): Delay compensation value for transceiver and cable length in nano seconds(ns).
        - IsPullOnly (bool): (This action only affects assigned ports.) This action will temporarily set the port as an Unassigned Port. This function is used to pull the configuration set by a Tcl script or an IxExplorer port file into the IxNetwork configuration.
        - Location (str): The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems. This would attempt and wait for chassis/port connection.
        - Name (str): The description of the port: (1) For an assigned port, the format is: (Port type) (card no.): (port no.) - (chassis name or IP). (2) For an (unassigned) port configuration, the format is: (Port type) Port 00x.
        - RxMode (str(capture | measure | captureAndMeasure | packetImpairment)): The receive mode of the virtual port.
        - TraceEnabled (bool): Enables/Disables rpf port trace for this port
        - TraceLevel (str(kCritical | kDebug | kError | kInfo | kNote | kTrace | kWarning)): PCPU Trace level
        - TraceTag (str): PCPU Trace Tag
        - TransmitIgnoreLinkStatus (bool): If true, the port ingores the link status when transmitting data.
        - TxGapControlMode (str(fixedMode | averageMode)): This object controls the Gap Control mode of the port.
        - TxMode (str(sequential | interleaved | sequentialCoarse | interleavedCoarse | packetImpairment)): The transmit mode.
        - Type (str(ethernet | ethernetvm | ethernetcm | novusmini | novusminipro | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan | novus5GTenTwentyFiveGigLan | novus5GTenTwentyFiveGigLanFcoe | starFourHundredGigLan | starFourHundredGigLanFcoe | ravenEightHundredGigLan | ravenEightHundredGigLanFcoe | aresOneEightHundredGigLanQddC | aresOneEightHundredGigLanQddCFcoe | sertHundredGigLan | aresOneEightHundredGigLanOsfpC | aresOneEightHundredGigLanOsfpCFcoe | aresOneM | aresOneMFcoe)): The type of port selection.
        - UseGlobalSettings (bool): Enables/Disables use of global settings instead of local settings on port

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedTo=None,
        DelayCompensation=None,
        IsPullOnly=None,
        Location=None,
        Name=None,
        RxMode=None,
        TraceEnabled=None,
        TraceLevel=None,
        TraceTag=None,
        TransmitIgnoreLinkStatus=None,
        TxGapControlMode=None,
        TxMode=None,
        Type=None,
        UseGlobalSettings=None,
    ):
        # type: (str, str, bool, str, str, str, bool, str, str, bool, str, str, str, bool) -> Vport
        """Adds a new vport resource on the server and adds it to the container.

        Args
        ----
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port)): The physical port to which the unassigned port is assigned.
        - DelayCompensation (str): Delay compensation value for transceiver and cable length in nano seconds(ns).
        - IsPullOnly (bool): (This action only affects assigned ports.) This action will temporarily set the port as an Unassigned Port. This function is used to pull the configuration set by a Tcl script or an IxExplorer port file into the IxNetwork configuration.
        - Location (str): The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems. This would attempt and wait for chassis/port connection.
        - Name (str): The description of the port: (1) For an assigned port, the format is: (Port type) (card no.): (port no.) - (chassis name or IP). (2) For an (unassigned) port configuration, the format is: (Port type) Port 00x.
        - RxMode (str(capture | measure | captureAndMeasure | packetImpairment)): The receive mode of the virtual port.
        - TraceEnabled (bool): Enables/Disables rpf port trace for this port
        - TraceLevel (str(kCritical | kDebug | kError | kInfo | kNote | kTrace | kWarning)): PCPU Trace level
        - TraceTag (str): PCPU Trace Tag
        - TransmitIgnoreLinkStatus (bool): If true, the port ingores the link status when transmitting data.
        - TxGapControlMode (str(fixedMode | averageMode)): This object controls the Gap Control mode of the port.
        - TxMode (str(sequential | interleaved | sequentialCoarse | interleavedCoarse | packetImpairment)): The transmit mode.
        - Type (str(ethernet | ethernetvm | ethernetcm | novusmini | novusminipro | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan | novus5GTenTwentyFiveGigLan | novus5GTenTwentyFiveGigLanFcoe | starFourHundredGigLan | starFourHundredGigLanFcoe | ravenEightHundredGigLan | ravenEightHundredGigLanFcoe | aresOneEightHundredGigLanQddC | aresOneEightHundredGigLanQddCFcoe | sertHundredGigLan | aresOneEightHundredGigLanOsfpC | aresOneEightHundredGigLanOsfpCFcoe | aresOneM | aresOneMFcoe)): The type of port selection.
        - UseGlobalSettings (bool): Enables/Disables use of global settings instead of local settings on port

        Returns
        -------
        - self: This instance with all currently retrieved vport resources using find and the newly added vport resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vport resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ActualSpeed=None,
        AdminMode=None,
        AssignedTo=None,
        AssignedToDisplayName=None,
        CaptureSupported=None,
        ConnectedTo=None,
        ConnectionInfo=None,
        ConnectionState=None,
        ConnectionStatus=None,
        ConnectionStatusDisplayName=None,
        DelayCompensation=None,
        DpdkPerformanceAcceleration=None,
        InternalId=None,
        IsAvailable=None,
        IsConnected=None,
        IsFramePreemptionSupported=None,
        IsMapped=None,
        IsPullOnly=None,
        IsVMPort=None,
        IxnChassisVersion=None,
        IxnClientVersion=None,
        IxosChassisVersion=None,
        LastLinkStateChangeEventTimestamp=None,
        Licenses=None,
        Location=None,
        MacsecEnabled=None,
        MaxStreamsSupported=None,
        Name=None,
        ResourceMode=None,
        RxMode=None,
        State=None,
        StateDetail=None,
        TraceEnabled=None,
        TraceLevel=None,
        TraceTag=None,
        TransmitIgnoreLinkStatus=None,
        TxGapControlMode=None,
        TxMode=None,
        Type=None,
        UseGlobalSettings=None,
        ValidTxModes=None,
    ):
        # type: (int, str, str, str, str, str, str, str, str, str, str, str, int, bool, bool, bool, bool, bool, bool, str, str, str, str, str, str, bool, str, str, str, str, str, str, bool, str, str, bool, str, str, str, bool, List[str]) -> Vport
        """Finds and retrieves vport resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vport resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vport resources from the server.

        Args
        ----
        - ActualSpeed (number): The actual speed.
        - AdminMode (str):
        - AssignedTo (str): (Deprecated, Read Only) A new port is assigned with this option.
        - AssignedToDisplayName (str):
        - CaptureSupported (str(data | control | dataAndControl | none)):
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port)): The physical port to which the unassigned port is assigned.
        - ConnectionInfo (str): Detailed information about location of the physical port that is assigned to this port configuration.
        - ConnectionState (str(assignedInUseByOther | assignedUnconnected | connectedLinkDown | connectedLinkUp | connecting | unassigned)): Consolidated state of the vport. This combines the connection state with link state.
        - ConnectionStatus (str): A string describing the status of the hardware connected to this vport
        - ConnectionStatusDisplayName (str):
        - DelayCompensation (str): Delay compensation value for transceiver and cable length in nano seconds(ns).
        - DpdkPerformanceAcceleration (str):
        - InternalId (number): For internal use.
        - IsAvailable (bool): If true, this virtual port is available for assigning to a physical port.
        - IsConnected (bool): If true, indicates that the port is connected.
        - IsFramePreemptionSupported (bool):
        - IsMapped (bool): If true, this virtual port is mapped.
        - IsPullOnly (bool): (This action only affects assigned ports.) This action will temporarily set the port as an Unassigned Port. This function is used to pull the configuration set by a Tcl script or an IxExplorer port file into the IxNetwork configuration.
        - IsVMPort (bool): If true the hardware connected to this vport is a virtual machine port
        - IxnChassisVersion (str): (Read Only) If true, the installer installs the same resources as installed by the IxNetwork Full installer/IxNetwork Chassis installer on chassis.
        - IxnClientVersion (str): (Read Only) If true, this installs full client side IxNetwork or IxNetwork-FT components.
        - IxosChassisVersion (str): (Read Only) If true, the installer installs the same resources as installed by IxOS on a chassis.
        - LastLinkStateChangeEventTimestamp (str): A string describing the last link status change client timestamp for the port.
        - Licenses (str): Number of licenses.
        - Location (str): The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems. This would attempt and wait for chassis/port connection.
        - MacsecEnabled (bool):
        - MaxStreamsSupported (str):
        - Name (str): The description of the port: (1) For an assigned port, the format is: (Port type) (card no.): (port no.) - (chassis name or IP). (2) For an (unassigned) port configuration, the format is: (Port type) Port 00x.
        - ResourceMode (str):
        - RxMode (str(capture | measure | captureAndMeasure | packetImpairment)): The receive mode of the virtual port.
        - State (str(busy | down | unassigned | up | versionMismatch)): The virtual port state.
        - StateDetail (str(busy | cpuNotReady | idle | inActive | l1ConfigFailed | protocolsNotSupported | versionMismatched | waitingForCPUStatus)): This attribute describes the state of the port.
        - TraceEnabled (bool): Enables/Disables rpf port trace for this port
        - TraceLevel (str(kCritical | kDebug | kError | kInfo | kNote | kTrace | kWarning)): PCPU Trace level
        - TraceTag (str): PCPU Trace Tag
        - TransmitIgnoreLinkStatus (bool): If true, the port ingores the link status when transmitting data.
        - TxGapControlMode (str(fixedMode | averageMode)): This object controls the Gap Control mode of the port.
        - TxMode (str(sequential | interleaved | sequentialCoarse | interleavedCoarse | packetImpairment)): The transmit mode.
        - Type (str(ethernet | ethernetvm | ethernetcm | novusmini | novusminipro | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan | novus5GTenTwentyFiveGigLan | novus5GTenTwentyFiveGigLanFcoe | starFourHundredGigLan | starFourHundredGigLanFcoe | ravenEightHundredGigLan | ravenEightHundredGigLanFcoe | aresOneEightHundredGigLanQddC | aresOneEightHundredGigLanQddCFcoe | sertHundredGigLan | aresOneEightHundredGigLanOsfpC | aresOneEightHundredGigLanOsfpCFcoe | aresOneM | aresOneMFcoe)): The type of port selection.
        - UseGlobalSettings (bool): Enables/Disables use of global settings instead of local settings on port
        - ValidTxModes (list(str[interleaved | interleavedCoarse | packetImpairment | sequential | sequentialCoarse])):

        Returns
        -------
        - self: This instance with matching vport resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vport data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vport resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddEgressOnlyTracking(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addEgressOnlyTracking operation on the server.

        Add Egress Only Tracking to the configuration. Pass only those ports which do not have egress only tracking enabled

        addEgressOnlyTracking(async_operation=bool)
        -------------------------------------------
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
            "addEgressOnlyTracking", payload=payload, response_object=None
        )

    def AddGclEntry(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addGclEntry operation on the server.

        Add an entry to the GCL list.

        addGclEntry(Arg2=string, Arg3=string, async_operation=bool)
        -----------------------------------------------------------
        - Arg2 (str): String stating duration of this entry
        - Arg3 (str): String stating gate states
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
        return self._execute("addGclEntry", payload=payload, response_object=None)

    def AddQuickFlowGroups(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addQuickFlowGroups operation on the server.

        Add quick flow traffic items to the configuration.

        addQuickFlowGroups(Arg2=number, async_operation=bool)
        -----------------------------------------------------
        - Arg2 (number): The number of quick flow groups to add.
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
            "addQuickFlowGroups", payload=payload, response_object=None
        )

    def AssignPorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the assignPorts operation on the server.

        Assign hardware ports to virtual ports using port display names. It connects all the ports in the list provided using their location attribute. It takes a bool as input which says ClearOwnership is required or not.

        assignPorts(Arg2=bool, async_operation=bool)list
        ------------------------------------------------
        - Arg2 (bool): If true, it will clear ownership on the hardware ports which have location attribute set.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str[None | /api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

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
        return self._execute("assignPorts", payload=payload, response_object=None)

    def ClearNeighborSolicitation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the clearNeighborSolicitation operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearNeighborSolicitation(async_operation=bool)
        -----------------------------------------------
        This function signature is used when there is a list of vports
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearNeighborSolicitation(async_operation=bool)bool
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "clearNeighborSolicitation", payload=payload, response_object=None
        )

    def ClearNeighborTable(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the clearNeighborTable operation on the server.

        This exec clears the learned neighbor table for the specified vport.

        clearNeighborTable(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "clearNeighborTable", payload=payload, response_object=None
        )

    def ClearPortTransmitDuration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearPortTransmitDuration operation on the server.

        Clear the port transmit duration.

        clearPortTransmitDuration(async_operation=bool)
        -----------------------------------------------
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
            "clearPortTransmitDuration", payload=payload, response_object=None
        )

    def ClearRpfLog(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearRpfLog operation on the server.

        Clears RPF logs for a list of ports.

        clearRpfLog(async_operation=bool)
        ---------------------------------
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
        return self._execute("clearRpfLog", payload=payload, response_object=None)

    def ConnectPort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the connectPort operation on the server.

        Connect a list of ports.

        connectPort(async_operation=bool)
        ---------------------------------
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
        return self._execute("connectPort", payload=payload, response_object=None)

    def ConnectPorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the connectPorts operation on the server.

        Connect a list of ports.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        connectPorts(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        connectPorts(Arg2=bool, async_operation=bool)
        ---------------------------------------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully
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
        return self._execute("connectPorts", payload=payload, response_object=None)

    def CopyTapSettings(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the copyTapSettings operation on the server.

        It will copy the values from a port to the given ports.

        copyTapSettings(Arg2=list, async_operation=bool)
        ------------------------------------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport])):
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
        return self._execute("copyTapSettings", payload=payload, response_object=None)

    def DeleteCustomDefaults(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the deleteCustomDefaults operation on the server.

        It will delete custom defaults for the given ports.

        deleteCustomDefaults(async_operation=bool)
        ------------------------------------------
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
            "deleteCustomDefaults", payload=payload, response_object=None
        )

    def EnableOAM(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the enableOAM operation on the server.

        Enable/Disable OAM on a list of ports.

        enableOAM(Arg2=bool, async_operation=bool)
        ------------------------------------------
        - Arg2 (bool): If true, it will enable OAM. Otherwise, it will disable OAM.
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
        return self._execute("enableOAM", payload=payload, response_object=None)

    def GetTapSettings(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the getTapSettings operation on the server.

        Get TAP Settings for the given ports.

        getTapSettings(async_operation=bool)
        ------------------------------------
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
        return self._execute("getTapSettings", payload=payload, response_object=None)

    def IgmpJoin(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpJoin operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpJoin(Arg2=string, async_operation=bool)
        -------------------------------------------
        - Arg2 (str): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpJoin(Arg2=string, Arg3=number, async_operation=bool)
        --------------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (number): NOT DEFINED
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
        return self._execute("igmpJoin", payload=payload, response_object=None)

    def IgmpLeave(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpLeave operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpLeave(Arg2=string, async_operation=bool)
        --------------------------------------------
        - Arg2 (str): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpLeave(Arg2=string, Arg3=number, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (number): NOT DEFINED
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
        return self._execute("igmpLeave", payload=payload, response_object=None)

    def Import(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the import operation on the server.

        Imports the port file (also supports legacy port files).

        import(Arg2=href, async_operation=bool)
        ---------------------------------------
        - Arg2 (obj(ixnetwork_restpy.files.Files)): The file to be imported.
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
        return self._execute("import", payload=payload, response_object=None)

    def LinkUpDn(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the linkUpDn operation on the server.

        Simulate port link up/down.

        linkUpDn(Arg2=enum, async_operation=bool)
        -----------------------------------------
        - Arg2 (str(down | up)): A valid enum value as specified by the restriction.
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
        return self._execute("linkUpDn", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "pauseStatelessTraffic", payload=payload, response_object=None
        )

    def PullPort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the pullPort operation on the server.

        Pulls config onto vport or group of vports.

        pullPort(async_operation=bool)
        ------------------------------
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
        return self._execute("pullPort", payload=payload, response_object=None)

    def RefreshUnresolvedNeighbors(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshUnresolvedNeighbors operation on the server.

        Refresh unresolved neighbours.

        refreshUnresolvedNeighbors(async_operation=bool)bool
        ----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshUnresolvedNeighbors", payload=payload, response_object=None
        )

    def ReleaseCapturePorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the releaseCapturePorts operation on the server.

        Release capture buffer from a list of ports.

        releaseCapturePorts(async_operation=bool)
        -----------------------------------------
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
            "releaseCapturePorts", payload=payload, response_object=None
        )

    def ReleasePort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the releasePort operation on the server.

        Release a hardware port.

        releasePort(async_operation=bool)
        ---------------------------------
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
        return self._execute("releasePort", payload=payload, response_object=None)

    def RemoveGclEntry(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the removeGclEntry operation on the server.

        Remove an entry from the GCL list.

        removeGclEntry(Arg2=number, async_operation=bool)
        -------------------------------------------------
        - Arg2 (number): Integer indicating GCL table entry index to remove
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
        return self._execute("removeGclEntry", payload=payload, response_object=None)

    def ResetPortCpu(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the resetPortCpu operation on the server.

        Reboot port CPU.

        resetPortCpu(async_operation=bool)
        ----------------------------------
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
        return self._execute("resetPortCpu", payload=payload, response_object=None)

    def ResetPortCpuAndFactoryDefault(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the resetPortCpuAndFactoryDefault operation on the server.

        Reboots the port CPU and restores the default settings.

        resetPortCpuAndFactoryDefault(async_operation=bool)
        ---------------------------------------------------
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
            "resetPortCpuAndFactoryDefault", payload=payload, response_object=None
        )

    def RestartPppNegotiation(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartPppNegotiation operation on the server.

        Restarts the PPP negotiation on the port.

        restartPppNegotiation(async_operation=bool)
        -------------------------------------------
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
        return self._execute(
            "restartPppNegotiation", payload=payload, response_object=None
        )

    def RestoreCustomDefaults(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restoreCustomDefaults operation on the server.

        It will restore custom defaults for the given ports.

        restoreCustomDefaults(async_operation=bool)
        -------------------------------------------
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
            "restoreCustomDefaults", payload=payload, response_object=None
        )

    def RestoreDefaults(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restoreDefaults operation on the server.

        Restore the default values for the given ports.

        restoreDefaults(async_operation=bool)
        -------------------------------------
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
        return self._execute("restoreDefaults", payload=payload, response_object=None)

    def SaveCustomDefaults(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the saveCustomDefaults operation on the server.

        It will save custom defaults for the given ports.

        saveCustomDefaults(async_operation=bool)
        ----------------------------------------
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
            "saveCustomDefaults", payload=payload, response_object=None
        )

    def SendArp(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendArp operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendArp(async_operation=bool)bool
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        sendArp(Arg2=list, async_operation=bool)bool
        --------------------------------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/interface])): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute("sendArp", payload=payload, response_object=None)

    def SendArpAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendArpAll operation on the server.

        NOT DEFINED

        sendArpAll(async_operation=bool)
        --------------------------------
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
        return self._execute("sendArpAll", payload=payload, response_object=None)

    def SendNs(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendNs operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendNs(async_operation=bool)bool
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        sendNs(Arg2=list, async_operation=bool)bool
        -------------------------------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/interface])): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute("sendNs", payload=payload, response_object=None)

    def SendNsAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendNsAll operation on the server.

        NOT DEFINED

        sendNsAll(async_operation=bool)
        -------------------------------
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
        return self._execute("sendNsAll", payload=payload, response_object=None)

    def SendRs(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendRs operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendRs(async_operation=bool)bool
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        sendRs(Arg2=list, async_operation=bool)bool
        -------------------------------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/interface])): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute("sendRs", payload=payload, response_object=None)

    def SendRsAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendRsAll operation on the server.

        NOT DEFINED

        sendRsAll(async_operation=bool)
        -------------------------------
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
        return self._execute("sendRsAll", payload=payload, response_object=None)

    def SetFactoryDefaults(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setFactoryDefaults operation on the server.

        Set default values for port settings.

        setFactoryDefaults(async_operation=bool)
        ----------------------------------------
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
            "setFactoryDefaults", payload=payload, response_object=None
        )

    def SetTapSettings(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setTapSettings operation on the server.

        Send TAP Settings to IxServer for the given ports.

        setTapSettings(async_operation=bool)
        ------------------------------------
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
        return self._execute("setTapSettings", payload=payload, response_object=None)

    def StartFecErrorInsertion(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startFecErrorInsertion operation on the server.

        Starts FEC error insertion on the port.

        startFecErrorInsertion(async_operation=bool)
        --------------------------------------------
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
            "startFecErrorInsertion", payload=payload, response_object=None
        )

    def StartPcsErrorGeneration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startPcsErrorGeneration operation on the server.

        Starts PCS error generation on the port.

        startPcsErrorGeneration(async_operation=bool)
        ---------------------------------------------
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
            "startPcsErrorGeneration", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "startStatelessTraffic", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "startStatelessTrafficBlocking", payload=payload, response_object=None
        )

    def StopFecErrorInsertion(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopFecErrorInsertion operation on the server.

        Stops FEC error insertion on the port.

        stopFecErrorInsertion(async_operation=bool)
        -------------------------------------------
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
            "stopFecErrorInsertion", payload=payload, response_object=None
        )

    def StopPcsErrorGeneration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopPcsErrorGeneration operation on the server.

        Stops PCS error generation on the port.

        stopPcsErrorGeneration(async_operation=bool)
        --------------------------------------------
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
            "stopPcsErrorGeneration", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "stopStatelessTraffic", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "stopStatelessTrafficBlocking", payload=payload, response_object=None
        )

    def SwitchMode(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the switchMode operation on the server.

        Switches the port mode. Takes vports as input.

        switchMode(Arg2=list, Arg3=bool, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (list(str)): List of valid Modes
        - Arg3 (bool): If true, it will clear ownership on the hardware ports for which mode switch is being done.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Warning Messages

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
        return self._execute("switchMode", payload=payload, response_object=None)

    def UnassignPorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the unassignPorts operation on the server.

        Unassign hardware ports.

        unassignPorts(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool): If true, virtual ports will be deleted.
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
        return self._execute("unassignPorts", payload=payload, response_object=None)

    def UpdateGclEntry(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the updateGclEntry operation on the server.

        Update an entry in the GCL list.

        updateGclEntry(Arg2=number, Arg3=string, Arg4=string, async_operation=bool)
        ---------------------------------------------------------------------------
        - Arg2 (number): Integer indicating GCL table index to update
        - Arg3 (str): String stating the new duration of this entry
        - Arg4 (str): String stating gate states
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
        return self._execute("updateGclEntry", payload=payload, response_object=None)

    def WriteRpfLogToFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the writeRpfLogToFile operation on the server.

        Write RPF log to file for a port

        writeRpfLogToFile(async_operation=bool)string
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

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
        return self._execute("writeRpfLogToFile", payload=payload, response_object=None)
