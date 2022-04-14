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


class SwitchTableFeaturesStatLearnedInfo(Base):
    """NOT DEFINED
    The SwitchTableFeaturesStatLearnedInfo class encapsulates a list of switchTableFeaturesStatLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchTableFeaturesStatLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "switchTableFeaturesStatLearnedInfo"
    _SDM_ATT_MAP = {
        "ApplyActions": "applyActions",
        "ApplyActionsMiss": "applyActionsMiss",
        "ApplySetField": "applySetField",
        "ApplySetFieldMiss": "applySetFieldMiss",
        "Config": "config",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "Instruction": "instruction",
        "InstructionMiss": "instructionMiss",
        "LocalIp": "localIp",
        "Match": "match",
        "MaxEntries": "maxEntries",
        "MetadataMatch": "metadataMatch",
        "MetadataWrite": "metadataWrite",
        "Name": "name",
        "NextTable": "nextTable",
        "NextTableMiss": "nextTableMiss",
        "TableId": "tableId",
        "WildCards": "wildCards",
        "WriteActions": "writeActions",
        "WriteActionsMiss": "writeActionsMiss",
        "WriteSetField": "writeSetField",
        "WriteSetFieldMiss": "writeSetFieldMiss",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SwitchTableFeaturesStatLearnedInfo, self).__init__(parent, list_op)

    @property
    def ApplyActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_f0ada513970ed351ca5e970e6ef90516.ApplyActionsLearnedInfo): An instance of the ApplyActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_f0ada513970ed351ca5e970e6ef90516 import (
            ApplyActionsLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplyActionsLearnedInfo", None) is not None:
                return self._properties.get("ApplyActionsLearnedInfo")
        return ApplyActionsLearnedInfo(self)

    @property
    def ApplyActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_e0bd92327edb05846bc35f8bd1b86f75.ApplyActionsMissLearnedInfo): An instance of the ApplyActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_e0bd92327edb05846bc35f8bd1b86f75 import (
            ApplyActionsMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplyActionsMissLearnedInfo", None) is not None:
                return self._properties.get("ApplyActionsMissLearnedInfo")
        return ApplyActionsMissLearnedInfo(self)

    @property
    def ApplySetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_7f197217be6a9c065d8988e7f77c824c.ApplySetFieldLearnedInfo): An instance of the ApplySetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_7f197217be6a9c065d8988e7f77c824c import (
            ApplySetFieldLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetFieldLearnedInfo", None) is not None:
                return self._properties.get("ApplySetFieldLearnedInfo")
        return ApplySetFieldLearnedInfo(self)

    @property
    def ApplySetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_a706fb38001dfd5efa880a5460efb716.ApplySetFieldMissLearnedInfo): An instance of the ApplySetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_a706fb38001dfd5efa880a5460efb716 import (
            ApplySetFieldMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetFieldMissLearnedInfo", None) is not None:
                return self._properties.get("ApplySetFieldMissLearnedInfo")
        return ApplySetFieldMissLearnedInfo(self)

    @property
    def InstructionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_efd9264f2fdac9ba267b1fa386b60932.InstructionLearnedInfo): An instance of the InstructionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_efd9264f2fdac9ba267b1fa386b60932 import (
            InstructionLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InstructionLearnedInfo", None) is not None:
                return self._properties.get("InstructionLearnedInfo")
        return InstructionLearnedInfo(self)

    @property
    def InstructionMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_f6640812737de8b6f4b5d356aa373810.InstructionMissLearnedInfo): An instance of the InstructionMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_f6640812737de8b6f4b5d356aa373810 import (
            InstructionMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InstructionMissLearnedInfo", None) is not None:
                return self._properties.get("InstructionMissLearnedInfo")
        return InstructionMissLearnedInfo(self)

    @property
    def MatchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_27b9713d3e27bb5c04d59532b30e2301.MatchLearnedInfo): An instance of the MatchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_27b9713d3e27bb5c04d59532b30e2301 import (
            MatchLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MatchLearnedInfo", None) is not None:
                return self._properties.get("MatchLearnedInfo")
        return MatchLearnedInfo(self)

    @property
    def NextTableLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_5090c2a2c198b079982b45c9cf94d021.NextTableLearnedInfo): An instance of the NextTableLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_5090c2a2c198b079982b45c9cf94d021 import (
            NextTableLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NextTableLearnedInfo", None) is not None:
                return self._properties.get("NextTableLearnedInfo")
        return NextTableLearnedInfo(self)

    @property
    def NextTableMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_966796c49aeac38cb610b65502943bb4.NextTableMissLearnedInfo): An instance of the NextTableMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_966796c49aeac38cb610b65502943bb4 import (
            NextTableMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NextTableMissLearnedInfo", None) is not None:
                return self._properties.get("NextTableMissLearnedInfo")
        return NextTableMissLearnedInfo(self)

    @property
    def WildcardsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_f184c966fff39cee4dc8824b2ddfcf0a.WildcardsLearnedInfo): An instance of the WildcardsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_f184c966fff39cee4dc8824b2ddfcf0a import (
            WildcardsLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WildcardsLearnedInfo", None) is not None:
                return self._properties.get("WildcardsLearnedInfo")
        return WildcardsLearnedInfo(self)

    @property
    def WriteActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_7610be485bc6b1f7d7ac09bbccbeac62.WriteActionsLearnedInfo): An instance of the WriteActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_7610be485bc6b1f7d7ac09bbccbeac62 import (
            WriteActionsLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteActionsLearnedInfo", None) is not None:
                return self._properties.get("WriteActionsLearnedInfo")
        return WriteActionsLearnedInfo(self)

    @property
    def WriteActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_47d66a2418998f7efdd78d201a013a3a.WriteActionsMissLearnedInfo): An instance of the WriteActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_47d66a2418998f7efdd78d201a013a3a import (
            WriteActionsMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteActionsMissLearnedInfo", None) is not None:
                return self._properties.get("WriteActionsMissLearnedInfo")
        return WriteActionsMissLearnedInfo(self)

    @property
    def WriteSetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_baa8ba69dbabb653f5ceb83cfeb81659.WriteSetFieldLearnedInfo): An instance of the WriteSetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_baa8ba69dbabb653f5ceb83cfeb81659 import (
            WriteSetFieldLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetFieldLearnedInfo", None) is not None:
                return self._properties.get("WriteSetFieldLearnedInfo")
        return WriteSetFieldLearnedInfo(self)

    @property
    def WriteSetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_9e1fd653a82d5a38c717d8c5e922868f.WriteSetFieldMissLearnedInfo): An instance of the WriteSetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_9e1fd653a82d5a38c717d8c5e922868f import (
            WriteSetFieldMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetFieldMissLearnedInfo", None) is not None:
                return self._properties.get("WriteSetFieldMissLearnedInfo")
        return WriteSetFieldMissLearnedInfo(self)

    @property
    def ApplyActions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActions"])

    @property
    def ApplyActionsMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActionsMiss"])

    @property
    def ApplySetField(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplySetField"])

    @property
    def ApplySetFieldMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplySetFieldMiss"])

    @property
    def Config(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Config"])

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathId"])

    @property
    def DataPathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathIdAsHex"])

    @property
    def Instruction(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Instruction"])

    @property
    def InstructionMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionMiss"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def Match(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Match"])

    @property
    def MaxEntries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxEntries"])

    @property
    def MetadataMatch(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MetadataMatch"])

    @property
    def MetadataWrite(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MetadataWrite"])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @property
    def NextTable(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextTable"])

    @property
    def NextTableMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextTableMiss"])

    @property
    def TableId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableId"])

    @property
    def WildCards(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["WildCards"])

    @property
    def WriteActions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActions"])

    @property
    def WriteActionsMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActionsMiss"])

    @property
    def WriteSetField(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteSetField"])

    @property
    def WriteSetFieldMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteSetFieldMiss"])

    def add(self):
        """Adds a new switchTableFeaturesStatLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved switchTableFeaturesStatLearnedInfo resources using find and the newly added switchTableFeaturesStatLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ApplyActions=None,
        ApplyActionsMiss=None,
        ApplySetField=None,
        ApplySetFieldMiss=None,
        Config=None,
        DataPathId=None,
        DataPathIdAsHex=None,
        Instruction=None,
        InstructionMiss=None,
        LocalIp=None,
        Match=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        Name=None,
        NextTable=None,
        NextTableMiss=None,
        TableId=None,
        WildCards=None,
        WriteActions=None,
        WriteActionsMiss=None,
        WriteSetField=None,
        WriteSetFieldMiss=None,
    ):
        # type: (str, str, str, str, int, str, str, str, str, str, str, int, str, str, str, str, str, str, str, str, str, str, str) -> SwitchTableFeaturesStatLearnedInfo
        """Finds and retrieves switchTableFeaturesStatLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchTableFeaturesStatLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchTableFeaturesStatLearnedInfo resources from the server.

        Args
        ----
        - ApplyActions (str): NOT DEFINED
        - ApplyActionsMiss (str): NOT DEFINED
        - ApplySetField (str): NOT DEFINED
        - ApplySetFieldMiss (str): NOT DEFINED
        - Config (number): NOT DEFINED
        - DataPathId (str): NOT DEFINED
        - DataPathIdAsHex (str): NOT DEFINED
        - Instruction (str): NOT DEFINED
        - InstructionMiss (str): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - Match (str): NOT DEFINED
        - MaxEntries (number): NOT DEFINED
        - MetadataMatch (str): NOT DEFINED
        - MetadataWrite (str): NOT DEFINED
        - Name (str): NOT DEFINED
        - NextTable (str): NOT DEFINED
        - NextTableMiss (str): NOT DEFINED
        - TableId (str): NOT DEFINED
        - WildCards (str): NOT DEFINED
        - WriteActions (str): NOT DEFINED
        - WriteActionsMiss (str): NOT DEFINED
        - WriteSetField (str): NOT DEFINED
        - WriteSetFieldMiss (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchTableFeaturesStatLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchTableFeaturesStatLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchTableFeaturesStatLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
