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


class Vport(Base):
    """This is the virtual port hierarchy, which is used to configure IxNetwork.
    The Vport class encapsulates a list of vport resources that are managed by the user.
    A list of resources can be retrieved from the server using the Vport.find() method.
    The list can be managed by using the Vport.add() and Vport.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vport'
    _SDM_ATT_MAP = {
        'ActualSpeed': 'actualSpeed',
        'AdminMode': 'adminMode',
        'AssignedTo': 'assignedTo',
        'AssignedToDisplayName': 'assignedToDisplayName',
        'CaptureSupported': 'captureSupported',
        'ConnectedTo': 'connectedTo',
        'ConnectionInfo': 'connectionInfo',
        'ConnectionState': 'connectionState',
        'ConnectionStatus': 'connectionStatus',
        'ConnectionStatusDisplayName': 'connectionStatusDisplayName',
        'DpdkPerformanceAcceleration': 'dpdkPerformanceAcceleration',
        'InternalId': 'internalId',
        'IsAvailable': 'isAvailable',
        'IsConnected': 'isConnected',
        'IsFramePreemptionSupported': 'isFramePreemptionSupported',
        'IsMapped': 'isMapped',
        'IsPullOnly': 'isPullOnly',
        'IsVMPort': 'isVMPort',
        'IxnChassisVersion': 'ixnChassisVersion',
        'IxnClientVersion': 'ixnClientVersion',
        'IxosChassisVersion': 'ixosChassisVersion',
        'Licenses': 'licenses',
        'Location': 'location',
        'Name': 'name',
        'ResourceMode': 'resourceMode',
        'RxMode': 'rxMode',
        'State': 'state',
        'StateDetail': 'stateDetail',
        'TraceEnabled': 'traceEnabled',
        'TraceLevel': 'traceLevel',
        'TraceTag': 'traceTag',
        'TransmitIgnoreLinkStatus': 'transmitIgnoreLinkStatus',
        'TxGapControlMode': 'txGapControlMode',
        'TxMode': 'txMode',
        'Type': 'type',
        'UseGlobalSettings': 'useGlobalSettings',
        'ValidTxModes': 'validTxModes',
    }

    def __init__(self, parent):
        super(Vport, self).__init__(parent)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.capture import Capture
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.discoveredneighbor.discoveredneighbor import DiscoveredNeighbor
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.interface import Interface
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interfacediscoveredaddress.interfacediscoveredaddress import InterfaceDiscoveredAddress
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.l1config import L1Config
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.protocolstack import ProtocolStack
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.protocols import Protocols
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ratecontrolparameters.ratecontrolparameters import RateControlParameters
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.tapsettings.tapsettings import TapSettings
        return TapSettings(self)

    @property
    def ActualSpeed(self):
        """
        Returns
        -------
        - number: The actual speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActualSpeed'])

    @property
    def AdminMode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdminMode'])

    @property
    def AssignedTo(self):
        """DEPRECATED 
        Returns
        -------
        - str: (Read Only) A new port is assigned with this option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AssignedTo'])

    @property
    def AssignedToDisplayName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AssignedToDisplayName'])

    @property
    def CaptureSupported(self):
        """
        Returns
        -------
        - str(data | control | dataAndControl | none): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureSupported'])

    @property
    def ConnectedTo(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/availableHardware/.../port): The physical port to which the unassigned port is assigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedTo'])
    @ConnectedTo.setter
    def ConnectedTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedTo'], value)

    @property
    def ConnectionInfo(self):
        """
        Returns
        -------
        - str: Detailed information about location of the physical port that is assigned to this port configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionInfo'])

    @property
    def ConnectionState(self):
        """
        Returns
        -------
        - str(assignedInUseByOther | assignedUnconnected | connectedLinkDown | connectedLinkUp | connecting | unassigned): Consolidated state of the vport. This combines the connection state with link state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionState'])

    @property
    def ConnectionStatus(self):
        """
        Returns
        -------
        - str: A string describing the status of the hardware connected to this vport
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionStatus'])

    @property
    def ConnectionStatusDisplayName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionStatusDisplayName'])

    @property
    def DpdkPerformanceAcceleration(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DpdkPerformanceAcceleration'])

    @property
    def InternalId(self):
        """
        Returns
        -------
        - number: For internal use.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InternalId'])

    @property
    def IsAvailable(self):
        """
        Returns
        -------
        - bool: If true, this virtual port is available for assigning to a physical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAvailable'])

    @property
    def IsConnected(self):
        """
        Returns
        -------
        - bool: If true, indicates that the port is connected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsConnected'])

    @property
    def IsFramePreemptionSupported(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsFramePreemptionSupported'])

    @property
    def IsMapped(self):
        """
        Returns
        -------
        - bool: If true, this virtual port is mapped.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMapped'])

    @property
    def IsPullOnly(self):
        """
        Returns
        -------
        - bool: (This action only affects assigned ports.) This action will temporarily set the port as an Unassigned Port. This function is used to pull the configuration set by a Tcl script or an IxExplorer port file into the IxNetwork configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPullOnly'])
    @IsPullOnly.setter
    def IsPullOnly(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsPullOnly'], value)

    @property
    def IsVMPort(self):
        """
        Returns
        -------
        - bool: If true the hardware connected to this vport is a virtual machine port
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsVMPort'])

    @property
    def IxnChassisVersion(self):
        """
        Returns
        -------
        - str: (Read Only) If true, the installer installs the same resources as installed by the IxNetwork Full installer/IxNetwork Chassis installer on chassis.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IxnChassisVersion'])

    @property
    def IxnClientVersion(self):
        """
        Returns
        -------
        - str: (Read Only) If true, this installs full client side IxNetwork or IxNetwork-FT components.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IxnClientVersion'])

    @property
    def IxosChassisVersion(self):
        """
        Returns
        -------
        - str: (Read Only) If true, the installer installs the same resources as installed by IxOS on a chassis.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IxosChassisVersion'])

    @property
    def Licenses(self):
        """
        Returns
        -------
        - str: Number of licenses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Licenses'])

    @property
    def Location(self):
        """
        Returns
        -------
        - str: The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Location'])
    @Location.setter
    def Location(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Location'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The description of the port: (1) For an assigned port, the format is: (Port type) (card no.): (port no.) - (chassis name or IP). (2) For an (unassigned) port configuration, the format is: (Port type) Port 00x.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ResourceMode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResourceMode'])

    @property
    def RxMode(self):
        """
        Returns
        -------
        - str(capture | measure | captureAndMeasure | packetImpairment): The receive mode of the virtual port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxMode'])
    @RxMode.setter
    def RxMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RxMode'], value)

    @property
    def State(self):
        """DEPRECATED 
        Returns
        -------
        - str(busy | down | unassigned | up | versionMismatch): The virtual port state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def StateDetail(self):
        """DEPRECATED 
        Returns
        -------
        - str(busy | cpuNotReady | idle | inActive | l1ConfigFailed | protocolsNotSupported | versionMismatched | waitingForCPUStatus): This attribute describes the state of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateDetail'])

    @property
    def TraceEnabled(self):
        """
        Returns
        -------
        - bool: Enables/Disables rpf port trace for this port
        """
        return self._get_attribute(self._SDM_ATT_MAP['TraceEnabled'])
    @TraceEnabled.setter
    def TraceEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TraceEnabled'], value)

    @property
    def TraceLevel(self):
        """
        Returns
        -------
        - str(kCritical | kDebug | kError | kInfo | kNote | kTrace | kWarning): PCPU Trace level
        """
        return self._get_attribute(self._SDM_ATT_MAP['TraceLevel'])
    @TraceLevel.setter
    def TraceLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TraceLevel'], value)

    @property
    def TraceTag(self):
        """
        Returns
        -------
        - str: PCPU Trace Tag
        """
        return self._get_attribute(self._SDM_ATT_MAP['TraceTag'])
    @TraceTag.setter
    def TraceTag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TraceTag'], value)

    @property
    def TransmitIgnoreLinkStatus(self):
        """
        Returns
        -------
        - bool: If true, the port ingores the link status when transmitting data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitIgnoreLinkStatus'])
    @TransmitIgnoreLinkStatus.setter
    def TransmitIgnoreLinkStatus(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmitIgnoreLinkStatus'], value)

    @property
    def TxGapControlMode(self):
        """
        Returns
        -------
        - str(fixedMode | averageMode): This object controls the Gap Control mode of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxGapControlMode'])
    @TxGapControlMode.setter
    def TxGapControlMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxGapControlMode'], value)

    @property
    def TxMode(self):
        """
        Returns
        -------
        - str(sequential | interleaved | sequentialCoarse | interleavedCoarse | packetImpairment): The transmit mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxMode'])
    @TxMode.setter
    def TxMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxMode'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(ethernet | ethernetvm | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan): The type of port selection.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def UseGlobalSettings(self):
        """
        Returns
        -------
        - bool: Enables/Disables use of global settings instead of local settings on port
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseGlobalSettings'])
    @UseGlobalSettings.setter
    def UseGlobalSettings(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseGlobalSettings'], value)

    @property
    def ValidTxModes(self):
        """
        Returns
        -------
        - list(str[interleaved | interleavedCoarse | packetImpairment | sequential | sequentialCoarse]): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValidTxModes'])

    def update(self, ConnectedTo=None, IsPullOnly=None, Location=None, Name=None, RxMode=None, TraceEnabled=None, TraceLevel=None, TraceTag=None, TransmitIgnoreLinkStatus=None, TxGapControlMode=None, TxMode=None, Type=None, UseGlobalSettings=None):
        """Updates vport resource on the server.

        Args
        ----
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/availableHardware/.../port)): The physical port to which the unassigned port is assigned.
        - IsPullOnly (bool): (This action only affects assigned ports.) This action will temporarily set the port as an Unassigned Port. This function is used to pull the configuration set by a Tcl script or an IxExplorer port file into the IxNetwork configuration.
        - Location (str): The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems.
        - Name (str): The description of the port: (1) For an assigned port, the format is: (Port type) (card no.): (port no.) - (chassis name or IP). (2) For an (unassigned) port configuration, the format is: (Port type) Port 00x.
        - RxMode (str(capture | measure | captureAndMeasure | packetImpairment)): The receive mode of the virtual port.
        - TraceEnabled (bool): Enables/Disables rpf port trace for this port
        - TraceLevel (str(kCritical | kDebug | kError | kInfo | kNote | kTrace | kWarning)): PCPU Trace level
        - TraceTag (str): PCPU Trace Tag
        - TransmitIgnoreLinkStatus (bool): If true, the port ingores the link status when transmitting data.
        - TxGapControlMode (str(fixedMode | averageMode)): This object controls the Gap Control mode of the port.
        - TxMode (str(sequential | interleaved | sequentialCoarse | interleavedCoarse | packetImpairment)): The transmit mode.
        - Type (str(ethernet | ethernetvm | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan)): The type of port selection.
        - UseGlobalSettings (bool): Enables/Disables use of global settings instead of local settings on port

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedTo=None, IsPullOnly=None, Location=None, Name=None, RxMode=None, TraceEnabled=None, TraceLevel=None, TraceTag=None, TransmitIgnoreLinkStatus=None, TxGapControlMode=None, TxMode=None, Type=None, UseGlobalSettings=None):
        """Adds a new vport resource on the server and adds it to the container.

        Args
        ----
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/availableHardware/.../port)): The physical port to which the unassigned port is assigned.
        - IsPullOnly (bool): (This action only affects assigned ports.) This action will temporarily set the port as an Unassigned Port. This function is used to pull the configuration set by a Tcl script or an IxExplorer port file into the IxNetwork configuration.
        - Location (str): The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems.
        - Name (str): The description of the port: (1) For an assigned port, the format is: (Port type) (card no.): (port no.) - (chassis name or IP). (2) For an (unassigned) port configuration, the format is: (Port type) Port 00x.
        - RxMode (str(capture | measure | captureAndMeasure | packetImpairment)): The receive mode of the virtual port.
        - TraceEnabled (bool): Enables/Disables rpf port trace for this port
        - TraceLevel (str(kCritical | kDebug | kError | kInfo | kNote | kTrace | kWarning)): PCPU Trace level
        - TraceTag (str): PCPU Trace Tag
        - TransmitIgnoreLinkStatus (bool): If true, the port ingores the link status when transmitting data.
        - TxGapControlMode (str(fixedMode | averageMode)): This object controls the Gap Control mode of the port.
        - TxMode (str(sequential | interleaved | sequentialCoarse | interleavedCoarse | packetImpairment)): The transmit mode.
        - Type (str(ethernet | ethernetvm | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan)): The type of port selection.
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

    def find(self, ActualSpeed=None, AdminMode=None, AssignedTo=None, AssignedToDisplayName=None, CaptureSupported=None, ConnectedTo=None, ConnectionInfo=None, ConnectionState=None, ConnectionStatus=None, ConnectionStatusDisplayName=None, DpdkPerformanceAcceleration=None, InternalId=None, IsAvailable=None, IsConnected=None, IsFramePreemptionSupported=None, IsMapped=None, IsPullOnly=None, IsVMPort=None, IxnChassisVersion=None, IxnClientVersion=None, IxosChassisVersion=None, Licenses=None, Location=None, Name=None, ResourceMode=None, RxMode=None, State=None, StateDetail=None, TraceEnabled=None, TraceLevel=None, TraceTag=None, TransmitIgnoreLinkStatus=None, TxGapControlMode=None, TxMode=None, Type=None, UseGlobalSettings=None, ValidTxModes=None):
        """Finds and retrieves vport resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vport resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vport resources from the server.

        Args
        ----
        - ActualSpeed (number): The actual speed.
        - AdminMode (str): 
        - AssignedTo (str): (Read Only) A new port is assigned with this option.
        - AssignedToDisplayName (str): 
        - CaptureSupported (str(data | control | dataAndControl | none)): 
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/availableHardware/.../port)): The physical port to which the unassigned port is assigned.
        - ConnectionInfo (str): Detailed information about location of the physical port that is assigned to this port configuration.
        - ConnectionState (str(assignedInUseByOther | assignedUnconnected | connectedLinkDown | connectedLinkUp | connecting | unassigned)): Consolidated state of the vport. This combines the connection state with link state.
        - ConnectionStatus (str): A string describing the status of the hardware connected to this vport
        - ConnectionStatusDisplayName (str): 
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
        - Licenses (str): Number of licenses.
        - Location (str): The current format is {chassisIp}/{frontPanelPort}.{fanoutPort} or {chassisIp};{cardId};{portId} for legacy systems.
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
        - Type (str(ethernet | ethernetvm | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan)): The type of port selection.
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

    def AddQuickFlowGroups(self, *args, **kwargs):
        """Executes the addQuickFlowGroups operation on the server.

        Add quick flow traffic items to the configuration.

        addQuickFlowGroups(Arg2=number)
        -------------------------------
        - Arg2 (number): The number of quick flow groups to add.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addQuickFlowGroups', payload=payload, response_object=None)

    def AssignPorts(self, *args, **kwargs):
        """Executes the assignPorts operation on the server.

        Assign hardware ports to virtual ports using port display names. It connects all the ports in the list provided using their location attribute. It takes a bool as input which says ClearOwnership is required or not.

        assignPorts(Arg2=bool)list
        --------------------------
        - Arg2 (bool): If true, it will clear ownership on the hardware ports which have location attribute set.
        - Returns list(str[None | /api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('assignPorts', payload=payload, response_object=None)

    def ClearNeighborSolicitation(self):
        """Executes the clearNeighborSolicitation operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('clearNeighborSolicitation', payload=payload, response_object=None)

    def ClearNeighborTable(self):
        """Executes the clearNeighborTable operation on the server.

        This exec clears the learned neighbor table for the specified vport.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('clearNeighborTable', payload=payload, response_object=None)

    def ClearPortTransmitDuration(self):
        """Executes the clearPortTransmitDuration operation on the server.

        Clear the port transmit duration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('clearPortTransmitDuration', payload=payload, response_object=None)

    def ConnectPort(self):
        """Executes the connectPort operation on the server.

        Connect a list of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('connectPort', payload=payload, response_object=None)

    def ConnectPorts(self, *args, **kwargs):
        """Executes the connectPorts operation on the server.

        Connect a list of ports.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        connectPorts(Arg2=bool)
        -----------------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('connectPorts', payload=payload, response_object=None)

    def CopyTapSettings(self, *args, **kwargs):
        """Executes the copyTapSettings operation on the server.

        It will copy the values from a port to the given ports.

        copyTapSettings(Arg2=list)
        --------------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('copyTapSettings', payload=payload, response_object=None)

    def DeleteCustomDefaults(self):
        """Executes the deleteCustomDefaults operation on the server.

        It will delete custom defaults for the given ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('deleteCustomDefaults', payload=payload, response_object=None)

    def EnableOAM(self, *args, **kwargs):
        """Executes the enableOAM operation on the server.

        Enable/Disable OAM on a list of ports.

        enableOAM(Arg2=bool)
        --------------------
        - Arg2 (bool): If true, it will enable OAM. Otherwise, it will disable OAM.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableOAM', payload=payload, response_object=None)

    def GetTapSettings(self):
        """Executes the getTapSettings operation on the server.

        Get TAP Settings for the given ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('getTapSettings', payload=payload, response_object=None)

    def IgmpJoin(self, *args, **kwargs):
        """Executes the igmpJoin operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpJoin(Arg2=string)
        ---------------------
        - Arg2 (str): NOT DEFINED

        igmpJoin(Arg2=string, Arg3=number)
        ----------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (number): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpJoin', payload=payload, response_object=None)

    def IgmpLeave(self, *args, **kwargs):
        """Executes the igmpLeave operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpLeave(Arg2=string)
        ----------------------
        - Arg2 (str): NOT DEFINED

        igmpLeave(Arg2=string, Arg3=number)
        -----------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (number): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpLeave', payload=payload, response_object=None)

    def Import(self, *args, **kwargs):
        """Executes the import operation on the server.

        Imports the port file (also supports legacy port files).

        import(Arg2=href)
        -----------------
        - Arg2 (obj(ixnetwork_restpy.files.Files)): The file to be imported.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('import', payload=payload, response_object=None)

    def LinkUpDn(self, *args, **kwargs):
        """Executes the linkUpDn operation on the server.

        Simulate port link up/down.

        linkUpDn(Arg2=enum)
        -------------------
        - Arg2 (str(down | up)): A valid enum value as specified by the restriction.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('linkUpDn', payload=payload, response_object=None)

    def PauseStatelessTraffic(self, *args, **kwargs):
        """Executes the pauseStatelessTraffic operation on the server.

        Pause or Resume stateless traffic.

        pauseStatelessTraffic(Arg2=bool)
        --------------------------------
        - Arg2 (bool): If true, it will pause running traffic. If false, it will resume previously paused traffic.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('pauseStatelessTraffic', payload=payload, response_object=None)

    def PullPort(self):
        """Executes the pullPort operation on the server.

        Pulls config onto vport or group of vports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('pullPort', payload=payload, response_object=None)

    def RefreshUnresolvedNeighbors(self):
        """Executes the refreshUnresolvedNeighbors operation on the server.

        Refresh unresolved neighbours.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshUnresolvedNeighbors', payload=payload, response_object=None)

    def ReleaseCapturePorts(self):
        """Executes the releaseCapturePorts operation on the server.

        Release capture buffer from a list of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('releaseCapturePorts', payload=payload, response_object=None)

    def ReleasePort(self):
        """Executes the releasePort operation on the server.

        Release a hardware port.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('releasePort', payload=payload, response_object=None)

    def ResetPortCpu(self):
        """Executes the resetPortCpu operation on the server.

        Reboot port CPU.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('resetPortCpu', payload=payload, response_object=None)

    def ResetPortCpuAndFactoryDefault(self):
        """Executes the resetPortCpuAndFactoryDefault operation on the server.

        Reboots the port CPU and restores the default settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('resetPortCpuAndFactoryDefault', payload=payload, response_object=None)

    def RestartPppNegotiation(self):
        """Executes the restartPppNegotiation operation on the server.

        Restarts the PPP negotiation on the port.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('restartPppNegotiation', payload=payload, response_object=None)

    def RestoreCustomDefaults(self):
        """Executes the restoreCustomDefaults operation on the server.

        It will restore custom defaults for the given ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('restoreCustomDefaults', payload=payload, response_object=None)

    def RestoreDefaults(self):
        """Executes the restoreDefaults operation on the server.

        Restore the default values for the given ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('restoreDefaults', payload=payload, response_object=None)

    def SaveCustomDefaults(self):
        """Executes the saveCustomDefaults operation on the server.

        It will save custom defaults for the given ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('saveCustomDefaults', payload=payload, response_object=None)

    def SendArp(self, *args, **kwargs):
        """Executes the sendArp operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendArp(Arg2=list)bool
        ----------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../interface])): NOT DEFINED
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendArp', payload=payload, response_object=None)

    def SendArpAll(self):
        """Executes the sendArpAll operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('sendArpAll', payload=payload, response_object=None)

    def SendNs(self, *args, **kwargs):
        """Executes the sendNs operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendNs(Arg2=list)bool
        ---------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../interface])): NOT DEFINED
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendNs', payload=payload, response_object=None)

    def SendNsAll(self):
        """Executes the sendNsAll operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('sendNsAll', payload=payload, response_object=None)

    def SendRs(self, *args, **kwargs):
        """Executes the sendRs operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendRs(Arg2=list)bool
        ---------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../interface])): NOT DEFINED
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendRs', payload=payload, response_object=None)

    def SendRsAll(self):
        """Executes the sendRsAll operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('sendRsAll', payload=payload, response_object=None)

    def SetFactoryDefaults(self):
        """Executes the setFactoryDefaults operation on the server.

        Set default values for port settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('setFactoryDefaults', payload=payload, response_object=None)

    def SetTapSettings(self):
        """Executes the setTapSettings operation on the server.

        Send TAP Settings to IxServer for the given ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('setTapSettings', payload=payload, response_object=None)

    def StartStatelessTraffic(self):
        """Executes the startStatelessTraffic operation on the server.

        Start the traffic configuration for stateless traffic items only.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('startStatelessTraffic', payload=payload, response_object=None)

    def StartStatelessTrafficBlocking(self):
        """Executes the startStatelessTrafficBlocking operation on the server.

        Start the traffic configuration for stateless traffic items only. This will block until traffic is fully started.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('startStatelessTrafficBlocking', payload=payload, response_object=None)

    def StopStatelessTraffic(self):
        """Executes the stopStatelessTraffic operation on the server.

        Stop the stateless traffic items.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stopStatelessTraffic', payload=payload, response_object=None)

    def StopStatelessTrafficBlocking(self):
        """Executes the stopStatelessTrafficBlocking operation on the server.

        Stop the traffic configuration for stateless traffic items only. This will block until traffic is fully stopped.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stopStatelessTrafficBlocking', payload=payload, response_object=None)

    def SwitchMode(self, *args, **kwargs):
        """Executes the switchMode operation on the server.

        Switches the port mode. Takes vports as input.

        switchMode(Arg2=list, Arg3=bool)string
        --------------------------------------
        - Arg2 (list(str)): List of valid Modes
        - Arg3 (bool): If true, it will clear ownership on the hardware ports for which mode switch is being done.
        - Returns str: Warning Messages

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('switchMode', payload=payload, response_object=None)

    def UnassignPorts(self, *args, **kwargs):
        """Executes the unassignPorts operation on the server.

        Unassign hardware ports.

        unassignPorts(Arg2=bool)
        ------------------------
        - Arg2 (bool): If true, virtual ports will be deleted.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('unassignPorts', payload=payload, response_object=None)
