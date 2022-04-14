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


class TableFeaturesLearnedInformation(Base):
    """NOT DEFINED
    The TableFeaturesLearnedInformation class encapsulates a list of tableFeaturesLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the TableFeaturesLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "tableFeaturesLearnedInformation"
    _SDM_ATT_MAP = {
        "ApplyActions": "applyActions",
        "ApplyActionsMiss": "applyActionsMiss",
        "ApplySetField": "applySetField",
        "ApplySetFieldMiss": "applySetFieldMiss",
        "Config": "config",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "ErrorCode": "errorCode",
        "ErrorType": "errorType",
        "Experimenter": "experimenter",
        "ExperimenterMiss": "experimenterMiss",
        "Instruction": "instruction",
        "InstructionMiss": "instructionMiss",
        "Latency": "latency",
        "LocalIp": "localIp",
        "Match": "match",
        "MaxEntries": "maxEntries",
        "MetadataMatch": "metadataMatch",
        "MetadataWrite": "metadataWrite",
        "Name": "name",
        "NegotiatedVersion": "negotiatedVersion",
        "NextTable": "nextTable",
        "NextTableMiss": "nextTableMiss",
        "RemoteIp": "remoteIp",
        "ReplyState": "replyState",
        "TableId": "tableId",
        "WildCards": "wildCards",
        "WriteActions": "writeActions",
        "WriteActionsMiss": "writeActionsMiss",
        "WriteSetField": "writeSetField",
        "WriteSetFieldMiss": "writeSetFieldMiss",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TableFeaturesLearnedInformation, self).__init__(parent, list_op)

    @property
    def ApplyActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_427966f07a706339c51b4b2579d48185.ApplyActionsLearnedInfo): An instance of the ApplyActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_427966f07a706339c51b4b2579d48185 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_29dd527cc42222be4c6c8dc459c87b3a.ApplyActionsMissLearnedInfo): An instance of the ApplyActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_29dd527cc42222be4c6c8dc459c87b3a import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_b3774cb70e932fe9e4e2fd85b8254cc7.ApplySetFieldLearnedInfo): An instance of the ApplySetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_b3774cb70e932fe9e4e2fd85b8254cc7 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_ca9fb065d79a7d3d4d9a28c53109f36d.ApplySetFieldMissLearnedInfo): An instance of the ApplySetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_ca9fb065d79a7d3d4d9a28c53109f36d import (
            ApplySetFieldMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetFieldMissLearnedInfo", None) is not None:
                return self._properties.get("ApplySetFieldMissLearnedInfo")
        return ApplySetFieldMissLearnedInfo(self)

    @property
    def ExperimenterLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenterlearnedinfo_d034823ddcf25b1a41294ca159dcef4e.ExperimenterLearnedInfo): An instance of the ExperimenterLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenterlearnedinfo_d034823ddcf25b1a41294ca159dcef4e import (
            ExperimenterLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ExperimenterLearnedInfo", None) is not None:
                return self._properties.get("ExperimenterLearnedInfo")
        return ExperimenterLearnedInfo(self)

    @property
    def ExperimenterMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimentermisslearnedinfo_0923b633c9928a39c744fa8ac410f5aa.ExperimenterMissLearnedInfo): An instance of the ExperimenterMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimentermisslearnedinfo_0923b633c9928a39c744fa8ac410f5aa import (
            ExperimenterMissLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ExperimenterMissLearnedInfo", None) is not None:
                return self._properties.get("ExperimenterMissLearnedInfo")
        return ExperimenterMissLearnedInfo(self)

    @property
    def InstructionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_80ca33d20320339607273c582ce4f442.InstructionLearnedInfo): An instance of the InstructionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_80ca33d20320339607273c582ce4f442 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_ce8fd9a44405bb24c6c41e827c64d18b.InstructionMissLearnedInfo): An instance of the InstructionMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_ce8fd9a44405bb24c6c41e827c64d18b import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_ee30567f6204f6f7481cc51a099d58c0.MatchLearnedInfo): An instance of the MatchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_ee30567f6204f6f7481cc51a099d58c0 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_940f2fd04cb5ee71971b7e0664f31b09.NextTableLearnedInfo): An instance of the NextTableLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_940f2fd04cb5ee71971b7e0664f31b09 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_c2ed3f54a804f198f49c836d72ac2851.NextTableMissLearnedInfo): An instance of the NextTableMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_c2ed3f54a804f198f49c836d72ac2851 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_7effe1050827b0e28ab3fd5c6dbd9848.WildcardsLearnedInfo): An instance of the WildcardsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_7effe1050827b0e28ab3fd5c6dbd9848 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_69f1804d172b0ba2df4ebcf348acc342.WriteActionsLearnedInfo): An instance of the WriteActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_69f1804d172b0ba2df4ebcf348acc342 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_def51b3c6d82c12abd66286c4c0fedd4.WriteActionsMissLearnedInfo): An instance of the WriteActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_def51b3c6d82c12abd66286c4c0fedd4 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_0f15ec57e03a894c34ded7eb719b7fd3.WriteSetFieldLearnedInfo): An instance of the WriteSetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_0f15ec57e03a894c34ded7eb719b7fd3 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_5edeea551686001d9d0f7a0c98781951.WriteSetFieldMissLearnedInfo): An instance of the WriteSetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_5edeea551686001d9d0f7a0c98781951 import (
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
    def ErrorCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorCode"])

    @property
    def ErrorType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorType"])

    @property
    def Experimenter(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Experimenter"])

    @property
    def ExperimenterMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterMiss"])

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
    def Latency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Latency"])

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
    def NegotiatedVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatedVersion"])

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
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteIp"])

    @property
    def ReplyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplyState"])

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
        """Adds a new tableFeaturesLearnedInformation resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved tableFeaturesLearnedInformation resources using find and the newly added tableFeaturesLearnedInformation resources available through an iterator or index

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
        ErrorCode=None,
        ErrorType=None,
        Experimenter=None,
        ExperimenterMiss=None,
        Instruction=None,
        InstructionMiss=None,
        Latency=None,
        LocalIp=None,
        Match=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        Name=None,
        NegotiatedVersion=None,
        NextTable=None,
        NextTableMiss=None,
        RemoteIp=None,
        ReplyState=None,
        TableId=None,
        WildCards=None,
        WriteActions=None,
        WriteActionsMiss=None,
        WriteSetField=None,
        WriteSetFieldMiss=None,
    ):
        # type: (str, str, str, str, int, str, str, str, str, str, str, str, str, int, str, str, int, str, str, str, str, str, str, str, str, str, str, str, str, str, str) -> TableFeaturesLearnedInformation
        """Finds and retrieves tableFeaturesLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tableFeaturesLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tableFeaturesLearnedInformation resources from the server.

        Args
        ----
        - ApplyActions (str): NOT DEFINED
        - ApplyActionsMiss (str): NOT DEFINED
        - ApplySetField (str): NOT DEFINED
        - ApplySetFieldMiss (str): NOT DEFINED
        - Config (number): NOT DEFINED
        - DataPathId (str): NOT DEFINED
        - DataPathIdAsHex (str): NOT DEFINED
        - ErrorCode (str): NOT DEFINED
        - ErrorType (str): NOT DEFINED
        - Experimenter (str): NOT DEFINED
        - ExperimenterMiss (str): NOT DEFINED
        - Instruction (str): NOT DEFINED
        - InstructionMiss (str): NOT DEFINED
        - Latency (number): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - Match (str): NOT DEFINED
        - MaxEntries (number): NOT DEFINED
        - MetadataMatch (str): NOT DEFINED
        - MetadataWrite (str): NOT DEFINED
        - Name (str): NOT DEFINED
        - NegotiatedVersion (str): NOT DEFINED
        - NextTable (str): NOT DEFINED
        - NextTableMiss (str): NOT DEFINED
        - RemoteIp (str): NOT DEFINED
        - ReplyState (str): NOT DEFINED
        - TableId (str): NOT DEFINED
        - WildCards (str): NOT DEFINED
        - WriteActions (str): NOT DEFINED
        - WriteActionsMiss (str): NOT DEFINED
        - WriteSetField (str): NOT DEFINED
        - WriteSetFieldMiss (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching tableFeaturesLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tableFeaturesLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tableFeaturesLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
