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

    def __init__(self, parent):
        super(Statistics, self).__init__(parent)

    @property
    def AutoRefresh(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh.AutoRefresh): An instance of the AutoRefresh class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh import AutoRefresh
        return AutoRefresh(self)._select()

    @property
    def CsvSnapshot(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot.CsvSnapshot): An instance of the CsvSnapshot class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot import CsvSnapshot
        return CsvSnapshot(self)._select()

    @property
    def Ixreporter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter.Ixreporter): An instance of the Ixreporter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter import Ixreporter
        return Ixreporter(self)._select()

    @property
    def MeasurementMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode.MeasurementMode): An instance of the MeasurementMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode import MeasurementMode
        return MeasurementMode(self)._select()

    @property
    def RawData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata.RawData): An instance of the RawData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata import RawData
        return RawData(self)._select()

    @property
    def View(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view.View): An instance of the View class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view import View
        return View(self)

    @property
    def AdditionalFcoeStat1(self):
        """
        Returns
        -------
        - str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames): Signifies additional FCOE stat 1
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat1'])
    @AdditionalFcoeStat1.setter
    def AdditionalFcoeStat1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat1'], value)

    @property
    def AdditionalFcoeStat2(self):
        """
        Returns
        -------
        - str(fcoeInvalidDelimiter | fcoeInvalidFrames | fcoeInvalidSize | fcoeNormalSizeBadFcCRC | fcoeNormalSizeGoodFcCRC | fcoeUndersizeBadFcCRC | fcoeUndersizeGoodFcCRC | fcoeValidFrames): Sets the additional FCoE shared stats.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat2'])
    @AdditionalFcoeStat2.setter
    def AdditionalFcoeStat2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdditionalFcoeStat2'], value)

    @property
    def CsvFilePath(self):
        """
        Returns
        -------
        - str: Sets the CSV file path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvFilePath'])
    @CsvFilePath.setter
    def CsvFilePath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CsvFilePath'], value)

    @property
    def CsvLogPollIntervalMultiplier(self):
        """
        Returns
        -------
        - number: Used to specify the time interval between log polling events.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvLogPollIntervalMultiplier'])
    @CsvLogPollIntervalMultiplier.setter
    def CsvLogPollIntervalMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CsvLogPollIntervalMultiplier'], value)

    @property
    def DataStorePollingIntervalMultiplier(self):
        """
        Returns
        -------
        - number: The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataStorePollingIntervalMultiplier'])
    @DataStorePollingIntervalMultiplier.setter
    def DataStorePollingIntervalMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataStorePollingIntervalMultiplier'], value)

    @property
    def EnableAutoDataStore(self):
        """
        Returns
        -------
        - bool: If this option is enabled, StatViewer writes the statistical values in binary format for all test results in a view. The test results is converted into a binary array and written to a file.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoDataStore'])
    @EnableAutoDataStore.setter
    def EnableAutoDataStore(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoDataStore'], value)

    @property
    def EnableCsvLogging(self):
        """
        Returns
        -------
        - bool: If this option is enabled, StatViewer writes the statistical values in comma separated value format for all test results in a view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCsvLogging'])
    @EnableCsvLogging.setter
    def EnableCsvLogging(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCsvLogging'], value)

    @property
    def EnableDataCenterSharedStats(self):
        """
        Returns
        -------
        - bool: If true, enables statistics for Data Center.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataCenterSharedStats'])
    @EnableDataCenterSharedStats.setter
    def EnableDataCenterSharedStats(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataCenterSharedStats'], value)

    @property
    def GuardrailEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GuardrailEnabled'])
    @GuardrailEnabled.setter
    def GuardrailEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GuardrailEnabled'], value)

    @property
    def MaxNumberOfStatsPerCustomGraph(self):
        """
        Returns
        -------
        - number: The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNumberOfStatsPerCustomGraph'])
    @MaxNumberOfStatsPerCustomGraph.setter
    def MaxNumberOfStatsPerCustomGraph(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxNumberOfStatsPerCustomGraph'], value)

    @property
    def PollInterval(self):
        """
        Returns
        -------
        - number: The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP['PollInterval'])
    @PollInterval.setter
    def PollInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PollInterval'], value)

    @property
    def TimeSynchronization(self):
        """
        Returns
        -------
        - str(syncTimeToSystemClock | syncTimeToTestStart): The statistics polling time can be configured to get synchronized with the system clock or reset it to 0 when the test starts. The time synchronization behavior can be changed only before the test starts and does not apply during test run.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeSynchronization'])
    @TimeSynchronization.setter
    def TimeSynchronization(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeSynchronization'], value)

    @property
    def TimestampPrecision(self):
        """
        Returns
        -------
        - number: The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the fstatistics display values with decimals ranging from 0 to 9.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimestampPrecision'])
    @TimestampPrecision.setter
    def TimestampPrecision(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimestampPrecision'], value)

    @property
    def UgsTcpPort(self):
        """
        Returns
        -------
        - number: Used to specify the UGS TCP port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UgsTcpPort'])

    def update(self, AdditionalFcoeStat1=None, AdditionalFcoeStat2=None, CsvFilePath=None, CsvLogPollIntervalMultiplier=None, DataStorePollingIntervalMultiplier=None, EnableAutoDataStore=None, EnableCsvLogging=None, EnableDataCenterSharedStats=None, GuardrailEnabled=None, MaxNumberOfStatsPerCustomGraph=None, PollInterval=None, TimeSynchronization=None, TimestampPrecision=None):
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

    def CheckViewTreeGroupExists(self, *args, **kwargs):
        """Executes the checkViewTreeGroupExists operation on the server.

        This command verifies that the specified group name exists in the StatViewer tree.

        checkViewTreeGroupExists(Arg2=string)
        -------------------------------------
        - Arg2 (str): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('checkViewTreeGroupExists', payload=payload, response_object=None)

    def DockStatViewer(self):
        """Executes the dockStatViewer operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('dockStatViewer', payload=payload, response_object=None)

    def GetPGIDList(self, *args, **kwargs):
        """Executes the getPGIDList operation on the server.

        NOT DEFINED

        getPGIDList(Arg2=string, Arg3=string)list
        -----------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (str): NOT DEFINED
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
        """Executes the getStatsFooters operation on the server.

        This command retrieves Stats Footers from traffic stats.

        getStatsFooters(Arg2=string, Arg3=string, Arg4=string)string
        ------------------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (str): NOT DEFINED
        - Arg4 (str): NOT DEFINED
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
