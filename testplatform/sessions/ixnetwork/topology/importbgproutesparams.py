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


class ImportBgpRoutesParams(Base):
	"""The ImportBgpRoutesParams class encapsulates a required importBgpRoutesParams node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the ImportBgpRoutesParams property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'importBgpRoutesParams'

	def __init__(self, parent):
		super(ImportBgpRoutesParams, self).__init__(parent)

	@property
	def BestRoutes(self):
		"""Import only the best routes (provided route file has this information).

		Returns:
			bool
		"""
		return self._get_attribute('bestRoutes')
	@BestRoutes.setter
	def BestRoutes(self, value):
		self._set_attribute('bestRoutes', value)

	@property
	def DataFile(self):
		"""Select source file having route information.

		Returns:
			obj(ixnetwork_restpy.files.Files)
		"""
		return self._get_attribute('dataFile')
	@DataFile.setter
	def DataFile(self, value):
		self._set_attribute('dataFile', value)

	@property
	def FileType(self):
		"""Import routes file type. Route import may fail in file type is not matching with the file being imported.

		Returns:
			str(cisco|csv|juniper)
		"""
		return self._get_attribute('fileType')
	@FileType.setter
	def FileType(self, value):
		self._set_attribute('fileType', value)

	@property
	def NextHop(self):
		"""Option for setting Next Hop modification type.

		Returns:
			str(overwriteTestersAddress|preserveFromFile)
		"""
		return self._get_attribute('nextHop')
	@NextHop.setter
	def NextHop(self, value):
		self._set_attribute('nextHop', value)

	@property
	def RouteDistributionType(self):
		"""Option to specify distribution type, for distributing imported routes across all BGP Peer. Options: Round-Robin, for allocating routes sequentially, and Replicate, for allocating all routes to each Peer.

		Returns:
			str(replicate|roundRobin)
		"""
		return self._get_attribute('routeDistributionType')
	@RouteDistributionType.setter
	def RouteDistributionType(self, value):
		self._set_attribute('routeDistributionType', value)

	def update(self, BestRoutes=None, DataFile=None, FileType=None, NextHop=None, RouteDistributionType=None):
		"""Updates a child instance of importBgpRoutesParams on the server.

		Args:
			BestRoutes (bool): Import only the best routes (provided route file has this information).
			DataFile (obj(ixnetwork_restpy.files.Files)): Select source file having route information.
			FileType (str(cisco|csv|juniper)): Import routes file type. Route import may fail in file type is not matching with the file being imported.
			NextHop (str(overwriteTestersAddress|preserveFromFile)): Option for setting Next Hop modification type.
			RouteDistributionType (str(replicate|roundRobin)): Option to specify distribution type, for distributing imported routes across all BGP Peer. Options: Round-Robin, for allocating routes sequentially, and Replicate, for allocating all routes to each Peer.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		fetchAndUpdateConfigFromCloud(Mode:string)
			Args:
				args[0] is Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

	def ImportBgpRoutes(self):
		"""Executes the importBgpRoutes operation on the server.

		Import IPv4 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('importBgpRoutes', payload=payload, response_object=None)
