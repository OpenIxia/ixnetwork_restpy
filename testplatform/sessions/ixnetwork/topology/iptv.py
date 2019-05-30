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


class Iptv(Base):
	"""The Iptv class encapsulates a required iptv node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Iptv property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'iptv'

	def __init__(self, parent):
		super(Iptv, self).__init__(parent)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableGeneralQueryResponse(self):
		"""If enabled, General Query Response is send.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableGeneralQueryResponse')

	@property
	def EnableGroupSpecificQueryResponse(self):
		"""If enabled, Group Specific Response is sent

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableGroupSpecificQueryResponse')

	@property
	def JoinLatencyThreshold(self):
		"""The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('joinLatencyThreshold')

	@property
	def LeaveLatencyThreshold(self):
		"""The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('leaveLatencyThreshold')

	@property
	def LogAllTimestamps(self):
		"""If enabled, all the captured timestamps for Join and Leave are saved to a log file.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('logAllTimestamps')

	@property
	def LogFailureTimestamps(self):
		"""If enabled, the timestamps for Join and Leave failures are saved to a log file.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('logFailureTimestamps')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NumChannelChangesBeforeView(self):
		"""Number of channels to change before stopping on a channel and watching it for View Duration.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numChannelChangesBeforeView')

	@property
	def State(self):
		"""Indicates the state IPTV

		Returns:
			list(str[notStarted|started])
		"""
		return self._get_attribute('state')

	@property
	def StbLeaveJoinDelay(self):
		"""Time in milliseconds between sending a Leave for the current channel and Join for the next channel.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('stbLeaveJoinDelay')

	@property
	def ViewDuration(self):
		"""Specifies the time in milliseconds to view the last channel.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('viewDuration')

	@property
	def ZapBehavior(self):
		"""Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('zapBehavior')

	@property
	def ZapDirection(self):
		"""Specifies the direction of changing channels.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('zapDirection')

	@property
	def ZapInterval(self):
		"""Interval in milliseconds between channel changes based on the selected type.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('zapInterval')

	@property
	def ZapIntervalType(self):
		"""Specifies the wait interval type before changing the channels.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('zapIntervalType')

	def update(self, Name=None):
		"""Updates a child instance of iptv on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def get_device_ids(self, PortNames=None, EnableGeneralQueryResponse=None, EnableGroupSpecificQueryResponse=None, JoinLatencyThreshold=None, LeaveLatencyThreshold=None, LogAllTimestamps=None, LogFailureTimestamps=None, NumChannelChangesBeforeView=None, StbLeaveJoinDelay=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
		"""Base class infrastructure that gets a list of iptv device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			EnableGeneralQueryResponse (str): optional regex of enableGeneralQueryResponse
			EnableGroupSpecificQueryResponse (str): optional regex of enableGroupSpecificQueryResponse
			JoinLatencyThreshold (str): optional regex of joinLatencyThreshold
			LeaveLatencyThreshold (str): optional regex of leaveLatencyThreshold
			LogAllTimestamps (str): optional regex of logAllTimestamps
			LogFailureTimestamps (str): optional regex of logFailureTimestamps
			NumChannelChangesBeforeView (str): optional regex of numChannelChangesBeforeView
			StbLeaveJoinDelay (str): optional regex of stbLeaveJoinDelay
			ViewDuration (str): optional regex of viewDuration
			ZapBehavior (str): optional regex of zapBehavior
			ZapDirection (str): optional regex of zapDirection
			ZapInterval (str): optional regex of zapInterval
			ZapIntervalType (str): optional regex of zapIntervalType

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

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

	def StartIptv(self, *args, **kwargs):
		"""Executes the startIptv operation on the server.

		Start IPTV

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		startIptv()

		startIptv(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		startIptv(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		startIptv(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the IPTV grid An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('startIptv', payload=payload, response_object=None)

	def StopIptv(self, *args, **kwargs):
		"""Executes the stopIptv operation on the server.

		Stop IPTV

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stopIptv()

		stopIptv(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stopIptv(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		stopIptv(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the IPTV grid An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stopIptv', payload=payload, response_object=None)
