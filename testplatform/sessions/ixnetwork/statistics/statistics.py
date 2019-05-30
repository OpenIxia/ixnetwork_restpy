# Copyright 1997 - 2018 by IXIA Keysight
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
	"""The Statistics class encapsulates a required statistics node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Statistics property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'statistics'

	def __init__(self, parent):
		super(Statistics, self).__init__(parent)

	@property
	def AutoRefresh(self):
		"""An instance of the AutoRefresh class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh.AutoRefresh)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh import AutoRefresh
		return AutoRefresh(self)._select()

	@property
	def CsvSnapshot(self):
		"""An instance of the CsvSnapshot class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot.CsvSnapshot)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot import CsvSnapshot
		return CsvSnapshot(self)._select()

	@property
	def Ixreporter(self):
		"""An instance of the Ixreporter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter.Ixreporter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter import Ixreporter
		return Ixreporter(self)._select()

	@property
	def MeasurementMode(self):
		"""An instance of the MeasurementMode class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode.MeasurementMode)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode import MeasurementMode
		return MeasurementMode(self)._select()

	@property
	def RawData(self):
		"""An instance of the RawData class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata.RawData)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata import RawData
		return RawData(self)._select()

	@property
	def View(self):
		"""An instance of the View class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view.View)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view import View
		return View(self)

	@property
	def AdditionalFcoeStat1(self):
		"""Signifies additional FCOE stat 1

		Returns:
			str(fcoeInvalidDelimiter|fcoeInvalidFrames|fcoeInvalidSize|fcoeNormalSizeBadFcCRC|fcoeNormalSizeGoodFcCRC|fcoeUndersizeBadFcCRC|fcoeUndersizeGoodFcCRC|fcoeValidFrames)
		"""
		return self._get_attribute('additionalFcoeStat1')
	@AdditionalFcoeStat1.setter
	def AdditionalFcoeStat1(self, value):
		self._set_attribute('additionalFcoeStat1', value)

	@property
	def AdditionalFcoeStat2(self):
		"""Sets the additional FCoE shared stats.

		Returns:
			str(fcoeInvalidDelimiter|fcoeInvalidFrames|fcoeInvalidSize|fcoeNormalSizeBadFcCRC|fcoeNormalSizeGoodFcCRC|fcoeUndersizeBadFcCRC|fcoeUndersizeGoodFcCRC|fcoeValidFrames)
		"""
		return self._get_attribute('additionalFcoeStat2')
	@AdditionalFcoeStat2.setter
	def AdditionalFcoeStat2(self, value):
		self._set_attribute('additionalFcoeStat2', value)

	@property
	def CsvFilePath(self):
		"""Sets the CSV file path.

		Returns:
			str
		"""
		return self._get_attribute('csvFilePath')
	@CsvFilePath.setter
	def CsvFilePath(self, value):
		self._set_attribute('csvFilePath', value)

	@property
	def CsvLogPollIntervalMultiplier(self):
		"""Used to specify the time interval between log polling events.

		Returns:
			number
		"""
		return self._get_attribute('csvLogPollIntervalMultiplier')
	@CsvLogPollIntervalMultiplier.setter
	def CsvLogPollIntervalMultiplier(self, value):
		self._set_attribute('csvLogPollIntervalMultiplier', value)

	@property
	def DataStorePollingIntervalMultiplier(self):
		"""The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.

		Returns:
			number
		"""
		return self._get_attribute('dataStorePollingIntervalMultiplier')
	@DataStorePollingIntervalMultiplier.setter
	def DataStorePollingIntervalMultiplier(self, value):
		self._set_attribute('dataStorePollingIntervalMultiplier', value)

	@property
	def EnableAutoDataStore(self):
		"""If this option is enabled, StatViewer writes the statistical values in binary format for all test results in a view. The test results is converted into a binary array and written to a file.

		Returns:
			bool
		"""
		return self._get_attribute('enableAutoDataStore')
	@EnableAutoDataStore.setter
	def EnableAutoDataStore(self, value):
		self._set_attribute('enableAutoDataStore', value)

	@property
	def EnableCsvLogging(self):
		"""If this option is enabled, StatViewer writes the statistical values in comma separated value format for all test results in a view.

		Returns:
			bool
		"""
		return self._get_attribute('enableCsvLogging')
	@EnableCsvLogging.setter
	def EnableCsvLogging(self, value):
		self._set_attribute('enableCsvLogging', value)

	@property
	def EnableDataCenterSharedStats(self):
		"""If true, enables statistics for Data Center.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataCenterSharedStats')
	@EnableDataCenterSharedStats.setter
	def EnableDataCenterSharedStats(self, value):
		self._set_attribute('enableDataCenterSharedStats', value)

	@property
	def GuardrailEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('guardrailEnabled')
	@GuardrailEnabled.setter
	def GuardrailEnabled(self, value):
		self._set_attribute('guardrailEnabled', value)

	@property
	def MaxNumberOfStatsPerCustomGraph(self):
		"""The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.

		Returns:
			number
		"""
		return self._get_attribute('maxNumberOfStatsPerCustomGraph')
	@MaxNumberOfStatsPerCustomGraph.setter
	def MaxNumberOfStatsPerCustomGraph(self, value):
		self._set_attribute('maxNumberOfStatsPerCustomGraph', value)

	@property
	def PollInterval(self):
		"""The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds).

		Returns:
			number
		"""
		return self._get_attribute('pollInterval')
	@PollInterval.setter
	def PollInterval(self, value):
		self._set_attribute('pollInterval', value)

	@property
	def TimeSynchronization(self):
		"""The statistics polling time can be configured to get synchronized with the system clock or reset it to 0 when the test starts. The time synchronization behavior can be changed only before the test starts and does not apply during test run.

		Returns:
			str(syncTimeToSystemClock|syncTimeToTestStart)
		"""
		return self._get_attribute('timeSynchronization')
	@TimeSynchronization.setter
	def TimeSynchronization(self, value):
		self._set_attribute('timeSynchronization', value)

	@property
	def TimestampPrecision(self):
		"""The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the fstatistics display values with decimals ranging from 0 to 9.

		Returns:
			number
		"""
		return self._get_attribute('timestampPrecision')
	@TimestampPrecision.setter
	def TimestampPrecision(self, value):
		self._set_attribute('timestampPrecision', value)

	@property
	def UgsTcpPort(self):
		"""Used to specify the UGS TCP port.

		Returns:
			number
		"""
		return self._get_attribute('ugsTcpPort')

	def update(self, AdditionalFcoeStat1=None, AdditionalFcoeStat2=None, CsvFilePath=None, CsvLogPollIntervalMultiplier=None, DataStorePollingIntervalMultiplier=None, EnableAutoDataStore=None, EnableCsvLogging=None, EnableDataCenterSharedStats=None, GuardrailEnabled=None, MaxNumberOfStatsPerCustomGraph=None, PollInterval=None, TimeSynchronization=None, TimestampPrecision=None):
		"""Updates a child instance of statistics on the server.

		Args:
			AdditionalFcoeStat1 (str(fcoeInvalidDelimiter|fcoeInvalidFrames|fcoeInvalidSize|fcoeNormalSizeBadFcCRC|fcoeNormalSizeGoodFcCRC|fcoeUndersizeBadFcCRC|fcoeUndersizeGoodFcCRC|fcoeValidFrames)): Signifies additional FCOE stat 1
			AdditionalFcoeStat2 (str(fcoeInvalidDelimiter|fcoeInvalidFrames|fcoeInvalidSize|fcoeNormalSizeBadFcCRC|fcoeNormalSizeGoodFcCRC|fcoeUndersizeBadFcCRC|fcoeUndersizeGoodFcCRC|fcoeValidFrames)): Sets the additional FCoE shared stats.
			CsvFilePath (str): Sets the CSV file path.
			CsvLogPollIntervalMultiplier (number): Used to specify the time interval between log polling events.
			DataStorePollingIntervalMultiplier (number): The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
			EnableAutoDataStore (bool): If this option is enabled, StatViewer writes the statistical values in binary format for all test results in a view. The test results is converted into a binary array and written to a file.
			EnableCsvLogging (bool): If this option is enabled, StatViewer writes the statistical values in comma separated value format for all test results in a view.
			EnableDataCenterSharedStats (bool): If true, enables statistics for Data Center.
			GuardrailEnabled (bool): NOT DEFINED
			MaxNumberOfStatsPerCustomGraph (number): The data store polling interval value is the result of the data store polling interval multiplier value multiplied by the polling interval value set for the test.
			PollInterval (number): The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds).
			TimeSynchronization (str(syncTimeToSystemClock|syncTimeToTestStart)): The statistics polling time can be configured to get synchronized with the system clock or reset it to 0 when the test starts. The time synchronization behavior can be changed only before the test starts and does not apply during test run.
			TimestampPrecision (number): The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the fstatistics display values with decimals ranging from 0 to 9.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def CheckViewTreeGroupExists(self, *args, **kwargs):
		"""Executes the checkViewTreeGroupExists operation on the server.

		This command verifies that the specified group name exists in the StatViewer tree.

		checkViewTreeGroupExists(Arg2:string)
			Args:
				args[0] is Arg2 (str): NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('checkViewTreeGroupExists', payload=payload, response_object=None)

	def DockStatViewer(self):
		"""Executes the dockStatViewer operation on the server.

		NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('dockStatViewer', payload=payload, response_object=None)

	def GetPGIDList(self, *args, **kwargs):
		"""Executes the getPGIDList operation on the server.

		NOT DEFINED

		getPGIDList(Arg2:string, Arg3:string)list
			Args:
				args[0] is Arg2 (str): NOT DEFINED
				args[1] is Arg3 (str): NOT DEFINED

			Returns:
				list(str): NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getPGIDList', payload=payload, response_object=None)

	def GetStatsFooters(self, *args, **kwargs):
		"""Executes the getStatsFooters operation on the server.

		This command retrieves Stats Footers from traffic stats.

		getStatsFooters(Arg2:string, Arg3:string, Arg4:string)string
			Args:
				args[0] is Arg2 (str): NOT DEFINED
				args[1] is Arg3 (str): NOT DEFINED
				args[2] is Arg4 (str): NOT DEFINED

			Returns:
				str: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getStatsFooters', payload=payload, response_object=None)
