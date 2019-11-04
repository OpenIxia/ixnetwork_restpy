# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class TableFeaturesLearnedInformation(Base):
	"""NOT DEFINED
	The TableFeaturesLearnedInformation class encapsulates a list of tableFeaturesLearnedInformation resources that is managed by the system.
	A list of resources can be retrieved from the server using the TableFeaturesLearnedInformation.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'tableFeaturesLearnedInformation'

	def __init__(self, parent):
		super(TableFeaturesLearnedInformation, self).__init__(parent)

	@property
	def ApplyActionsLearnedInfo(self):
		"""An instance of the ApplyActionsLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_chbseufjdglvbnnmzwfybmvksw5mbw.ApplyActionsLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_chbseufjdglvbnnmzwfybmvksw5mbw import ApplyActionsLearnedInfo
		return ApplyActionsLearnedInfo(self)

	@property
	def ApplyActionsMissLearnedInfo(self):
		"""An instance of the ApplyActionsMissLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_ufjdglvbnnnaxnztgvhcm5lzeluzm8.ApplyActionsMissLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_ufjdglvbnnnaxnztgvhcm5lzeluzm8 import ApplyActionsMissLearnedInfo
		return ApplyActionsMissLearnedInfo(self)

	@property
	def ApplySetFieldLearnedInfo(self):
		"""An instance of the ApplySetFieldLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_hbsevnldezpzwxktgvhcm5lzeluzm8.ApplySetFieldLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_hbsevnldezpzwxktgvhcm5lzeluzm8 import ApplySetFieldLearnedInfo
		return ApplySetFieldLearnedInfo(self)

	@property
	def ApplySetFieldMissLearnedInfo(self):
		"""An instance of the ApplySetFieldMissLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_nldezpzwxktwlzc0xlyxjuzwrjbmzv.ApplySetFieldMissLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_nldezpzwxktwlzc0xlyxjuzwrjbmzv import ApplySetFieldMissLearnedInfo
		return ApplySetFieldMissLearnedInfo(self)

	@property
	def ExperimenterLearnedInfo(self):
		"""An instance of the ExperimenterLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenterlearnedinfo_ehblcmltzw50zxjmzwfybmvksw5mbw.ExperimenterLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenterlearnedinfo_ehblcmltzw50zxjmzwfybmvksw5mbw import ExperimenterLearnedInfo
		return ExperimenterLearnedInfo(self)

	@property
	def ExperimenterMissLearnedInfo(self):
		"""An instance of the ExperimenterMissLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimentermisslearnedinfo_mltzw50zxjnaxnztgvhcm5lzeluzm8.ExperimenterMissLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimentermisslearnedinfo_mltzw50zxjnaxnztgvhcm5lzeluzm8 import ExperimenterMissLearnedInfo
		return ExperimenterMissLearnedInfo(self)

	@property
	def InstructionLearnedInfo(self):
		"""An instance of the InstructionLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_9pbnn0cnvjdglvbkxlyxjuzwrjbmzv.InstructionLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_9pbnn0cnvjdglvbkxlyxjuzwrjbmzv import InstructionLearnedInfo
		return InstructionLearnedInfo(self)

	@property
	def InstructionMissLearnedInfo(self):
		"""An instance of the InstructionMissLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_cnvjdglvbk1pc3nmzwfybmvksw5mbw.InstructionMissLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_cnvjdglvbk1pc3nmzwfybmvksw5mbw import InstructionMissLearnedInfo
		return InstructionMissLearnedInfo(self)

	@property
	def MatchLearnedInfo(self):
		"""An instance of the MatchLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_1hdglvbi9tyxrjaexlyxjuzwrjbmzv.MatchLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_1hdglvbi9tyxrjaexlyxjuzwrjbmzv import MatchLearnedInfo
		return MatchLearnedInfo(self)

	@property
	def NextTableLearnedInfo(self):
		"""An instance of the NextTableLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_bi9uzxh0vgfibgvmzwfybmvksw5mbw.NextTableLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_bi9uzxh0vgfibgvmzwfybmvksw5mbw import NextTableLearnedInfo
		return NextTableLearnedInfo(self)

	@property
	def NextTableMissLearnedInfo(self):
		"""An instance of the NextTableMissLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_xh0vgfibgvnaxnztgvhcm5lzeluzm8.NextTableMissLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_xh0vgfibgvnaxnztgvhcm5lzeluzm8 import NextTableMissLearnedInfo
		return NextTableMissLearnedInfo(self)

	@property
	def WildcardsLearnedInfo(self):
		"""An instance of the WildcardsLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_bi93awxky2fyzhnmzwfybmvksw5mbw.WildcardsLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_bi93awxky2fyzhnmzwfybmvksw5mbw import WildcardsLearnedInfo
		return WildcardsLearnedInfo(self)

	@property
	def WriteActionsLearnedInfo(self):
		"""An instance of the WriteActionsLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_cml0zufjdglvbnnmzwfybmvksw5mbw.WriteActionsLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_cml0zufjdglvbnnmzwfybmvksw5mbw import WriteActionsLearnedInfo
		return WriteActionsLearnedInfo(self)

	@property
	def WriteActionsMissLearnedInfo(self):
		"""An instance of the WriteActionsMissLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_ufjdglvbnnnaxnztgvhcm5lzeluzm8.WriteActionsMissLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_ufjdglvbnnnaxnztgvhcm5lzeluzm8 import WriteActionsMissLearnedInfo
		return WriteActionsMissLearnedInfo(self)

	@property
	def WriteSetFieldLearnedInfo(self):
		"""An instance of the WriteSetFieldLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_ml0zvnldezpzwxktgvhcm5lzeluzm8.WriteSetFieldLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_ml0zvnldezpzwxktgvhcm5lzeluzm8 import WriteSetFieldLearnedInfo
		return WriteSetFieldLearnedInfo(self)

	@property
	def WriteSetFieldMissLearnedInfo(self):
		"""An instance of the WriteSetFieldMissLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_nldezpzwxktwlzc0xlyxjuzwrjbmzv.WriteSetFieldMissLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_nldezpzwxktwlzc0xlyxjuzwrjbmzv import WriteSetFieldMissLearnedInfo
		return WriteSetFieldMissLearnedInfo(self)

	@property
	def ApplyActions(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('applyActions')

	@property
	def ApplyActionsMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('applyActionsMiss')

	@property
	def ApplySetField(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('applySetField')

	@property
	def ApplySetFieldMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('applySetFieldMiss')

	@property
	def Config(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('config')

	@property
	def DataPathId(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('dataPathId')

	@property
	def DataPathIdAsHex(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('dataPathIdAsHex')

	@property
	def ErrorCode(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('errorCode')

	@property
	def ErrorType(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('errorType')

	@property
	def Experimenter(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('experimenter')

	@property
	def ExperimenterMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('experimenterMiss')

	@property
	def Instruction(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('instruction')

	@property
	def InstructionMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('instructionMiss')

	@property
	def Latency(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('latency')

	@property
	def LocalIp(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('localIp')

	@property
	def Match(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('match')

	@property
	def MaxEntries(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxEntries')

	@property
	def MetadataMatch(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('metadataMatch')

	@property
	def MetadataWrite(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('metadataWrite')

	@property
	def Name(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('name')

	@property
	def NegotiatedVersion(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('negotiatedVersion')

	@property
	def NextTable(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('nextTable')

	@property
	def NextTableMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('nextTableMiss')

	@property
	def RemoteIp(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('remoteIp')

	@property
	def ReplyState(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('replyState')

	@property
	def TableId(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('tableId')

	@property
	def WildCards(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('wildCards')

	@property
	def WriteActions(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('writeActions')

	@property
	def WriteActionsMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('writeActionsMiss')

	@property
	def WriteSetField(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('writeSetField')

	@property
	def WriteSetFieldMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('writeSetFieldMiss')

	def find(self, ApplyActions=None, ApplyActionsMiss=None, ApplySetField=None, ApplySetFieldMiss=None, Config=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, Experimenter=None, ExperimenterMiss=None, Instruction=None, InstructionMiss=None, Latency=None, LocalIp=None, Match=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, Name=None, NegotiatedVersion=None, NextTable=None, NextTableMiss=None, RemoteIp=None, ReplyState=None, TableId=None, WildCards=None, WriteActions=None, WriteActionsMiss=None, WriteSetField=None, WriteSetFieldMiss=None):
		"""Finds and retrieves tableFeaturesLearnedInformation data from the server.

		All named parameters support regex and can be used to selectively retrieve tableFeaturesLearnedInformation data from the server.
		By default the find method takes no parameters and will retrieve all tableFeaturesLearnedInformation data from the server.

		Args:
			ApplyActions (str): NOT DEFINED
			ApplyActionsMiss (str): NOT DEFINED
			ApplySetField (str): NOT DEFINED
			ApplySetFieldMiss (str): NOT DEFINED
			Config (number): NOT DEFINED
			DataPathId (str): NOT DEFINED
			DataPathIdAsHex (str): NOT DEFINED
			ErrorCode (str): NOT DEFINED
			ErrorType (str): NOT DEFINED
			Experimenter (str): NOT DEFINED
			ExperimenterMiss (str): NOT DEFINED
			Instruction (str): NOT DEFINED
			InstructionMiss (str): NOT DEFINED
			Latency (number): NOT DEFINED
			LocalIp (str): NOT DEFINED
			Match (str): NOT DEFINED
			MaxEntries (number): NOT DEFINED
			MetadataMatch (str): NOT DEFINED
			MetadataWrite (str): NOT DEFINED
			Name (str): NOT DEFINED
			NegotiatedVersion (str): NOT DEFINED
			NextTable (str): NOT DEFINED
			NextTableMiss (str): NOT DEFINED
			RemoteIp (str): NOT DEFINED
			ReplyState (str): NOT DEFINED
			TableId (str): NOT DEFINED
			WildCards (str): NOT DEFINED
			WriteActions (str): NOT DEFINED
			WriteActionsMiss (str): NOT DEFINED
			WriteSetField (str): NOT DEFINED
			WriteSetFieldMiss (str): NOT DEFINED

		Returns:
			self: This instance with matching tableFeaturesLearnedInformation data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of tableFeaturesLearnedInformation data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the tableFeaturesLearnedInformation data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
