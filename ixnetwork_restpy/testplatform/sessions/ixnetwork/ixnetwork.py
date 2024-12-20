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


class Ixnetwork(Base):
    """This is the root node of the hierarchy
    The Ixnetwork class encapsulates a required / resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ixnetwork"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Ixnetwork, self).__init__(parent, list_op)

    @property
    def AvailableHardware(self):
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.availablehardware.AvailableHardware): An instance of the AvailableHardware class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.availablehardware import (
            AvailableHardware,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AvailableHardware", None) is not None:
                return self._properties.get("AvailableHardware")
        return AvailableHardware(self)._select()

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.globals.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.globals import (
            Globals,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Globals", None) is not None:
                return self._properties.get("Globals")
        return Globals(self)._select()

    @property
    def Impairment(self):
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.impairment.Impairment): An instance of the Impairment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.impairment import (
            Impairment,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Impairment", None) is not None:
                return self._properties.get("Impairment")
        return Impairment(self)._select()

    @property
    def Lag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag_cd537f07f912db233dacbe727e8568d7.Lag): An instance of the Lag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag_cd537f07f912db233dacbe727e8568d7 import (
            Lag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lag", None) is not None:
                return self._properties.get("Lag")
        return Lag(self)

    @property
    def Locations(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.locations.Locations): An instance of the Locations class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.locations import (
            Locations,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Locations", None) is not None:
                return self._properties.get("Locations")
        return Locations(self)

    @property
    def QuickTest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.quicktest.QuickTest): An instance of the QuickTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.quicktest import (
            QuickTest,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("QuickTest", None) is not None:
                return self._properties.get("QuickTest")
        return QuickTest(self)._select()

    @property
    def Reporter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.reporter.Reporter): An instance of the Reporter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.reporter import (
            Reporter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Reporter", None) is not None:
                return self._properties.get("Reporter")
        return Reporter(self)._select()

    @property
    def ResourceManager(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager.ResourceManager): An instance of the ResourceManager class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager import (
            ResourceManager,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ResourceManager", None) is not None:
                return self._properties.get("ResourceManager")
        return ResourceManager(self)._select()

    @property
    def Statistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statistics.Statistics): An instance of the Statistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statistics import (
            Statistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Statistics", None) is not None:
                return self._properties.get("Statistics")
        return Statistics(self)._select()

    @property
    def Timeline(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.timeline.Timeline): An instance of the Timeline class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.timeline import (
            Timeline,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Timeline", None) is not None:
                return self._properties.get("Timeline")
        return Timeline(self)._select()

    @property
    def Topology(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology_9d0fe0bb2c064aa7010adbdb6cf68958.Topology): An instance of the Topology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology_9d0fe0bb2c064aa7010adbdb6cf68958 import (
            Topology,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Topology", None) is not None:
                return self._properties.get("Topology")
        return Topology(self)

    @property
    def Traffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.traffic.Traffic): An instance of the Traffic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.traffic import (
            Traffic,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Traffic", None) is not None:
                return self._properties.get("Traffic")
        return Traffic(self)._select()

    @property
    def Vport(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport): An instance of the Vport class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport import Vport

        if len(self._object_properties) > 0:
            if self._properties.get("Vport", None) is not None:
                return self._properties.get("Vport")
        return Vport(self)

    @property
    def Watch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.watch.Watch): An instance of the Watch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.watch import Watch

        if len(self._object_properties) > 0:
            if self._properties.get("Watch", None) is not None:
                return self._properties.get("Watch")
        return Watch(self)._select()

    def AddOfflinePorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addOfflinePorts operation on the server.

        Add Ports (offline)

        addOfflinePorts(Arg1=number, Arg2=string, async_operation=bool)
        ---------------------------------------------------------------
        - Arg1 (number): Number of Ports to add (1-100)
        - Arg2 (str): Type of Ports to add, 'Ethernet' by default
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addOfflinePorts", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the first Quick Test found in the current configuration.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        applyITWizardConfiguration(TestName=string, async_operation=bool)
        -----------------------------------------------------------------
        - TestName (str): The name of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def ApplyL1Blocking(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyL1Blocking operation on the server.

        Apply L1 blocking.

        applyL1Blocking(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyL1Blocking", payload=payload, response_object=None)

    def AssignPorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the assignPorts operation on the server.

        Assign hardware ports to virtual ports using port display names.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        assignPorts(Arg1=list, Arg2=list, Arg3=bool, async_operation=bool)list
        ----------------------------------------------------------------------
        - Arg1 (list(str)): A list of port display names, if empty then /vport's location attribute value is used.
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): A list of virtual port object references that hardware ports will be attached to.
        - Arg3 (bool): If true, it will clear ownership on the hardware ports.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str[None | /api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        assignPorts(Arg1=list, Arg2=bool, async_operation=bool)list
        -----------------------------------------------------------
        - Arg1 (list(str)): A list of port display names, if empty then /vport's location attribute value is used.
        - Arg2 (bool): If true, it will clear ownership on the hardware ports which have location attribute set.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str[None | /api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        assignPorts(Arg1=list, Arg2=list, Arg3=list, Arg4=bool, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg1 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to include.
        - Arg2 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to exclude.
        - Arg3 (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): A list of virtual port object references that hardware ports will be attached to.
        - Arg4 (bool): If true, it will clear ownership on the hardware ports.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str[None | /api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        assignPorts(Arg1=bool, async_operation=bool)list
        ------------------------------------------------
        - Arg1 (bool): If true, it will clear ownership on the hardware ports which have location attribute set.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str[None | /api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("assignPorts", payload=payload, response_object=None)

    def ClearAppLibraryStats(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearAppLibraryStats operation on the server.

        Clears the statistics published by AppLibrary.

        clearAppLibraryStats(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearAppLibraryStats", payload=payload, response_object=None
        )

    def ClearCardOwnershipById(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the clearCardOwnershipById operation on the server.

        Clear ownership on all ports from the given IxVM card.

        clearCardOwnershipById(Arg1=string, async_operation=bool)number
        ---------------------------------------------------------------
        - Arg1 (str): The card ID.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: Returns the card ID.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearCardOwnershipById", payload=payload, response_object=None
        )

    def ClearCPDPStats(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearCPDPStats operation on the server.

        Clear control pland and data plane statistics.

        clearCPDPStats(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("clearCPDPStats", payload=payload, response_object=None)

    def ClearPortsAndTrafficStats(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearPortsAndTrafficStats operation on the server.

        The command to clear the existing port and traffic statistics.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearPortsAndTrafficStats(async_operation=bool)
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearPortsAndTrafficStats(Arg1=list, async_operation=bool)
        ----------------------------------------------------------
        - Arg1 (list(str[waitForPortStatsRefresh | waitForTrafficStatsRefresh])):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearPortsAndTrafficStats", payload=payload, response_object=None
        )

    def ClearProtocolStats(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearProtocolStats operation on the server.

        Clear the protocol statistics.

        clearProtocolStats(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearProtocolStats", payload=payload, response_object=None
        )

    def ClearStats(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearStats operation on the server.

        The command to clear the existing statistics.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearStats(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearStats(Arg1=list, async_operation=bool)
        -------------------------------------------
        - Arg1 (list(str[waitForPortStatsRefresh | waitForTrafficStatsRefresh])):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("clearStats", payload=payload, response_object=None)

    def CloseAllTabs(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the closeAllTabs operation on the server.

        This command closes all the captures if no parameter is specified; or a specific list of online captures

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeAllTabs(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        closeAllTabs(Arg1=list, async_operation=bool)
        ---------------------------------------------
        - Arg1 (list(str)): The list of capture names to be closed.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("closeAllTabs", payload=payload, response_object=None)

    def CollectLogs(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the collectLogs operation on the server.

        This command collects all of the IxNetwork logs and puts them in a .zip file

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        collectLogs(Arg1=href, async_operation=bool)string
        --------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

        collectLogs(Arg1=href, Arg2=list, async_operation=bool)string
        -------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

        collectLogs(Arg1=href, Arg2=list, Arg3=string, async_operation=bool)string
        --------------------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile
        - Arg3 (str): Desired Profile names in case CollectLogOption is specificProfile. Options are: All-Profiles, Analyzer, Impairment, StatViewer-Reporter, IxLoad Lite, StackManager, MiddleWare, QuickTests, AES, HLAPI
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

        collectLogs(Arg1=href, Arg2=list, Arg3=string, Arg4=string, async_operation=bool)string
        ---------------------------------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile
        - Arg3 (str): Desired Profile names in case CollectLogOption is specificProfile. Options are: All-Profiles, Analyzer, Impairment, StatViewer-Reporter, IxLoad Lite, StackManager, MiddleWare, QuickTests, AES, HLAPI
        - Arg4 (str): Start Date in format yyyy-M-d H:mm (2019-01-01 00:00)
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

        collectLogs(Arg1=href, Arg2=list, Arg3=string, Arg4=string, Arg5=string, async_operation=bool)string
        ----------------------------------------------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (list(str[currentInstance | specificProfile])): CollectLogOptions enum: provide currentInstance or specificProfile
        - Arg3 (str): Desired Profile names in case CollectLogOption is specificProfile. Options are: All-Profiles, Analyzer, Impairment, StatViewer-Reporter, IxLoad Lite, StackManager, MiddleWare, QuickTests, AES, HLAPI
        - Arg4 (str): Start Date in format yyyy-M-d H:mm (2019-01-01 00:00)
        - Arg5 (str): End Date in format yyyy-M-d H:mm (2019-01-01 00:00)
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

        collectLogs(Arg1=href, Arg2=string, async_operation=bool)string
        ---------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (str): A string value.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

        collectLogs(Arg1=href, Arg2=string, Arg3=string, async_operation=bool)string
        ----------------------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command
        - Arg2 (str): A string value.
        - Arg3 (str): A string value.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: No return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("collectLogs", payload=payload, response_object=None)

    def ConfigureCustomGraphWebUI(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the configureCustomGraphWebUI operation on the server.

        Creates Custom Graph WebUI View

        configureCustomGraphWebUI(Operation=string, ViewCaption=string, RowIdentifier=list, ColumnIdentifier=list, CustomGraphCaption=string, ExtraPayload=list, async_operation=bool)
        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Operation (str): The Operation to perform
        - ViewCaption (str): View Caption
        - RowIdentifier (list(str)): Row Identifier
        - ColumnIdentifier (list(str)): Column Identifier
        - CustomGraphCaption (str): Custom Graph Web UI Caption
        - ExtraPayload (list(str)): Extra Payload
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "configureCustomGraphWebUI", payload=payload, response_object=None
        )

    def ConnectCardById(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the connectCardById operation on the server.

        Establish connection to the IxVM card.

        connectCardById(Arg1=string, async_operation=bool)number
        --------------------------------------------------------
        - Arg1 (str): Card ID to which connection is required.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: Returns the connected card ID or error, if any.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("connectCardById", payload=payload, response_object=None)

    def ConnectToChassis(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the connectToChassis operation on the server.

        Connect to a virtual chassis.

        connectToChassis(Arg1=string, async_operation=bool)
        ---------------------------------------------------
        - Arg1 (str): The hostname or IP address of the chassis.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("connectToChassis", payload=payload, response_object=None)

    def ConvertToNgpf(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the convertToNgpf operation on the server.

        Convert loaded classic config to ngpf config.

        convertToNgpf(Arg1=bool, Arg2=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg1 (bool): mix - retain classic config where it is not supported and do not convert the supported classic protocols as well on the same port
        - Arg2 (bool): dmtep - dont map traffic end point
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("convertToNgpf", payload=payload, response_object=None)

    def CopyFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the copyFile operation on the server.

        Copies from first stream into the second stream.

        copyFile(Arg1=href, Arg2=href, async_operation=bool)
        ----------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): The source file for the copy operation. This stream must be readable.
        - Arg2 (obj(ixnetwork_restpy.files.Files)): The destination file for the copy operation. This stream must be writable.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("copyFile", payload=payload, response_object=None)

    def CreateFDWebUIView(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the createFDWebUIView operation on the server.

        Creates Flow Detective WebUI View

        createFDWebUIView(TrafficItems=list, RxPorts=list, FlowState=enum, FlowPerformers=enum, async_operation=bool)
        -------------------------------------------------------------------------------------------------------------
        - TrafficItems (list(str)): A list of Traffic Items.
        - RxPorts (list(str)): A list of Ports.
        - FlowState (str(kShowAllFlows | kShowOnlyDeadFlows | kShowOnlyLiveFlows)): The Flow State
        - FlowPerformers (str(kBestCondition | kWorstCondition)): Best/Worst Performers
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("createFDWebUIView", payload=payload, response_object=None)

    def DisconnectCardById(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the disconnectCardById operation on the server.

        Close connection to the IxVM card.

        disconnectCardById(Arg1=string, async_operation=bool)number
        -----------------------------------------------------------
        - Arg1 (str): The card ID.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: Returns the card ID.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disconnectCardById", payload=payload, response_object=None
        )

    def FetchColDisplayNamesForProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the fetchColDisplayNamesForProtocol operation on the server.

        Fetches List of Display Names of columns given a Protocol obj

        fetchColDisplayNamesForProtocol(Arg1=string, async_operation=bool)list
        ----------------------------------------------------------------------
        - Arg1 (str): objref to a protocol
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): List of Display names of columns

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "fetchColDisplayNamesForProtocol", payload=payload, response_object=None
        )

    def FetchObjectDetailsInBulk(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the fetchObjectDetailsInBulk operation on the server.

        This command fetches topology/port/lag/dg/ng names in bulk

        fetchObjectDetailsInBulk(Arg1=enum, Arg2=string, async_operation=bool)string
        ----------------------------------------------------------------------------
        - Arg1 (str(dg | lag | ng | port | topology)):
        - Arg2 (str):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "fetchObjectDetailsInBulk", payload=payload, response_object=None
        )

    def FetchPropertyNameForDisplayName(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the fetchPropertyNameForDisplayName operation on the server.

        Fetches List of Property Names of columns given a Protocol obj and List of Display Names

        fetchPropertyNameForDisplayName(Arg1=string, Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg1 (str): objref to a protocol
        - Arg2 (list(str)): List of DisplayNames of columns
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): List of Property names of columns

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "fetchPropertyNameForDisplayName", payload=payload, response_object=None
        )

    def FetchRgUserOwnershipControlMode(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the fetchRgUserOwnershipControlMode operation on the server.

        Used to get the current port resource group user ownership mode - userPerResourceGroup or userPerFrontPanel. Takes locations as input.

        fetchRgUserOwnershipControlMode(Arg1=string, async_operation=bool)string
        ------------------------------------------------------------------------
        - Arg1 (str): Location port.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Current resource group user ownership mode - userPerResourceGroup or userPerFrontPanel

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "fetchRgUserOwnershipControlMode", payload=payload, response_object=None
        )

    def GenerateByteValues(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[int], None]
        """Executes the generateByteValues operation on the server.

        Generates an array of bytes from input Hex Values based on a selected pattern.

        generateByteValues(Arg1=string, Arg2=string, Arg3=string, Arg4=number, Arg5=bool, async_operation=bool)list
        -----------------------------------------------------------------------------------------------------------
        - Arg1 (str): The pattern type. Available options are: single, increment, decrement, random
        - Arg2 (str): Single/Start Value. This should be in Hex format
        - Arg3 (str): Step/Mask Value. This should be in Hex format
        - Arg4 (number): Count of values required
        - Arg5 (bool): Boolean flag to indicate Word length based calculation instead of Byte length based calculation. True for Word Length
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(number): Returns an array of bytes

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "generateByteValues", payload=payload, response_object=None
        )

    def GenerateHexValues(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateHexValues operation on the server.

        Generates a series of Hex values based on a selected pattern

        generateHexValues(Arg1=string, Arg2=string, Arg3=string, Arg4=number, Arg5=bool, async_operation=bool)string
        ------------------------------------------------------------------------------------------------------------
        - Arg1 (str): The pattern type. Available options are: single, increment, decrement, random
        - Arg2 (str): Single/Start Value. This should be in Hex format
        - Arg3 (str): Step/Mask Value. This should be in Hex format
        - Arg4 (number): Count of values required
        - Arg5 (bool): Boolean flag to indicate Word length based calculation instead of Byte length based calculation. True for Word Length
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Returns a string which contains a series of hex values

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateHexValues", payload=payload, response_object=None)

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the generateReport operation on the server.

        This report feature generates an integrated test report file.

        generateReport(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def GetAggregatedDeviceGroupStatus(self, *args, **kwargs):
        """Executes the getAggregatedDeviceGroupStatus operation on the server.

        getAggregatedDeviceGroupStatus(async_operation=bool)list
        --------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology],arg2:list[dict(arg1:str,arg2:number)])):

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAggregatedDeviceGroupStatus", payload=payload, response_object=None
        )

    def GetAllPorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getAllPorts operation on the server.

        The command to get all the ports.

        getAllPorts(async_operation=bool)string
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string with all the ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getAllPorts", payload=payload, response_object=None)

    def GetAvailableGlobalStatsActions(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getAvailableGlobalStatsActions operation on the server.

        The command to get the available global statistics actions.

        getAvailableGlobalStatsActions(async_operation=bool)string
        ----------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string containing the list of all available global statistics actions.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAvailableGlobalStatsActions", payload=payload, response_object=None
        )

    def GetAvailableOfflinePortTypes(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getAvailableOfflinePortTypes operation on the server.

        gets all Available Offline Port Types

        getAvailableOfflinePortTypes(async_operation=bool)string
        --------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAvailableOfflinePortTypes", payload=payload, response_object=None
        )

    def GetAvailableProtocolStats(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getAvailableProtocolStats operation on the server.

        The command to get available protocol statistics.

        getAvailableProtocolStats(async_operation=bool)string
        -----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string with all the legacy protocols statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAvailableProtocolStats", payload=payload, response_object=None
        )

    def GetAvailableRpfLogPorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getAvailableRpfLogPorts operation on the server.

        gets all Available ports available for RPF logs

        getAvailableRpfLogPorts(async_operation=bool)string
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAvailableRpfLogPorts", payload=payload, response_object=None
        )

    def GetAvailableSlotLicense(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the getAvailableSlotLicense operation on the server.

        This exec returns number of AppLibrary Slot License avaibale for use in the chassis.

        getAvailableSlotLicense(Arg1=string, async_operation=bool)number
        ----------------------------------------------------------------
        - Arg1 (str): The IPv4 address of the chassis.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: The number of AppLibrary Slot License available for use in the chassis.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAvailableSlotLicense", payload=payload, response_object=None
        )

    def GetAvailableStatsForProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getAvailableStatsForProtocol operation on the server.

        The command to get available statistics for the protocol.

        getAvailableStatsForProtocol(Arg1=string, async_operation=bool)string
        ---------------------------------------------------------------------
        - Arg1 (str): Protocol name.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string with all the available statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAvailableStatsForProtocol", payload=payload, response_object=None
        )

    def GetAvailableStatsForSourceType(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getAvailableStatsForSourceType operation on the server.

        The command to get available statistics for the source type.

        getAvailableStatsForSourceType(Arg1=string, async_operation=bool)string
        -----------------------------------------------------------------------
        - Arg1 (str): Source type.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string with all the available statistics.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getAvailableStatsForSourceType", payload=payload, response_object=None
        )

    def GetChassisMode(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getChassisMode operation on the server.

        Get current chassis mode(default/highRoute/ionvsFdb/unknown) for the default chassis.

        getChassisMode(async_operation=bool)enum
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(default\~highRoute\~ionvsFdb\~unknown): current mode of chassis(default/highRoute/ionvsFdb/unknown).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getChassisMode", payload=payload, response_object=None)

    def GetConfiguredProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getConfiguredProtocols operation on the server.

        The command to get the configured protocols.

        getConfiguredProtocols(async_operation=bool)string
        --------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A list with all the protocols configured in the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getConfiguredProtocols", payload=payload, response_object=None
        )

    def GetConfiguredProtocolsForPort(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getConfiguredProtocolsForPort operation on the server.

        The command to get the configured protocols for the port.

        getConfiguredProtocolsForPort(Arg1=number, async_operation=bool)string
        ----------------------------------------------------------------------
        - Arg1 (number): Port ID.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string with all the available protocols configured on the port.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getConfiguredProtocolsForPort", payload=payload, response_object=None
        )

    def GetCsvColumnNames(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getCsvColumnNames operation on the server.

        getCsvColumnNames(Arg1=href, async_operation=bool)list
        ------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str):

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getCsvColumnNames", payload=payload, response_object=None)

    def GetCurrentIxiaFileFormatTypeVersion(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the getCurrentIxiaFileFormatTypeVersion operation on the server.

        This command sets the current Ixia file format type version.

        getCurrentIxiaFileFormatTypeVersion(async_operation=bool)number
        ---------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: Returns current Ixia file format type version.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getCurrentIxiaFileFormatTypeVersion", payload=payload, response_object=None
        )

    def GetDefaultSnapshotSettings(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the GetDefaultSnapshotSettings operation on the server.

        Gets the default snapshot settings.

        GetDefaultSnapshotSettings(async_operation=bool)list
        ----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): An array with settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "GetDefaultSnapshotSettings", payload=payload, response_object=None
        )

    def GetFDViewEnabledObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getFDViewEnabledObjects operation on the server.

        Fetches TI and Ports that are enabled for the FD WebUI Stat view

        getFDViewEnabledObjects(async_operation=bool)string
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getFDViewEnabledObjects", payload=payload, response_object=None
        )

    def GetInstalledSlotLicenseCount(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the getInstalledSlotLicenseCount operation on the server.

        This exec returns number of AppLibrary Slot License installed in the chassis.

        getInstalledSlotLicenseCount(Arg1=string, async_operation=bool)number
        ---------------------------------------------------------------------
        - Arg1 (str): The IPv4 address of the chassis.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: The number of AppLibrary Slot License installed in the chassis.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getInstalledSlotLicenseCount", payload=payload, response_object=None
        )

    def GetIntersectionPortsForProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getIntersectionPortsForProtocols operation on the server.

        The command to get intersection ports for the protocols.

        getIntersectionPortsForProtocols(Arg1=list, async_operation=bool)string
        -----------------------------------------------------------------------
        - Arg1 (list(str)): A list of protocol names.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: The list of port IDs that have all the given protocols configured.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIntersectionPortsForProtocols", payload=payload, response_object=None
        )

    def GetIxVmCardByIp(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the getIxVmCardByIp operation on the server.

        Obtain IxVM card ID by providing management IP address.

        getIxVmCardByIp(Arg1=string, async_operation=bool)number
        --------------------------------------------------------
        - Arg1 (str): Management IP address of the card.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: Returns the card ID which has corresponding IP address on the management interface.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getIxVmCardByIp", payload=payload, response_object=None)

    def GetLicenseSummary(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getLicenseSummary operation on the server.

        getLicenseSummary(async_operation=bool)string
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getLicenseSummary", payload=payload, response_object=None)

    def GetMemoryUsageInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getMemoryUsageInfo operation on the server.

        Retrieve memory usage information

        getMemoryUsageInfo(async_operation=bool)string
        ----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: String containing memory usage: virtual, private, peak virtual bytes and bytes in all heaps

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getMemoryUsageInfo", payload=payload, response_object=None
        )

    def GetNamePatternPreview(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getNamePatternPreview operation on the server.

        This command gets a preview for a pattern

        getNamePatternPreview(Arg1=string, Arg2=number, async_operation=bool)string
        ---------------------------------------------------------------------------
        - Arg1 (str): pattern to be set
        - Arg2 (number): count of values to return for the preview
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getNamePatternPreview", payload=payload, response_object=None
        )

    def GetNetworkGroupSize(self, *args, **kwargs):
        """Executes the getNetworkGroupSize operation on the server.

        getNetworkGroupSize(async_operation=bool)list
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology],arg2:list[dict(arg1:str,arg2:number)])):

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getNetworkGroupSize", payload=payload, response_object=None
        )

    def GetPastApplicationInstances(self, *args, **kwargs):
        """Executes the getPastApplicationInstances operation on the server.

        This command collects dat abaout all the past IxNetwork instances

        getPastApplicationInstances(async_operation=bool)list
        -----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(arg1:list[dict(arg1:str,arg2:str)])): List of past instances with their attribute data

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getPastApplicationInstances", payload=payload, response_object=None
        )

    def GetPortRpfTraceProperties(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getPortRpfTraceProperties operation on the server.

        gets all Available port and their rpf trace properties

        getPortRpfTraceProperties(async_operation=bool)string
        -----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getPortRpfTraceProperties", payload=payload, response_object=None
        )

    def GetPortsForProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getPortsForProtocol operation on the server.

        The command to get ports for the protocol.

        getPortsForProtocol(Arg1=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg1 (str): Protocol name.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string with all the port IDs having the protocol configured.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getPortsForProtocol", payload=payload, response_object=None
        )

    def GetProtocolAggregatedStatus(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getProtocolAggregatedStatus operation on the server.

        getProtocolAggregatedStatus(async_operation=bool)string
        -------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getProtocolAggregatedStatus", payload=payload, response_object=None
        )

    def GetRbMemoryUsageInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getRbMemoryUsageInfo operation on the server.

        Fetch the memory usage information by RB protocols.

        getRbMemoryUsageInfo(async_operation=bool)string
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Returns memory usage information by RB protocols.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getRbMemoryUsageInfo", payload=payload, response_object=None
        )

    def GetRecommendedSettings(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the getRecommendedSettings operation on the server.

        It will get the recommended settings for the given copper type. Available choices are: oneMeter, threeMeters, fiveMeters.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getRecommendedSettings(Arg1=string, Arg2=list, async_operation=bool)
        --------------------------------------------------------------------
        - Arg1 (str):
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port])):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getRecommendedSettings(Arg1=string, Arg2=list, async_operation=bool)
        --------------------------------------------------------------------
        - Arg1 (str):
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport])):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getRecommendedSettings", payload=payload, response_object=None
        )

    def GetRpfLogForPort(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getRpfLogForPort operation on the server.

        gets RPF logs for the mentioned port

        getRpfLogForPort(Arg1=string, async_operation=bool)string
        ---------------------------------------------------------
        - Arg1 (str):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getRpfLogForPort", payload=payload, response_object=None)

    def GetSlotLicenseInUse(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[int], None]
        """Executes the getSlotLicenseInUse operation on the server.

        This exec returns a list of slots/cards of the chassis that are currently using the AppLibrary Slot Licenses.

        getSlotLicenseInUse(Arg1=string, async_operation=bool)list
        ----------------------------------------------------------
        - Arg1 (str): The IPv4 address of the chassis.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(number): An array of slot/card numbers of the chassis that currently checked-out AppLibrary Slot Licenses.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getSlotLicenseInUse", payload=payload, response_object=None
        )

    def GetSystemResources(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getSystemResources operation on the server.

        This command collects system resources include System Memory and Disk Usage and all processes running

        getSystemResources(Arg1=bool, async_operation=bool)string
        ---------------------------------------------------------
        - Arg1 (bool): Whether we want to see system processes in the output list.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getSystemResources", payload=payload, response_object=None
        )

    def GetTapSettings(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the getTapSettings operation on the server.

        Get TAP Settings for all the connected chassis.

        getTapSettings(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getTapSettings", payload=payload, response_object=None)

    def GetTopologyStatus(self, *args, **kwargs):
        """Executes the getTopologyStatus operation on the server.

        getTopologyStatus(async_operation=bool)list
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology],arg2:list[dict(arg1:str,arg2:number)],arg3:str[notstarted\~starting\~started\~stopping\~error\~mixed])):

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getTopologyStatus", payload=payload, response_object=None)

    def GetTxDeviationPpm(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the getTxDeviationPpm operation on the server.

        Fetches tx deviation ppm value.

        getTxDeviationPpm(Arg1=string, async_operation=bool)number
        ----------------------------------------------------------
        - Arg1 (str): Port location. E.g. : 100.101.101.1/1.1
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: Tx deviation ppm value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getTxDeviationPpm", payload=payload, response_object=None)

    def GetUnionPortsForProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getUnionPortsForProtocols operation on the server.

        The command to get union ports for the protocols.

        getUnionPortsForProtocols(Arg1=list, async_operation=bool)string
        ----------------------------------------------------------------
        - Arg1 (list(str)): A list of protocol names.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: The list of port IDs that have at least one of the given protocols configured.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getUnionPortsForProtocols", payload=payload, response_object=None
        )

    def HwRebootCardByIDs(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the hwRebootCardByIDs operation on the server.

        Perform hard reboot on virtual cards.

        hwRebootCardByIDs(Arg1=list, async_operation=bool)bool
        ------------------------------------------------------
        - Arg1 (list(number)): An array of card IDs.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: Returns whether or not the command is successful.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("hwRebootCardByIDs", payload=payload, response_object=None)

    def IgmpJoin(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpJoin operation on the server.

        Executing this command sends IGMP join message.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpJoin(Arg1=string, async_operation=bool)
        -------------------------------------------
        - Arg1 (str): This is a multicast IPv4 address as an argument to igmpJoin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpJoin(Arg1=string, Arg2=number, async_operation=bool)
        --------------------------------------------------------
        - Arg1 (str): This is a multicast IPv4 address as an argument to igmpJoin.
        - Arg2 (number): This is an integer value as an argument to igmpJoin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("igmpJoin", payload=payload, response_object=None)

    def IgmpLeave(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpLeave operation on the server.

        Executing this command sends IGMP leave message.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpLeave(Arg1=string, async_operation=bool)
        --------------------------------------------
        - Arg1 (str): This is a multicast IPv4 address as an argument to igmpLeave.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpLeave(Arg1=string, Arg2=number, async_operation=bool)
        ---------------------------------------------------------
        - Arg1 (str): This is a multicast IPv4 address as an argument to igmpLeave.
        - Arg2 (number): This is an integer value as an argument to igmpLeave.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("igmpLeave", payload=payload, response_object=None)

    def Import(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the import operation on the server.

        Imports a legacy IxAutomate configuration from the specified file.

        import(File=string, async_operation=bool)
        -----------------------------------------
        - File (str): The IxAutomate configuration file that will be imported.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("import", payload=payload, response_object=None)

    def LoadConfig(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the loadConfig operation on the server.

        Load an existing configuration file.

        loadConfig(Arg1=href, async_operation=bool)
        -------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A readFrom file handle
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("loadConfig", payload=payload, response_object=None)

    def LoadTopology(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the loadTopology operation on the server.

        Load a chassis topology from file.

        loadTopology(Arg1=string, async_operation=bool)string
        -----------------------------------------------------
        - Arg1 (str): Path to the CSV configuration file.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Returns an array of objects containing information about each port from the loaded chassis topology.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("loadTopology", payload=payload, response_object=None)

    def MergeCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the mergeCapture operation on the server.

        This command will merge one offline capture with on running capture.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mergeCapture(Arg1=string, Arg2=href, Arg3=enum, Arg4=string, async_operation=bool)
        ----------------------------------------------------------------------------------
        - Arg1 (str): Full path to the capture file.
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/vport/capture)): The port capture object.
        - Arg3 (str(control | data)): The type of the capture, either data or control.
        - Arg4 (str): The full path where the resulted merged capture will be saved, the result capture name needs to contain extension also.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        mergeCapture(Arg1=string, Arg2=string, Arg3=string, async_operation=bool)
        -------------------------------------------------------------------------
        - Arg1 (str): Full path to the first capture file.
        - Arg2 (str): Full path to the second capture file.
        - Arg3 (str): The full path where the resulted merged capture will be saved, the result capture name needs to contain extension also.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("mergeCapture", payload=payload, response_object=None)

    def NewConfig(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the newConfig operation on the server.

        Clear the current configuration and create an empty configuration.

        newConfig(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("newConfig", payload=payload, response_object=None)

    def RebootVirtualChassis(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the rebootVirtualChassis operation on the server.

        Perform hard reboot on the connected virtual chassis.

        rebootVirtualChassis(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "rebootVirtualChassis", payload=payload, response_object=None
        )

    def RebuildChassisTopology(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the rebuildChassisTopology operation on the server.

        Rebuild the chassis topology using automatically discovered appliances.

        rebuildChassisTopology(Arg1=string, Arg2=bool, Arg3=bool, async_operation=bool)
        -------------------------------------------------------------------------------
        - Arg1 (str): IxNetwork version that should be used to filter appliances.
        - Arg2 (bool): Flag that enables reconfiguration on the same slots for the previous cards.
        - Arg3 (bool): Promiscuous mode.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "rebuildChassisTopology", payload=payload, response_object=None
        )

    def RediscoverAppliances(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the rediscoverAppliances operation on the server.

        Return a list of discovered machines after performing rediscovery on all systems.

        rediscoverAppliances(async_operation=bool)string
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Returns a list of discovered machines in XML format.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "rediscoverAppliances", payload=payload, response_object=None
        )

    def Refresh(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the refresh operation on the server.

        NOT DEFINED

        refresh(Arg1=string, async_operation=bool)
        ------------------------------------------
        - Arg1 (str): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("refresh", payload=payload, response_object=None)

    def RefreshChassisTopology(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the refreshChassisTopology operation on the server.

        Obtain updated configuration of the chassis topology.

        refreshChassisTopology(async_operation=bool)string
        --------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Returns an array of objects containing information about each port from the new chassis topology.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "refreshChassisTopology", payload=payload, response_object=None
        )

    def RemoveAllTclViews(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the removeAllTclViews operation on the server.

        Deletes all the views that were created from using this API.

        removeAllTclViews(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("removeAllTclViews", payload=payload, response_object=None)

    def SaveCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the saveCapture operation on the server.

        This command saves the current capture data to the specified directory.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        DEPRECATED saveCapture(Arg1=string, async_operation=bool)
        ---------------------------------------------------------
        - Arg1 (str): Directory for saving the captures
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        DEPRECATED saveCapture(Arg1=string, Arg2=string, async_operation=bool)
        ----------------------------------------------------------------------
        - Arg1 (str): Directory for saving the captures
        - Arg2 (str): Suffix used for naming the capture files
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("saveCapture", payload=payload, response_object=None)

    def SaveCaptureFiles(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the saveCaptureFiles operation on the server.

        Save existing capture files to a new user specified location

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        saveCaptureFiles(Arg1=string, async_operation=bool)list
        -------------------------------------------------------
        - Arg1 (str): Directory for saving the captures
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): A list of relative paths of all the captures saved

        saveCaptureFiles(Arg1=string, Arg2=string, async_operation=bool)list
        --------------------------------------------------------------------
        - Arg1 (str): Directory for saving the captures
        - Arg2 (str): Suffix used for naming the capture files
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): A list of relative paths of all the captures saved

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("saveCaptureFiles", payload=payload, response_object=None)

    def SaveConfig(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the saveConfig operation on the server.

        Save the current configuration to a file.

        saveConfig(Arg1=href, async_operation=bool)
        -------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("saveConfig", payload=payload, response_object=None)

    def SaveSystemResources(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the saveSystemResources operation on the server.

        This command collects system resources include System Memory and Disk Usage and all processes running and saves into a csv

        saveSystemResources(async_operation=bool)string
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Returns the save file path.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "saveSystemResources", payload=payload, response_object=None
        )

    def Scriptgen(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the scriptgen operation on the server.

        Create a script of the current configuration.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        DEPRECATED scriptgen(async_operation=bool)string
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A string value.

        DEPRECATED scriptgen(Arg1=href, async_operation=bool)
        -----------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        DEPRECATED scriptgen(Arg1=href, Arg2=string, async_operation=bool)
        ------------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
        - Arg2 (str): A string value.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        DEPRECATED scriptgen(Arg1=href, Arg2=string, Arg3=list, async_operation=bool)
        -----------------------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
        - Arg2 (str): The type of script to create.
        - Arg3 (list(str)): The scriptgen options.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        DEPRECATED scriptgen(Arg1=href, Arg2=string, Arg3=list, Arg4=number, Arg5=number, async_operation=bool)
        -------------------------------------------------------------------------------------------------------
        - Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
        - Arg2 (str): A string value.
        - Arg3 (list(str)): A list of string values.
        - Arg4 (number): An integer.
        - Arg5 (number): An integer.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("scriptgen", payload=payload, response_object=None)

    def Select(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the select operation on the server.

        Select nodes and properties from the hierarchy

        select(Selects=list, async_operation=bool)string
        ------------------------------------------------
        - Selects (list(dict(from:str[None | /api/v1/sessions/1/ixnetwork/],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(child:str,properties:list[str])]))): A list of select structures.Each select structure consists of a starting point in the hierarchy. This starting point must exist and is defined as the 'from' value.Properties for the 'from' value are optional and can be retrieved using the 'properties' list.To retrieve all properties specify the '*' wildcard. Regex is not supported in the 'properties' list.Individual nodes under the starting point can be retrieved. These are specified in the 'children' list.Each item in the children list contains a 'child' name, a list of 'properties' and a list of filters by which to reduce the result set.The 'child' name can be a single name or a regex.Properties that reference another object can have that object's content inlined by specifying inline children.Any child nodes below the object reference can be expanded as long as they are specified in the inline children.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: A json encoded string of result sets.The encoded string will contain a list of result sets with each select producing a result set.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("select", payload=payload, response_object=None)

    def SendArpAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendArpAll operation on the server.

        Send ARP for all interfaces.

        sendArpAll(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("sendArpAll", payload=payload, response_object=None)

    def SendNsAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendNsAll operation on the server.

        Send neighbor solicitation to all interfaces.

        sendNsAll(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("sendNsAll", payload=payload, response_object=None)

    def SendRsAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendRsAll operation on the server.

        Send router solicitation to all interfaces.

        sendRsAll(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("sendRsAll", payload=payload, response_object=None)

    def SetChassisMode(self, *args, **kwargs):
        """Executes the setChassisMode operation on the server.

        Switch Mode(default/highRoute/ionvsFdb) for the default chassis.

        setChassisMode(Arg1=enum, Arg2=bool, async_operation=bool)object
        ----------------------------------------------------------------
        - Arg1 (str(default | highRoute | ionvsFdb)): Takes as input corresponding mode (default/highRoute/ionvsFdb).
        - Arg2 (bool): take ownership if required.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns dict(arg1:str,arg2:str): Result if succesful or not,chassis hostname and the response message.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("setChassisMode", payload=payload, response_object=None)

    def SetGuardRailVersion(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setGuardRailVersion operation on the server.

        Disables GuardRail for TCL.

        setGuardRailVersion(Arg1=string, async_operation=bool)
        ------------------------------------------------------
        - Arg1 (str): Deprecated.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "setGuardRailVersion", payload=payload, response_object=None
        )

    def SetLoggingLevel(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setLoggingLevel operation on the server.

        setLoggingLevel(Arg1=enum, async_operation=bool)
        ------------------------------------------------
        - Arg1 (str(kDebug | kError | kFatal | kInfo | kNote | kNothing | kWarn)):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("setLoggingLevel", payload=payload, response_object=None)

    def SetNamePattern(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the setNamePattern operation on the server.

        This command sets topology/port/lag/dg/ng names in bulk following a pattern

        setNamePattern(Arg1=string, async_operation=bool)string
        -------------------------------------------------------
        - Arg1 (str): details to be SET. Format is json, expects the first value in the series
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("setNamePattern", payload=payload, response_object=None)

    def SetObjectInBulk(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the setObjectInBulk operation on the server.

        This command sets topology/port/lag/dg/ng names in bulk

        setObjectInBulk(Arg1=string, async_operation=bool)string
        --------------------------------------------------------
        - Arg1 (str): details to be SET. Format is json
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("setObjectInBulk", payload=payload, response_object=None)

    def SetObjectInBulkV2(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the setObjectInBulkV2 operation on the server.

        This command sets topology/port/lag/dg/ng names in bulk

        setObjectInBulkV2(Arg1=string, async_operation=bool)string
        ----------------------------------------------------------
        - Arg1 (str): details to be SET. Format is json, expects the first value in the series
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("setObjectInBulkV2", payload=payload, response_object=None)

    def SetPortRpfTraceProperties(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setPortRpfTraceProperties operation on the server.

        sets all Available port and their rpf trace properties

        setPortRpfTraceProperties(Arg1=string, async_operation=bool)
        ------------------------------------------------------------
        - Arg1 (str):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "setPortRpfTraceProperties", payload=payload, response_object=None
        )

    def SetPortTransmitDuration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setPortTransmitDuration operation on the server.

        Set the port transmit duration.

        setPortTransmitDuration(Arg1=list, async_operation=bool)
        --------------------------------------------------------
        - Arg1 (list(dict(arg1:number,arg2:list[str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/traffic | /api/v1/sessions/1/ixnetwork/traffic/trafficItem | /api/v1/sessions/1/ixnetwork/traffic/trafficItem/highLevelStream | /api/v1/sessions/1/ixnetwork/vport]]))): An array of structures. Each structure is an duration and a valid object reference.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "setPortTransmitDuration", payload=payload, response_object=None
        )

    def SetSnapshotSettingsToDefault(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the SetSnapshotSettingsToDefault operation on the server.

        Set the settings of snapshot to default.

        SetSnapshotSettingsToDefault(Arg1=string, async_operation=bool)
        ---------------------------------------------------------------
        - Arg1 (str): The setting name.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "SetSnapshotSettingsToDefault", payload=payload, response_object=None
        )

    def SetTapSettings(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setTapSettings operation on the server.

        Send TAP Settings to IxServer for all the connected chassis.

        setTapSettings(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("setTapSettings", payload=payload, response_object=None)

    def SetTxDeviationPpm(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the setTxDeviationPpm operation on the server.

        Configures tx deviation ppm.

        setTxDeviationPpm(Arg1=string, Arg2=number, async_operation=bool)
        -----------------------------------------------------------------
        - Arg1 (str): Port location. E.g. : 100.101.101.1/1.1
        - Arg2 (number): Ppm value. E.g. : 10
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("setTxDeviationPpm", payload=payload, response_object=None)

    def StartAllProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startAllProtocols operation on the server.

        Starts all configured protocols under /vport/protocols, /vport/protocolStack and /topology

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startAllProtocols(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startAllProtocols(Arg1=enum, async_operation=bool)
        --------------------------------------------------
        - Arg1 (str(async | sync)): An enum indicating whether or not the exec will be executed synchronously or asynchronously
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("startAllProtocols", payload=payload, response_object=None)

    def StartCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startCapture operation on the server.

        The command to start the packet capture for the selected port or group of ports.

        startCapture(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("startCapture", payload=payload, response_object=None)

    def StartTestConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startTestConfiguration operation on the server.

        Starts the first Quick Test found in the current configuration.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startTestConfiguration(async_operation=bool)
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startTestConfiguration(TestName=string, async_operation=bool)
        -------------------------------------------------------------
        - TestName (str): The name of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "startTestConfiguration", payload=payload, response_object=None
        )

    def StopAllProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopAllProtocols operation on the server.

        Stops all configured protocols under /vport/protocols, /vport/protocolStack and /topology

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopAllProtocols(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopAllProtocols(Arg1=enum, async_operation=bool)
        -------------------------------------------------
        - Arg1 (str(async | sync)): An enum indicating whether or not the exec will be executed synchronously or asynchronously
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopAllProtocols", payload=payload, response_object=None)

    def StopCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopCapture operation on the server.

        The command to stop the packet capture on the selected port or group of ports.

        stopCapture(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopCapture", payload=payload, response_object=None)

    def StopTestConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopTestConfiguration operation on the server.

        Stops the currently running Quick Test.

        stopTestConfiguration(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "stopTestConfiguration", payload=payload, response_object=None
        )

    def SwitchModeLocations(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the switchModeLocations operation on the server.

        Switches the port mode. Takes locations as input.

        switchModeLocations(Arg1=list, Arg2=list, Arg3=bool, async_operation=bool)string
        --------------------------------------------------------------------------------
        - Arg1 (list(str)): A list of locations.
        - Arg2 (list(str)): List of valid Modes.
        - Arg3 (bool): If true, it will clear ownership on the hardware ports for which mode switch is being done.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Warning messages.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "switchModeLocations", payload=payload, response_object=None
        )

    def SwitchRgUserOwnershipControlMode(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the switchRgUserOwnershipControlMode operation on the server.

        Switches the port resource group user ownership mode. Takes locations as input. This operation will clear ownership on all ports of the card.

        switchRgUserOwnershipControlMode(Arg1=string, Arg2=string, async_operation=bool)string
        --------------------------------------------------------------------------------------
        - Arg1 (str): Location port.
        - Arg2 (str): Ownership control mode - userPerResourceGroup or userPerFrontPanel.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Warning messages.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "switchRgUserOwnershipControlMode", payload=payload, response_object=None
        )

    def SyncStatisticsStartTimeWithClientClock(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the syncStatisticsStartTimeWithClientClock operation on the server.

        Make the statistics timestamps relative to the time on the client machine or relative to the test start.

        syncStatisticsStartTimeWithClientClock(Arg1=bool, async_operation=bool)
        -----------------------------------------------------------------------
        - Arg1 (bool): True = relative to system time, false = relative to test start.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "syncStatisticsStartTimeWithClientClock",
            payload=payload,
            response_object=None,
        )

    def TakeViewCSVSnapshot(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the TakeViewCSVSnapshot operation on the server.

        Performs Snapshot CSV on the given views.

        TakeViewCSVSnapshot(Arg1=list, Arg2=list, async_operation=bool)
        ---------------------------------------------------------------
        - Arg1 (list(str)): A list of views for which to take a snapshot.
        - Arg2 (list(str)): A list of settings, given in the form of SettingName:SettingValue.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "TakeViewCSVSnapshot", payload=payload, response_object=None
        )

    def WaitForLicenseBroadcast(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the waitForLicenseBroadcast operation on the server.

        Wait for the license broadcast to be complete.

        waitForLicenseBroadcast(Arg1=number, async_operation=bool)
        ----------------------------------------------------------
        - Arg1 (number): Seconds to wait.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {}
        for i in range(len(args)):
            payload["Arg%s" % (i + 1)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "waitForLicenseBroadcast", payload=payload, response_object=None
        )
