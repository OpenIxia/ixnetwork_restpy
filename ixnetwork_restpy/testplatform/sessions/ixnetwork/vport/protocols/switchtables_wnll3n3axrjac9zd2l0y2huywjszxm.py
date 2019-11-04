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


class SwitchTables(Base):
	"""This object allows to define the configuration parameters for the switch tables.
	The SwitchTables class encapsulates a list of switchTables resources that is be managed by the user.
	A list of resources can be retrieved from the server using the SwitchTables.find() method.
	The list can be managed by the user by using the SwitchTables.add() and SwitchTables.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'switchTables'

	def __init__(self, parent):
		super(SwitchTables, self).__init__(parent)

	@property
	def ApplyActions(self):
		"""An instance of the ApplyActions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_l0y2huywjszxmvyxbwbhlby3rpb25z.ApplyActions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_l0y2huywjszxmvyxbwbhlby3rpb25z import ApplyActions
		return ApplyActions(self)._select()

	@property
	def ApplyActionsMiss(self):
		"""An instance of the ApplyActionsMiss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_ywjszxmvyxbwbhlby3rpb25ztwlzcw.ApplyActionsMiss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_ywjszxmvyxbwbhlby3rpb25ztwlzcw import ApplyActionsMiss
		return ApplyActionsMiss(self)._select()

	@property
	def ApplySetField(self):
		"""An instance of the ApplySetField class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_y2huywjszxmvyxbwbhltzxrgawvsza.ApplySetField)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_y2huywjszxmvyxbwbhltzxrgawvsza import ApplySetField
		return ApplySetField(self)._select()

	@property
	def ApplySetFieldMask(self):
		"""An instance of the ApplySetFieldMask class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_wjszxmvyxbwbhltzxrgawvsze1hc2s.ApplySetFieldMask)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_wjszxmvyxbwbhltzxrgawvsze1hc2s import ApplySetFieldMask
		return ApplySetFieldMask(self)._select()

	@property
	def ApplySetFieldMiss(self):
		"""An instance of the ApplySetFieldMiss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_wjszxmvyxbwbhltzxrgawvsze1pc3m.ApplySetFieldMiss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_wjszxmvyxbwbhltzxrgawvsze1pc3m import ApplySetFieldMiss
		return ApplySetFieldMiss(self)._select()

	@property
	def ApplySetFieldMissMask(self):
		"""An instance of the ApplySetFieldMissMask class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_mvyxbwbhltzxrgawvsze1pc3nnyxnr.ApplySetFieldMissMask)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_mvyxbwbhltzxrgawvsze1pc3nnyxnr import ApplySetFieldMissMask
		return ApplySetFieldMissMask(self)._select()

	@property
	def FeaturesSupported(self):
		"""An instance of the FeaturesSupported class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_wjszxmvzmvhdhvyzxntdxbwb3j0zwq.FeaturesSupported)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_wjszxmvzmvhdhvyzxntdxbwb3j0zwq import FeaturesSupported
		return FeaturesSupported(self)._select()

	@property
	def Instruction(self):
		"""An instance of the Instruction class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_2l0y2huywjszxmvaw5zdhj1y3rpb24.Instruction)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_2l0y2huywjszxmvaw5zdhj1y3rpb24 import Instruction
		return Instruction(self)._select()

	@property
	def InstructionMiss(self):
		"""An instance of the InstructionMiss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_huywjszxmvaw5zdhj1y3rpb25naxnz.InstructionMiss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_huywjszxmvaw5zdhj1y3rpb25naxnz import InstructionMiss
		return InstructionMiss(self)._select()

	@property
	def Match(self):
		"""An instance of the Match class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_xrjac9zd2l0y2huywjszxmvbwf0y2g.Match)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_xrjac9zd2l0y2huywjszxmvbwf0y2g import Match
		return Match(self)._select()

	@property
	def MatchMask(self):
		"""An instance of the MatchMask class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_9zd2l0y2huywjszxmvbwf0y2hnyxnr.MatchMask)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_9zd2l0y2huywjszxmvbwf0y2hnyxnr import MatchMask
		return MatchMask(self)._select()

	@property
	def Wildcards(self):
		"""An instance of the Wildcards class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_9zd2l0y2huywjszxmvd2lszgnhcmrz.Wildcards)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_9zd2l0y2huywjszxmvd2lszgnhcmrz import Wildcards
		return Wildcards(self)._select()

	@property
	def WildcardsMask(self):
		"""An instance of the WildcardsMask class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_y2huywjszxmvd2lszgnhcmrztwfzaw.WildcardsMask)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_y2huywjszxmvd2lszgnhcmrztwfzaw import WildcardsMask
		return WildcardsMask(self)._select()

	@property
	def WildcardsSupported(self):
		"""An instance of the WildcardsSupported class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_jszxmvd2lszgnhcmrzu3vwcg9ydgvk.WildcardsSupported)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_jszxmvd2lszgnhcmrzu3vwcg9ydgvk import WildcardsSupported
		return WildcardsSupported(self)._select()

	@property
	def WriteActions(self):
		"""An instance of the WriteActions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_l0y2huywjszxmvd3jpdgvby3rpb25z.WriteActions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_l0y2huywjszxmvd3jpdgvby3rpb25z import WriteActions
		return WriteActions(self)._select()

	@property
	def WriteActionsMiss(self):
		"""An instance of the WriteActionsMiss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_ywjszxmvd3jpdgvby3rpb25ztwlzcw.WriteActionsMiss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_ywjszxmvd3jpdgvby3rpb25ztwlzcw import WriteActionsMiss
		return WriteActionsMiss(self)._select()

	@property
	def WriteSetField(self):
		"""An instance of the WriteSetField class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_y2huywjszxmvd3jpdgvtzxrgawvsza.WriteSetField)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_y2huywjszxmvd3jpdgvtzxrgawvsza import WriteSetField
		return WriteSetField(self)._select()

	@property
	def WriteSetFieldMask(self):
		"""An instance of the WriteSetFieldMask class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_wjszxmvd3jpdgvtzxrgawvsze1hc2s.WriteSetFieldMask)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_wjszxmvd3jpdgvtzxrgawvsze1hc2s import WriteSetFieldMask
		return WriteSetFieldMask(self)._select()

	@property
	def WriteSetFieldMiss(self):
		"""An instance of the WriteSetFieldMiss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_wjszxmvd3jpdgvtzxrgawvsze1pc3m.WriteSetFieldMiss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_wjszxmvd3jpdgvtzxrgawvsze1pc3m import WriteSetFieldMiss
		return WriteSetFieldMiss(self)._select()

	@property
	def WriteSetFieldMissMask(self):
		"""An instance of the WriteSetFieldMissMask class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_mvd3jpdgvtzxrgawvsze1pc3nnyxnr.WriteSetFieldMissMask)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_mvd3jpdgvtzxrgawvsze1pc3nnyxnr import WriteSetFieldMissMask
		return WriteSetFieldMissMask(self)._select()

	@property
	def AutoConfigureNextTable(self):
		"""If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.

		Returns:
			bool
		"""
		return self._get_attribute('autoConfigureNextTable')
	@AutoConfigureNextTable.setter
	def AutoConfigureNextTable(self, value):
		self._set_attribute('autoConfigureNextTable', value)

	@property
	def MaxEntries(self):
		"""Indicates the maximum number of entries supported. The default value is 10,000.

		Returns:
			str
		"""
		return self._get_attribute('maxEntries')
	@MaxEntries.setter
	def MaxEntries(self, value):
		self._set_attribute('maxEntries', value)

	@property
	def MetadataMatch(self):
		"""Specify the bits of metadata which the table can match.

		Returns:
			str
		"""
		return self._get_attribute('metadataMatch')
	@MetadataMatch.setter
	def MetadataMatch(self, value):
		self._set_attribute('metadataMatch', value)

	@property
	def MetadataWrite(self):
		"""Specify the bits of metadata which the table can write.

		Returns:
			str
		"""
		return self._get_attribute('metadataWrite')
	@MetadataWrite.setter
	def MetadataWrite(self, value):
		self._set_attribute('metadataWrite', value)

	@property
	def NextTable(self):
		"""Specify the next table property.

		Returns:
			str
		"""
		return self._get_attribute('nextTable')
	@NextTable.setter
	def NextTable(self, value):
		self._set_attribute('nextTable', value)

	@property
	def NextTableMiss(self):
		"""Specify the next table-miss property.

		Returns:
			str
		"""
		return self._get_attribute('nextTableMiss')
	@NextTableMiss.setter
	def NextTableMiss(self, value):
		self._set_attribute('nextTableMiss', value)

	@property
	def NumberOfTables(self):
		"""Indicates the number of entries in the table range.

		Returns:
			number
		"""
		return self._get_attribute('numberOfTables')
	@NumberOfTables.setter
	def NumberOfTables(self, value):
		self._set_attribute('numberOfTables', value)

	@property
	def TableId(self):
		"""Indicates the Identifier of the switch table.

		Returns:
			str
		"""
		return self._get_attribute('tableId')
	@TableId.setter
	def TableId(self, value):
		self._set_attribute('tableId', value)

	@property
	def TableName(self):
		"""Indicates the name of the switch table.

		Returns:
			str
		"""
		return self._get_attribute('tableName')
	@TableName.setter
	def TableName(self, value):
		self._set_attribute('tableName', value)

	def update(self, AutoConfigureNextTable=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, NumberOfTables=None, TableId=None, TableName=None):
		"""Updates a child instance of switchTables on the server.

		Args:
			AutoConfigureNextTable (bool): If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
			MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
			MetadataMatch (str): Specify the bits of metadata which the table can match.
			MetadataWrite (str): Specify the bits of metadata which the table can write.
			NextTable (str): Specify the next table property.
			NextTableMiss (str): Specify the next table-miss property.
			NumberOfTables (number): Indicates the number of entries in the table range.
			TableId (str): Indicates the Identifier of the switch table.
			TableName (str): Indicates the name of the switch table.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, AutoConfigureNextTable=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, NumberOfTables=None, TableId=None, TableName=None):
		"""Adds a new switchTables node on the server and retrieves it in this instance.

		Args:
			AutoConfigureNextTable (bool): If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
			MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
			MetadataMatch (str): Specify the bits of metadata which the table can match.
			MetadataWrite (str): Specify the bits of metadata which the table can write.
			NextTable (str): Specify the next table property.
			NextTableMiss (str): Specify the next table-miss property.
			NumberOfTables (number): Indicates the number of entries in the table range.
			TableId (str): Indicates the Identifier of the switch table.
			TableName (str): Indicates the name of the switch table.

		Returns:
			self: This instance with all currently retrieved switchTables data using find and the newly added switchTables data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the switchTables data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AutoConfigureNextTable=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, NumberOfTables=None, TableId=None, TableName=None):
		"""Finds and retrieves switchTables data from the server.

		All named parameters support regex and can be used to selectively retrieve switchTables data from the server.
		By default the find method takes no parameters and will retrieve all switchTables data from the server.

		Args:
			AutoConfigureNextTable (bool): If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
			MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
			MetadataMatch (str): Specify the bits of metadata which the table can match.
			MetadataWrite (str): Specify the bits of metadata which the table can write.
			NextTable (str): Specify the next table property.
			NextTableMiss (str): Specify the next table-miss property.
			NumberOfTables (number): Indicates the number of entries in the table range.
			TableId (str): Indicates the Identifier of the switch table.
			TableName (str): Indicates the name of the switch table.

		Returns:
			self: This instance with matching switchTables data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of switchTables data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the switchTables data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
