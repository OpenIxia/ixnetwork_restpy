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
    The SwitchTables class encapsulates a list of switchTables resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchTables.find() method.
    The list can be managed by using the SwitchTables.add() and SwitchTables.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchTables'

    def __init__(self, parent):
        super(SwitchTables, self).__init__(parent)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_753da9f1e188445d11daa2a9c777c1ae.ApplyActions): An instance of the ApplyActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_753da9f1e188445d11daa2a9c777c1ae import ApplyActions
        return ApplyActions(self)._select()

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_0034e7f006a25730415fb046118d8f0f.ApplyActionsMiss): An instance of the ApplyActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_0034e7f006a25730415fb046118d8f0f import ApplyActionsMiss
        return ApplyActionsMiss(self)._select()

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_684d6c996e51caba7ed4ab607bc484cd.ApplySetField): An instance of the ApplySetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_684d6c996e51caba7ed4ab607bc484cd import ApplySetField
        return ApplySetField(self)._select()

    @property
    def ApplySetFieldMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_2c52fa41324c50f257cd7659e07ad887.ApplySetFieldMask): An instance of the ApplySetFieldMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_2c52fa41324c50f257cd7659e07ad887 import ApplySetFieldMask
        return ApplySetFieldMask(self)._select()

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_866d1ffcb6bf27961b44885ecc66fcf0.ApplySetFieldMiss): An instance of the ApplySetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_866d1ffcb6bf27961b44885ecc66fcf0 import ApplySetFieldMiss
        return ApplySetFieldMiss(self)._select()

    @property
    def ApplySetFieldMissMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_a9675d24d22663d3a37f927c3066d489.ApplySetFieldMissMask): An instance of the ApplySetFieldMissMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_a9675d24d22663d3a37f927c3066d489 import ApplySetFieldMissMask
        return ApplySetFieldMissMask(self)._select()

    @property
    def FeaturesSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_aa25a37a30889eaead8814aa942aec86.FeaturesSupported): An instance of the FeaturesSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_aa25a37a30889eaead8814aa942aec86 import FeaturesSupported
        return FeaturesSupported(self)._select()

    @property
    def Instruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_0d364e4e8a01a6abd031dd741dfdebc9.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_0d364e4e8a01a6abd031dd741dfdebc9 import Instruction
        return Instruction(self)._select()

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_a769629e477b31da22a676ba2f9ccbb0.InstructionMiss): An instance of the InstructionMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_a769629e477b31da22a676ba2f9ccbb0 import InstructionMiss
        return InstructionMiss(self)._select()

    @property
    def Match(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_a03c68a7ac0dc12f04d68c5cd5ceb00e.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_a03c68a7ac0dc12f04d68c5cd5ceb00e import Match
        return Match(self)._select()

    @property
    def MatchMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_8127195c3bd47737c106a1e8634be391.MatchMask): An instance of the MatchMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_8127195c3bd47737c106a1e8634be391 import MatchMask
        return MatchMask(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_cf5678cba6a90ceaa15815cc3fc04496.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_cf5678cba6a90ceaa15815cc3fc04496 import Wildcards
        return Wildcards(self)._select()

    @property
    def WildcardsMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_68c094d2bfa54aa7a14eeec32581c241.WildcardsMask): An instance of the WildcardsMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_68c094d2bfa54aa7a14eeec32581c241 import WildcardsMask
        return WildcardsMask(self)._select()

    @property
    def WildcardsSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_7faf5b5edcb26380f0795371d42c6c9e.WildcardsSupported): An instance of the WildcardsSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_7faf5b5edcb26380f0795371d42c6c9e import WildcardsSupported
        return WildcardsSupported(self)._select()

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_7796236eb5e11aead4d960bd9986b104.WriteActions): An instance of the WriteActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_7796236eb5e11aead4d960bd9986b104 import WriteActions
        return WriteActions(self)._select()

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_528f706ad8d07b813e4c1103e9154413.WriteActionsMiss): An instance of the WriteActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_528f706ad8d07b813e4c1103e9154413 import WriteActionsMiss
        return WriteActionsMiss(self)._select()

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_3985ce10db31ca110bfd234b49e52ae2.WriteSetField): An instance of the WriteSetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_3985ce10db31ca110bfd234b49e52ae2 import WriteSetField
        return WriteSetField(self)._select()

    @property
    def WriteSetFieldMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_03d92019240a1ead8d53db40b7309eb0.WriteSetFieldMask): An instance of the WriteSetFieldMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_03d92019240a1ead8d53db40b7309eb0 import WriteSetFieldMask
        return WriteSetFieldMask(self)._select()

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_7cd3d1265f5135d0949bfa1c5e7d3b36.WriteSetFieldMiss): An instance of the WriteSetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_7cd3d1265f5135d0949bfa1c5e7d3b36 import WriteSetFieldMiss
        return WriteSetFieldMiss(self)._select()

    @property
    def WriteSetFieldMissMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_b19dc5e5831be942bf542492b9f5154d.WriteSetFieldMissMask): An instance of the WriteSetFieldMissMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_b19dc5e5831be942bf542492b9f5154d import WriteSetFieldMissMask
        return WriteSetFieldMissMask(self)._select()

    @property
    def AutoConfigureNextTable(self):
        """
        Returns
        -------
        - bool: If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
        """
        return self._get_attribute('autoConfigureNextTable')
    @AutoConfigureNextTable.setter
    def AutoConfigureNextTable(self, value):
        self._set_attribute('autoConfigureNextTable', value)

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - str: Indicates the maximum number of entries supported. The default value is 10,000.
        """
        return self._get_attribute('maxEntries')
    @MaxEntries.setter
    def MaxEntries(self, value):
        self._set_attribute('maxEntries', value)

    @property
    def MetadataMatch(self):
        """
        Returns
        -------
        - str: Specify the bits of metadata which the table can match.
        """
        return self._get_attribute('metadataMatch')
    @MetadataMatch.setter
    def MetadataMatch(self, value):
        self._set_attribute('metadataMatch', value)

    @property
    def MetadataWrite(self):
        """
        Returns
        -------
        - str: Specify the bits of metadata which the table can write.
        """
        return self._get_attribute('metadataWrite')
    @MetadataWrite.setter
    def MetadataWrite(self, value):
        self._set_attribute('metadataWrite', value)

    @property
    def NextTable(self):
        """
        Returns
        -------
        - str: Specify the next table property.
        """
        return self._get_attribute('nextTable')
    @NextTable.setter
    def NextTable(self, value):
        self._set_attribute('nextTable', value)

    @property
    def NextTableMiss(self):
        """
        Returns
        -------
        - str: Specify the next table-miss property.
        """
        return self._get_attribute('nextTableMiss')
    @NextTableMiss.setter
    def NextTableMiss(self, value):
        self._set_attribute('nextTableMiss', value)

    @property
    def NumberOfTables(self):
        """
        Returns
        -------
        - number: Indicates the number of entries in the table range.
        """
        return self._get_attribute('numberOfTables')
    @NumberOfTables.setter
    def NumberOfTables(self, value):
        self._set_attribute('numberOfTables', value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - str: Indicates the Identifier of the switch table.
        """
        return self._get_attribute('tableId')
    @TableId.setter
    def TableId(self, value):
        self._set_attribute('tableId', value)

    @property
    def TableName(self):
        """
        Returns
        -------
        - str: Indicates the name of the switch table.
        """
        return self._get_attribute('tableName')
    @TableName.setter
    def TableName(self, value):
        self._set_attribute('tableName', value)

    def update(self, AutoConfigureNextTable=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, NumberOfTables=None, TableId=None, TableName=None):
        """Updates switchTables resource on the server.

        Args
        ----
        - AutoConfigureNextTable (bool): If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
        - MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
        - MetadataMatch (str): Specify the bits of metadata which the table can match.
        - MetadataWrite (str): Specify the bits of metadata which the table can write.
        - NextTable (str): Specify the next table property.
        - NextTableMiss (str): Specify the next table-miss property.
        - NumberOfTables (number): Indicates the number of entries in the table range.
        - TableId (str): Indicates the Identifier of the switch table.
        - TableName (str): Indicates the name of the switch table.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AutoConfigureNextTable=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, NumberOfTables=None, TableId=None, TableName=None):
        """Adds a new switchTables resource on the server and adds it to the container.

        Args
        ----
        - AutoConfigureNextTable (bool): If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
        - MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
        - MetadataMatch (str): Specify the bits of metadata which the table can match.
        - MetadataWrite (str): Specify the bits of metadata which the table can write.
        - NextTable (str): Specify the next table property.
        - NextTableMiss (str): Specify the next table-miss property.
        - NumberOfTables (number): Indicates the number of entries in the table range.
        - TableId (str): Indicates the Identifier of the switch table.
        - TableName (str): Indicates the name of the switch table.

        Returns
        -------
        - self: This instance with all currently retrieved switchTables resources using find and the newly added switchTables resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained switchTables resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoConfigureNextTable=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, NumberOfTables=None, TableId=None, TableName=None):
        """Finds and retrieves switchTables resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchTables resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchTables resources from the server.

        Args
        ----
        - AutoConfigureNextTable (bool): If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
        - MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
        - MetadataMatch (str): Specify the bits of metadata which the table can match.
        - MetadataWrite (str): Specify the bits of metadata which the table can write.
        - NextTable (str): Specify the next table property.
        - NextTableMiss (str): Specify the next table-miss property.
        - NumberOfTables (number): Indicates the number of entries in the table range.
        - TableId (str): Indicates the Identifier of the switch table.
        - TableName (str): Indicates the name of the switch table.

        Returns
        -------
        - self: This instance with matching switchTables resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of switchTables data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchTables resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
