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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class SwitchTables(Base):
    """This object allows to define the configuration parameters for the switch tables.
    The SwitchTables class encapsulates a list of switchTables resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchTables.find() method.
    The list can be managed by using the SwitchTables.add() and SwitchTables.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "switchTables"
    _SDM_ATT_MAP = {
        "AutoConfigureNextTable": "autoConfigureNextTable",
        "MaxEntries": "maxEntries",
        "MetadataMatch": "metadataMatch",
        "MetadataWrite": "metadataWrite",
        "NextTable": "nextTable",
        "NextTableMiss": "nextTableMiss",
        "NumberOfTables": "numberOfTables",
        "TableId": "tableId",
        "TableName": "tableName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SwitchTables, self).__init__(parent, list_op)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_ec6a3d2ae6bb0592212467e2b9ae0f03.ApplyActions): An instance of the ApplyActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_ec6a3d2ae6bb0592212467e2b9ae0f03 import (
            ApplyActions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplyActions", None) is not None:
                return self._properties.get("ApplyActions")
        return ApplyActions(self)._select()

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_c88d65e1e0f8f637a660f0fb9cd6f4a7.ApplyActionsMiss): An instance of the ApplyActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_c88d65e1e0f8f637a660f0fb9cd6f4a7 import (
            ApplyActionsMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplyActionsMiss", None) is not None:
                return self._properties.get("ApplyActionsMiss")
        return ApplyActionsMiss(self)._select()

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_0df63c15745bdf9e39be14dd8ed2de8c.ApplySetField): An instance of the ApplySetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_0df63c15745bdf9e39be14dd8ed2de8c import (
            ApplySetField,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetField", None) is not None:
                return self._properties.get("ApplySetField")
        return ApplySetField(self)._select()

    @property
    def ApplySetFieldMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_ac2394ebbb58a0e3e4bd90699e8e83eb.ApplySetFieldMask): An instance of the ApplySetFieldMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmask_ac2394ebbb58a0e3e4bd90699e8e83eb import (
            ApplySetFieldMask,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetFieldMask", None) is not None:
                return self._properties.get("ApplySetFieldMask")
        return ApplySetFieldMask(self)._select()

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_d5e913768f62c6a315b980602e613536.ApplySetFieldMiss): An instance of the ApplySetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_d5e913768f62c6a315b980602e613536 import (
            ApplySetFieldMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetFieldMiss", None) is not None:
                return self._properties.get("ApplySetFieldMiss")
        return ApplySetFieldMiss(self)._select()

    @property
    def ApplySetFieldMissMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_a1d1c1318096b8b862772ca0daea5218.ApplySetFieldMissMask): An instance of the ApplySetFieldMissMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmissmask_a1d1c1318096b8b862772ca0daea5218 import (
            ApplySetFieldMissMask,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetFieldMissMask", None) is not None:
                return self._properties.get("ApplySetFieldMissMask")
        return ApplySetFieldMissMask(self)._select()

    @property
    def FeaturesSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_92f575d2a2332efe64bd7fe760fcf22c.FeaturesSupported): An instance of the FeaturesSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_92f575d2a2332efe64bd7fe760fcf22c import (
            FeaturesSupported,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FeaturesSupported", None) is not None:
                return self._properties.get("FeaturesSupported")
        return FeaturesSupported(self)._select()

    @property
    def Instruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_fc4b94bed361448b3d919547f5d505a9.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_fc4b94bed361448b3d919547f5d505a9 import (
            Instruction,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Instruction", None) is not None:
                return self._properties.get("Instruction")
        return Instruction(self)._select()

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_c4b2f1d7f7d9c8ad00aae67c1b5af082.InstructionMiss): An instance of the InstructionMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_c4b2f1d7f7d9c8ad00aae67c1b5af082 import (
            InstructionMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InstructionMiss", None) is not None:
                return self._properties.get("InstructionMiss")
        return InstructionMiss(self)._select()

    @property
    def Match(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_768aa9c10fbecd20329c8a8a8482495f.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_768aa9c10fbecd20329c8a8a8482495f import (
            Match,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Match", None) is not None:
                return self._properties.get("Match")
        return Match(self)._select()

    @property
    def MatchMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_3e54fe54588386540da4d88f8eefac19.MatchMask): An instance of the MatchMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchmask_3e54fe54588386540da4d88f8eefac19 import (
            MatchMask,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MatchMask", None) is not None:
                return self._properties.get("MatchMask")
        return MatchMask(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_d37a03c83fd57b830f05531c024bda35.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_d37a03c83fd57b830f05531c024bda35 import (
            Wildcards,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Wildcards", None) is not None:
                return self._properties.get("Wildcards")
        return Wildcards(self)._select()

    @property
    def WildcardsMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_58852c1aea55c59402d8fa035d06df5c.WildcardsMask): An instance of the WildcardsMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsmask_58852c1aea55c59402d8fa035d06df5c import (
            WildcardsMask,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WildcardsMask", None) is not None:
                return self._properties.get("WildcardsMask")
        return WildcardsMask(self)._select()

    @property
    def WildcardsSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_2837a6d44c3d53ed96a2b701bb9d6365.WildcardsSupported): An instance of the WildcardsSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_2837a6d44c3d53ed96a2b701bb9d6365 import (
            WildcardsSupported,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WildcardsSupported", None) is not None:
                return self._properties.get("WildcardsSupported")
        return WildcardsSupported(self)._select()

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_b6ffad884e16fd072bdbe0c697cc514e.WriteActions): An instance of the WriteActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_b6ffad884e16fd072bdbe0c697cc514e import (
            WriteActions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteActions", None) is not None:
                return self._properties.get("WriteActions")
        return WriteActions(self)._select()

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_133562c2fb0ad0f2921733e2c487aa05.WriteActionsMiss): An instance of the WriteActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_133562c2fb0ad0f2921733e2c487aa05 import (
            WriteActionsMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteActionsMiss", None) is not None:
                return self._properties.get("WriteActionsMiss")
        return WriteActionsMiss(self)._select()

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_1d3fe60ac5d235c8b6ffa41f05cf0752.WriteSetField): An instance of the WriteSetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_1d3fe60ac5d235c8b6ffa41f05cf0752 import (
            WriteSetField,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetField", None) is not None:
                return self._properties.get("WriteSetField")
        return WriteSetField(self)._select()

    @property
    def WriteSetFieldMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_70c7a66c3e5975b41b9e4e368cebf9cc.WriteSetFieldMask): An instance of the WriteSetFieldMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmask_70c7a66c3e5975b41b9e4e368cebf9cc import (
            WriteSetFieldMask,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetFieldMask", None) is not None:
                return self._properties.get("WriteSetFieldMask")
        return WriteSetFieldMask(self)._select()

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_89c5b6da627e4dc15d5aad1904210c18.WriteSetFieldMiss): An instance of the WriteSetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_89c5b6da627e4dc15d5aad1904210c18 import (
            WriteSetFieldMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetFieldMiss", None) is not None:
                return self._properties.get("WriteSetFieldMiss")
        return WriteSetFieldMiss(self)._select()

    @property
    def WriteSetFieldMissMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_f99c606569bcd266be92a115b6a3b059.WriteSetFieldMissMask): An instance of the WriteSetFieldMissMask class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmissmask_f99c606569bcd266be92a115b6a3b059 import (
            WriteSetFieldMissMask,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetFieldMissMask", None) is not None:
                return self._properties.get("WriteSetFieldMissMask")
        return WriteSetFieldMissMask(self)._select()

    @property
    def AutoConfigureNextTable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the Next Tables are automatically configured. The Next Table and Next Table Miss fields are grayed out.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoConfigureNextTable"])

    @AutoConfigureNextTable.setter
    def AutoConfigureNextTable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoConfigureNextTable"], value)

    @property
    def MaxEntries(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the maximum number of entries supported. The default value is 10,000.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxEntries"])

    @MaxEntries.setter
    def MaxEntries(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxEntries"], value)

    @property
    def MetadataMatch(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the bits of metadata which the table can match.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MetadataMatch"])

    @MetadataMatch.setter
    def MetadataMatch(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MetadataMatch"], value)

    @property
    def MetadataWrite(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the bits of metadata which the table can write.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MetadataWrite"])

    @MetadataWrite.setter
    def MetadataWrite(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MetadataWrite"], value)

    @property
    def NextTable(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the next table property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextTable"])

    @NextTable.setter
    def NextTable(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextTable"], value)

    @property
    def NextTableMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the next table-miss property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextTableMiss"])

    @NextTableMiss.setter
    def NextTableMiss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextTableMiss"], value)

    @property
    def NumberOfTables(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the number of entries in the table range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfTables"])

    @NumberOfTables.setter
    def NumberOfTables(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfTables"], value)

    @property
    def TableId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the Identifier of the switch table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableId"])

    @TableId.setter
    def TableId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableId"], value)

    @property
    def TableName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the name of the switch table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableName"])

    @TableName.setter
    def TableName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableName"], value)

    def update(
        self,
        AutoConfigureNextTable=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        NextTable=None,
        NextTableMiss=None,
        NumberOfTables=None,
        TableId=None,
        TableName=None,
    ):
        # type: (bool, str, str, str, str, str, int, str, str) -> SwitchTables
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

    def add(
        self,
        AutoConfigureNextTable=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        NextTable=None,
        NextTableMiss=None,
        NumberOfTables=None,
        TableId=None,
        TableName=None,
    ):
        # type: (bool, str, str, str, str, str, int, str, str) -> SwitchTables
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

    def find(
        self,
        AutoConfigureNextTable=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        NextTable=None,
        NextTableMiss=None,
        NumberOfTables=None,
        TableId=None,
        TableName=None,
    ):
        # type: (bool, str, str, str, str, str, int, str, str) -> SwitchTables
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
