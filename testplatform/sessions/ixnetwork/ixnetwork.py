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


class Ixnetwork(Base):
	"""The Ixnetwork class encapsulates a system managed / node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Ixnetwork property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'ixnetwork'

	def __init__(self, parent):
		super(Ixnetwork, self).__init__(parent)

	@property
	def AvailableHardware(self):
		"""An instance of the AvailableHardware class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.availablehardware.AvailableHardware)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.availablehardware import AvailableHardware
		return AvailableHardware(self)._select()

	@property
	def Globals(self):
		"""An instance of the Globals class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.globals.Globals)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.globals import Globals
		return Globals(self)._select()

	@property
	def Impairment(self):
		"""An instance of the Impairment class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.impairment.Impairment)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.impairment import Impairment
		return Impairment(self)._select()

	@property
	def Lag(self):
		"""An instance of the Lag class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag.Lag)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag import Lag
		return Lag(self)

	@property
	def QuickTest(self):
		"""An instance of the QuickTest class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.quicktest.QuickTest)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.quicktest import QuickTest
		return QuickTest(self)._select()

	@property
	def ResourceManager(self):
		"""An instance of the ResourceManager class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager.ResourceManager)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager import ResourceManager
		return ResourceManager(self)._select()

	@property
	def Statistics(self):
		"""An instance of the Statistics class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statistics.Statistics)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statistics import Statistics
		return Statistics(self)._select()

	@property
	def Timeline(self):
		"""An instance of the Timeline class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.timeline.Timeline)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.timeline import Timeline
		return Timeline(self)._select()

	@property
	def Topology(self):
		"""An instance of the Topology class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology.Topology)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology import Topology
		return Topology(self)

	@property
	def Traffic(self):
		"""An instance of the Traffic class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.traffic.Traffic)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.traffic import Traffic
		return Traffic(self)._select()

	@property
	def Vport(self):
		"""An instance of the Vport class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport import Vport
		return Vport(self)

	def ApplyITWizardConfiguration(self, *args, **kwargs):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the first Quick Test found in the current configuration.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		applyITWizardConfiguration()

		applyITWizardConfiguration(TestName:string)
			Args:
				args[0] is TestName (str): The name of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

	def ApplyL1Blocking(self):
		"""Executes the applyL1Blocking operation on the server.

		Apply L1 blocking.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('applyL1Blocking', payload=payload, response_object=None)

	def AssignPorts(self, *args, **kwargs):
		"""Executes the assignPorts operation on the server.

		Assign hardware ports to virtual ports.

		assignPorts(Arg1:list, Arg2:list, Arg3:list, Arg4:bool)list
			Args:
				args[0] is Arg1 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to include.
				args[1] is Arg2 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to exclude.
				args[2] is Arg3 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): A list of virtual port object references that hardware ports will be attached to.
				args[3] is Arg4 (bool): If true, it will clear ownership on the hardware ports.

			Returns:
				list(str[None|/api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('assignPorts', payload=payload, response_object=None)

	def ClearAppLibraryStats(self):
		"""Executes the clearAppLibraryStats operation on the server.

		Clears the statistics published by AppLibrary.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('clearAppLibraryStats', payload=payload, response_object=None)

	def ClearCardOwnershipById(self, *args, **kwargs):
		"""Executes the clearCardOwnershipById operation on the server.

		Clear ownership on all ports from the given IxVM card.

		clearCardOwnershipById(Arg1:string)number
			Args:
				args[0] is Arg1 (str): The card ID.

			Returns:
				number: Returns the card ID.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('clearCardOwnershipById', payload=payload, response_object=None)

	def ClearCPDPStats(self):
		"""Executes the clearCPDPStats operation on the server.

		Clear control pland and data plane statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('clearCPDPStats', payload=payload, response_object=None)

	def ClearPortsAndTrafficStats(self, *args, **kwargs):
		"""Executes the clearPortsAndTrafficStats operation on the server.

		The command to clear the existing port and traffic statistics.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		clearPortsAndTrafficStats()

		clearPortsAndTrafficStats(Arg1:list)
			Args:
				args[0] is Arg1 (list(str[waitForPortStatsRefresh|waitForTrafficStatsRefresh])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('clearPortsAndTrafficStats', payload=payload, response_object=None)

	def ClearProtocolStats(self):
		"""Executes the clearProtocolStats operation on the server.

		Clear the protocol statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('clearProtocolStats', payload=payload, response_object=None)

	def ClearStats(self, *args, **kwargs):
		"""Executes the clearStats operation on the server.

		The command to clear the existing statistics.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		clearStats()

		clearStats(Arg1:list)
			Args:
				args[0] is Arg1 (list(str[waitForPortStatsRefresh|waitForTrafficStatsRefresh])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('clearStats', payload=payload, response_object=None)

	def CloseAllTabs(self, *args, **kwargs):
		"""Executes the closeAllTabs operation on the server.

		This command closes all the captures if no parameter is specified; or a specific list of online captures

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		closeAllTabs()

		closeAllTabs(Arg1:list)
			Args:
				args[0] is Arg1 (list(str)): The list of capture names to be closed.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('closeAllTabs', payload=payload, response_object=None)

	def CollectLogs(self, *args, **kwargs):
		"""Executes the collectLogs operation on the server.

		This command collects all of the IxNetwork logs and puts them in a .zip file.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		collectLogs(Arg1:href)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.

		collectLogs(Arg1:href, Arg2:list)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
				args[1] is Arg2 (list(str[currentInstance|specificProfile])): The instance to collect logs for.

		collectLogs(Arg1:href, Arg2:list, Arg3:string)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command.
				args[1] is Arg2 (list(str[currentInstance|specificProfile])): A valid enum as specified by the restriction.
				args[2] is Arg3 (str): A string value.

		collectLogs(Arg1:href, Arg2:list, Arg3:string, Arg4:string)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A string value.
				args[1] is Arg2 (list(str[currentInstance|specificProfile])): An enum value indicating the item to collect logs for.
				args[2] is Arg3 (str): A string value.
				args[3] is Arg4 (str): A string value.

		collectLogs(Arg1:href, Arg2:list, Arg3:string, Arg4:string, Arg5:string)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command.
				args[1] is Arg2 (list(str[currentInstance|specificProfile])): A valid enum as specified by the restriction.
				args[2] is Arg3 (str): A string value.
				args[3] is Arg4 (str): A string value.
				args[4] is Arg5 (str): A string value.

		collectLogs(Arg1:href, Arg2:string)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
				args[1] is Arg2 (str): A string value.

		collectLogs(Arg1:href, Arg2:string, Arg3:string)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
				args[1] is Arg2 (str): A string value.
				args[2] is Arg3 (str): A string value.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('collectLogs', payload=payload, response_object=None)

	def ConnectCardById(self, *args, **kwargs):
		"""Executes the connectCardById operation on the server.

		Establish connection to the IxVM card.

		connectCardById(Arg1:string)number
			Args:
				args[0] is Arg1 (str): Card ID to which connection is required.

			Returns:
				number: Returns the connected card ID or error, if any.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('connectCardById', payload=payload, response_object=None)

	def ConnectToChassis(self, *args, **kwargs):
		"""Executes the connectToChassis operation on the server.

		Connect to a virtual chassis.

		connectToChassis(Arg1:string)
			Args:
				args[0] is Arg1 (str): The hostname or IP address of the chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('connectToChassis', payload=payload, response_object=None)

	def CopyFile(self, *args, **kwargs):
		"""Executes the copyFile operation on the server.

		Copies from first stream into the second stream.

		copyFile(Arg1:href, Arg2:href)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): The source file for the copy operation. This stream must be readable.
				args[1] is Arg2 (obj(ixnetwork_restpy.files.Files)): The destination file for the copy operation. This stream must be writable.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('copyFile', payload=payload, response_object=None)

	def DisconnectCardById(self, *args, **kwargs):
		"""Executes the disconnectCardById operation on the server.

		Close connection to the IxVM card.

		disconnectCardById(Arg1:string)number
			Args:
				args[0] is Arg1 (str): The card ID.

			Returns:
				number: Returns the card ID.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('disconnectCardById', payload=payload, response_object=None)

	def GenerateReport(self):
		"""Executes the generateReport operation on the server.

		This report feature generates an integrated test report file.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('generateReport', payload=payload, response_object=None)

	def GetAggregatedDeviceGroupStatus(self):
		"""Executes the getAggregatedDeviceGroupStatus operation on the server.

			Returns:
				list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:list[dict(arg1:str,arg2:number)])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getAggregatedDeviceGroupStatus', payload=payload, response_object=None)

	def GetAllPorts(self):
		"""Executes the getAllPorts operation on the server.

		The command to get all the ports.

			Returns:
				str: A string with all the ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getAllPorts', payload=payload, response_object=None)

	def GetAvailableProtocolStats(self):
		"""Executes the getAvailableProtocolStats operation on the server.

		The command to get available protocol statistics.

			Returns:
				str: A string with all the legacy protocols statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getAvailableProtocolStats', payload=payload, response_object=None)

	def GetAvailableSlotLicense(self, *args, **kwargs):
		"""Executes the getAvailableSlotLicense operation on the server.

		This exec returns number of AppLibrary Slot License avaibale for use in the chassis.

		getAvailableSlotLicense(Arg1:string)number
			Args:
				args[0] is Arg1 (str): The IPv4 address of the chassis.

			Returns:
				number: The number of AppLibrary Slot License available for use in the chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getAvailableSlotLicense', payload=payload, response_object=None)

	def GetAvailableStatsForProtocol(self, *args, **kwargs):
		"""Executes the getAvailableStatsForProtocol operation on the server.

		The command to get available statistics for the protocol.

		getAvailableStatsForProtocol(Arg1:string)string
			Args:
				args[0] is Arg1 (str): Protocol name.

			Returns:
				str: A string with all the available statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getAvailableStatsForProtocol', payload=payload, response_object=None)

	def GetAvailableStatsForSourceType(self, *args, **kwargs):
		"""Executes the getAvailableStatsForSourceType operation on the server.

		The command to get available statistics for the source type.

		getAvailableStatsForSourceType(Arg1:string)string
			Args:
				args[0] is Arg1 (str): Source type.

			Returns:
				str: A string with all the available statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getAvailableStatsForSourceType', payload=payload, response_object=None)

	def GetConfiguredProtocols(self):
		"""Executes the getConfiguredProtocols operation on the server.

		The command to get the configured protocols.

			Returns:
				str: A list with all the protocols configured in the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getConfiguredProtocols', payload=payload, response_object=None)

	def GetConfiguredProtocolsForPort(self, *args, **kwargs):
		"""Executes the getConfiguredProtocolsForPort operation on the server.

		The command to get the configured protocols for the port.

		getConfiguredProtocolsForPort(Arg1:number)string
			Args:
				args[0] is Arg1 (number): Port ID.

			Returns:
				str: A string with all the available protocols configured on the port.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getConfiguredProtocolsForPort', payload=payload, response_object=None)

	def GetCsvColumnNames(self, *args, **kwargs):
		"""Executes the getCsvColumnNames operation on the server.

		getCsvColumnNames(Arg1:href)list
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): 

			Returns:
				list(str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getCsvColumnNames', payload=payload, response_object=None)

	def GetCurrentIxiaFileFormatTypeVersion(self):
		"""Executes the getCurrentIxiaFileFormatTypeVersion operation on the server.

		This command sets the current Ixia file format type version.

			Returns:
				number: Returns current Ixia file format type version.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getCurrentIxiaFileFormatTypeVersion', payload=payload, response_object=None)

	def GetDefaultSnapshotSettings(self):
		"""Executes the GetDefaultSnapshotSettings operation on the server.

		Gets the default snapshot settings.

			Returns:
				list(str): An array with settings.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('GetDefaultSnapshotSettings', payload=payload, response_object=None)

	def GetInstalledSlotLicenseCount(self, *args, **kwargs):
		"""Executes the getInstalledSlotLicenseCount operation on the server.

		This exec returns number of AppLibrary Slot License installed in the chassis.

		getInstalledSlotLicenseCount(Arg1:string)number
			Args:
				args[0] is Arg1 (str): The IPv4 address of the chassis.

			Returns:
				number: The number of AppLibrary Slot License installed in the chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getInstalledSlotLicenseCount', payload=payload, response_object=None)

	def GetIntersectionPortsForProtocols(self, *args, **kwargs):
		"""Executes the getIntersectionPortsForProtocols operation on the server.

		The command to get intersection ports for the protocols.

		getIntersectionPortsForProtocols(Arg1:list)string
			Args:
				args[0] is Arg1 (list(str)): A list of protocol names.

			Returns:
				str: The list of port IDs that have all the given protocols configured.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIntersectionPortsForProtocols', payload=payload, response_object=None)

	def GetIxVmCardByIp(self, *args, **kwargs):
		"""Executes the getIxVmCardByIp operation on the server.

		Obtain IxVM card ID by providing management IP address.

		getIxVmCardByIp(Arg1:string)number
			Args:
				args[0] is Arg1 (str): Management IP address of the card.

			Returns:
				number: Returns the card ID which has corresponding IP address on the management interface.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIxVmCardByIp', payload=payload, response_object=None)

	def GetMemoryUsageInfo(self):
		"""Executes the getMemoryUsageInfo operation on the server.

		Retrieve memory usage information

			Returns:
				str: String containing memory usage: virtual, private, peak virtual bytes and bytes in all heaps

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getMemoryUsageInfo', payload=payload, response_object=None)

	def GetNetworkGroupSize(self):
		"""Executes the getNetworkGroupSize operation on the server.

			Returns:
				list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:list[dict(arg1:str,arg2:number)])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getNetworkGroupSize', payload=payload, response_object=None)

	def GetPortsForProtocol(self, *args, **kwargs):
		"""Executes the getPortsForProtocol operation on the server.

		The command to get ports for the protocol.

		getPortsForProtocol(Arg1:string)string
			Args:
				args[0] is Arg1 (str): Protocol name.

			Returns:
				str: A string with all the port IDs having the protocol configured.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getPortsForProtocol', payload=payload, response_object=None)

	def GetRbMemoryUsageInfo(self):
		"""Executes the getRbMemoryUsageInfo operation on the server.

		Fetch the memory usage information by RB protocols.

			Returns:
				str: Returns memory usage information by RB protocols.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getRbMemoryUsageInfo', payload=payload, response_object=None)

	def GetRecommendedSettings(self, *args, **kwargs):
		"""Executes the getRecommendedSettings operation on the server.

		It will get the recommended settings for the given copper type. Available choices are: oneMeter, threeMeters, fiveMeters.

		getRecommendedSettings(Arg1:string, Arg2:list)
			Args:
				args[0] is Arg1 (str): 
				args[1] is Arg2 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getRecommendedSettings', payload=payload, response_object=None)

	def GetSlotLicenseInUse(self, *args, **kwargs):
		"""Executes the getSlotLicenseInUse operation on the server.

		This exec returns a list of slots/cards of the chassis that are currently using the AppLibrary Slot Licenses.

		getSlotLicenseInUse(Arg1:string)list
			Args:
				args[0] is Arg1 (str): The IPv4 address of the chassis.

			Returns:
				list(number): An array of slot/card numbers of the chassis that currently checked-out AppLibrary Slot Licenses.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getSlotLicenseInUse', payload=payload, response_object=None)

	def GetTapSettings(self):
		"""Executes the getTapSettings operation on the server.

		Get TAP Settings for all the connected chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getTapSettings', payload=payload, response_object=None)

	def GetTopologyStatus(self):
		"""Executes the getTopologyStatus operation on the server.

			Returns:
				list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:list[dict(arg1:str,arg2:number)],arg3:str[notstarted\~starting\~started\~stopping\~error\~mixed])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('getTopologyStatus', payload=payload, response_object=None)

	def GetUnionPortsForProtocols(self, *args, **kwargs):
		"""Executes the getUnionPortsForProtocols operation on the server.

		The command to get union ports for the protocols.

		getUnionPortsForProtocols(Arg1:list)string
			Args:
				args[0] is Arg1 (list(str)): A list of protocol names.

			Returns:
				str: The list of port IDs that have at least one of the given protocols configured.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getUnionPortsForProtocols', payload=payload, response_object=None)

	def HwRebootCardByIDs(self, *args, **kwargs):
		"""Executes the hwRebootCardByIDs operation on the server.

		Perform hard reboot on virtual cards.

		hwRebootCardByIDs(Arg1:list)bool
			Args:
				args[0] is Arg1 (list(number)): An array of card IDs.

			Returns:
				bool: Returns whether or not the command is successful.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('hwRebootCardByIDs', payload=payload, response_object=None)

	def IgmpJoin(self, *args, **kwargs):
		"""Executes the igmpJoin operation on the server.

		Executing this command sends IGMP join message.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		igmpJoin(Arg1:string)
			Args:
				args[0] is Arg1 (str): This is a multicast IPv4 address as an argument to igmpJoin.

		igmpJoin(Arg1:string, Arg2:number)
			Args:
				args[0] is Arg1 (str): This is a multicast IPv4 address as an argument to igmpJoin.
				args[1] is Arg2 (number): This is an integer value as an argument to igmpJoin.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('igmpJoin', payload=payload, response_object=None)

	def IgmpLeave(self, *args, **kwargs):
		"""Executes the igmpLeave operation on the server.

		Executing this command sends IGMP leave message.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		igmpLeave(Arg1:string)
			Args:
				args[0] is Arg1 (str): This is a multicast IPv4 address as an argument to igmpLeave.

		igmpLeave(Arg1:string, Arg2:number)
			Args:
				args[0] is Arg1 (str): This is a multicast IPv4 address as an argument to igmpLeave.
				args[1] is Arg2 (number): This is an integer value as an argument to igmpLeave.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('igmpLeave', payload=payload, response_object=None)

	def Import(self, *args, **kwargs):
		"""Executes the import operation on the server.

		Imports a legacy IxAutomate configuration from the specified file.

		import(File:string)
			Args:
				args[0] is File (str): The IxAutomate configuration file that will be imported.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('import', payload=payload, response_object=None)

	def LoadConfig(self, *args, **kwargs):
		"""Executes the loadConfig operation on the server.

		Load an existing configuration file.

		loadConfig(Arg1:href)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A readFrom file handle

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('loadConfig', payload=payload, response_object=None)

	def LoadTopology(self, *args, **kwargs):
		"""Executes the loadTopology operation on the server.

		Load a chassis topology from file.

		loadTopology(Arg1:string)string
			Args:
				args[0] is Arg1 (str): Path to the CSV configuration file.

			Returns:
				str: Returns an array of objects containing information about each port from the loaded chassis topology.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('loadTopology', payload=payload, response_object=None)

	def MergeCapture(self, *args, **kwargs):
		"""Executes the mergeCapture operation on the server.

		This command will merge one offline capture with on running capture.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		mergeCapture(Arg1:string, Arg2:href, Arg3:enum, Arg4:string)
			Args:
				args[0] is Arg1 (str): Full path to the capture file.
				args[1] is Arg2 (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=capture)): The port capture object.
				args[2] is Arg3 (str(control|data)): The type of the capture, either data or control.
				args[3] is Arg4 (str): The full path where the resulted merged capture will be saved, the resulted capture name needs to contain extension also.

		mergeCapture(Arg1:string, Arg2:string, Arg3:string)
			Args:
				args[0] is Arg1 (str): Full path to the first capture file.
				args[1] is Arg2 (str): Full path to the second capture file.
				args[2] is Arg3 (str): The full path where the resulted merged capture will be saved, the result capture name needs to contain extension also.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('mergeCapture', payload=payload, response_object=None)

	def NewConfig(self):
		"""Executes the newConfig operation on the server.

		Clear the current configuration and create an empty configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('newConfig', payload=payload, response_object=None)

	def RebootVirtualChassis(self):
		"""Executes the rebootVirtualChassis operation on the server.

		Perform hard reboot on the connected virtual chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('rebootVirtualChassis', payload=payload, response_object=None)

	def RebuildChassisTopology(self, *args, **kwargs):
		"""Executes the rebuildChassisTopology operation on the server.

		Rebuild the chassis topology using automatically discovered appliances.

		rebuildChassisTopology(Arg1:string, Arg2:bool, Arg3:bool)
			Args:
				args[0] is Arg1 (str): IxNetwork version that should be used to filter appliances.
				args[1] is Arg2 (bool): Flag that enables reconfiguration on the same slots for the previous cards.
				args[2] is Arg3 (bool): Promiscuous mode.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('rebuildChassisTopology', payload=payload, response_object=None)

	def RediscoverAppliances(self):
		"""Executes the rediscoverAppliances operation on the server.

		Return a list of discovered machines after performing rediscovery on all systems.

			Returns:
				str: Returns a list of discovered machines in XML format.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('rediscoverAppliances', payload=payload, response_object=None)

	def Refresh(self, *args, **kwargs):
		"""Executes the refresh operation on the server.

		NOT DEFINED

		refresh(Arg1:string)
			Args:
				args[0] is Arg1 (str): NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('refresh', payload=payload, response_object=None)

	def RefreshChassisTopology(self):
		"""Executes the refreshChassisTopology operation on the server.

		Obtain updated configuration of the chassis topology.

			Returns:
				str: Returns an array of objects containing information about each port from the new chassis topology.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('refreshChassisTopology', payload=payload, response_object=None)

	def RemoveAllTclViews(self):
		"""Executes the removeAllTclViews operation on the server.

		Deletes all the views that were created from using this API.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('removeAllTclViews', payload=payload, response_object=None)

	def SaveCapture(self, *args, **kwargs):
		"""Executes the saveCapture operation on the server.

		This command saves the current capture data to the specified directory.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		DEPRECATED saveCapture(Arg1:string)
			Args:
				args[0] is Arg1 (str): Directory for saving the captures

		DEPRECATED saveCapture(Arg1:string, Arg2:string)
			Args:
				args[0] is Arg1 (str): Directory for saving the captures
				args[1] is Arg2 (str): Suffix used for naming the capture files

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('saveCapture', payload=payload, response_object=None)

	def SaveCaptureFiles(self, *args, **kwargs):
		"""Executes the saveCaptureFiles operation on the server.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		saveCaptureFiles(Arg1:string)list
			Args:
				args[0] is Arg1 (str): Directory for saving the captures

			Returns:
				list(str): A list of relative paths of all the captures saved

		saveCaptureFiles(Arg1:string, Arg2:string)list
			Args:
				args[0] is Arg1 (str): Directory for saving the captures
				args[1] is Arg2 (str): Suffix used for naming the capture files

			Returns:
				list(str): A list of relative paths of all the captures saved

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('saveCaptureFiles', payload=payload, response_object=None)

	def SaveConfig(self, *args, **kwargs):
		"""Executes the saveConfig operation on the server.

		Save the current configuration to a file.

		saveConfig(Arg1:href)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('saveConfig', payload=payload, response_object=None)

	def Scriptgen(self, *args, **kwargs):
		"""Executes the scriptgen operation on the server.

		Create a script of the current configuration.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		scriptgen()string

			Returns:
				str: A string value.

		DEPRECATED scriptgen(Arg1:href)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A valid output file handle from the ixNet writeTo command.

		DEPRECATED scriptgen(Arg1:href, Arg2:string)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
				args[1] is Arg2 (str): A string value.

		DEPRECATED scriptgen(Arg1:href, Arg2:string, Arg3:list)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
				args[1] is Arg2 (str): The type of script to create.
				args[2] is Arg3 (list(str)): The scriptgen options.

		DEPRECATED scriptgen(Arg1:href, Arg2:string, Arg3:list, Arg4:number, Arg5:number)
			Args:
				args[0] is Arg1 (obj(ixnetwork_restpy.files.Files)): A writeTo file handle.
				args[1] is Arg2 (str): A string value.
				args[2] is Arg3 (list(str)): A list of string values.
				args[3] is Arg4 (number): An integer.
				args[4] is Arg5 (number): An integer.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('scriptgen', payload=payload, response_object=None)

	def Select(self, *args, **kwargs):
		"""Executes the select operation on the server.

		Select nodes and properties from the hierarchy

		select(Selects:list)string
			Args:
				args[0] is Selects (list(dict(from:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(child:str,properties:list[str])]))): A list of select structures.Each select structure consists of a starting point in the hierarchy. This starting point must exist and is defined as the 'from' value.Properties for the 'from' value are optional and can be retrieved using the 'properties' list.To retrieve all properties specify the '*' wildcard. Regex is not supported in the 'properties' list.Individual nodes under the starting point can be retrieved. These are specified in the 'children' list.Each item in the children list contains a 'child' name, a list of 'properties' and a list of filters by which to reduce the result set.The 'child' name can be a single name or a regex.Properties that reference another object can have that object's content inlined by specifying inline children.Any child nodes below the object reference can be expanded as long as they are specified in the inline children.

			Returns:
				str: A json encoded string of result sets.The encoded string will contain a list of result sets with each select producing a result set.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('select', payload=payload, response_object=None)

	def SendArpAll(self):
		"""Executes the sendArpAll operation on the server.

		Send ARP for all interfaces.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('sendArpAll', payload=payload, response_object=None)

	def SendNsAll(self):
		"""Executes the sendNsAll operation on the server.

		Send neighbor solicitation to all interfaces.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('sendNsAll', payload=payload, response_object=None)

	def SendRsAll(self):
		"""Executes the sendRsAll operation on the server.

		Send router solicitation to all interfaces.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('sendRsAll', payload=payload, response_object=None)

	def SetGuardRailVersion(self, *args, **kwargs):
		"""Executes the setGuardRailVersion operation on the server.

		Disables GuardRail for TCL.

		setGuardRailVersion(Arg1:string)
			Args:
				args[0] is Arg1 (str): Deprecated.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('setGuardRailVersion', payload=payload, response_object=None)

	def SetLoggingLevel(self, *args, **kwargs):
		"""Executes the setLoggingLevel operation on the server.

		setLoggingLevel(Arg1:enum)
			Args:
				args[0] is Arg1 (str(kDebug|kError|kFatal|kInfo|kNothing|kWarn)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('setLoggingLevel', payload=payload, response_object=None)

	def SetPortTransmitDuration(self, *args, **kwargs):
		"""Executes the setPortTransmitDuration operation on the server.

		Set the port transmit duration.

		setPortTransmitDuration(Arg1:list)
			Args:
				args[0] is Arg1 (list(dict(arg1:number,arg2:list[str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport]]))): An array of structures. Each structure is an duration and a valid object reference.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('setPortTransmitDuration', payload=payload, response_object=None)

	def SetSnapshotSettingsToDefault(self, *args, **kwargs):
		"""Executes the SetSnapshotSettingsToDefault operation on the server.

		Set the settings of snapshot to default.

		SetSnapshotSettingsToDefault(Arg1:string)
			Args:
				args[0] is Arg1 (str): The setting name.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('SetSnapshotSettingsToDefault', payload=payload, response_object=None)

	def SetTapSettings(self):
		"""Executes the setTapSettings operation on the server.

		Send TAP Settings to IxServer for all the connected chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('setTapSettings', payload=payload, response_object=None)

	def StartAllProtocols(self, *args, **kwargs):
		"""Executes the startAllProtocols operation on the server.

		Starts all configured protocols under /vport/protocols, /vport/protocolStack and /topology

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		startAllProtocols()

		startAllProtocols(Arg1:enum)
			Args:
				args[0] is Arg1 (str(async|sync)): An enum indicating whether or not the exec will be executed synchronously or asynsynchronously

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('startAllProtocols', payload=payload, response_object=None)

	def StartCapture(self):
		"""Executes the startCapture operation on the server.

		The command to start the packet capture for the selected port or group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('startCapture', payload=payload, response_object=None)

	def StartTestConfiguration(self, *args, **kwargs):
		"""Executes the startTestConfiguration operation on the server.

		Starts the first Quick Test found in the current configuration.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		startTestConfiguration()

		startTestConfiguration(TestName:string)
			Args:
				args[0] is TestName (str): The name of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('startTestConfiguration', payload=payload, response_object=None)

	def StopAllProtocols(self, *args, **kwargs):
		"""Executes the stopAllProtocols operation on the server.

		Stops all configured protocols under /vport/protocols, /vport/protocolStack and /topology

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stopAllProtocols()

		stopAllProtocols(Arg1:enum)
			Args:
				args[0] is Arg1 (str(async|sync)): An enum indicating whether or not the exec will be executed synchronously or asynsynchronously

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stopAllProtocols', payload=payload, response_object=None)

	def StopCapture(self):
		"""Executes the stopCapture operation on the server.

		The command to stop the packet capture on the selected port or group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('stopCapture', payload=payload, response_object=None)

	def StopTestConfiguration(self):
		"""Executes the stopTestConfiguration operation on the server.

		Stops the currently running Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = None
		return self._execute('stopTestConfiguration', payload=payload, response_object=None)

	def SyncStatisticsStartTimeWithClientClock(self, *args, **kwargs):
		"""Executes the syncStatisticsStartTimeWithClientClock operation on the server.

		Make the statistics timestamps relative to the time on the client machine or relative to the test start.

		syncStatisticsStartTimeWithClientClock(Arg1:bool)
			Args:
				args[0] is Arg1 (bool): True = relative to system time, false = relative to test start.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('syncStatisticsStartTimeWithClientClock', payload=payload, response_object=None)

	def TakeViewCSVSnapshot(self, *args, **kwargs):
		"""Executes the TakeViewCSVSnapshot operation on the server.

		Performs Snapshot CSV on the given views.

		TakeViewCSVSnapshot(Arg1:list, Arg2:list)
			Args:
				args[0] is Arg1 (list(str)): A list of views for which to take a snapshot.
				args[1] is Arg2 (list(str)): A list of settings, given in the form of SettingName:SettingValue.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('TakeViewCSVSnapshot', payload=payload, response_object=None)

	def WaitForLicenseBroadcast(self, *args, **kwargs):
		"""Executes the waitForLicenseBroadcast operation on the server.

		Wait for the license broadcast to be complete.

		waitForLicenseBroadcast(Arg1:number)
			Args:
				args[0] is Arg1 (number): Seconds to wait.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = {}
		for i in range(len(args)): payload['Arg%s' % (i + 1)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('waitForLicenseBroadcast', payload=payload, response_object=None)
