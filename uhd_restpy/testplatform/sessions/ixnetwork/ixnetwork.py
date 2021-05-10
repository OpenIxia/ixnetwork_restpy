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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Ixnetwork(Base):
    """This is the root node of the hierarchy
    The Ixnetwork class encapsulates a required / resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ixnetwork'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(Ixnetwork, self).__init__(parent)

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.globals.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.globals import Globals
        return Globals(self)._select()

    @property
    def Lag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.lag.lag_cd537f07f912db233dacbe727e8568d7.Lag): An instance of the Lag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.lag.lag_cd537f07f912db233dacbe727e8568d7 import Lag
        return Lag(self)

    @property
    def Locations(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.locations.locations.Locations): An instance of the Locations class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.locations.locations import Locations
        return Locations(self)

    @property
    def QuickTest(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.quicktest.QuickTest): An instance of the QuickTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.quicktest import QuickTest
        return QuickTest(self)._select()

    @property
    def ResourceManager(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager.ResourceManager): An instance of the ResourceManager class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager import ResourceManager
        return ResourceManager(self)._select()

    @property
    def Statistics(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.statistics.Statistics): An instance of the Statistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.statistics import Statistics
        return Statistics(self)._select()

    @property
    def Timeline(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.timeline.timeline.Timeline): An instance of the Timeline class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.timeline.timeline import Timeline
        return Timeline(self)._select()

    @property
    def Topology(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.topology_9d0fe0bb2c064aa7010adbdb6cf68958.Topology): An instance of the Topology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.topology_9d0fe0bb2c064aa7010adbdb6cf68958 import Topology
        return Topology(self)

    @property
    def Traffic(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.traffic.Traffic): An instance of the Traffic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.traffic import Traffic
        return Traffic(self)._select()

    @property
    def Vport(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport): An instance of the Vport class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.vport import Vport
        return Vport(self)

    @property
    def Watch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.watch.watch.Watch): An instance of the Watch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.watch.watch import Watch
        return Watch(self)._select()

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the first Quick Test found in the current configuration.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        applyITWizardConfiguration(TestName=string)
        -------------------------------------------
        - TestName (str): The name of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def ApplyL1Blocking(self):
        """Executes the applyL1Blocking operation on the server.

        Apply L1 blocking.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('applyL1Blocking', payload=payload, response_object=None)

    def AssignPorts(self, *args, **kwargs):
        """Executes the assignPorts operation on the server.

        Assign hardware ports to virtual ports using port display names.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        assignPorts(Arg1=list, Arg2=list, Arg3=bool)list
        ------------------------------------------------
        - Arg1 (list(str)): A list of port display names, if empty then /vport's location attribute value is used.
        - Arg2 (list(str[None | /api/v1/sessions/9/ixnetwork/vport])): A list of virtual port object references that hardware ports will be attached to.
        - Arg3 (bool): If true, it will clear ownership on the hardware ports.
        - Returns list(str[None | /api/v1/sessions/9/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        assignPorts(Arg1=list, Arg2=bool)list
        -------------------------------------
        - Arg1 (list(str)): A list of port display names, if empty then /vport's location attribute value is used.
        - Arg2 (bool): If true, it will clear ownership on the hardware ports which have location attribute set.
        - Returns list(str[None | /api/v1/sessions/9/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        assignPorts(Arg1=list, Arg2=list, Arg3=list, Arg4=bool)list
        -----------------------------------------------------------
        - Arg1 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to include.
        - Arg2 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to exclude.
        - Arg3 (list(str[None | /api/v1/sessions/9/ixnetwork/vport])): A list of virtual port object references that hardware ports will be attached to.
        - Arg4 (bool): If true, it will clear ownership on the hardware ports.
        - Returns list(str[None | /api/v1/sessions/9/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        assignPorts(Arg1=bool)list
        --------------------------
        - Arg1 (bool): If true, it will clear ownership on the hardware ports which have location attribute set.
        - Returns list(str[None | /api/v1/sessions/9/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('assignPorts', payload=payload, response_object=None)

    def ClearAppLibraryStats(self):
        """Executes the clearAppLibraryStats operation on the server.

        Clears the statistics published by AppLibrary.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('clearAppLibraryStats', payload=payload, response_object=None)

    def ClearCPDPStats(self):
        """Executes the clearCPDPStats operation on the server.

        Clear control plane and data plane statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('clearCPDPStats', payload=payload, response_object=None)

    def ClearPortsAndTrafficStats(self, *args, **kwargs):
        """Executes the clearPortsAndTrafficStats operation on the server.

        The command to clear the existing port and traffic statistics.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearPortsAndTrafficStats(Arg1=list)
        ------------------------------------
        - Arg1 (list(str[waitForPortStatsRefresh | waitForTrafficStatsRefresh])): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearPortsAndTrafficStats', payload=payload, response_object=None)

    def ClearProtocolStats(self):
        """Executes the clearProtocolStats operation on the server.

        Clear the protocol statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('clearProtocolStats', payload=payload, response_object=None)

    def ClearStats(self, *args, **kwargs):
        """Executes the clearStats operation on the server.

        The command to clear the existing statistics.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearStats(Arg1=list)
        ---------------------
        - Arg1 (list(str[waitForPortStatsRefresh | waitForTrafficStatsRefresh])): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearStats', payload=payload, response_object=None)

    def CloseAllTabs(self, *args, **kwargs):
        """Executes the closeAllTabs operation on the server.

        This command closes all the captures if no parameter is specified; or a specific list of online captures

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeAllTabs(Arg1=list)
        -----------------------
        - Arg1 (list(str)): The list of capture names to be closed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('closeAllTabs', payload=payload, response_object=None)

    def CollectLogs(self, *args, **kwargs):
        """Executes the collectLogs operation on the server.

        This command collects all of the IxNetwork logs and puts them in a .zip file. Takes CollectLogOptions and ProfileName. Collect logs in a date range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        collectLogs(Arg1=href, Arg2=list, Arg3=string, Arg4=string, Arg5=string)
        ------------------------------------------------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile
        - Arg3 (str): Desired Profile names in case CollectLogOption is specificProfile. Options are: All-Profiles, Analyzer, Impairment, StatViewer-Reporter, IxLoad Lite, StackManager, MiddleWare, QuickTests, AES, HLAPI
        - Arg4 (str): Start Date in format yyyy-M-d H:mm (2019-01-01 00:00)
        - Arg5 (str): End Date in format yyyy-M-d H:mm (2019-01-01 00:00)

        collectLogs(Arg1=href, Arg2=list, Arg3=string, Arg4=string)
        -----------------------------------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile
        - Arg3 (str): Desired Profile names in case CollectLogOption is specificProfile. Options are: All-Profiles, Analyzer, Impairment, StatViewer-Reporter, IxLoad Lite, StackManager, MiddleWare, QuickTests, AES, HLAPI
        - Arg4 (str): Start Date in format yyyy-M-d H:mm (2019-01-01 00:00)

        collectLogs(Arg1=href, Arg2=list, Arg3=string)
        ----------------------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile
        - Arg3 (str): Desired Profile names in case CollectLogOption is specificProfile. Options are: All-Profiles, Analyzer, Impairment, StatViewer-Reporter, IxLoad Lite, StackManager, MiddleWare, QuickTests, AES, HLAPI

        collectLogs(Arg1=href, Arg2=list)
        ---------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile

        collectLogs(Arg1=href, Arg2=string, Arg3=string)
        ------------------------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (str): A string value.
        - Arg3 (str): A string value.

        collectLogs(Arg1=href, Arg2=string)
        -----------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (str): A string value.

        collectLogs(Arg1=href)
        ----------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A valid output file handle from the ixNet writeTo command

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('collectLogs', payload=payload, response_object=None)

    def CopyFile(self, *args, **kwargs):
        """Executes the copyFile operation on the server.

        Copies from first stream into the second stream.

        copyFile(Arg1=href, Arg2=href)
        ------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): The source file for the copy operation. This stream must be readable.
        - Arg2 (obj(uhd_restpy.files.Files)): The destination file for the copy operation. This stream must be writable.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('copyFile', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        This report feature generates an integrated test report file.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('generateReport', payload=payload, response_object=None)

    def GetAggregatedDeviceGroupStatus(self):
        """Executes the getAggregatedDeviceGroupStatus operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getAggregatedDeviceGroupStatus', payload=payload, response_object=None)

    def GetAllPorts(self):
        """Executes the getAllPorts operation on the server.

        The command to get all the ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getAllPorts', payload=payload, response_object=None)

    def GetAvailableProtocolStats(self):
        """Executes the getAvailableProtocolStats operation on the server.

        The command to get available protocol statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getAvailableProtocolStats', payload=payload, response_object=None)

    def GetAvailableStatsForProtocol(self, *args, **kwargs):
        """Executes the getAvailableStatsForProtocol operation on the server.

        The command to get available statistics for the protocol.

        getAvailableStatsForProtocol(Arg1=string)string
        -----------------------------------------------
        - Arg1 (str): Protocol name.
        - Returns str: A string with all the available statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getAvailableStatsForProtocol', payload=payload, response_object=None)

    def GetAvailableStatsForSourceType(self, *args, **kwargs):
        """Executes the getAvailableStatsForSourceType operation on the server.

        The command to get available statistics for the source type.

        getAvailableStatsForSourceType(Arg1=string)string
        -------------------------------------------------
        - Arg1 (str): Source type.
        - Returns str: A string with all the available statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getAvailableStatsForSourceType', payload=payload, response_object=None)

    def GetChassisMode(self):
        """Executes the getChassisMode operation on the server.

        Get current chassis mode(default/highRoute/unknown) for the default chassis.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getChassisMode', payload=payload, response_object=None)

    def GetConfiguredProtocols(self):
        """Executes the getConfiguredProtocols operation on the server.

        The command to get the configured protocols.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getConfiguredProtocols', payload=payload, response_object=None)

    def GetConfiguredProtocolsForPort(self, *args, **kwargs):
        """Executes the getConfiguredProtocolsForPort operation on the server.

        The command to get the configured protocols for the port.

        getConfiguredProtocolsForPort(Arg1=number)string
        ------------------------------------------------
        - Arg1 (number): Port ID.
        - Returns str: A string with all the available protocols configured on the port.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getConfiguredProtocolsForPort', payload=payload, response_object=None)

    def GetCsvColumnNames(self, *args, **kwargs):
        """Executes the getCsvColumnNames operation on the server.

        getCsvColumnNames(Arg1=href)list
        --------------------------------
        - Arg1 (obj(uhd_restpy.files.Files)): 
        - Returns list(str): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCsvColumnNames', payload=payload, response_object=None)

    def GetCurrentIxiaFileFormatTypeVersion(self):
        """Executes the getCurrentIxiaFileFormatTypeVersion operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getCurrentIxiaFileFormatTypeVersion', payload=payload, response_object=None)

    def GetDefaultSnapshotSettings(self):
        """Executes the GetDefaultSnapshotSettings operation on the server.

        Gets the default snapshot settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('GetDefaultSnapshotSettings', payload=payload, response_object=None)

    def GetIntersectionPortsForProtocols(self, *args, **kwargs):
        """Executes the getIntersectionPortsForProtocols operation on the server.

        The command to get intersection ports for the protocols.

        getIntersectionPortsForProtocols(Arg1=list)string
        -------------------------------------------------
        - Arg1 (list(str)): A list of protocol names.
        - Returns str: The list of port IDs that have all the given protocols configured.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getIntersectionPortsForProtocols', payload=payload, response_object=None)

    def GetNetworkGroupSize(self):
        """Executes the getNetworkGroupSize operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getNetworkGroupSize', payload=payload, response_object=None)

    def GetPortsForProtocol(self, *args, **kwargs):
        """Executes the getPortsForProtocol operation on the server.

        The command to get ports for the protocol.

        getPortsForProtocol(Arg1=string)string
        --------------------------------------
        - Arg1 (str): Protocol name.
        - Returns str: A string with all the port IDs having the protocol configured.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPortsForProtocol', payload=payload, response_object=None)

    def GetRbMemoryUsageInfo(self):
        """Executes the getRbMemoryUsageInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getRbMemoryUsageInfo', payload=payload, response_object=None)

    def GetRecommendedSettings(self, *args, **kwargs):
        """Executes the getRecommendedSettings operation on the server.

        It will get the recommended settings for the given copper type. Available choices are: oneMeter, threeMeters, fiveMeters.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getRecommendedSettings(Arg1=string, Arg2=list)
        ----------------------------------------------
        - Arg1 (str): 
        - Arg2 (list(str[None | /api/v1/sessions/9/ixnetwork/availableHardware/.../port])): 

        getRecommendedSettings(Arg1=string, Arg2=list)
        ----------------------------------------------
        - Arg1 (str): 
        - Arg2 (list(str[None | /api/v1/sessions/9/ixnetwork/vport])): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getRecommendedSettings', payload=payload, response_object=None)

    def GetTapSettings(self):
        """Executes the getTapSettings operation on the server.

        Get TAP Settings for all the connected chassis.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getTapSettings', payload=payload, response_object=None)

    def GetTopologyStatus(self):
        """Executes the getTopologyStatus operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('getTopologyStatus', payload=payload, response_object=None)

    def GetUnionPortsForProtocols(self, *args, **kwargs):
        """Executes the getUnionPortsForProtocols operation on the server.

        The command to get union ports for the protocols.

        getUnionPortsForProtocols(Arg1=list)string
        ------------------------------------------
        - Arg1 (list(str)): A list of protocol names.
        - Returns str: The list of port IDs that have at least one of the given protocols configured.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getUnionPortsForProtocols', payload=payload, response_object=None)

    def IgmpJoin(self, *args, **kwargs):
        """Executes the igmpJoin operation on the server.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpJoin(Arg1=string, Arg2=number)
        ----------------------------------
        - Arg1 (str): 
        - Arg2 (number): 

        igmpJoin(Arg1=string)
        ---------------------
        - Arg1 (str): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpJoin', payload=payload, response_object=None)

    def IgmpLeave(self, *args, **kwargs):
        """Executes the igmpLeave operation on the server.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpLeave(Arg1=string, Arg2=number)
        -----------------------------------
        - Arg1 (str): 
        - Arg2 (number): 

        igmpLeave(Arg1=string)
        ----------------------
        - Arg1 (str): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpLeave', payload=payload, response_object=None)

    def Import(self, *args, **kwargs):
        """Executes the import operation on the server.

        Imports a legacy IxAutomate configuration from the specified file.

        import(File=string)
        -------------------
        - File (str): The IxAutomate configuration file that will be imported.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('import', payload=payload, response_object=None)

    def LoadConfig(self, *args, **kwargs):
        """Executes the loadConfig operation on the server.

        Load an existing configuration file.

        loadConfig(Arg1=href)
        ---------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A readFrom file handle

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('loadConfig', payload=payload, response_object=None)

    def MergeCapture(self, *args, **kwargs):
        """Executes the mergeCapture operation on the server.

        This command will merge one offline capture with on running capture.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mergeCapture(Arg1=string, Arg2=href, Arg3=enum, Arg4=string)
        ------------------------------------------------------------
        - Arg1 (str): Full path to the capture file.
        - Arg2 (str(None | /api/v1/sessions/9/ixnetwork/vport/.../capture)): The port capture object.
        - Arg3 (str(control | data)): The type of the capture, either data or control.
        - Arg4 (str): The full path where the resulted merged capture will be saved, the resulted capture name needs to contain extension also.

        mergeCapture(Arg1=string, Arg2=string, Arg3=string)
        ---------------------------------------------------
        - Arg1 (str): Full path to the first capture file.
        - Arg2 (str): Full path to the second capture file.
        - Arg3 (str): The full path where the resulted merged capture will be saved, the result capture name needs to contain extension also.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mergeCapture', payload=payload, response_object=None)

    def NewConfig(self):
        """Executes the newConfig operation on the server.

        Clear the current configuration and create an empty configuration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('newConfig', payload=payload, response_object=None)

    def Refresh(self, *args, **kwargs):
        """Executes the refresh operation on the server.

        NOT DEFINED

        refresh(Arg1=string)
        --------------------
        - Arg1 (str): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('refresh', payload=payload, response_object=None)

    def SaveCapture(self, *args, **kwargs):
        """Executes the saveCapture operation on the server.

        This exec saves the capture data to a specified directory.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        DEPRECATED saveCapture(Arg1=string, Arg2=string)
        ------------------------------------------------
        - Arg1 (str): Directory for saving the captures
        - Arg2 (str): Suffix used for naming the capture files

        DEPRECATED saveCapture(Arg1=string)
        -----------------------------------
        - Arg1 (str): Directory for saving the captures

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('saveCapture', payload=payload, response_object=None)

    def SaveCaptureFiles(self, *args, **kwargs):
        """Executes the saveCaptureFiles operation on the server.

        Save existing capture files to a new user specified location and allows user to provide a suffix used for naming the new capture files

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        saveCaptureFiles(Arg1=string, Arg2=string)list
        ----------------------------------------------
        - Arg1 (str): Directory for saving the captures
        - Arg2 (str): Suffix used for naming the capture files
        - Returns list(str): A list of relative paths of all the captures saved

        saveCaptureFiles(Arg1=string)list
        ---------------------------------
        - Arg1 (str): Directory for saving the captures
        - Returns list(str): A list of relative paths of all the captures saved

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('saveCaptureFiles', payload=payload, response_object=None)

    def SaveConfig(self, *args, **kwargs):
        """Executes the saveConfig operation on the server.

        Save the current configuration to a file.

        saveConfig(Arg1=href)
        ---------------------
        - Arg1 (obj(uhd_restpy.files.Files)): A writeTo file handle.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('saveConfig', payload=payload, response_object=None)

    def Select(self, *args, **kwargs):
        """Executes the select operation on the server.

        Select nodes and properties from the hierarchy

        select(Selects=list)string
        --------------------------
        - Selects (list(dict(from:str[None | /api/v1/sessions/9/ixnetwork//.../*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(child:str,properties:list[str])]))): A list of select structures.Each select structure consists of a starting point in the hierarchy. This starting point must exist and is defined as the 'from' value.Properties for the 'from' value are optional and can be retrieved using the 'properties' list.To retrieve all properties specify the '*' wildcard. Regex is not supported in the 'properties' list.Individual nodes under the starting point can be retrieved. These are specified in the 'children' list.Each item in the children list contains a 'child' name, a list of 'properties' and a list of filters by which to reduce the result set.The 'child' name can be a single name or a regex.Properties that reference another object can have that object's content inlined by specifying inline children.Any child nodes below the object reference can be expanded as long as they are specified in the inline children.
        - Returns str: A json encoded string of result sets.The encoded string will contain a list of result sets with each select producing a result set.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('select', payload=payload, response_object=None)

    def SendArpAll(self):
        """Executes the sendArpAll operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('sendArpAll', payload=payload, response_object=None)

    def SendNsAll(self):
        """Executes the sendNsAll operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('sendNsAll', payload=payload, response_object=None)

    def SendRsAll(self):
        """Executes the sendRsAll operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('sendRsAll', payload=payload, response_object=None)

    def SetChassisMode(self, *args, **kwargs):
        """Executes the setChassisMode operation on the server.

        Switch Mode(default/highRoute) for the default chassis.

        setChassisMode(Arg1=enum, Arg2=bool)object
        ------------------------------------------
        - Arg1 (str(default | highRoute)): Takes as input corresponding mode (default/highRoute).
        - Arg2 (bool): take ownership if required.
        - Returns dict(arg1:str,arg2:str): Result if succesful or not,chassis hostname and the response message.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setChassisMode', payload=payload, response_object=None)

    def SetGuardRailVersion(self, *args, **kwargs):
        """Executes the setGuardRailVersion operation on the server.

        Disables GuardRail for TCL.

        setGuardRailVersion(Arg1=string)
        --------------------------------
        - Arg1 (str): Deprecated.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setGuardRailVersion', payload=payload, response_object=None)

    def SetLoggingLevel(self, *args, **kwargs):
        """Executes the setLoggingLevel operation on the server.

        setLoggingLevel(Arg1=enum)
        --------------------------
        - Arg1 (str(kDebug | kError | kFatal | kInfo | kNote | kNothing | kWarn)): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setLoggingLevel', payload=payload, response_object=None)

    def SetPortTransmitDuration(self, *args, **kwargs):
        """Executes the setPortTransmitDuration operation on the server.

        Set the port transmit duration.

        setPortTransmitDuration(Arg1=list)
        ----------------------------------
        - Arg1 (list(dict(arg1:number,arg2:list[str[None | /api/v1/sessions/9/ixnetwork/lag | /api/v1/sessions/9/ixnetwork/traffic | /api/v1/sessions/9/ixnetwork/traffic/.../trafficItem | /api/v1/sessions/9/ixnetwork/traffic/.../highLevelStream | /api/v1/sessions/9/ixnetwork/vport]]))): An array of structures. Each structure is an duration and a valid object reference.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setPortTransmitDuration', payload=payload, response_object=None)

    def SetSnapshotSettingsToDefault(self, *args, **kwargs):
        """Executes the SetSnapshotSettingsToDefault operation on the server.

        Set the settings of snapshot to default.

        SetSnapshotSettingsToDefault(Arg1=string)
        -----------------------------------------
        - Arg1 (str): The setting name.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('SetSnapshotSettingsToDefault', payload=payload, response_object=None)

    def SetTapSettings(self):
        """Executes the setTapSettings operation on the server.

        Send TAP Settings to IxServer for all the connected chassis.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('setTapSettings', payload=payload, response_object=None)

    def StartAllProtocols(self, *args, **kwargs):
        """Executes the startAllProtocols operation on the server.

        Starts all configured protocols under /vport/protocols, /vport/protocolStack and /topology

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startAllProtocols(Arg1=enum)
        ----------------------------
        - Arg1 (str(async | sync)): An enum indicating whether or not the exec will be executed synchronously or asynchronously

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startAllProtocols', payload=payload, response_object=None)

    def StartCapture(self):
        """Executes the startCapture operation on the server.

        The command to start the packet capture for the selected port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('startCapture', payload=payload, response_object=None)

    def StopAllProtocols(self, *args, **kwargs):
        """Executes the stopAllProtocols operation on the server.

        Stops all configured protocols under /vport/protocols, /vport/protocolStack and /topology

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopAllProtocols(Arg1=enum)
        ---------------------------
        - Arg1 (str(async | sync)): An enum indicating whether or not the exec will be executed synchronously or asynchronously

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopAllProtocols', payload=payload, response_object=None)

    def StopCapture(self):
        """Executes the stopCapture operation on the server.

        The command to stop the packet capture on the selected port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('stopCapture', payload=payload, response_object=None)

    def StopTestConfiguration(self):
        """Executes the stopTestConfiguration operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = None
        return self._execute('stopTestConfiguration', payload=payload, response_object=None)

    def SwitchModeLocations(self, *args, **kwargs):
        """Executes the switchModeLocations operation on the server.

        Switches the port mode. Takes locations as input.

        switchModeLocations(Arg1=list, Arg2=list, Arg3=bool)string
        ----------------------------------------------------------
        - Arg1 (list(str)): A list of locations.
        - Arg2 (list(str)): List of valid Modes.
        - Arg3 (bool): If true, it will clear ownership on the hardware ports for which mode switch is being done.
        - Returns str: Warning messages.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('switchModeLocations', payload=payload, response_object=None)

    def SyncStatisticsStartTimeWithClientClock(self, *args, **kwargs):
        """Executes the syncStatisticsStartTimeWithClientClock operation on the server.

        Make the statistics timestamps relative to the time on the client machine or relative to the test start.

        syncStatisticsStartTimeWithClientClock(Arg1=bool)
        -------------------------------------------------
        - Arg1 (bool): True = relative to system time, false = relative to test start.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('syncStatisticsStartTimeWithClientClock', payload=payload, response_object=None)

    def TakeViewCSVSnapshot(self, *args, **kwargs):
        """Executes the TakeViewCSVSnapshot operation on the server.

        Performs Snapshot CSV on the given views.

        TakeViewCSVSnapshot(Arg1=list, Arg2=list)
        -----------------------------------------
        - Arg1 (list(str)): A list of views for which to take a snapshot.
        - Arg2 (list(str)): A list of settings, given in the form of SettingName:SettingValue.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('TakeViewCSVSnapshot', payload=payload, response_object=None)

    def WaitForLicenseBroadcast(self, *args, **kwargs):
        """Executes the waitForLicenseBroadcast operation on the server.

        waitForLicenseBroadcast(Arg1=number)
        ------------------------------------
        - Arg1 (number): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('waitForLicenseBroadcast', payload=payload, response_object=None)
