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


class Preferences(Base):
    """The preferences node contains user configurable user level preferences
    The Preferences class encapsulates a required preferences resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "preferences"
    _SDM_ATT_MAP = {
        "AllowProtocolSessionStateLog": "allowProtocolSessionStateLog",
        "AutoCleanLogs": "autoCleanLogs",
        "AutoSaveIntervalMin": "autoSaveIntervalMin",
        "AutoSaveLocation": "autoSaveLocation",
        "ClientTraceLevel": "clientTraceLevel",
        "ConfigurationAtIxNetworkStartup": "configurationAtIxNetworkStartup",
        "ConnectPortsOnLoadConfig": "connectPortsOnLoadConfig",
        "DeleteDumpFilesOlderThan": "deleteDumpFilesOlderThan",
        "DisableMinimizedScenario": "disableMinimizedScenario",
        "DisableProtoSpecificConnectors": "disableProtoSpecificConnectors",
        "DropPacketsOnHighRx": "dropPacketsOnHighRx",
        "EnableAutoSave": "enableAutoSave",
        "EnableCloudTools": "enableCloudTools",
        "EnableDpdkForNewConfig": "enableDpdkForNewConfig",
        "EnablePCPUGuardRail": "enablePCPUGuardRail",
        "EnableScriptWatch": "enableScriptWatch",
        "ForceLegacyPortNameInStats": "forceLegacyPortNameInStats",
        "IncludeTroubleshootingComments": "includeTroubleshootingComments",
        "LatestConfigInDiagEnabled": "latestConfigInDiagEnabled",
        "PcpuGuardRailCriticalThreshold": "pcpuGuardRailCriticalThreshold",
        "PcpuGuardRailWarningThreshold": "pcpuGuardRailWarningThreshold",
        "PhyMode": "phyMode",
        "PingChassisOnConnect": "pingChassisOnConnect",
        "ProcessProtocolStateChangeAsync": "processProtocolStateChangeAsync",
        "ProtocolGridSortingOrder": "protocolGridSortingOrder",
        "RebootPortOnGuardRailCritical": "rebootPortOnGuardRailCritical",
        "RebootPortsOnConnect": "rebootPortsOnConnect",
        "ReceiveMode": "receiveMode",
        "RecentChassisList": "recentChassisList",
        "RecentFiles": "recentFiles",
        "ResourceManagerLocation": "resourceManagerLocation",
        "ScriptgenTextEditorPath": "scriptgenTextEditorPath",
        "SelectDGOnCreation": "selectDGOnCreation",
        "SequenceCheckingWhenNoTxRxSync": "sequenceCheckingWhenNoTxRxSync",
        "ShortenScenarioObjectNameInMiddle": "shortenScenarioObjectNameInMiddle",
        "StreamLogsToSyslogServer": "streamLogsToSyslogServer",
        "SyslogHost": "syslogHost",
        "SyslogPort": "syslogPort",
        "TopologyTreeSortingMode": "topologyTreeSortingMode",
        "TransmitMode": "transmitMode",
        "UseNewApiBrowser": "useNewApiBrowser",
    }
    _SDM_ENUM_MAP = {
        "clientTraceLevel": ["debug", "error", "fatal", "info", "warn"],
        "configurationAtIxNetworkStartup": [
            "useEmptyConfiguration",
            "useLastSavedConfiguration",
        ],
        "phyMode": ["copper", "fiber"],
        "protocolGridSortingOrder": ["CreationTime", "TopologyName"],
        "receiveMode": ["capturePackets", "measureTrafficFlow"],
        "topologyTreeSortingMode": ["Number", "String"],
        "transmitMode": ["interleavedStreams", "sequentialStreams"],
    }

    def __init__(self, parent, list_op=False):
        super(Preferences, self).__init__(parent, list_op)

    @property
    def Analyzer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.preferences.analyzer.analyzer.Analyzer): An instance of the Analyzer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.preferences.analyzer.analyzer import (
            Analyzer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Analyzer", None) is not None:
                return self._properties.get("Analyzer")
        return Analyzer(self)._select()

    @property
    def Statistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.preferences.statistics.statistics.Statistics): An instance of the Statistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.preferences.statistics.statistics import (
            Statistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Statistics", None) is not None:
                return self._properties.get("Statistics")
        return Statistics(self)._select()

    @property
    def AllowProtocolSessionStateLog(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables logging each protocol session state change. This option is very heavy for performance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AllowProtocolSessionStateLog"])

    @AllowProtocolSessionStateLog.setter
    def AllowProtocolSessionStateLog(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AllowProtocolSessionStateLog"], value)

    @property
    def AutoCleanLogs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this will fire auto log deletion everyday, bound by other properties such as client/chassis days etc under /globals/diagnostics/cleanup
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoCleanLogs"])

    @AutoCleanLogs.setter
    def AutoCleanLogs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoCleanLogs"], value)

    @property
    def AutoSaveIntervalMin(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Set the interval time in minutes in which the configuration will be saved automatically
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoSaveIntervalMin"])

    @AutoSaveIntervalMin.setter
    def AutoSaveIntervalMin(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoSaveIntervalMin"], value)

    @property
    def AutoSaveLocation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the location where the configuration will be saved automatically
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoSaveLocation"])

    @AutoSaveLocation.setter
    def AutoSaveLocation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoSaveLocation"], value)

    @property
    def ClientTraceLevel(self):
        # type: () -> str
        """
        Returns
        -------
        - str(debug | error | fatal | info | warn): Set the IxNetwork Client side Log/Trace level
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientTraceLevel"])

    @ClientTraceLevel.setter
    def ClientTraceLevel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientTraceLevel"], value)

    @property
    def ConfigurationAtIxNetworkStartup(self):
        # type: () -> str
        """
        Returns
        -------
        - str(useEmptyConfiguration | useLastSavedConfiguration): Controls which configuration to load when IxNetwork starts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfigurationAtIxNetworkStartup"])

    @ConfigurationAtIxNetworkStartup.setter
    def ConfigurationAtIxNetworkStartup(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConfigurationAtIxNetworkStartup"], value)

    @property
    def ConnectPortsOnLoadConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded (Should be used only in IxNetwork Desktop App)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectPortsOnLoadConfig"])

    @ConnectPortsOnLoadConfig.setter
    def ConnectPortsOnLoadConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectPortsOnLoadConfig"], value)

    @property
    def DeleteDumpFilesOlderThan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Dump Files older than the days set are deleted automatically. Need to restart IxNetwork for this option to take effect.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeleteDumpFilesOlderThan"])

    @DeleteDumpFilesOlderThan.setter
    def DeleteDumpFilesOlderThan(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeleteDumpFilesOlderThan"], value)

    @property
    def DisableMinimizedScenario(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When true, Device Group will be auto selected in Scenario on a new Topology creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableMinimizedScenario"])

    @DisableMinimizedScenario.setter
    def DisableMinimizedScenario(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableMinimizedScenario"], value)

    @property
    def DisableProtoSpecificConnectors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When true, Device Group will be auto selected in Scenario on a new Topology creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableProtoSpecificConnectors"])

    @DisableProtoSpecificConnectors.setter
    def DisableProtoSpecificConnectors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableProtoSpecificConnectors"], value)

    @property
    def DropPacketsOnHighRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: drop packets on high rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DropPacketsOnHighRx"])

    @DropPacketsOnHighRx.setter
    def DropPacketsOnHighRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DropPacketsOnHighRx"], value)

    @property
    def EnableAutoSave(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true,saves the configuration automatically. IxNetwork wont prompt to open the auto backup file when running in TCL Server mode. For performance reasons users additionally have to add a decimal registry key ForceAutoSave in Computer/HKEY_CURRENT_USER/Software/Ixia Communications/IxNetwork/Debug to do the auto save. Doesnt work yet on Linux
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoSave"])

    @EnableAutoSave.setter
    def EnableAutoSave(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoSave"], value)

    @property
    def EnableCloudTools(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls whether Cloud Tool options will be enabled or not. This is related to learning MAC / IP address for a topology running on VM ports, deployed in AWS
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCloudTools"])

    @EnableCloudTools.setter
    def EnableCloudTools(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCloudTools"], value)

    @property
    def EnableDpdkForNewConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the default DPDK enable/disable state when a new config is created.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDpdkForNewConfig"])

    @EnableDpdkForNewConfig.setter
    def EnableDpdkForNewConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDpdkForNewConfig"], value)

    @property
    def EnablePCPUGuardRail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: enable pcpu guardrail
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePCPUGuardRail"])

    @EnablePCPUGuardRail.setter
    def EnablePCPUGuardRail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePCPUGuardRail"], value)

    @property
    def EnableScriptWatch(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls script watch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableScriptWatch"])

    @EnableScriptWatch.setter
    def EnableScriptWatch(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableScriptWatch"], value)

    @property
    def ForceLegacyPortNameInStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceLegacyPortNameInStats"])

    @ForceLegacyPortNameInStats.setter
    def ForceLegacyPortNameInStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceLegacyPortNameInStats"], value)

    @property
    def IncludeTroubleshootingComments(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Includes troubleshooting comments in the script
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTroubleshootingComments"])

    @IncludeTroubleshootingComments.setter
    def IncludeTroubleshootingComments(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTroubleshootingComments"], value)

    @property
    def LatestConfigInDiagEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatestConfigInDiagEnabled"])

    @LatestConfigInDiagEnabled.setter
    def LatestConfigInDiagEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatestConfigInDiagEnabled"], value)

    @property
    def PcpuGuardRailCriticalThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: pcpu guardrail critical threshold
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcpuGuardRailCriticalThreshold"])

    @PcpuGuardRailCriticalThreshold.setter
    def PcpuGuardRailCriticalThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcpuGuardRailCriticalThreshold"], value)

    @property
    def PcpuGuardRailWarningThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: pcpu guardrail warning threshold
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcpuGuardRailWarningThreshold"])

    @PcpuGuardRailWarningThreshold.setter
    def PcpuGuardRailWarningThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcpuGuardRailWarningThreshold"], value)

    @property
    def PhyMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(copper | fiber): Set the media in Default Port Settings
        """
        return self._get_attribute(self._SDM_ATT_MAP["PhyMode"])

    @PhyMode.setter
    def PhyMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PhyMode"], value)

    @property
    def PingChassisOnConnect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls whether to ping the chassis before connecting the ports. Must run IxNetwork in administrator mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["PingChassisOnConnect"])

    @PingChassisOnConnect.setter
    def PingChassisOnConnect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PingChassisOnConnect"], value)

    @property
    def ProcessProtocolStateChangeAsync(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When true, protocol state change events are handled Asynchronously
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProcessProtocolStateChangeAsync"])

    @ProcessProtocolStateChangeAsync.setter
    def ProcessProtocolStateChangeAsync(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProcessProtocolStateChangeAsync"], value)

    @property
    def ProtocolGridSortingOrder(self):
        # type: () -> str
        """
        Returns
        -------
        - str(CreationTime | TopologyName): Set the sorting mode of Protocol Grid Topology
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolGridSortingOrder"])

    @ProtocolGridSortingOrder.setter
    def ProtocolGridSortingOrder(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolGridSortingOrder"], value)

    @property
    def RebootPortOnGuardRailCritical(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: reboot port on critical memory threshold
        """
        return self._get_attribute(self._SDM_ATT_MAP["RebootPortOnGuardRailCritical"])

    @RebootPortOnGuardRailCritical.setter
    def RebootPortOnGuardRailCritical(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RebootPortOnGuardRailCritical"], value)

    @property
    def RebootPortsOnConnect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the application will reboot any connected virtual ports when the configuration is loaded
        """
        return self._get_attribute(self._SDM_ATT_MAP["RebootPortsOnConnect"])

    @RebootPortsOnConnect.setter
    def RebootPortsOnConnect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RebootPortsOnConnect"], value)

    @property
    def ReceiveMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(capturePackets | measureTrafficFlow): Set the receive mode in Default Port settings
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveMode"])

    @ReceiveMode.setter
    def ReceiveMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveMode"], value)

    @property
    def RecentChassisList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of recently used chassis
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentChassisList"])

    @RecentChassisList.setter
    def RecentChassisList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["RecentChassisList"], value)

    @property
    def RecentFiles(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of recently used files
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecentFiles"])

    @property
    def ResourceManagerLocation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the Resource Manager resources location
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResourceManagerLocation"])

    @ResourceManagerLocation.setter
    def ResourceManagerLocation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResourceManagerLocation"], value)

    @property
    def ScriptgenTextEditorPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the text editor path for Scriptgen
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScriptgenTextEditorPath"])

    @ScriptgenTextEditorPath.setter
    def ScriptgenTextEditorPath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScriptgenTextEditorPath"], value)

    @property
    def SelectDGOnCreation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When true, Device Group will be auto selected in Scenario on a new Topology creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectDGOnCreation"])

    @SelectDGOnCreation.setter
    def SelectDGOnCreation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectDGOnCreation"], value)

    @property
    def SequenceCheckingWhenNoTxRxSync(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When true, advanced sequence checking is preferred if Tx-Rx Sync is unavailable on any port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceCheckingWhenNoTxRxSync"])

    @SequenceCheckingWhenNoTxRxSync.setter
    def SequenceCheckingWhenNoTxRxSync(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceCheckingWhenNoTxRxSync"], value)

    @property
    def ShortenScenarioObjectNameInMiddle(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Shorten Topology/DG/NG names in the middle. If this is true, Topology/Device Group/Network Group names are shortened in the middle (with .), otherwise at the end
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ShortenScenarioObjectNameInMiddle"]
        )

    @ShortenScenarioObjectNameInMiddle.setter
    def ShortenScenarioObjectNameInMiddle(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ShortenScenarioObjectNameInMiddle"], value
        )

    @property
    def StreamLogsToSyslogServer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables streaming Logs To Syslog Server
        """
        return self._get_attribute(self._SDM_ATT_MAP["StreamLogsToSyslogServer"])

    @StreamLogsToSyslogServer.setter
    def StreamLogsToSyslogServer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StreamLogsToSyslogServer"], value)

    @property
    def SyslogHost(self):
        # type: () -> str
        """
        Returns
        -------
        - str: syslog host
        """
        return self._get_attribute(self._SDM_ATT_MAP["SyslogHost"])

    @SyslogHost.setter
    def SyslogHost(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SyslogHost"], value)

    @property
    def SyslogPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: syslog Port
        """
        return self._get_attribute(self._SDM_ATT_MAP["SyslogPort"])

    @SyslogPort.setter
    def SyslogPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SyslogPort"], value)

    @property
    def TopologyTreeSortingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(Number | String): Set the sorting mode of Scenario Tree
        """
        return self._get_attribute(self._SDM_ATT_MAP["TopologyTreeSortingMode"])

    @TopologyTreeSortingMode.setter
    def TopologyTreeSortingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TopologyTreeSortingMode"], value)

    @property
    def TransmitMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(interleavedStreams | sequentialStreams): Set the transmit mode in Default Port settings
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitMode"])

    @TransmitMode.setter
    def TransmitMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitMode"], value)

    @property
    def UseNewApiBrowser(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, new API browser will be used, otherwise the old one.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseNewApiBrowser"])

    @UseNewApiBrowser.setter
    def UseNewApiBrowser(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseNewApiBrowser"], value)

    def update(
        self,
        AllowProtocolSessionStateLog=None,
        AutoCleanLogs=None,
        AutoSaveIntervalMin=None,
        AutoSaveLocation=None,
        ClientTraceLevel=None,
        ConfigurationAtIxNetworkStartup=None,
        ConnectPortsOnLoadConfig=None,
        DeleteDumpFilesOlderThan=None,
        DisableMinimizedScenario=None,
        DisableProtoSpecificConnectors=None,
        DropPacketsOnHighRx=None,
        EnableAutoSave=None,
        EnableCloudTools=None,
        EnableDpdkForNewConfig=None,
        EnablePCPUGuardRail=None,
        EnableScriptWatch=None,
        ForceLegacyPortNameInStats=None,
        IncludeTroubleshootingComments=None,
        LatestConfigInDiagEnabled=None,
        PcpuGuardRailCriticalThreshold=None,
        PcpuGuardRailWarningThreshold=None,
        PhyMode=None,
        PingChassisOnConnect=None,
        ProcessProtocolStateChangeAsync=None,
        ProtocolGridSortingOrder=None,
        RebootPortOnGuardRailCritical=None,
        RebootPortsOnConnect=None,
        ReceiveMode=None,
        RecentChassisList=None,
        ResourceManagerLocation=None,
        ScriptgenTextEditorPath=None,
        SelectDGOnCreation=None,
        SequenceCheckingWhenNoTxRxSync=None,
        ShortenScenarioObjectNameInMiddle=None,
        StreamLogsToSyslogServer=None,
        SyslogHost=None,
        SyslogPort=None,
        TopologyTreeSortingMode=None,
        TransmitMode=None,
        UseNewApiBrowser=None,
    ):
        # type: (bool, bool, int, str, str, str, bool, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, bool, bool, str, bool, bool, str, List[str], str, str, bool, bool, bool, bool, str, int, str, str, bool) -> Preferences
        """Updates preferences resource on the server.

        Args
        ----
        - AllowProtocolSessionStateLog (bool): Enables logging each protocol session state change. This option is very heavy for performance.
        - AutoCleanLogs (bool): If true, this will fire auto log deletion everyday, bound by other properties such as client/chassis days etc under /globals/diagnostics/cleanup
        - AutoSaveIntervalMin (number): Set the interval time in minutes in which the configuration will be saved automatically
        - AutoSaveLocation (str): Set the location where the configuration will be saved automatically
        - ClientTraceLevel (str(debug | error | fatal | info | warn)): Set the IxNetwork Client side Log/Trace level
        - ConfigurationAtIxNetworkStartup (str(useEmptyConfiguration | useLastSavedConfiguration)): Controls which configuration to load when IxNetwork starts
        - ConnectPortsOnLoadConfig (bool): If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded (Should be used only in IxNetwork Desktop App)
        - DeleteDumpFilesOlderThan (number): Dump Files older than the days set are deleted automatically. Need to restart IxNetwork for this option to take effect.
        - DisableMinimizedScenario (bool): When true, Device Group will be auto selected in Scenario on a new Topology creation
        - DisableProtoSpecificConnectors (bool): When true, Device Group will be auto selected in Scenario on a new Topology creation
        - DropPacketsOnHighRx (bool): drop packets on high rx
        - EnableAutoSave (bool): If true,saves the configuration automatically. IxNetwork wont prompt to open the auto backup file when running in TCL Server mode. For performance reasons users additionally have to add a decimal registry key ForceAutoSave in Computer/HKEY_CURRENT_USER/Software/Ixia Communications/IxNetwork/Debug to do the auto save. Doesnt work yet on Linux
        - EnableCloudTools (bool): Controls whether Cloud Tool options will be enabled or not. This is related to learning MAC / IP address for a topology running on VM ports, deployed in AWS
        - EnableDpdkForNewConfig (bool): Sets the default DPDK enable/disable state when a new config is created.
        - EnablePCPUGuardRail (bool): enable pcpu guardrail
        - EnableScriptWatch (bool): Controls script watch.
        - ForceLegacyPortNameInStats (bool): When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        - IncludeTroubleshootingComments (bool): Includes troubleshooting comments in the script
        - LatestConfigInDiagEnabled (bool):
        - PcpuGuardRailCriticalThreshold (number): pcpu guardrail critical threshold
        - PcpuGuardRailWarningThreshold (number): pcpu guardrail warning threshold
        - PhyMode (str(copper | fiber)): Set the media in Default Port Settings
        - PingChassisOnConnect (bool): Controls whether to ping the chassis before connecting the ports. Must run IxNetwork in administrator mode
        - ProcessProtocolStateChangeAsync (bool): When true, protocol state change events are handled Asynchronously
        - ProtocolGridSortingOrder (str(CreationTime | TopologyName)): Set the sorting mode of Protocol Grid Topology
        - RebootPortOnGuardRailCritical (bool): reboot port on critical memory threshold
        - RebootPortsOnConnect (bool): If true the application will reboot any connected virtual ports when the configuration is loaded
        - ReceiveMode (str(capturePackets | measureTrafficFlow)): Set the receive mode in Default Port settings
        - RecentChassisList (list(str)): List of recently used chassis
        - ResourceManagerLocation (str): Set the Resource Manager resources location
        - ScriptgenTextEditorPath (str): Set the text editor path for Scriptgen
        - SelectDGOnCreation (bool): When true, Device Group will be auto selected in Scenario on a new Topology creation
        - SequenceCheckingWhenNoTxRxSync (bool): When true, advanced sequence checking is preferred if Tx-Rx Sync is unavailable on any port.
        - ShortenScenarioObjectNameInMiddle (bool): Shorten Topology/DG/NG names in the middle. If this is true, Topology/Device Group/Network Group names are shortened in the middle (with .), otherwise at the end
        - StreamLogsToSyslogServer (bool): Enables streaming Logs To Syslog Server
        - SyslogHost (str): syslog host
        - SyslogPort (number): syslog Port
        - TopologyTreeSortingMode (str(Number | String)): Set the sorting mode of Scenario Tree
        - TransmitMode (str(interleavedStreams | sequentialStreams)): Set the transmit mode in Default Port settings
        - UseNewApiBrowser (bool): If true, new API browser will be used, otherwise the old one.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AllowProtocolSessionStateLog=None,
        AutoCleanLogs=None,
        AutoSaveIntervalMin=None,
        AutoSaveLocation=None,
        ClientTraceLevel=None,
        ConfigurationAtIxNetworkStartup=None,
        ConnectPortsOnLoadConfig=None,
        DeleteDumpFilesOlderThan=None,
        DisableMinimizedScenario=None,
        DisableProtoSpecificConnectors=None,
        DropPacketsOnHighRx=None,
        EnableAutoSave=None,
        EnableCloudTools=None,
        EnableDpdkForNewConfig=None,
        EnablePCPUGuardRail=None,
        EnableScriptWatch=None,
        ForceLegacyPortNameInStats=None,
        IncludeTroubleshootingComments=None,
        LatestConfigInDiagEnabled=None,
        PcpuGuardRailCriticalThreshold=None,
        PcpuGuardRailWarningThreshold=None,
        PhyMode=None,
        PingChassisOnConnect=None,
        ProcessProtocolStateChangeAsync=None,
        ProtocolGridSortingOrder=None,
        RebootPortOnGuardRailCritical=None,
        RebootPortsOnConnect=None,
        ReceiveMode=None,
        RecentChassisList=None,
        RecentFiles=None,
        ResourceManagerLocation=None,
        ScriptgenTextEditorPath=None,
        SelectDGOnCreation=None,
        SequenceCheckingWhenNoTxRxSync=None,
        ShortenScenarioObjectNameInMiddle=None,
        StreamLogsToSyslogServer=None,
        SyslogHost=None,
        SyslogPort=None,
        TopologyTreeSortingMode=None,
        TransmitMode=None,
        UseNewApiBrowser=None,
    ):
        # type: (bool, bool, int, str, str, str, bool, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, bool, bool, str, bool, bool, str, List[str], List[str], str, str, bool, bool, bool, bool, str, int, str, str, bool) -> Preferences
        """Finds and retrieves preferences resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve preferences resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all preferences resources from the server.

        Args
        ----
        - AllowProtocolSessionStateLog (bool): Enables logging each protocol session state change. This option is very heavy for performance.
        - AutoCleanLogs (bool): If true, this will fire auto log deletion everyday, bound by other properties such as client/chassis days etc under /globals/diagnostics/cleanup
        - AutoSaveIntervalMin (number): Set the interval time in minutes in which the configuration will be saved automatically
        - AutoSaveLocation (str): Set the location where the configuration will be saved automatically
        - ClientTraceLevel (str(debug | error | fatal | info | warn)): Set the IxNetwork Client side Log/Trace level
        - ConfigurationAtIxNetworkStartup (str(useEmptyConfiguration | useLastSavedConfiguration)): Controls which configuration to load when IxNetwork starts
        - ConnectPortsOnLoadConfig (bool): If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded (Should be used only in IxNetwork Desktop App)
        - DeleteDumpFilesOlderThan (number): Dump Files older than the days set are deleted automatically. Need to restart IxNetwork for this option to take effect.
        - DisableMinimizedScenario (bool): When true, Device Group will be auto selected in Scenario on a new Topology creation
        - DisableProtoSpecificConnectors (bool): When true, Device Group will be auto selected in Scenario on a new Topology creation
        - DropPacketsOnHighRx (bool): drop packets on high rx
        - EnableAutoSave (bool): If true,saves the configuration automatically. IxNetwork wont prompt to open the auto backup file when running in TCL Server mode. For performance reasons users additionally have to add a decimal registry key ForceAutoSave in Computer/HKEY_CURRENT_USER/Software/Ixia Communications/IxNetwork/Debug to do the auto save. Doesnt work yet on Linux
        - EnableCloudTools (bool): Controls whether Cloud Tool options will be enabled or not. This is related to learning MAC / IP address for a topology running on VM ports, deployed in AWS
        - EnableDpdkForNewConfig (bool): Sets the default DPDK enable/disable state when a new config is created.
        - EnablePCPUGuardRail (bool): enable pcpu guardrail
        - EnableScriptWatch (bool): Controls script watch.
        - ForceLegacyPortNameInStats (bool): When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        - IncludeTroubleshootingComments (bool): Includes troubleshooting comments in the script
        - LatestConfigInDiagEnabled (bool):
        - PcpuGuardRailCriticalThreshold (number): pcpu guardrail critical threshold
        - PcpuGuardRailWarningThreshold (number): pcpu guardrail warning threshold
        - PhyMode (str(copper | fiber)): Set the media in Default Port Settings
        - PingChassisOnConnect (bool): Controls whether to ping the chassis before connecting the ports. Must run IxNetwork in administrator mode
        - ProcessProtocolStateChangeAsync (bool): When true, protocol state change events are handled Asynchronously
        - ProtocolGridSortingOrder (str(CreationTime | TopologyName)): Set the sorting mode of Protocol Grid Topology
        - RebootPortOnGuardRailCritical (bool): reboot port on critical memory threshold
        - RebootPortsOnConnect (bool): If true the application will reboot any connected virtual ports when the configuration is loaded
        - ReceiveMode (str(capturePackets | measureTrafficFlow)): Set the receive mode in Default Port settings
        - RecentChassisList (list(str)): List of recently used chassis
        - RecentFiles (list(str)): List of recently used files
        - ResourceManagerLocation (str): Set the Resource Manager resources location
        - ScriptgenTextEditorPath (str): Set the text editor path for Scriptgen
        - SelectDGOnCreation (bool): When true, Device Group will be auto selected in Scenario on a new Topology creation
        - SequenceCheckingWhenNoTxRxSync (bool): When true, advanced sequence checking is preferred if Tx-Rx Sync is unavailable on any port.
        - ShortenScenarioObjectNameInMiddle (bool): Shorten Topology/DG/NG names in the middle. If this is true, Topology/Device Group/Network Group names are shortened in the middle (with .), otherwise at the end
        - StreamLogsToSyslogServer (bool): Enables streaming Logs To Syslog Server
        - SyslogHost (str): syslog host
        - SyslogPort (number): syslog Port
        - TopologyTreeSortingMode (str(Number | String)): Set the sorting mode of Scenario Tree
        - TransmitMode (str(interleavedStreams | sequentialStreams)): Set the transmit mode in Default Port settings
        - UseNewApiBrowser (bool): If true, new API browser will be used, otherwise the old one.

        Returns
        -------
        - self: This instance with matching preferences resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of preferences data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the preferences resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
