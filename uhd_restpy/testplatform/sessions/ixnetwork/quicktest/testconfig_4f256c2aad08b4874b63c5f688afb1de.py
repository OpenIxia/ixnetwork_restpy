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


class TestConfig(Base):
    """Test configuration
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'Duration': 'duration',
        'EnableAllSlavesStatus': 'enableAllSlavesStatus',
        'EnableExpectedGrandMasterStatus': 'enableExpectedGrandMasterStatus',
        'EnableNonExpectedMasterStatus': 'enableNonExpectedMasterStatus',
        'ExpectedMasterClockId': 'expectedMasterClockId',
        'ExpectedMasterPort': 'expectedMasterPort',
        'GrandMasterStatus': 'grandMasterStatus',
        'MasterPorts': 'masterPorts',
        'MaxOutstanding': 'maxOutstanding',
        'NonExpectedMasterStatus': 'nonExpectedMasterStatus',
        'Numtrials': 'numtrials',
        'ProtocolItem': 'protocolItem',
        'Runmode': 'runmode',
        'SetupRate': 'setupRate',
        'SlavePorts': 'slavePorts',
        'StartTraffic': 'startTraffic',
        'TeardownRate': 'teardownRate',
        'UseExistingSetupRate': 'useExistingSetupRate',
    }
    _SDM_ENUM_MAP = {
        'runmode': ['duration', 'noframes'],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The wait time in hours, minutes, and seconds, that is required for the PTP protocol to negotiate
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableAllSlavesStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Master Clock ID of all the slave clocks is the same as the ID of the clock configured as Expected Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAllSlavesStatus'])
    @EnableAllSlavesStatus.setter
    def EnableAllSlavesStatus(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableAllSlavesStatus'], value)

    @property
    def EnableExpectedGrandMasterStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Status of the clock configured as Expected Master is Grand Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExpectedGrandMasterStatus'])
    @EnableExpectedGrandMasterStatus.setter
    def EnableExpectedGrandMasterStatus(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableExpectedGrandMasterStatus'], value)

    @property
    def EnableNonExpectedMasterStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Status of clocks configured as Master is not Grand Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableNonExpectedMasterStatus'])
    @EnableNonExpectedMasterStatus.setter
    def EnableNonExpectedMasterStatus(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableNonExpectedMasterStatus'], value)

    @property
    def ExpectedMasterClockId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: ID of the Expected Master Clock
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExpectedMasterClockId'])
    @ExpectedMasterClockId.setter
    def ExpectedMasterClockId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ExpectedMasterClockId'], value)

    @property
    def ExpectedMasterPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Port selected as Expected Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExpectedMasterPort'])
    @ExpectedMasterPort.setter
    def ExpectedMasterPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ExpectedMasterPort'], value)

    @property
    def GrandMasterStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Port selected as Grand Master Clock
        """
        return self._get_attribute(self._SDM_ATT_MAP['GrandMasterStatus'])
    @GrandMasterStatus.setter
    def GrandMasterStatus(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['GrandMasterStatus'], value)

    @property
    def MasterPorts(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Ports selected as Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterPorts'])
    @MasterPorts.setter
    def MasterPorts(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MasterPorts'], value)

    @property
    def MaxOutstanding(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of connection requests or tear down requests that can be pending at any one time
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstanding'])
    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstanding'], value)

    @property
    def NonExpectedMasterStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Clocks configured as Master are not Grand Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['NonExpectedMasterStatus'])
    @NonExpectedMasterStatus.setter
    def NonExpectedMasterStatus(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NonExpectedMasterStatus'], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of trials that can be run
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def ProtocolItem(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def Runmode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(duration | noframes): Running mode used
        """
        return self._get_attribute(self._SDM_ATT_MAP['Runmode'])
    @Runmode.setter
    def Runmode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Runmode'], value)

    @property
    def SetupRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of PTP connections to be initiated per second
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRate'])
    @SetupRate.setter
    def SetupRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SetupRate'], value)

    @property
    def SlavePorts(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The ports selected as slaves
        """
        return self._get_attribute(self._SDM_ATT_MAP['SlavePorts'])
    @SlavePorts.setter
    def SlavePorts(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SlavePorts'], value)

    @property
    def StartTraffic(self):
        # type: () -> str
        """
        Returns
        -------
        - str: All traffic configured in IxNetwork is initiated on running this test
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartTraffic'])
    @StartTraffic.setter
    def StartTraffic(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StartTraffic'], value)

    @property
    def TeardownRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of PTP connections to tear down per second
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    @property
    def UseExistingSetupRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Currently set Setup Rate value is used
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseExistingSetupRate'])
    @UseExistingSetupRate.setter
    def UseExistingSetupRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UseExistingSetupRate'], value)

    def update(self, Duration=None, EnableAllSlavesStatus=None, EnableExpectedGrandMasterStatus=None, EnableNonExpectedMasterStatus=None, ExpectedMasterClockId=None, ExpectedMasterPort=None, GrandMasterStatus=None, MasterPorts=None, MaxOutstanding=None, NonExpectedMasterStatus=None, Numtrials=None, ProtocolItem=None, Runmode=None, SetupRate=None, SlavePorts=None, StartTraffic=None, TeardownRate=None, UseExistingSetupRate=None):
        # type: (int, str, str, str, str, str, str, str, int, str, int, List[str], str, int, str, str, int, bool) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - Duration (number): The wait time in hours, minutes, and seconds, that is required for the PTP protocol to negotiate
        - EnableAllSlavesStatus (str): Master Clock ID of all the slave clocks is the same as the ID of the clock configured as Expected Master
        - EnableExpectedGrandMasterStatus (str): Status of the clock configured as Expected Master is Grand Master
        - EnableNonExpectedMasterStatus (str): Status of clocks configured as Master is not Grand Master
        - ExpectedMasterClockId (str): ID of the Expected Master Clock
        - ExpectedMasterPort (str): Port selected as Expected Master
        - GrandMasterStatus (str): Port selected as Grand Master Clock
        - MasterPorts (str): Ports selected as Master
        - MaxOutstanding (number): Maximum number of connection requests or tear down requests that can be pending at any one time
        - NonExpectedMasterStatus (str): Clocks configured as Master are not Grand Master
        - Numtrials (number): Number of trials that can be run
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - Runmode (str(duration | noframes)): Running mode used
        - SetupRate (number): The number of PTP connections to be initiated per second
        - SlavePorts (str): The ports selected as slaves
        - StartTraffic (str): All traffic configured in IxNetwork is initiated on running this test
        - TeardownRate (number): The number of PTP connections to tear down per second
        - UseExistingSetupRate (bool): Currently set Setup Rate value is used

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Duration=None, EnableAllSlavesStatus=None, EnableExpectedGrandMasterStatus=None, EnableNonExpectedMasterStatus=None, ExpectedMasterClockId=None, ExpectedMasterPort=None, GrandMasterStatus=None, MasterPorts=None, MaxOutstanding=None, NonExpectedMasterStatus=None, Numtrials=None, ProtocolItem=None, Runmode=None, SetupRate=None, SlavePorts=None, StartTraffic=None, TeardownRate=None, UseExistingSetupRate=None):
        # type: (int, str, str, str, str, str, str, str, int, str, int, List[str], str, int, str, str, int, bool) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - Duration (number): The wait time in hours, minutes, and seconds, that is required for the PTP protocol to negotiate
        - EnableAllSlavesStatus (str): Master Clock ID of all the slave clocks is the same as the ID of the clock configured as Expected Master
        - EnableExpectedGrandMasterStatus (str): Status of the clock configured as Expected Master is Grand Master
        - EnableNonExpectedMasterStatus (str): Status of clocks configured as Master is not Grand Master
        - ExpectedMasterClockId (str): ID of the Expected Master Clock
        - ExpectedMasterPort (str): Port selected as Expected Master
        - GrandMasterStatus (str): Port selected as Grand Master Clock
        - MasterPorts (str): Ports selected as Master
        - MaxOutstanding (number): Maximum number of connection requests or tear down requests that can be pending at any one time
        - NonExpectedMasterStatus (str): Clocks configured as Master are not Grand Master
        - Numtrials (number): Number of trials that can be run
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - Runmode (str(duration | noframes)): Running mode used
        - SetupRate (number): The number of PTP connections to be initiated per second
        - SlavePorts (str): The ports selected as slaves
        - StartTraffic (str): All traffic configured in IxNetwork is initiated on running this test
        - TeardownRate (number): The number of PTP connections to tear down per second
        - UseExistingSetupRate (bool): Currently set Setup Rate value is used

        Returns
        -------
        - self: This instance with matching testConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('waitForTest', payload=payload, response_object=None)
