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


class ResourceManager(Base):
	"""The ResourceManager class encapsulates a required resourceManager node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the ResourceManager property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'resourceManager'

	def __init__(self, parent):
		super(ResourceManager, self).__init__(parent)

	def ExportConfig(self, *args, **kwargs):
		"""Executes the exportConfig operation on the server.

		Export the entire configuration or fragments of it in a text based format

		exportConfig(Arg2:list, Arg3:bool, Arg4:enum)string
			Args:
				args[0] is Arg2 (list(str)): A list of xpaths each of which is a starting point in the configuration. The only supported xpath notation is by index or descendant-or-self:*. To export the entire configuration specify /descendant-or-self:*
				args[1] is Arg3 (bool): True to include attributes that are equal to the default in the export, false to exclude them
				args[2] is Arg4 (str(json)): The format of the exported configuration

			Returns:
				str: JSON configuration as a string

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('exportConfig', payload=payload, response_object=None)

	def ExportConfigFile(self, *args, **kwargs):
		"""Executes the exportConfigFile operation on the server.

		Export the entire configuration or fragments of it in a text based format

		exportConfigFile(Arg2:list, Arg3:bool, Arg4:enum, Arg5:href)
			Args:
				args[0] is Arg2 (list(str)): A list of xpaths each of which is a starting point in the configuration. The only supported xpath notation is by index or descendant-or-self:*. To export the entire configuration specify /descendant-or-self:*
				args[1] is Arg3 (bool): True to include attributes that are equal to the default in the export, false to exclude them
				args[2] is Arg4 (str(json)): The format of the exported configuration
				args[3] is Arg5 (obj(ixnetwork_restpy.files.Files)): The file object to write the configuration to

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('exportConfigFile', payload=payload, response_object=None)

	def ImportConfig(self, *args, **kwargs):
		"""Executes the importConfig operation on the server.

		Create or update the test tool configuration

		importConfig(Arg2:string, Arg3:bool)list
			Args:
				args[0] is Arg2 (str): The configuration as a string
				args[1] is Arg3 (bool): True to create a new configuration, false to update the current configuration

			Returns:
				list(str): A list of errors that occurred during import

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('importConfig', payload=payload, response_object=None)

	def ImportConfigFile(self, *args, **kwargs):
		"""Executes the importConfigFile operation on the server.

		Create or update the test tool configuration

		importConfigFile(Arg2:href, Arg3:bool)list
			Args:
				args[0] is Arg2 (obj(ixnetwork_restpy.files.Files)): The file object to read the configuration from
				args[1] is Arg3 (bool): True to create a new configuration, false to update the current configuration

			Returns:
				list(str): A list of errors that occurred during import

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('importConfigFile', payload=payload, response_object=None)
