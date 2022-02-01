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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Preferences(Base):
    """The preferences node contains user configurable system wide preferences
    The Preferences class encapsulates a required preferences resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'preferences'
    _SDM_ATT_MAP = {
        'AllowProtocolSessionStateLog': 'allowProtocolSessionStateLog',
        'AutoSaveIntervalMin': 'autoSaveIntervalMin',
        'AutoSaveLocation': 'autoSaveLocation',
        'ClientTraceLevel': 'clientTraceLevel',
        'ConfigurationAtIxNetworkStartup': 'configurationAtIxNetworkStartup',
        'ConnectPortsOnLoadConfig': 'connectPortsOnLoadConfig',
        'DeleteDumpFilesOlderThan': 'deleteDumpFilesOlderThan',
        'EnableAutoSave': 'enableAutoSave',
        'EnableCloudTools': 'enableCloudTools',
        'ForceLegacyPortNameInStats': 'forceLegacyPortNameInStats',
        'IncludeTroubleshootingComments': 'includeTroubleshootingComments',
        'LatestConfigInDiagEnabled': 'latestConfigInDiagEnabled',
        'PhyMode': 'phyMode',
        'PingChassisOnConnect': 'pingChassisOnConnect',
        'RebootPortsOnConnect': 'rebootPortsOnConnect',
        'ReceiveMode': 'receiveMode',
        'RecentChassisList': 'recentChassisList',
        'RecentFiles': 'recentFiles',
        'ResourceManagerLocation': 'resourceManagerLocation',
        'ScriptgenTextEditorPath': 'scriptgenTextEditorPath',
        'StreamLogsToSyslogServer': 'streamLogsToSyslogServer',
        'SyslogHost': 'syslogHost',
        'SyslogPort': 'syslogPort',
        'TransmitMode': 'transmitMode',
    }
    _SDM_ENUM_MAP = {
        'clientTraceLevel': ['debug', 'error', 'fatal', 'info', 'warn'],
        'configurationAtIxNetworkStartup': ['useEmptyConfiguration', 'useLastSavedConfiguration'],
        'phyMode': ['copper', 'fiber'],
        'receiveMode': ['capturePackets', 'measureTrafficFlow'],
        'transmitMode': ['interleavedStreams', 'sequentialStreams'],
    }

    def __init__(self, parent, list_op=False):
        super(Preferences, self).__init__(parent, list_op)

    @property
    def AllowProtocolSessionStateLog(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables logging each protocol session state change. This option is very heavy for performance.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowProtocolSessionStateLog'])
    @AllowProtocolSessionStateLog.setter
    def AllowProtocolSessionStateLog(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['AllowProtocolSessionStateLog'], value)

    @property
    def AutoSaveIntervalMin(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Set the interval time in minutes in which the configuration will be saved automatically
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoSaveIntervalMin'])
    @AutoSaveIntervalMin.setter
    def AutoSaveIntervalMin(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['AutoSaveIntervalMin'], value)

    @property
    def AutoSaveLocation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the location where the configuration will be saved automatically
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoSaveLocation'])
    @AutoSaveLocation.setter
    def AutoSaveLocation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AutoSaveLocation'], value)

    @property
    def ClientTraceLevel(self):
        # type: () -> str
        """
        Returns
        -------
        - str(debug | error | fatal | info | warn): Set the IxNetwork Client side Log/Trace level
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientTraceLevel'])
    @ClientTraceLevel.setter
    def ClientTraceLevel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ClientTraceLevel'], value)

    @property
    def ConfigurationAtIxNetworkStartup(self):
        # type: () -> str
        """
        Returns
        -------
        - str(useEmptyConfiguration | useLastSavedConfiguration): Controls which configuration to load when IxNetwork starts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigurationAtIxNetworkStartup'])
    @ConfigurationAtIxNetworkStartup.setter
    def ConfigurationAtIxNetworkStartup(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ConfigurationAtIxNetworkStartup'], value)

    @property
    def ConnectPortsOnLoadConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectPortsOnLoadConfig'])
    @ConnectPortsOnLoadConfig.setter
    def ConnectPortsOnLoadConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ConnectPortsOnLoadConfig'], value)

    @property
    def DeleteDumpFilesOlderThan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Dump Files older than the days set are deleted automatically. Need to restart IxNetwork for this option to take effect.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeleteDumpFilesOlderThan'])
    @DeleteDumpFilesOlderThan.setter
    def DeleteDumpFilesOlderThan(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DeleteDumpFilesOlderThan'], value)

    @property
    def EnableAutoSave(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true,saves the configuration automatically. IxNetwork wont prompt to open the auto backup file when running in TCL Server mode. For performance reasons users additionally have to add a decimal registry key ForceAutoSave in Computer/HKEY_CURRENT_USER/Software/Ixia Communications/IxNetwork/Debug to do the auto save. Doesnt work yet on Linux
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoSave'])
    @EnableAutoSave.setter
    def EnableAutoSave(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoSave'], value)

    @property
    def EnableCloudTools(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls whether Cloud Tool options will be enabled or not. This is related to learning MAC / IP address for a topology running on VM ports, deployed in AWS
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCloudTools'])
    @EnableCloudTools.setter
    def EnableCloudTools(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableCloudTools'], value)

    @property
    def ForceLegacyPortNameInStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceLegacyPortNameInStats'])
    @ForceLegacyPortNameInStats.setter
    def ForceLegacyPortNameInStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ForceLegacyPortNameInStats'], value)

    @property
    def IncludeTroubleshootingComments(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Includes troubleshooting comments in the script
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTroubleshootingComments'])
    @IncludeTroubleshootingComments.setter
    def IncludeTroubleshootingComments(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IncludeTroubleshootingComments'], value)

    @property
    def LatestConfigInDiagEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatestConfigInDiagEnabled'])
    @LatestConfigInDiagEnabled.setter
    def LatestConfigInDiagEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['LatestConfigInDiagEnabled'], value)

    @property
    def PhyMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(copper | fiber): Set the media in Default Port Settings
        """
        return self._get_attribute(self._SDM_ATT_MAP['PhyMode'])
    @PhyMode.setter
    def PhyMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PhyMode'], value)

    @property
    def PingChassisOnConnect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls whether to ping the chassis before connecting the ports. Must run IxNetwork in administrator mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingChassisOnConnect'])
    @PingChassisOnConnect.setter
    def PingChassisOnConnect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['PingChassisOnConnect'], value)

    @property
    def RebootPortsOnConnect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the application will reboot any connected virtual ports when the configuration is loaded
        """
        return self._get_attribute(self._SDM_ATT_MAP['RebootPortsOnConnect'])
    @RebootPortsOnConnect.setter
    def RebootPortsOnConnect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['RebootPortsOnConnect'], value)

    @property
    def ReceiveMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(capturePackets | measureTrafficFlow): Set the receive mode in Default Port settings
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceiveMode'])
    @ReceiveMode.setter
    def ReceiveMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ReceiveMode'], value)

    @property
    def RecentChassisList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of recently used chassis
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecentChassisList'])
    @RecentChassisList.setter
    def RecentChassisList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['RecentChassisList'], value)

    @property
    def RecentFiles(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List of recently used files
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecentFiles'])

    @property
    def ResourceManagerLocation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the Resource Manager resources location
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResourceManagerLocation'])
    @ResourceManagerLocation.setter
    def ResourceManagerLocation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ResourceManagerLocation'], value)

    @property
    def ScriptgenTextEditorPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the text editor path for Scriptgen
        """
        return self._get_attribute(self._SDM_ATT_MAP['ScriptgenTextEditorPath'])
    @ScriptgenTextEditorPath.setter
    def ScriptgenTextEditorPath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ScriptgenTextEditorPath'], value)

    @property
    def StreamLogsToSyslogServer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables streaming Logs To Syslog Server
        """
        return self._get_attribute(self._SDM_ATT_MAP['StreamLogsToSyslogServer'])
    @StreamLogsToSyslogServer.setter
    def StreamLogsToSyslogServer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['StreamLogsToSyslogServer'], value)

    @property
    def SyslogHost(self):
        # type: () -> str
        """
        Returns
        -------
        - str: syslog host
        """
        return self._get_attribute(self._SDM_ATT_MAP['SyslogHost'])
    @SyslogHost.setter
    def SyslogHost(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SyslogHost'], value)

    @property
    def SyslogPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: syslog Port
        """
        return self._get_attribute(self._SDM_ATT_MAP['SyslogPort'])
    @SyslogPort.setter
    def SyslogPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SyslogPort'], value)

    @property
    def TransmitMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(interleavedStreams | sequentialStreams): Set the transmit mode in Default Port settings
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitMode'])
    @TransmitMode.setter
    def TransmitMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TransmitMode'], value)

    def update(self, AllowProtocolSessionStateLog=None, AutoSaveIntervalMin=None, AutoSaveLocation=None, ClientTraceLevel=None, ConfigurationAtIxNetworkStartup=None, ConnectPortsOnLoadConfig=None, DeleteDumpFilesOlderThan=None, EnableAutoSave=None, EnableCloudTools=None, ForceLegacyPortNameInStats=None, IncludeTroubleshootingComments=None, LatestConfigInDiagEnabled=None, PhyMode=None, PingChassisOnConnect=None, RebootPortsOnConnect=None, ReceiveMode=None, RecentChassisList=None, ResourceManagerLocation=None, ScriptgenTextEditorPath=None, StreamLogsToSyslogServer=None, SyslogHost=None, SyslogPort=None, TransmitMode=None):
        # type: (bool, int, str, str, str, bool, int, bool, bool, bool, bool, bool, str, bool, bool, str, List[str], str, str, bool, str, int, str) -> Preferences
        """Updates preferences resource on the server.

        Args
        ----
        - AllowProtocolSessionStateLog (bool): Enables logging each protocol session state change. This option is very heavy for performance.
        - AutoSaveIntervalMin (number): Set the interval time in minutes in which the configuration will be saved automatically
        - AutoSaveLocation (str): Set the location where the configuration will be saved automatically
        - ClientTraceLevel (str(debug | error | fatal | info | warn)): Set the IxNetwork Client side Log/Trace level
        - ConfigurationAtIxNetworkStartup (str(useEmptyConfiguration | useLastSavedConfiguration)): Controls which configuration to load when IxNetwork starts
        - ConnectPortsOnLoadConfig (bool): If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded
        - DeleteDumpFilesOlderThan (number): Dump Files older than the days set are deleted automatically. Need to restart IxNetwork for this option to take effect.
        - EnableAutoSave (bool): If true,saves the configuration automatically. IxNetwork wont prompt to open the auto backup file when running in TCL Server mode. For performance reasons users additionally have to add a decimal registry key ForceAutoSave in Computer/HKEY_CURRENT_USER/Software/Ixia Communications/IxNetwork/Debug to do the auto save. Doesnt work yet on Linux
        - EnableCloudTools (bool): Controls whether Cloud Tool options will be enabled or not. This is related to learning MAC / IP address for a topology running on VM ports, deployed in AWS
        - ForceLegacyPortNameInStats (bool): When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        - IncludeTroubleshootingComments (bool): Includes troubleshooting comments in the script
        - LatestConfigInDiagEnabled (bool): 
        - PhyMode (str(copper | fiber)): Set the media in Default Port Settings
        - PingChassisOnConnect (bool): Controls whether to ping the chassis before connecting the ports. Must run IxNetwork in administrator mode
        - RebootPortsOnConnect (bool): If true the application will reboot any connected virtual ports when the configuration is loaded
        - ReceiveMode (str(capturePackets | measureTrafficFlow)): Set the receive mode in Default Port settings
        - RecentChassisList (list(str)): List of recently used chassis
        - ResourceManagerLocation (str): Set the Resource Manager resources location
        - ScriptgenTextEditorPath (str): Set the text editor path for Scriptgen
        - StreamLogsToSyslogServer (bool): Enables streaming Logs To Syslog Server
        - SyslogHost (str): syslog host
        - SyslogPort (number): syslog Port
        - TransmitMode (str(interleavedStreams | sequentialStreams)): Set the transmit mode in Default Port settings

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AllowProtocolSessionStateLog=None, AutoSaveIntervalMin=None, AutoSaveLocation=None, ClientTraceLevel=None, ConfigurationAtIxNetworkStartup=None, ConnectPortsOnLoadConfig=None, DeleteDumpFilesOlderThan=None, EnableAutoSave=None, EnableCloudTools=None, ForceLegacyPortNameInStats=None, IncludeTroubleshootingComments=None, LatestConfigInDiagEnabled=None, PhyMode=None, PingChassisOnConnect=None, RebootPortsOnConnect=None, ReceiveMode=None, RecentChassisList=None, RecentFiles=None, ResourceManagerLocation=None, ScriptgenTextEditorPath=None, StreamLogsToSyslogServer=None, SyslogHost=None, SyslogPort=None, TransmitMode=None):
        # type: (bool, int, str, str, str, bool, int, bool, bool, bool, bool, bool, str, bool, bool, str, List[str], List[str], str, str, bool, str, int, str) -> Preferences
        """Finds and retrieves preferences resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve preferences resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all preferences resources from the server.

        Args
        ----
        - AllowProtocolSessionStateLog (bool): Enables logging each protocol session state change. This option is very heavy for performance.
        - AutoSaveIntervalMin (number): Set the interval time in minutes in which the configuration will be saved automatically
        - AutoSaveLocation (str): Set the location where the configuration will be saved automatically
        - ClientTraceLevel (str(debug | error | fatal | info | warn)): Set the IxNetwork Client side Log/Trace level
        - ConfigurationAtIxNetworkStartup (str(useEmptyConfiguration | useLastSavedConfiguration)): Controls which configuration to load when IxNetwork starts
        - ConnectPortsOnLoadConfig (bool): If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded
        - DeleteDumpFilesOlderThan (number): Dump Files older than the days set are deleted automatically. Need to restart IxNetwork for this option to take effect.
        - EnableAutoSave (bool): If true,saves the configuration automatically. IxNetwork wont prompt to open the auto backup file when running in TCL Server mode. For performance reasons users additionally have to add a decimal registry key ForceAutoSave in Computer/HKEY_CURRENT_USER/Software/Ixia Communications/IxNetwork/Debug to do the auto save. Doesnt work yet on Linux
        - EnableCloudTools (bool): Controls whether Cloud Tool options will be enabled or not. This is related to learning MAC / IP address for a topology running on VM ports, deployed in AWS
        - ForceLegacyPortNameInStats (bool): When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        - IncludeTroubleshootingComments (bool): Includes troubleshooting comments in the script
        - LatestConfigInDiagEnabled (bool): 
        - PhyMode (str(copper | fiber)): Set the media in Default Port Settings
        - PingChassisOnConnect (bool): Controls whether to ping the chassis before connecting the ports. Must run IxNetwork in administrator mode
        - RebootPortsOnConnect (bool): If true the application will reboot any connected virtual ports when the configuration is loaded
        - ReceiveMode (str(capturePackets | measureTrafficFlow)): Set the receive mode in Default Port settings
        - RecentChassisList (list(str)): List of recently used chassis
        - RecentFiles (list(str)): List of recently used files
        - ResourceManagerLocation (str): Set the Resource Manager resources location
        - ScriptgenTextEditorPath (str): Set the text editor path for Scriptgen
        - StreamLogsToSyslogServer (bool): Enables streaming Logs To Syslog Server
        - SyslogHost (str): syslog host
        - SyslogPort (number): syslog Port
        - TransmitMode (str(interleavedStreams | sequentialStreams)): Set the transmit mode in Default Port settings

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
