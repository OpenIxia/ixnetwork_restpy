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


class Statistics(Base):
    """Generates test statistics for IxNetwork.
    The Statistics class encapsulates a required statistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'statistics'
    _SDM_ATT_MAP = {
        'AdditionalFcoeStat1': 'additionalFcoeStat1',
        'AdditionalFcoeStat2': 'additionalFcoeStat2',
        'CsvFilePath': 'csvFilePath',
        'CsvLogPollIntervalMultiplier': 'csvLogPollIntervalMultiplier',
        'DataStorePollingIntervalMultiplier': 'dataStorePollingIntervalMultiplier',
        'EnableAutoDataStore': 'enableAutoDataStore',
        'EnableCsvLogging': 'enableCsvLogging',
        'EnableDataCenterSharedStats': 'enableDataCenterSharedStats',
        'GuardrailEnabled': 'guardrailEnabled',
        'MaxNumberOfStatsPerCustomGraph': 'maxNumberOfStatsPerCustomGraph',
        'PollInterval': 'pollInterval',
        'TimeSynchronization': 'timeSynchronization',
        'TimestampPrecision': 'timestampPrecision',
        'UgsTcpPort': 'ugsTcpPort',
    }
    _SDM_ENUM_MAP = {
        'additionalFcoeStat1': ['fcoeInvalidDelimiter', 'fcoeInvalidFrames', 'fcoeInvalidSize', 'fcoeNormalSizeBadFcCRC', 'fcoeNormalSizeGoodFcCRC', 'fcoeUndersizeBadFcCRC', 'fcoeUndersizeGoodFcCRC', 'fcoeValidFrames'],
        'additionalFcoeStat2': ['fcoeInvalidDelimiter', 'fcoeInvalidFrames', 'fcoeInvalidSize', 'fcoeNormalSizeBadFcCRC', 'fcoeNormalSizeGoodFcCRC', 'fcoeUndersizeBadFcCRC', 'fcoeUndersizeGoodFcCRC', 'fcoeValidFrames'],
        'timeSynchronization': ['syncTimeToSystemClock', 'syncTimeToTestStart'],
    }

    def __init__(self, parent, list_op=False):
        super(Statistics, self).__init__(parent, list_op)

    @property
    def AutoRefresh(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh.AutoRefresh): An instance of the AutoRefresh class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh import AutoRefresh
        if len(self._object_properties) > 0:
            if self._properties.get('AutoRefresh', None) is not None:
                return self._properties.get('AutoRefresh')
        return AutoRefresh(self)._select()

    @property
    def CsvSnapshot(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot.CsvSnapshot): An instance of the CsvSnapshot class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot import CsvSnapshot
        if len(self._object_properties) > 0:
            if self._properties.get('CsvSnapshot', None) is not None:
                return self._properties.get('CsvSnapshot')
        return CsvSnapshot(self)._select()

    @property
    def Ixreporter(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter.Ixreporter): An instance of the Ixreporter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter import Ixreporter
        if len(self._object_properties) > 0:
            if self._properties.get('Ixreporter', None) is not None:
                return self._properties.get('Ixreporter')
        return Ixreporter(self)._select()

    @property
    def MeasurementMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode.MeasurementMode): An instance of the MeasurementMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode import MeasurementMode
        if len(self._object_properties) > 0:
            if self._properties.get('MeasurementMode', None) is not None:
                return self._properties.get('MeasurementMode')
        return MeasurementMode(self)._select()

    @property
    def RawData(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata.RawData): An instance of the RawData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata import RawData
        if len(self._object_properties) > 0:
            if self._properties.get('RawData', None) is not None:
                return self._properties.get('RawData')
        return RawData(self)._select()

    @property
    def View(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.view.View): An instance of the View class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.view import View
        if len(self._object_properties) > 0:
            if self._properties.get('View', None) is not None:
                return self._properties.get('View')
        return View(self)

    @property
    def AdditionalFcoeStat1(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames): Signifies additional FCOE stat 1
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat1'])
    @AdditionalFcoeStat1.setter
    def AdditionalFcoeStat1(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat1'], value)

    @property
    def AdditionalFcoeStat2(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames): Sets the additional FCoE shared stats.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat2'])
    @AdditionalFcoeStat2.setter
    def AdditionalFcoeStat2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat2'], value)

    @property
    def CsvFilePath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the CSV file path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvFilePath'])
    @CsvFilePath.setter
    def CsvFilePath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvFilePath'], value)

    @property
    def CsvLogPollIntervalMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Used to specify the time interval between log polling events.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvLogPollIntervalMultiplier'])
    @CsvLogPollIntervalMultiplier.setter
    def CsvLogPollIntervalMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvLogPollIntervalMultiplier'], value)

    @property
    def DataStorePollingIntervalMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataStorePollingIntervalMultiplier'])
    @DataStorePollingIntervalMultiplier.setter
    def DataStorePollingIntervalMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DataStorePollingIntervalMultiplier'], value)

    @property
    def EnableAutoDataStore(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If this option is enabled, StatViewer writes the statistical values in binary format for all test results in a view. The test results is converted into a binary array and written to a file.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoDataStore'])
    @EnableAutoDataStore.setter
    def EnableAutoDataStore(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoDataStore'], value)

    @property
    def EnableCsvLogging(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If this option is enabled, StatViewer writes the statistical values in comma separated value format for all test results in a view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCsvLogging'])
    @EnableCsvLogging.setter
    def EnableCsvLogging(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableCsvLogging'], value)

    @property
    def EnableDataCenterSharedStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables statistics for Data Center.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataCenterSharedStats'])
    @EnableDataCenterSharedStats.setter
    def EnableDataCenterSharedStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableDataCenterSharedStats'], value)

    @property
    def GuardrailEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GuardrailEnabled'])
    @GuardrailEnabled.setter
    def GuardrailEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['GuardrailEnabled'], value)

    @property
    def MaxNumberOfStatsPerCustomGraph(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNumberOfStatsPerCustomGraph'])
    @MaxNumberOfStatsPerCustomGraph.setter
    def MaxNumberOfStatsPerCustomGraph(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxNumberOfStatsPerCustomGraph'], value)

    @property
    def PollInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP['PollInterval'])
    @PollInterval.setter
    def PollInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PollInterval'], value)

    @property
    def TimeSynchronization(self):
        # type: () -> str
        """
        Returns
        -------
        - str(syncTimeToSystemClock | syncTimeToTestStart): The statistics polling time can be configured to get synchronized with the system clock or reset it to 0 when the test starts. The time synchronization behavior can be changed only before the test starts and does not apply during test run.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeSynchronization'])
    @TimeSynchronization.setter
    def TimeSynchronization(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TimeSynchronization'], value)

    @property
    def TimestampPrecision(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the fstatistics display values with decimals ranging from 0 to 9.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimestampPrecision'])
    @TimestampPrecision.setter
    def TimestampPrecision(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TimestampPrecision'], value)

    @property
    def UgsTcpPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Used to specify the UGS TCP port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UgsTcpPort'])

    def update(self, AdditionalFcoeStat1=None, AdditionalFcoeStat2=None, CsvFilePath=None, CsvLogPollIntervalMultiplier=None, DataStorePollingIntervalMultiplier=None, EnableAutoDataStore=None, EnableCsvLogging=None, EnableDataCenterSharedStats=None, GuardrailEnabled=None, MaxNumberOfStatsPerCustomGraph=None, PollInterval=None, TimeSynchronization=None, TimestampPrecision=None):
        # type: (str, str, str, int, int, bool, bool, bool, bool, int, int, str, int) -> Statistics
        """Updates statistics resource on the server.

        Args
        ----
        - AdditionalFcoeStat1 (str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames)): Signifies additional FCOE stat 1
        - AdditionalFcoeStat2 (str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames)): Sets the additional FCoE shared stats.
        - CsvFilePath (str): Sets the CSV file path.
        - CsvLogPollIntervalMultiplier (number): Used to specify the time interval between log polling events.
        - DataStorePollingIntervalMultiplier (number): The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        - EnableAutoDataStore (bool): If this option is enabled, StatViewer writes the statistical values in binary format for all test results in a view. The test results is converted into a binary array and written to a file.
        - EnableCsvLogging (bool): If this option is enabled, StatViewer writes the statistical values in comma separated value format for all test results in a view.
        - EnableDataCenterSharedStats (bool): If true, enables statistics for Data Center.
        - GuardrailEnabled (bool): NOT DEFINED
        - MaxNumberOfStatsPerCustomGraph (number): The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        - PollInterval (number): The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds).
        - TimeSynchronization (str(syncTimeToSystemClock | syncTimeToTestStart)): The statistics polling time can be configured to get synchronized with the system clock or reset it to 0 when the test starts. The time synchronization behavior can be changed only before the test starts and does not apply during test run.
        - TimestampPrecision (number): The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the fstatistics display values with decimals ranging from 0 to 9.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AdditionalFcoeStat1=None, AdditionalFcoeStat2=None, CsvFilePath=None, CsvLogPollIntervalMultiplier=None, DataStorePollingIntervalMultiplier=None, EnableAutoDataStore=None, EnableCsvLogging=None, EnableDataCenterSharedStats=None, GuardrailEnabled=None, MaxNumberOfStatsPerCustomGraph=None, PollInterval=None, TimeSynchronization=None, TimestampPrecision=None, UgsTcpPort=None):
        # type: (str, str, str, int, int, bool, bool, bool, bool, int, int, str, int, int) -> Statistics
        """Finds and retrieves statistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve statistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all statistics resources from the server.

        Args
        ----
        - AdditionalFcoeStat1 (str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames)): Signifies additional FCOE stat 1
        - AdditionalFcoeStat2 (str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames)): Sets the additional FCoE shared stats.
        - CsvFilePath (str): Sets the CSV file path.
        - CsvLogPollIntervalMultiplier (number): Used to specify the time interval between log polling events.
        - DataStorePollingIntervalMultiplier (number): The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        - EnableAutoDataStore (bool): If this option is enabled, StatViewer writes the statistical values in binary format for all test results in a view. The test results is converted into a binary array and written to a file.
        - EnableCsvLogging (bool): If this option is enabled, StatViewer writes the statistical values in comma separated value format for all test results in a view.
        - EnableDataCenterSharedStats (bool): If true, enables statistics for Data Center.
        - GuardrailEnabled (bool): NOT DEFINED
        - MaxNumberOfStatsPerCustomGraph (number): The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        - PollInterval (number): The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds).
        - TimeSynchronization (str(syncTimeToSystemClock | syncTimeToTestStart)): The statistics polling time can be configured to get synchronized with the system clock or reset it to 0 when the test starts. The time synchronization behavior can be changed only before the test starts and does not apply during test run.
        - TimestampPrecision (number): The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the fstatistics display values with decimals ranging from 0 to 9.
        - UgsTcpPort (number): Used to specify the UGS TCP port.

        Returns
        -------
        - self: This instance with matching statistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of statistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the statistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CheckViewTreeGroupExists(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the checkViewTreeGroupExists operation on the server.

        This command verifies that the specified group name exists in the StatViewer tree.

        checkViewTreeGroupExists(Arg2=string, async_operation=bool)
        -----------------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('checkViewTreeGroupExists', payload=payload, response_object=None)

    def DockStatViewer(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the dockStatViewer operation on the server.

        NOT DEFINED

        dockStatViewer(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dockStatViewer', payload=payload, response_object=None)

    def GetPGIDList(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPGIDList operation on the server.

        NOT DEFINED

        getPGIDList(Arg2=string, Arg3=string, async_operation=bool)list
        ---------------------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (str): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPGIDList', payload=payload, response_object=None)

    def GetStatsFooters(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getStatsFooters operation on the server.

        This command retrieves Stats Footers from traffic stats.

        getStatsFooters(Arg2=string, Arg3=string, Arg4=string, async_operation=bool)string
        ----------------------------------------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (str): NOT DEFINED
        - Arg4 (str): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getStatsFooters', payload=payload, response_object=None)
