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


class ControllerTables(Base):
    """This view lists all the controller table features that can be configured.
    The ControllerTables class encapsulates a list of controllerTables resources that are managed by the user.
    A list of resources can be retrieved from the server using the ControllerTables.find() method.
    The list can be managed by using the ControllerTables.add() and ControllerTables.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'controllerTables'

    def __init__(self, parent):
        super(ControllerTables, self).__init__(parent)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_df8955851ad5d0673dd88b47b7369e35.ApplyActions): An instance of the ApplyActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_df8955851ad5d0673dd88b47b7369e35 import ApplyActions
        return ApplyActions(self)._select()

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_8ebb9c94e4a8550ba98f27d504d7e9dd.ApplyActionsMiss): An instance of the ApplyActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_8ebb9c94e4a8550ba98f27d504d7e9dd import ApplyActionsMiss
        return ApplyActionsMiss(self)._select()

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_d2709edccf7369b6b3923fe2b08a1dac.ApplySetField): An instance of the ApplySetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_d2709edccf7369b6b3923fe2b08a1dac import ApplySetField
        return ApplySetField(self)._select()

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_25a655c6dcc33830dac2c53ef1a0b8b9.ApplySetFieldMiss): An instance of the ApplySetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmiss_25a655c6dcc33830dac2c53ef1a0b8b9 import ApplySetFieldMiss
        return ApplySetFieldMiss(self)._select()

    @property
    def ControllerTableFlowRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertableflowranges_88b7d022d4061c169a3ec4c12bf4fcb0.ControllerTableFlowRanges): An instance of the ControllerTableFlowRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertableflowranges_88b7d022d4061c169a3ec4c12bf4fcb0 import ControllerTableFlowRanges
        return ControllerTableFlowRanges(self)

    @property
    def FeaturesSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_518a040c89e18b3809a31074121e3e3c.FeaturesSupported): An instance of the FeaturesSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_518a040c89e18b3809a31074121e3e3c import FeaturesSupported
        return FeaturesSupported(self)._select()

    @property
    def Instruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_fc4c8d936f9a47dfb9b78be59d9816fe.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_fc4c8d936f9a47dfb9b78be59d9816fe import Instruction
        return Instruction(self)._select()

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_ed6ad9a3510df5c276705931e63b5ced.InstructionMiss): An instance of the InstructionMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_ed6ad9a3510df5c276705931e63b5ced import InstructionMiss
        return InstructionMiss(self)._select()

    @property
    def Match(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_2409de9ca2e0bc083fcfe8a1c1b8a2d0.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_2409de9ca2e0bc083fcfe8a1c1b8a2d0 import Match
        return Match(self)._select()

    @property
    def TableModificationTriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablemodificationtriggerattributes_da2df8c4d69df02c66589255cb37f2ee.TableModificationTriggerAttributes): An instance of the TableModificationTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablemodificationtriggerattributes_da2df8c4d69df02c66589255cb37f2ee import TableModificationTriggerAttributes
        return TableModificationTriggerAttributes(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_e113074f6eac47b307248dd232bbc64f.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_e113074f6eac47b307248dd232bbc64f import Wildcards
        return Wildcards(self)._select()

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_859fb7a3fc2b09b85372f9e405104e53.WriteActions): An instance of the WriteActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_859fb7a3fc2b09b85372f9e405104e53 import WriteActions
        return WriteActions(self)._select()

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_6e6e3b702378be691e7c951333ee284c.WriteActionsMiss): An instance of the WriteActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_6e6e3b702378be691e7c951333ee284c import WriteActionsMiss
        return WriteActionsMiss(self)._select()

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_1ea0f4e35e89dda3c1e4eec50f631e87.WriteSetField): An instance of the WriteSetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_1ea0f4e35e89dda3c1e4eec50f631e87 import WriteSetField
        return WriteSetField(self)._select()

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_bd1b824bbc6181cb8a367ba9bfc78479.WriteSetFieldMiss): An instance of the WriteSetFieldMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmiss_bd1b824bbc6181cb8a367ba9bfc78479 import WriteSetFieldMiss
        return WriteSetFieldMiss(self)._select()

    @property
    def ApplyActionExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Apply Action Experimenter.
        """
        return self._get_attribute('applyActionExperimenterData')
    @ApplyActionExperimenterData.setter
    def ApplyActionExperimenterData(self, value):
        self._set_attribute('applyActionExperimenterData', value)

    @property
    def ApplyActionExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Apply Action Experimenter.
        """
        return self._get_attribute('applyActionExperimenterDataLength')
    @ApplyActionExperimenterDataLength.setter
    def ApplyActionExperimenterDataLength(self, value):
        self._set_attribute('applyActionExperimenterDataLength', value)

    @property
    def ApplyActionExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for Apply Action Experimenter.
        """
        return self._get_attribute('applyActionExperimenterId')
    @ApplyActionExperimenterId.setter
    def ApplyActionExperimenterId(self, value):
        self._set_attribute('applyActionExperimenterId', value)

    @property
    def ApplyActionMissExperimenterData(self):
        """
        Returns
        -------
        - str: Experimenter Data The data of the apply action for table-miss of Controller Table Experimenter.
        """
        return self._get_attribute('applyActionMissExperimenterData')
    @ApplyActionMissExperimenterData.setter
    def ApplyActionMissExperimenterData(self, value):
        self._set_attribute('applyActionMissExperimenterData', value)

    @property
    def ApplyActionMissExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Apply Action Miss Experimenter.
        """
        return self._get_attribute('applyActionMissExperimenterDataLength')
    @ApplyActionMissExperimenterDataLength.setter
    def ApplyActionMissExperimenterDataLength(self, value):
        self._set_attribute('applyActionMissExperimenterDataLength', value)

    @property
    def ApplyActionMissExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for Apply Action Miss Experimenter.
        """
        return self._get_attribute('applyActionMissExperimenterId')
    @ApplyActionMissExperimenterId.setter
    def ApplyActionMissExperimenterId(self, value):
        self._set_attribute('applyActionMissExperimenterId', value)

    @property
    def Config(self):
        """
        Returns
        -------
        - number: Specify the bitmap of OFPTC_* values. The default value is 0.
        """
        return self._get_attribute('config')
    @Config.setter
    def Config(self, value):
        self._set_attribute('config', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If selected, this table is used in this controller configuration.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Experimenter.
        """
        return self._get_attribute('experimenterData')
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute('experimenterData', value)

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Experimenter for table-miss.
        """
        return self._get_attribute('experimenterDataLength')
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute('experimenterDataLength', value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter.
        """
        return self._get_attribute('experimenterId')
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute('experimenterId', value)

    @property
    def ExperimenterMissData(self):
        """
        Returns
        -------
        - str: The data of the Experimenter for table-miss.
        """
        return self._get_attribute('experimenterMissData')
    @ExperimenterMissData.setter
    def ExperimenterMissData(self, value):
        self._set_attribute('experimenterMissData', value)

    @property
    def ExperimenterMissDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Experimenter for table-miss.
        """
        return self._get_attribute('experimenterMissDataLength')
    @ExperimenterMissDataLength.setter
    def ExperimenterMissDataLength(self, value):
        self._set_attribute('experimenterMissDataLength', value)

    @property
    def ExperimenterMissId(self):
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter for table-miss.
        """
        return self._get_attribute('experimenterMissId')
    @ExperimenterMissId.setter
    def ExperimenterMissId(self, value):
        self._set_attribute('experimenterMissId', value)

    @property
    def ExperimenterMissType(self):
        """
        Returns
        -------
        - number: The type of experimenter for table-miss.
        """
        return self._get_attribute('experimenterMissType')
    @ExperimenterMissType.setter
    def ExperimenterMissType(self, value):
        self._set_attribute('experimenterMissType', value)

    @property
    def ExperimenterType(self):
        """
        Returns
        -------
        - number: The type of experimenter.
        """
        return self._get_attribute('experimenterType')
    @ExperimenterType.setter
    def ExperimenterType(self, value):
        self._set_attribute('experimenterType', value)

    @property
    def InstructionExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Instruction Experimenter.
        """
        return self._get_attribute('instructionExperimenterData')
    @InstructionExperimenterData.setter
    def InstructionExperimenterData(self, value):
        self._set_attribute('instructionExperimenterData', value)

    @property
    def InstructionExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the experimental instruction of Controller Table Experimenter.
        """
        return self._get_attribute('instructionExperimenterDataLength')
    @InstructionExperimenterDataLength.setter
    def InstructionExperimenterDataLength(self, value):
        self._set_attribute('instructionExperimenterDataLength', value)

    @property
    def InstructionExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter.
        """
        return self._get_attribute('instructionExperimenterId')
    @InstructionExperimenterId.setter
    def InstructionExperimenterId(self, value):
        self._set_attribute('instructionExperimenterId', value)

    @property
    def InstructionMissExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Instruction Miss Experimenter.
        """
        return self._get_attribute('instructionMissExperimenterData')
    @InstructionMissExperimenterData.setter
    def InstructionMissExperimenterData(self, value):
        self._set_attribute('instructionMissExperimenterData', value)

    @property
    def InstructionMissExperimenterDataLength(self):
        """
        Returns
        -------
        - number: It indicates the data length of the Instruction Miss Experimenter
        """
        return self._get_attribute('instructionMissExperimenterDataLength')
    @InstructionMissExperimenterDataLength.setter
    def InstructionMissExperimenterDataLength(self, value):
        self._set_attribute('instructionMissExperimenterDataLength', value)

    @property
    def InstructionMissExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier of Instruction Miss Experimenter.
        """
        return self._get_attribute('instructionMissExperimenterId')
    @InstructionMissExperimenterId.setter
    def InstructionMissExperimenterId(self, value):
        self._set_attribute('instructionMissExperimenterId', value)

    @property
    def MatchExperimenterData(self):
        """
        Returns
        -------
        - str: The match data of the Controller Table Experimenter.
        """
        return self._get_attribute('matchExperimenterData')
    @MatchExperimenterData.setter
    def MatchExperimenterData(self, value):
        self._set_attribute('matchExperimenterData', value)

    @property
    def MatchExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute('matchExperimenterDataLength')
    @MatchExperimenterDataLength.setter
    def MatchExperimenterDataLength(self, value):
        self._set_attribute('matchExperimenterDataLength', value)

    @property
    def MatchExperimenterField(self):
        """
        Returns
        -------
        - number: The identifier for match experimenter of Controller Table Experimenter.
        """
        return self._get_attribute('matchExperimenterField')
    @MatchExperimenterField.setter
    def MatchExperimenterField(self, value):
        self._set_attribute('matchExperimenterField', value)

    @property
    def MatchExperimenterHasMask(self):
        """
        Returns
        -------
        - bool: Mask If selected, the match experimenter hash mask field of Controller Table Experimenter is available.
        """
        return self._get_attribute('matchExperimenterHasMask')
    @MatchExperimenterHasMask.setter
    def MatchExperimenterHasMask(self, value):
        self._set_attribute('matchExperimenterHasMask', value)

    @property
    def MatchExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute('matchExperimenterId')
    @MatchExperimenterId.setter
    def MatchExperimenterId(self, value):
        self._set_attribute('matchExperimenterId', value)

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - number: Specify the maximum number of entries supported. The default value is 0.
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
        - str: Specify the bits of metadata table that can match. The default value is 0.
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
        - str: Specify the bits of metadata table that can write. The default value is 0.
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
        - str: Next table property.
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
        - str: Next table for table-miss.
        """
        return self._get_attribute('nextTableMiss')
    @NextTableMiss.setter
    def NextTableMiss(self, value):
        self._set_attribute('nextTableMiss', value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - number: Specify the controller table identifier. Lower numbered tables are consulted first.
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
        - str: Specify the name of the controller table.
        """
        return self._get_attribute('tableName')
    @TableName.setter
    def TableName(self, value):
        self._set_attribute('tableName', value)

    @property
    def WildcardExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute('wildcardExperimenterData')
    @WildcardExperimenterData.setter
    def WildcardExperimenterData(self, value):
        self._set_attribute('wildcardExperimenterData', value)

    @property
    def WildcardExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute('wildcardExperimenterDataLength')
    @WildcardExperimenterDataLength.setter
    def WildcardExperimenterDataLength(self, value):
        self._set_attribute('wildcardExperimenterDataLength', value)

    @property
    def WildcardExperimenterField(self):
        """
        Returns
        -------
        - number: The identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute('wildcardExperimenterField')
    @WildcardExperimenterField.setter
    def WildcardExperimenterField(self, value):
        self._set_attribute('wildcardExperimenterField', value)

    @property
    def WildcardExperimenterHasMask(self):
        """
        Returns
        -------
        - bool: Mask If selected, the wildcard experimenter hash mask field of Controller Table Experimenter is available.
        """
        return self._get_attribute('wildcardExperimenterHasMask')
    @WildcardExperimenterHasMask.setter
    def WildcardExperimenterHasMask(self, value):
        self._set_attribute('wildcardExperimenterHasMask', value)

    @property
    def WildcardExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute('wildcardExperimenterId')
    @WildcardExperimenterId.setter
    def WildcardExperimenterId(self, value):
        self._set_attribute('wildcardExperimenterId', value)

    @property
    def WriteActionExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Write Action Experimenter.
        """
        return self._get_attribute('writeActionExperimenterData')
    @WriteActionExperimenterData.setter
    def WriteActionExperimenterData(self, value):
        self._set_attribute('writeActionExperimenterData', value)

    @property
    def WriteActionExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Write Action Miss Experimenter.
        """
        return self._get_attribute('writeActionExperimenterDataLength')
    @WriteActionExperimenterDataLength.setter
    def WriteActionExperimenterDataLength(self, value):
        self._set_attribute('writeActionExperimenterDataLength', value)

    @property
    def WriteActionExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for Write Action Experimenter.
        """
        return self._get_attribute('writeActionExperimenterId')
    @WriteActionExperimenterId.setter
    def WriteActionExperimenterId(self, value):
        self._set_attribute('writeActionExperimenterId', value)

    @property
    def WriteActionMissExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Write Action Miss Experimenter.
        """
        return self._get_attribute('writeActionMissExperimenterData')
    @WriteActionMissExperimenterData.setter
    def WriteActionMissExperimenterData(self, value):
        self._set_attribute('writeActionMissExperimenterData', value)

    @property
    def WriteActionMissExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Write Action Miss Experimenter.
        """
        return self._get_attribute('writeActionMissExperimenterDataLength')
    @WriteActionMissExperimenterDataLength.setter
    def WriteActionMissExperimenterDataLength(self, value):
        self._set_attribute('writeActionMissExperimenterDataLength', value)

    @property
    def WriteActionMissExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier of Write Action Miss Experimenter.
        """
        return self._get_attribute('writeActionMissExperimenterId')
    @WriteActionMissExperimenterId.setter
    def WriteActionMissExperimenterId(self, value):
        self._set_attribute('writeActionMissExperimenterId', value)

    def update(self, ApplyActionExperimenterData=None, ApplyActionExperimenterDataLength=None, ApplyActionExperimenterId=None, ApplyActionMissExperimenterData=None, ApplyActionMissExperimenterDataLength=None, ApplyActionMissExperimenterId=None, Config=None, Enabled=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterId=None, ExperimenterMissData=None, ExperimenterMissDataLength=None, ExperimenterMissId=None, ExperimenterMissType=None, ExperimenterType=None, InstructionExperimenterData=None, InstructionExperimenterDataLength=None, InstructionExperimenterId=None, InstructionMissExperimenterData=None, InstructionMissExperimenterDataLength=None, InstructionMissExperimenterId=None, MatchExperimenterData=None, MatchExperimenterDataLength=None, MatchExperimenterField=None, MatchExperimenterHasMask=None, MatchExperimenterId=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, TableId=None, TableName=None, WildcardExperimenterData=None, WildcardExperimenterDataLength=None, WildcardExperimenterField=None, WildcardExperimenterHasMask=None, WildcardExperimenterId=None, WriteActionExperimenterData=None, WriteActionExperimenterDataLength=None, WriteActionExperimenterId=None, WriteActionMissExperimenterData=None, WriteActionMissExperimenterDataLength=None, WriteActionMissExperimenterId=None):
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
        return self._update(locals())

    def add(self, ApplyActionExperimenterData=None, ApplyActionExperimenterDataLength=None, ApplyActionExperimenterId=None, ApplyActionMissExperimenterData=None, ApplyActionMissExperimenterDataLength=None, ApplyActionMissExperimenterId=None, Config=None, Enabled=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterId=None, ExperimenterMissData=None, ExperimenterMissDataLength=None, ExperimenterMissId=None, ExperimenterMissType=None, ExperimenterType=None, InstructionExperimenterData=None, InstructionExperimenterDataLength=None, InstructionExperimenterId=None, InstructionMissExperimenterData=None, InstructionMissExperimenterDataLength=None, InstructionMissExperimenterId=None, MatchExperimenterData=None, MatchExperimenterDataLength=None, MatchExperimenterField=None, MatchExperimenterHasMask=None, MatchExperimenterId=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, TableId=None, TableName=None, WildcardExperimenterData=None, WildcardExperimenterDataLength=None, WildcardExperimenterField=None, WildcardExperimenterHasMask=None, WildcardExperimenterId=None, WriteActionExperimenterData=None, WriteActionExperimenterDataLength=None, WriteActionExperimenterId=None, WriteActionMissExperimenterData=None, WriteActionMissExperimenterDataLength=None, WriteActionMissExperimenterId=None):
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
        return self._create(locals())

    def remove(self):
        """Deletes all the contained controllerTables resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ApplyActionExperimenterData=None, ApplyActionExperimenterDataLength=None, ApplyActionExperimenterId=None, ApplyActionMissExperimenterData=None, ApplyActionMissExperimenterDataLength=None, ApplyActionMissExperimenterId=None, Config=None, Enabled=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterId=None, ExperimenterMissData=None, ExperimenterMissDataLength=None, ExperimenterMissId=None, ExperimenterMissType=None, ExperimenterType=None, InstructionExperimenterData=None, InstructionExperimenterDataLength=None, InstructionExperimenterId=None, InstructionMissExperimenterData=None, InstructionMissExperimenterDataLength=None, InstructionMissExperimenterId=None, MatchExperimenterData=None, MatchExperimenterDataLength=None, MatchExperimenterField=None, MatchExperimenterHasMask=None, MatchExperimenterId=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, TableId=None, TableName=None, WildcardExperimenterData=None, WildcardExperimenterDataLength=None, WildcardExperimenterField=None, WildcardExperimenterHasMask=None, WildcardExperimenterId=None, WriteActionExperimenterData=None, WriteActionExperimenterDataLength=None, WriteActionExperimenterId=None, WriteActionMissExperimenterData=None, WriteActionMissExperimenterDataLength=None, WriteActionMissExperimenterId=None):
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
        return self._select(locals())

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

    def TableModificationTrigger(self):
        """Executes the tableModificationTrigger operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('tableModificationTrigger', payload=payload, response_object=None)
