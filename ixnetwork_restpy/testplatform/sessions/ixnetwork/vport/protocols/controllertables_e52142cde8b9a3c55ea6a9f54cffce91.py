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


class ControllerTables(Base):
    """This view lists all the controller table features that can be configured.
    The ControllerTables class encapsulates a list of controllerTables resources that are managed by the user.
    A list of resources can be retrieved from the server using the ControllerTables.find() method.
    The list can be managed by using the ControllerTables.add() and ControllerTables.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "controllerTables"
    _SDM_ATT_MAP = {
        "ApplyActionExperimenterData": "applyActionExperimenterData",
        "ApplyActionExperimenterDataLength": "applyActionExperimenterDataLength",
        "ApplyActionExperimenterId": "applyActionExperimenterId",
        "ApplyActionMissExperimenterData": "applyActionMissExperimenterData",
        "ApplyActionMissExperimenterDataLength": "applyActionMissExperimenterDataLength",
        "ApplyActionMissExperimenterId": "applyActionMissExperimenterId",
        "Config": "config",
        "Enabled": "enabled",
        "ExperimenterData": "experimenterData",
        "ExperimenterDataLength": "experimenterDataLength",
        "ExperimenterId": "experimenterId",
        "ExperimenterMissData": "experimenterMissData",
        "ExperimenterMissDataLength": "experimenterMissDataLength",
        "ExperimenterMissId": "experimenterMissId",
        "ExperimenterMissType": "experimenterMissType",
        "ExperimenterType": "experimenterType",
        "InstructionExperimenterData": "instructionExperimenterData",
        "InstructionExperimenterDataLength": "instructionExperimenterDataLength",
        "InstructionExperimenterId": "instructionExperimenterId",
        "InstructionMissExperimenterData": "instructionMissExperimenterData",
        "InstructionMissExperimenterDataLength": "instructionMissExperimenterDataLength",
        "InstructionMissExperimenterId": "instructionMissExperimenterId",
        "MatchExperimenterData": "matchExperimenterData",
        "MatchExperimenterDataLength": "matchExperimenterDataLength",
        "MatchExperimenterField": "matchExperimenterField",
        "MatchExperimenterHasMask": "matchExperimenterHasMask",
        "MatchExperimenterId": "matchExperimenterId",
        "MaxEntries": "maxEntries",
        "MetadataMatch": "metadataMatch",
        "MetadataWrite": "metadataWrite",
        "NextTable": "nextTable",
        "NextTableMiss": "nextTableMiss",
        "TableId": "tableId",
        "TableName": "tableName",
        "WildcardExperimenterData": "wildcardExperimenterData",
        "WildcardExperimenterDataLength": "wildcardExperimenterDataLength",
        "WildcardExperimenterField": "wildcardExperimenterField",
        "WildcardExperimenterHasMask": "wildcardExperimenterHasMask",
        "WildcardExperimenterId": "wildcardExperimenterId",
        "WriteActionExperimenterData": "writeActionExperimenterData",
        "WriteActionExperimenterDataLength": "writeActionExperimenterDataLength",
        "WriteActionExperimenterId": "writeActionExperimenterId",
        "WriteActionMissExperimenterData": "writeActionMissExperimenterData",
        "WriteActionMissExperimenterDataLength": "writeActionMissExperimenterDataLength",
        "WriteActionMissExperimenterId": "writeActionMissExperimenterId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ControllerTables, self).__init__(parent, list_op)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_f3190fab64661538563653e07df155a5.ApplyActions): An instance of the ApplyActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_f3190fab64661538563653e07df155a5 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_c6e26bae5086b5561d3714cc015046b0.ApplyActionsMiss): An instance of the ApplyActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_c6e26bae5086b5561d3714cc015046b0 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_253c9a5a708bdb2312cf5d52ad1f87ad.ApplySetField): An instance of the ApplySetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_253c9a5a708bdb2312cf5d52ad1f87ad import (
            ApplySetField,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetField", None) is not None:
                return self._properties.get("ApplySetField")
        return ApplySetField(self)._select()

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_cecf6f2fc7109bdd9f0f43cfdcab4a67.ApplySetFieldMiss): An instance of the ApplySetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_cecf6f2fc7109bdd9f0f43cfdcab4a67 import (
            ApplySetFieldMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetFieldMiss", None) is not None:
                return self._properties.get("ApplySetFieldMiss")
        return ApplySetFieldMiss(self)._select()

    @property
    def ControllerTableFlowRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertableflowranges_e75acbbcda7835d3ccf85f0dda576bbc.ControllerTableFlowRanges): An instance of the ControllerTableFlowRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertableflowranges_e75acbbcda7835d3ccf85f0dda576bbc import (
            ControllerTableFlowRanges,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ControllerTableFlowRanges", None) is not None:
                return self._properties.get("ControllerTableFlowRanges")
        return ControllerTableFlowRanges(self)

    @property
    def FeaturesSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_54813e4d9341e0be8768b74817aeac3d.FeaturesSupported): An instance of the FeaturesSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_54813e4d9341e0be8768b74817aeac3d import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_da8215ede02e2b1110439290731db450.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_da8215ede02e2b1110439290731db450 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_2ad1cd6bc93242f96042d2e2049a9732.InstructionMiss): An instance of the InstructionMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_2ad1cd6bc93242f96042d2e2049a9732 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_090b898f6d78ba3c4bdf0995a399336f.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_090b898f6d78ba3c4bdf0995a399336f import (
            Match,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Match", None) is not None:
                return self._properties.get("Match")
        return Match(self)._select()

    @property
    def TableModificationTriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablemodificationtriggerattributes_fa8f1d7a5a2f67cd2c8b254e201fdc5a.TableModificationTriggerAttributes): An instance of the TableModificationTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablemodificationtriggerattributes_fa8f1d7a5a2f67cd2c8b254e201fdc5a import (
            TableModificationTriggerAttributes,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("TableModificationTriggerAttributes", None)
                is not None
            ):
                return self._properties.get("TableModificationTriggerAttributes")
        return TableModificationTriggerAttributes(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_82e961cfac4b8a1d597719e0a8012db9.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_82e961cfac4b8a1d597719e0a8012db9 import (
            Wildcards,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Wildcards", None) is not None:
                return self._properties.get("Wildcards")
        return Wildcards(self)._select()

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_53b6fc380cbeecaf17b7c6a2c7a64909.WriteActions): An instance of the WriteActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_53b6fc380cbeecaf17b7c6a2c7a64909 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_d80c3286af9e5d78bc736e7aeda2cd71.WriteActionsMiss): An instance of the WriteActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_d80c3286af9e5d78bc736e7aeda2cd71 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_fbe5072e08f345f2a2c8d7c98b09a8a5.WriteSetField): An instance of the WriteSetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_fbe5072e08f345f2a2c8d7c98b09a8a5 import (
            WriteSetField,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetField", None) is not None:
                return self._properties.get("WriteSetField")
        return WriteSetField(self)._select()

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_499a12e92955cf043867d8a88984286f.WriteSetFieldMiss): An instance of the WriteSetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_499a12e92955cf043867d8a88984286f import (
            WriteSetFieldMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetFieldMiss", None) is not None:
                return self._properties.get("WriteSetFieldMiss")
        return WriteSetFieldMiss(self)._select()

    @property
    def ApplyActionExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the Apply Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActionExperimenterData"])

    @ApplyActionExperimenterData.setter
    def ApplyActionExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyActionExperimenterData"], value)

    @property
    def ApplyActionExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the Apply Action Experimenter.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ApplyActionExperimenterDataLength"]
        )

    @ApplyActionExperimenterDataLength.setter
    def ApplyActionExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ApplyActionExperimenterDataLength"], value
        )

    @property
    def ApplyActionExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for Apply Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActionExperimenterId"])

    @ApplyActionExperimenterId.setter
    def ApplyActionExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyActionExperimenterId"], value)

    @property
    def ApplyActionMissExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Experimenter Data The data of the apply action for table-miss of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActionMissExperimenterData"])

    @ApplyActionMissExperimenterData.setter
    def ApplyActionMissExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyActionMissExperimenterData"], value)

    @property
    def ApplyActionMissExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the Apply Action Miss Experimenter.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ApplyActionMissExperimenterDataLength"]
        )

    @ApplyActionMissExperimenterDataLength.setter
    def ApplyActionMissExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ApplyActionMissExperimenterDataLength"], value
        )

    @property
    def ApplyActionMissExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for Apply Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActionMissExperimenterId"])

    @ApplyActionMissExperimenterId.setter
    def ApplyActionMissExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyActionMissExperimenterId"], value)

    @property
    def Config(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the bitmap of OFPTC_* values. The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Config"])

    @Config.setter
    def Config(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Config"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, this table is used in this controller configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterData"])

    @ExperimenterData.setter
    def ExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterData"], value)

    @property
    def ExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterDataLength"])

    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterDataLength"], value)

    @property
    def ExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterId"])

    @ExperimenterId.setter
    def ExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterId"], value)

    @property
    def ExperimenterMissData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterMissData"])

    @ExperimenterMissData.setter
    def ExperimenterMissData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterMissData"], value)

    @property
    def ExperimenterMissDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterMissDataLength"])

    @ExperimenterMissDataLength.setter
    def ExperimenterMissDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterMissDataLength"], value)

    @property
    def ExperimenterMissId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterMissId"])

    @ExperimenterMissId.setter
    def ExperimenterMissId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterMissId"], value)

    @property
    def ExperimenterMissType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterMissType"])

    @ExperimenterMissType.setter
    def ExperimenterMissType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterMissType"], value)

    @property
    def ExperimenterType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterType"])

    @ExperimenterType.setter
    def ExperimenterType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterType"], value)

    @property
    def InstructionExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the Instruction Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionExperimenterData"])

    @InstructionExperimenterData.setter
    def InstructionExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InstructionExperimenterData"], value)

    @property
    def InstructionExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the experimental instruction of Controller Table Experimenter.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["InstructionExperimenterDataLength"]
        )

    @InstructionExperimenterDataLength.setter
    def InstructionExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["InstructionExperimenterDataLength"], value
        )

    @property
    def InstructionExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionExperimenterId"])

    @InstructionExperimenterId.setter
    def InstructionExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InstructionExperimenterId"], value)

    @property
    def InstructionMissExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the Instruction Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionMissExperimenterData"])

    @InstructionMissExperimenterData.setter
    def InstructionMissExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InstructionMissExperimenterData"], value)

    @property
    def InstructionMissExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It indicates the data length of the Instruction Miss Experimenter
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["InstructionMissExperimenterDataLength"]
        )

    @InstructionMissExperimenterDataLength.setter
    def InstructionMissExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["InstructionMissExperimenterDataLength"], value
        )

    @property
    def InstructionMissExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier of Instruction Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionMissExperimenterId"])

    @InstructionMissExperimenterId.setter
    def InstructionMissExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InstructionMissExperimenterId"], value)

    @property
    def MatchExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The match data of the Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchExperimenterData"])

    @MatchExperimenterData.setter
    def MatchExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchExperimenterData"], value)

    @property
    def MatchExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchExperimenterDataLength"])

    @MatchExperimenterDataLength.setter
    def MatchExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchExperimenterDataLength"], value)

    @property
    def MatchExperimenterField(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identifier for match experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchExperimenterField"])

    @MatchExperimenterField.setter
    def MatchExperimenterField(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchExperimenterField"], value)

    @property
    def MatchExperimenterHasMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Mask If selected, the match experimenter hash mask field of Controller Table Experimenter is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchExperimenterHasMask"])

    @MatchExperimenterHasMask.setter
    def MatchExperimenterHasMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchExperimenterHasMask"], value)

    @property
    def MatchExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchExperimenterId"])

    @MatchExperimenterId.setter
    def MatchExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchExperimenterId"], value)

    @property
    def MaxEntries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the maximum number of entries supported. The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxEntries"])

    @MaxEntries.setter
    def MaxEntries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxEntries"], value)

    @property
    def MetadataMatch(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the bits of metadata table that can match. The default value is 0.
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
        - str: Specify the bits of metadata table that can write. The default value is 0.
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
        - str: Next table property.
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
        - str: Next table for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextTableMiss"])

    @NextTableMiss.setter
    def NextTableMiss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextTableMiss"], value)

    @property
    def TableId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the controller table identifier. Lower numbered tables are consulted first.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableId"])

    @TableId.setter
    def TableId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableId"], value)

    @property
    def TableName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the name of the controller table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableName"])

    @TableName.setter
    def TableName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableName"], value)

    @property
    def WildcardExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WildcardExperimenterData"])

    @WildcardExperimenterData.setter
    def WildcardExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["WildcardExperimenterData"], value)

    @property
    def WildcardExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WildcardExperimenterDataLength"])

    @WildcardExperimenterDataLength.setter
    def WildcardExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WildcardExperimenterDataLength"], value)

    @property
    def WildcardExperimenterField(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WildcardExperimenterField"])

    @WildcardExperimenterField.setter
    def WildcardExperimenterField(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WildcardExperimenterField"], value)

    @property
    def WildcardExperimenterHasMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Mask If selected, the wildcard experimenter hash mask field of Controller Table Experimenter is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WildcardExperimenterHasMask"])

    @WildcardExperimenterHasMask.setter
    def WildcardExperimenterHasMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WildcardExperimenterHasMask"], value)

    @property
    def WildcardExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WildcardExperimenterId"])

    @WildcardExperimenterId.setter
    def WildcardExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WildcardExperimenterId"], value)

    @property
    def WriteActionExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the Write Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActionExperimenterData"])

    @WriteActionExperimenterData.setter
    def WriteActionExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteActionExperimenterData"], value)

    @property
    def WriteActionExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the Write Action Miss Experimenter.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["WriteActionExperimenterDataLength"]
        )

    @WriteActionExperimenterDataLength.setter
    def WriteActionExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["WriteActionExperimenterDataLength"], value
        )

    @property
    def WriteActionExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier for Write Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActionExperimenterId"])

    @WriteActionExperimenterId.setter
    def WriteActionExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteActionExperimenterId"], value)

    @property
    def WriteActionMissExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The data of the Write Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActionMissExperimenterData"])

    @WriteActionMissExperimenterData.setter
    def WriteActionMissExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteActionMissExperimenterData"], value)

    @property
    def WriteActionMissExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data length of the Write Action Miss Experimenter.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["WriteActionMissExperimenterDataLength"]
        )

    @WriteActionMissExperimenterDataLength.setter
    def WriteActionMissExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["WriteActionMissExperimenterDataLength"], value
        )

    @property
    def WriteActionMissExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier of Write Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActionMissExperimenterId"])

    @WriteActionMissExperimenterId.setter
    def WriteActionMissExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteActionMissExperimenterId"], value)

    def update(
        self,
        ApplyActionExperimenterData=None,
        ApplyActionExperimenterDataLength=None,
        ApplyActionExperimenterId=None,
        ApplyActionMissExperimenterData=None,
        ApplyActionMissExperimenterDataLength=None,
        ApplyActionMissExperimenterId=None,
        Config=None,
        Enabled=None,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterId=None,
        ExperimenterMissData=None,
        ExperimenterMissDataLength=None,
        ExperimenterMissId=None,
        ExperimenterMissType=None,
        ExperimenterType=None,
        InstructionExperimenterData=None,
        InstructionExperimenterDataLength=None,
        InstructionExperimenterId=None,
        InstructionMissExperimenterData=None,
        InstructionMissExperimenterDataLength=None,
        InstructionMissExperimenterId=None,
        MatchExperimenterData=None,
        MatchExperimenterDataLength=None,
        MatchExperimenterField=None,
        MatchExperimenterHasMask=None,
        MatchExperimenterId=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        NextTable=None,
        NextTableMiss=None,
        TableId=None,
        TableName=None,
        WildcardExperimenterData=None,
        WildcardExperimenterDataLength=None,
        WildcardExperimenterField=None,
        WildcardExperimenterHasMask=None,
        WildcardExperimenterId=None,
        WriteActionExperimenterData=None,
        WriteActionExperimenterDataLength=None,
        WriteActionExperimenterId=None,
        WriteActionMissExperimenterData=None,
        WriteActionMissExperimenterDataLength=None,
        WriteActionMissExperimenterId=None,
    ):
        # type: (str, int, int, str, int, int, int, bool, str, int, int, str, int, int, int, int, str, int, int, str, int, int, str, int, int, bool, int, int, str, str, str, str, int, str, str, int, int, bool, int, str, int, int, str, int, int) -> ControllerTables
        """Updates controllerTables resource on the server.

        Args
        ----
        - ApplyActionExperimenterData (str): The data of the Apply Action Experimenter.
        - ApplyActionExperimenterDataLength (number): The data length of the Apply Action Experimenter.
        - ApplyActionExperimenterId (number): The unique identifier for Apply Action Experimenter.
        - ApplyActionMissExperimenterData (str): Experimenter Data The data of the apply action for table-miss of Controller Table Experimenter.
        - ApplyActionMissExperimenterDataLength (number): The data length of the Apply Action Miss Experimenter.
        - ApplyActionMissExperimenterId (number): The unique identifier for Apply Action Miss Experimenter.
        - Config (number): Specify the bitmap of OFPTC_* values. The default value is 0.
        - Enabled (bool): If selected, this table is used in this controller configuration.
        - ExperimenterData (str): The data of the Experimenter.
        - ExperimenterDataLength (number): The data length of the Experimenter for table-miss.
        - ExperimenterId (number): The unique identifier for the Experimenter.
        - ExperimenterMissData (str): The data of the Experimenter for table-miss.
        - ExperimenterMissDataLength (number): The data length of the Experimenter for table-miss.
        - ExperimenterMissId (number): The unique identifier for the Experimenter for table-miss.
        - ExperimenterMissType (number): The type of experimenter for table-miss.
        - ExperimenterType (number): The type of experimenter.
        - InstructionExperimenterData (str): The data of the Instruction Experimenter.
        - InstructionExperimenterDataLength (number): The data length of the experimental instruction of Controller Table Experimenter.
        - InstructionExperimenterId (number): The unique identifier for the Experimenter.
        - InstructionMissExperimenterData (str): The data of the Instruction Miss Experimenter.
        - InstructionMissExperimenterDataLength (number): It indicates the data length of the Instruction Miss Experimenter
        - InstructionMissExperimenterId (number): The unique identifier of Instruction Miss Experimenter.
        - MatchExperimenterData (str): The match data of the Controller Table Experimenter.
        - MatchExperimenterDataLength (number): The data length of the wildcard experimenter of Controller Table Experimenter.
        - MatchExperimenterField (number): The identifier for match experimenter of Controller Table Experimenter.
        - MatchExperimenterHasMask (bool): Mask If selected, the match experimenter hash mask field of Controller Table Experimenter is available.
        - MatchExperimenterId (number): The unique identifier for wildcard experimenter of Controller Table Experimenter.
        - MaxEntries (number): Specify the maximum number of entries supported. The default value is 0.
        - MetadataMatch (str): Specify the bits of metadata table that can match. The default value is 0.
        - MetadataWrite (str): Specify the bits of metadata table that can write. The default value is 0.
        - NextTable (str): Next table property.
        - NextTableMiss (str): Next table for table-miss.
        - TableId (number): Specify the controller table identifier. Lower numbered tables are consulted first.
        - TableName (str): Specify the name of the controller table.
        - WildcardExperimenterData (str): The data of the wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterDataLength (number): The data length of the wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterField (number): The identifier for wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterHasMask (bool): Mask If selected, the wildcard experimenter hash mask field of Controller Table Experimenter is available.
        - WildcardExperimenterId (number): The unique identifier for wildcard experimenter of Controller Table Experimenter.
        - WriteActionExperimenterData (str): The data of the Write Action Experimenter.
        - WriteActionExperimenterDataLength (number): The data length of the Write Action Miss Experimenter.
        - WriteActionExperimenterId (number): The unique identifier for Write Action Experimenter.
        - WriteActionMissExperimenterData (str): The data of the Write Action Miss Experimenter.
        - WriteActionMissExperimenterDataLength (number): The data length of the Write Action Miss Experimenter.
        - WriteActionMissExperimenterId (number): The unique identifier of Write Action Miss Experimenter.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ApplyActionExperimenterData=None,
        ApplyActionExperimenterDataLength=None,
        ApplyActionExperimenterId=None,
        ApplyActionMissExperimenterData=None,
        ApplyActionMissExperimenterDataLength=None,
        ApplyActionMissExperimenterId=None,
        Config=None,
        Enabled=None,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterId=None,
        ExperimenterMissData=None,
        ExperimenterMissDataLength=None,
        ExperimenterMissId=None,
        ExperimenterMissType=None,
        ExperimenterType=None,
        InstructionExperimenterData=None,
        InstructionExperimenterDataLength=None,
        InstructionExperimenterId=None,
        InstructionMissExperimenterData=None,
        InstructionMissExperimenterDataLength=None,
        InstructionMissExperimenterId=None,
        MatchExperimenterData=None,
        MatchExperimenterDataLength=None,
        MatchExperimenterField=None,
        MatchExperimenterHasMask=None,
        MatchExperimenterId=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        NextTable=None,
        NextTableMiss=None,
        TableId=None,
        TableName=None,
        WildcardExperimenterData=None,
        WildcardExperimenterDataLength=None,
        WildcardExperimenterField=None,
        WildcardExperimenterHasMask=None,
        WildcardExperimenterId=None,
        WriteActionExperimenterData=None,
        WriteActionExperimenterDataLength=None,
        WriteActionExperimenterId=None,
        WriteActionMissExperimenterData=None,
        WriteActionMissExperimenterDataLength=None,
        WriteActionMissExperimenterId=None,
    ):
        # type: (str, int, int, str, int, int, int, bool, str, int, int, str, int, int, int, int, str, int, int, str, int, int, str, int, int, bool, int, int, str, str, str, str, int, str, str, int, int, bool, int, str, int, int, str, int, int) -> ControllerTables
        """Adds a new controllerTables resource on the server and adds it to the container.

        Args
        ----
        - ApplyActionExperimenterData (str): The data of the Apply Action Experimenter.
        - ApplyActionExperimenterDataLength (number): The data length of the Apply Action Experimenter.
        - ApplyActionExperimenterId (number): The unique identifier for Apply Action Experimenter.
        - ApplyActionMissExperimenterData (str): Experimenter Data The data of the apply action for table-miss of Controller Table Experimenter.
        - ApplyActionMissExperimenterDataLength (number): The data length of the Apply Action Miss Experimenter.
        - ApplyActionMissExperimenterId (number): The unique identifier for Apply Action Miss Experimenter.
        - Config (number): Specify the bitmap of OFPTC_* values. The default value is 0.
        - Enabled (bool): If selected, this table is used in this controller configuration.
        - ExperimenterData (str): The data of the Experimenter.
        - ExperimenterDataLength (number): The data length of the Experimenter for table-miss.
        - ExperimenterId (number): The unique identifier for the Experimenter.
        - ExperimenterMissData (str): The data of the Experimenter for table-miss.
        - ExperimenterMissDataLength (number): The data length of the Experimenter for table-miss.
        - ExperimenterMissId (number): The unique identifier for the Experimenter for table-miss.
        - ExperimenterMissType (number): The type of experimenter for table-miss.
        - ExperimenterType (number): The type of experimenter.
        - InstructionExperimenterData (str): The data of the Instruction Experimenter.
        - InstructionExperimenterDataLength (number): The data length of the experimental instruction of Controller Table Experimenter.
        - InstructionExperimenterId (number): The unique identifier for the Experimenter.
        - InstructionMissExperimenterData (str): The data of the Instruction Miss Experimenter.
        - InstructionMissExperimenterDataLength (number): It indicates the data length of the Instruction Miss Experimenter
        - InstructionMissExperimenterId (number): The unique identifier of Instruction Miss Experimenter.
        - MatchExperimenterData (str): The match data of the Controller Table Experimenter.
        - MatchExperimenterDataLength (number): The data length of the wildcard experimenter of Controller Table Experimenter.
        - MatchExperimenterField (number): The identifier for match experimenter of Controller Table Experimenter.
        - MatchExperimenterHasMask (bool): Mask If selected, the match experimenter hash mask field of Controller Table Experimenter is available.
        - MatchExperimenterId (number): The unique identifier for wildcard experimenter of Controller Table Experimenter.
        - MaxEntries (number): Specify the maximum number of entries supported. The default value is 0.
        - MetadataMatch (str): Specify the bits of metadata table that can match. The default value is 0.
        - MetadataWrite (str): Specify the bits of metadata table that can write. The default value is 0.
        - NextTable (str): Next table property.
        - NextTableMiss (str): Next table for table-miss.
        - TableId (number): Specify the controller table identifier. Lower numbered tables are consulted first.
        - TableName (str): Specify the name of the controller table.
        - WildcardExperimenterData (str): The data of the wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterDataLength (number): The data length of the wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterField (number): The identifier for wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterHasMask (bool): Mask If selected, the wildcard experimenter hash mask field of Controller Table Experimenter is available.
        - WildcardExperimenterId (number): The unique identifier for wildcard experimenter of Controller Table Experimenter.
        - WriteActionExperimenterData (str): The data of the Write Action Experimenter.
        - WriteActionExperimenterDataLength (number): The data length of the Write Action Miss Experimenter.
        - WriteActionExperimenterId (number): The unique identifier for Write Action Experimenter.
        - WriteActionMissExperimenterData (str): The data of the Write Action Miss Experimenter.
        - WriteActionMissExperimenterDataLength (number): The data length of the Write Action Miss Experimenter.
        - WriteActionMissExperimenterId (number): The unique identifier of Write Action Miss Experimenter.

        Returns
        -------
        - self: This instance with all currently retrieved controllerTables resources using find and the newly added controllerTables resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained controllerTables resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ApplyActionExperimenterData=None,
        ApplyActionExperimenterDataLength=None,
        ApplyActionExperimenterId=None,
        ApplyActionMissExperimenterData=None,
        ApplyActionMissExperimenterDataLength=None,
        ApplyActionMissExperimenterId=None,
        Config=None,
        Enabled=None,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterId=None,
        ExperimenterMissData=None,
        ExperimenterMissDataLength=None,
        ExperimenterMissId=None,
        ExperimenterMissType=None,
        ExperimenterType=None,
        InstructionExperimenterData=None,
        InstructionExperimenterDataLength=None,
        InstructionExperimenterId=None,
        InstructionMissExperimenterData=None,
        InstructionMissExperimenterDataLength=None,
        InstructionMissExperimenterId=None,
        MatchExperimenterData=None,
        MatchExperimenterDataLength=None,
        MatchExperimenterField=None,
        MatchExperimenterHasMask=None,
        MatchExperimenterId=None,
        MaxEntries=None,
        MetadataMatch=None,
        MetadataWrite=None,
        NextTable=None,
        NextTableMiss=None,
        TableId=None,
        TableName=None,
        WildcardExperimenterData=None,
        WildcardExperimenterDataLength=None,
        WildcardExperimenterField=None,
        WildcardExperimenterHasMask=None,
        WildcardExperimenterId=None,
        WriteActionExperimenterData=None,
        WriteActionExperimenterDataLength=None,
        WriteActionExperimenterId=None,
        WriteActionMissExperimenterData=None,
        WriteActionMissExperimenterDataLength=None,
        WriteActionMissExperimenterId=None,
    ):
        # type: (str, int, int, str, int, int, int, bool, str, int, int, str, int, int, int, int, str, int, int, str, int, int, str, int, int, bool, int, int, str, str, str, str, int, str, str, int, int, bool, int, str, int, int, str, int, int) -> ControllerTables
        """Finds and retrieves controllerTables resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve controllerTables resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all controllerTables resources from the server.

        Args
        ----
        - ApplyActionExperimenterData (str): The data of the Apply Action Experimenter.
        - ApplyActionExperimenterDataLength (number): The data length of the Apply Action Experimenter.
        - ApplyActionExperimenterId (number): The unique identifier for Apply Action Experimenter.
        - ApplyActionMissExperimenterData (str): Experimenter Data The data of the apply action for table-miss of Controller Table Experimenter.
        - ApplyActionMissExperimenterDataLength (number): The data length of the Apply Action Miss Experimenter.
        - ApplyActionMissExperimenterId (number): The unique identifier for Apply Action Miss Experimenter.
        - Config (number): Specify the bitmap of OFPTC_* values. The default value is 0.
        - Enabled (bool): If selected, this table is used in this controller configuration.
        - ExperimenterData (str): The data of the Experimenter.
        - ExperimenterDataLength (number): The data length of the Experimenter for table-miss.
        - ExperimenterId (number): The unique identifier for the Experimenter.
        - ExperimenterMissData (str): The data of the Experimenter for table-miss.
        - ExperimenterMissDataLength (number): The data length of the Experimenter for table-miss.
        - ExperimenterMissId (number): The unique identifier for the Experimenter for table-miss.
        - ExperimenterMissType (number): The type of experimenter for table-miss.
        - ExperimenterType (number): The type of experimenter.
        - InstructionExperimenterData (str): The data of the Instruction Experimenter.
        - InstructionExperimenterDataLength (number): The data length of the experimental instruction of Controller Table Experimenter.
        - InstructionExperimenterId (number): The unique identifier for the Experimenter.
        - InstructionMissExperimenterData (str): The data of the Instruction Miss Experimenter.
        - InstructionMissExperimenterDataLength (number): It indicates the data length of the Instruction Miss Experimenter
        - InstructionMissExperimenterId (number): The unique identifier of Instruction Miss Experimenter.
        - MatchExperimenterData (str): The match data of the Controller Table Experimenter.
        - MatchExperimenterDataLength (number): The data length of the wildcard experimenter of Controller Table Experimenter.
        - MatchExperimenterField (number): The identifier for match experimenter of Controller Table Experimenter.
        - MatchExperimenterHasMask (bool): Mask If selected, the match experimenter hash mask field of Controller Table Experimenter is available.
        - MatchExperimenterId (number): The unique identifier for wildcard experimenter of Controller Table Experimenter.
        - MaxEntries (number): Specify the maximum number of entries supported. The default value is 0.
        - MetadataMatch (str): Specify the bits of metadata table that can match. The default value is 0.
        - MetadataWrite (str): Specify the bits of metadata table that can write. The default value is 0.
        - NextTable (str): Next table property.
        - NextTableMiss (str): Next table for table-miss.
        - TableId (number): Specify the controller table identifier. Lower numbered tables are consulted first.
        - TableName (str): Specify the name of the controller table.
        - WildcardExperimenterData (str): The data of the wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterDataLength (number): The data length of the wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterField (number): The identifier for wildcard experimenter of Controller Table Experimenter.
        - WildcardExperimenterHasMask (bool): Mask If selected, the wildcard experimenter hash mask field of Controller Table Experimenter is available.
        - WildcardExperimenterId (number): The unique identifier for wildcard experimenter of Controller Table Experimenter.
        - WriteActionExperimenterData (str): The data of the Write Action Experimenter.
        - WriteActionExperimenterDataLength (number): The data length of the Write Action Miss Experimenter.
        - WriteActionExperimenterId (number): The unique identifier for Write Action Experimenter.
        - WriteActionMissExperimenterData (str): The data of the Write Action Miss Experimenter.
        - WriteActionMissExperimenterDataLength (number): The data length of the Write Action Miss Experimenter.
        - WriteActionMissExperimenterId (number): The unique identifier of Write Action Miss Experimenter.

        Returns
        -------
        - self: This instance with matching controllerTables resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of controllerTables data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the controllerTables resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def TableModificationTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the tableModificationTrigger operation on the server.

        NOT DEFINED

        tableModificationTrigger(async_operation=bool)bool
        --------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "tableModificationTrigger", payload=payload, response_object=None
        )
