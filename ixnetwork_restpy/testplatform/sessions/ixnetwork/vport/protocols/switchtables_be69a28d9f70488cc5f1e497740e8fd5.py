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


class SwitchTables(Base):
    """This object allows to define the configuration parameters for the switch tables.
    The SwitchTables class encapsulates a list of switchTables resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchTables.find() method.
    The list can be managed by using the SwitchTables.add() and SwitchTables.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchTables'
    _SDM_ATT_MAP = {
        'AutoConfigureNextTable': 'autoConfigureNextTable',
        'MaxEntries': 'maxEntries',
        'MetadataMatch': 'metadataMatch',
        'MetadataWrite': 'metadataWrite',
        'NextTable': 'nextTable',
        'NextTableMiss': 'nextTableMiss',
        'NumberOfTables': 'numberOfTables',
        'TableId': 'tableId',
        'TableName': 'tableName',
    }

    def __init__(self, parent):
        super(SwitchTables, self).__init__(parent)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_f430716c835ec2dce739b00212ff871f.ApplyActions): An instance of the ApplyActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_f430716c835ec2dce739b00212ff871f import ApplyActions
        return ApplyActions(self)._select()

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_3cf07c7df561bc375b2952a23f13aa2c.ApplyActionsMiss): An instance of the ApplyActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_3cf07c7df561bc375b2952a23f13aa2c import ApplyActionsMiss
        return ApplyActionsMiss(self)._select()

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_27ccc386a8f839f0f862705bd39aaca8.ApplySetField): An instance of the ApplySetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_27ccc386a8f839f0f862705bd39aaca8 import ApplySetField
        return ApplySetField(self)._select()

    @property
    def ApplySetFieldMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_47d6ed5736991ff7d6a73f1525043f50.ApplySetFieldMask): An instance of the ApplySetFieldMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_47d6ed5736991ff7d6a73f1525043f50 import ApplySetFieldMask
        return ApplySetFieldMask(self)._select()

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_caab5fbd149b7f6b97cf43dcce17840c.ApplySetFieldMiss): An instance of the ApplySetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_caab5fbd149b7f6b97cf43dcce17840c import ApplySetFieldMiss
        return ApplySetFieldMiss(self)._select()

    @property
    def ApplySetFieldMissMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_24778fe53673d35fd3e3ea07cf538fc0.ApplySetFieldMissMask): An instance of the ApplySetFieldMissMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_24778fe53673d35fd3e3ea07cf538fc0 import ApplySetFieldMissMask
        return ApplySetFieldMissMask(self)._select()

    @property
    def FeaturesSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_157053473402b6f9ddb28b8af708b5cd.FeaturesSupported): An instance of the FeaturesSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_157053473402b6f9ddb28b8af708b5cd import FeaturesSupported
        return FeaturesSupported(self)._select()

    @property
    def Instruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_2ea701c64dd7c771b8df298ca6f96902.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_2ea701c64dd7c771b8df298ca6f96902 import Instruction
        return Instruction(self)._select()

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_59c91d8e6597b03e471411340a9fa331.InstructionMiss): An instance of the InstructionMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_59c91d8e6597b03e471411340a9fa331 import InstructionMiss
        return InstructionMiss(self)._select()

    @property
    def Match(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_1c447af57b9d3fad71f4a7cbe12a942b.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_1c447af57b9d3fad71f4a7cbe12a942b import Match
        return Match(self)._select()

    @property
    def MatchMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_fd4e73e7cc86e967c8c209c958229f70.MatchMask): An instance of the MatchMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_fd4e73e7cc86e967c8c209c958229f70 import MatchMask
        return MatchMask(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_5513fddbbb965f8abc36036de70eab7a.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_5513fddbbb965f8abc36036de70eab7a import Wildcards
        return Wildcards(self)._select()

    @property
    def WildcardsMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_46deb970c8d7ad9a3348e4eb21d34166.WildcardsMask): An instance of the WildcardsMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_46deb970c8d7ad9a3348e4eb21d34166 import WildcardsMask
        return WildcardsMask(self)._select()

    @property
    def WildcardsSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_30584fd46ca1157c8d65eba239520375.WildcardsSupported): An instance of the WildcardsSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_30584fd46ca1157c8d65eba239520375 import WildcardsSupported
        return WildcardsSupported(self)._select()

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_39416f32af218003a0073b24063a6a2b.WriteActions): An instance of the WriteActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_39416f32af218003a0073b24063a6a2b import WriteActions
        return WriteActions(self)._select()

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_a081ed7dbae22e500b36fee76b0dccc9.WriteActionsMiss): An instance of the WriteActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_a081ed7dbae22e500b36fee76b0dccc9 import WriteActionsMiss
        return WriteActionsMiss(self)._select()

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_c0e3d946283b9ad63b8ab9ea42efec94.WriteSetField): An instance of the WriteSetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_c0e3d946283b9ad63b8ab9ea42efec94 import WriteSetField
        return WriteSetField(self)._select()

    @property
    def WriteSetFieldMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_9fa9af58f5689699c49f1f453402d163.WriteSetFieldMask): An instance of the WriteSetFieldMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_9fa9af58f5689699c49f1f453402d163 import WriteSetFieldMask
        return WriteSetFieldMask(self)._select()

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_bc63a2deae2dd1dcfe0925c54c890e24.WriteSetFieldMiss): An instance of the WriteSetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_bc63a2deae2dd1dcfe0925c54c890e24 import WriteSetFieldMiss
        return WriteSetFieldMiss(self)._select()

    @property
    def WriteSetFieldMissMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_89b80ba1397c320f115dd7c575fb9b06.WriteSetFieldMissMask): An instance of the WriteSetFieldMissMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_89b80ba1397c320f115dd7c575fb9b06 import WriteSetFieldMissMask
        return WriteSetFieldMissMask(self)._select()

    @property
    def AutoConfigureNextTable(self):
        """
        Returns
        -------
        - bool: If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoConfigureNextTable'])
    @AutoConfigureNextTable.setter
    def AutoConfigureNextTable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoConfigureNextTable'], value)

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - str: Indicates the maximum number of entries supported. The default value is 10,000.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxEntries'])
    @MaxEntries.setter
    def MaxEntries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxEntries'], value)

    @property
    def MetadataMatch(self):
        """
        Returns
        -------
        - str: Specify the bits of metadata which the table can match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataMatch'])
    @MetadataMatch.setter
    def MetadataMatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetadataMatch'], value)

    @property
    def MetadataWrite(self):
        """
        Returns
        -------
        - str: Specify the bits of metadata which the table can write.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataWrite'])
    @MetadataWrite.setter
    def MetadataWrite(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetadataWrite'], value)

    @property
    def NextTable(self):
        """
        Returns
        -------
        - str: Specify the next table property.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTable'])
    @NextTable.setter
    def NextTable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextTable'], value)

    @property
    def NextTableMiss(self):
        """
        Returns
        -------
        - str: Specify the next table-miss property.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTableMiss'])
    @NextTableMiss.setter
    def NextTableMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextTableMiss'], value)

    @property
    def NumberOfTables(self):
        """
        Returns
        -------
        - number: Indicates the number of entries in the table range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfTables'])
    @NumberOfTables.setter
    def NumberOfTables(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfTables'], value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - str: Indicates the Identifier of the switch table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])
    @TableId.setter
    def TableId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableId'], value)

    @property
    def TableName(self):
        """
        Returns
        -------
        - str: Indicates the name of the switch table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableName'])
    @TableName.setter
    def TableName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableName'], value)

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
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

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
