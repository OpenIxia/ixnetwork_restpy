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


class ControllerTables(Base):
    """This view lists all the controller table features that can be configured.
    The ControllerTables class encapsulates a list of controllerTables resources that are managed by the user.
    A list of resources can be retrieved from the server using the ControllerTables.find() method.
    The list can be managed by using the ControllerTables.add() and ControllerTables.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'controllerTables'
    _SDM_ATT_MAP = {
        'ApplyActionExperimenterData': 'applyActionExperimenterData',
        'ApplyActionExperimenterDataLength': 'applyActionExperimenterDataLength',
        'ApplyActionExperimenterId': 'applyActionExperimenterId',
        'ApplyActionMissExperimenterData': 'applyActionMissExperimenterData',
        'ApplyActionMissExperimenterDataLength': 'applyActionMissExperimenterDataLength',
        'ApplyActionMissExperimenterId': 'applyActionMissExperimenterId',
        'Config': 'config',
        'Enabled': 'enabled',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'ExperimenterId': 'experimenterId',
        'ExperimenterMissData': 'experimenterMissData',
        'ExperimenterMissDataLength': 'experimenterMissDataLength',
        'ExperimenterMissId': 'experimenterMissId',
        'ExperimenterMissType': 'experimenterMissType',
        'ExperimenterType': 'experimenterType',
        'InstructionExperimenterData': 'instructionExperimenterData',
        'InstructionExperimenterDataLength': 'instructionExperimenterDataLength',
        'InstructionExperimenterId': 'instructionExperimenterId',
        'InstructionMissExperimenterData': 'instructionMissExperimenterData',
        'InstructionMissExperimenterDataLength': 'instructionMissExperimenterDataLength',
        'InstructionMissExperimenterId': 'instructionMissExperimenterId',
        'MatchExperimenterData': 'matchExperimenterData',
        'MatchExperimenterDataLength': 'matchExperimenterDataLength',
        'MatchExperimenterField': 'matchExperimenterField',
        'MatchExperimenterHasMask': 'matchExperimenterHasMask',
        'MatchExperimenterId': 'matchExperimenterId',
        'MaxEntries': 'maxEntries',
        'MetadataMatch': 'metadataMatch',
        'MetadataWrite': 'metadataWrite',
        'NextTable': 'nextTable',
        'NextTableMiss': 'nextTableMiss',
        'TableId': 'tableId',
        'TableName': 'tableName',
        'WildcardExperimenterData': 'wildcardExperimenterData',
        'WildcardExperimenterDataLength': 'wildcardExperimenterDataLength',
        'WildcardExperimenterField': 'wildcardExperimenterField',
        'WildcardExperimenterHasMask': 'wildcardExperimenterHasMask',
        'WildcardExperimenterId': 'wildcardExperimenterId',
        'WriteActionExperimenterData': 'writeActionExperimenterData',
        'WriteActionExperimenterDataLength': 'writeActionExperimenterDataLength',
        'WriteActionExperimenterId': 'writeActionExperimenterId',
        'WriteActionMissExperimenterData': 'writeActionMissExperimenterData',
        'WriteActionMissExperimenterDataLength': 'writeActionMissExperimenterDataLength',
        'WriteActionMissExperimenterId': 'writeActionMissExperimenterId',
    }

    def __init__(self, parent):
        super(ControllerTables, self).__init__(parent)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_7cc389d126607ec8b26d8ad9bd512718.ApplyActions): An instance of the ApplyActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactions_7cc389d126607ec8b26d8ad9bd512718 import ApplyActions
        return ApplyActions(self)._select()

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_a7d43275ef19fb4ebc8f9bbe939e313c.ApplyActionsMiss): An instance of the ApplyActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmiss_a7d43275ef19fb4ebc8f9bbe939e313c import ApplyActionsMiss
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
    def ControllerTableFlowRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertableflowranges_0f6872240515a222427575f97cf825e6.ControllerTableFlowRanges): An instance of the ControllerTableFlowRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertableflowranges_0f6872240515a222427575f97cf825e6 import ControllerTableFlowRanges
        return ControllerTableFlowRanges(self)

    @property
    def FeaturesSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_57abd318d46df3968689e589b041ed16.FeaturesSupported): An instance of the FeaturesSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.featuressupported_57abd318d46df3968689e589b041ed16 import FeaturesSupported
        return FeaturesSupported(self)._select()

    @property
    def Instruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_c2ff56ba96c610b35eec762a5079af51.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_c2ff56ba96c610b35eec762a5079af51 import Instruction
        return Instruction(self)._select()

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_4ca2fb2fcb8f5e871b966532ecd3a4b9.InstructionMiss): An instance of the InstructionMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmiss_4ca2fb2fcb8f5e871b966532ecd3a4b9 import InstructionMiss
        return InstructionMiss(self)._select()

    @property
    def Match(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_a5d285e29f18f9048c45c9030e3e0c6d.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_a5d285e29f18f9048c45c9030e3e0c6d import Match
        return Match(self)._select()

    @property
    def TableModificationTriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablemodificationtriggerattributes_2e754e1d82366b608f2ff76e36adebf5.TableModificationTriggerAttributes): An instance of the TableModificationTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablemodificationtriggerattributes_2e754e1d82366b608f2ff76e36adebf5 import TableModificationTriggerAttributes
        return TableModificationTriggerAttributes(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_f6ce08a881df2d49dd74d8486ec02dd5.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_f6ce08a881df2d49dd74d8486ec02dd5 import Wildcards
        return Wildcards(self)._select()

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_4d81d18c4276cc40dc486d8abe77992b.WriteActions): An instance of the WriteActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactions_4d81d18c4276cc40dc486d8abe77992b import WriteActions
        return WriteActions(self)._select()

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_7163b6294b0b33454cca0b3fae7dd77a.WriteActionsMiss): An instance of the WriteActionsMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmiss_7163b6294b0b33454cca0b3fae7dd77a import WriteActionsMiss
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
    def ApplyActionExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Apply Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionExperimenterData'])
    @ApplyActionExperimenterData.setter
    def ApplyActionExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActionExperimenterData'], value)

    @property
    def ApplyActionExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Apply Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionExperimenterDataLength'])
    @ApplyActionExperimenterDataLength.setter
    def ApplyActionExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActionExperimenterDataLength'], value)

    @property
    def ApplyActionExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for Apply Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionExperimenterId'])
    @ApplyActionExperimenterId.setter
    def ApplyActionExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActionExperimenterId'], value)

    @property
    def ApplyActionMissExperimenterData(self):
        """
        Returns
        -------
        - str: Experimenter Data The data of the apply action for table-miss of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionMissExperimenterData'])
    @ApplyActionMissExperimenterData.setter
    def ApplyActionMissExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActionMissExperimenterData'], value)

    @property
    def ApplyActionMissExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Apply Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionMissExperimenterDataLength'])
    @ApplyActionMissExperimenterDataLength.setter
    def ApplyActionMissExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActionMissExperimenterDataLength'], value)

    @property
    def ApplyActionMissExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for Apply Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionMissExperimenterId'])
    @ApplyActionMissExperimenterId.setter
    def ApplyActionMissExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActionMissExperimenterId'], value)

    @property
    def Config(self):
        """
        Returns
        -------
        - number: Specify the bitmap of OFPTC_* values. The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Config'])
    @Config.setter
    def Config(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Config'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If selected, this table is used in this controller configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterData'], value)

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'], value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterId'], value)

    @property
    def ExperimenterMissData(self):
        """
        Returns
        -------
        - str: The data of the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterMissData'])
    @ExperimenterMissData.setter
    def ExperimenterMissData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterMissData'], value)

    @property
    def ExperimenterMissDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterMissDataLength'])
    @ExperimenterMissDataLength.setter
    def ExperimenterMissDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterMissDataLength'], value)

    @property
    def ExperimenterMissId(self):
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterMissId'])
    @ExperimenterMissId.setter
    def ExperimenterMissId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterMissId'], value)

    @property
    def ExperimenterMissType(self):
        """
        Returns
        -------
        - number: The type of experimenter for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterMissType'])
    @ExperimenterMissType.setter
    def ExperimenterMissType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterMissType'], value)

    @property
    def ExperimenterType(self):
        """
        Returns
        -------
        - number: The type of experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterType'])
    @ExperimenterType.setter
    def ExperimenterType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterType'], value)

    @property
    def InstructionExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Instruction Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionExperimenterData'])
    @InstructionExperimenterData.setter
    def InstructionExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionExperimenterData'], value)

    @property
    def InstructionExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the experimental instruction of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionExperimenterDataLength'])
    @InstructionExperimenterDataLength.setter
    def InstructionExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionExperimenterDataLength'], value)

    @property
    def InstructionExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionExperimenterId'])
    @InstructionExperimenterId.setter
    def InstructionExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionExperimenterId'], value)

    @property
    def InstructionMissExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Instruction Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionMissExperimenterData'])
    @InstructionMissExperimenterData.setter
    def InstructionMissExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionMissExperimenterData'], value)

    @property
    def InstructionMissExperimenterDataLength(self):
        """
        Returns
        -------
        - number: It indicates the data length of the Instruction Miss Experimenter
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionMissExperimenterDataLength'])
    @InstructionMissExperimenterDataLength.setter
    def InstructionMissExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionMissExperimenterDataLength'], value)

    @property
    def InstructionMissExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier of Instruction Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionMissExperimenterId'])
    @InstructionMissExperimenterId.setter
    def InstructionMissExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionMissExperimenterId'], value)

    @property
    def MatchExperimenterData(self):
        """
        Returns
        -------
        - str: The match data of the Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchExperimenterData'])
    @MatchExperimenterData.setter
    def MatchExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchExperimenterData'], value)

    @property
    def MatchExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchExperimenterDataLength'])
    @MatchExperimenterDataLength.setter
    def MatchExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchExperimenterDataLength'], value)

    @property
    def MatchExperimenterField(self):
        """
        Returns
        -------
        - number: The identifier for match experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchExperimenterField'])
    @MatchExperimenterField.setter
    def MatchExperimenterField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchExperimenterField'], value)

    @property
    def MatchExperimenterHasMask(self):
        """
        Returns
        -------
        - bool: Mask If selected, the match experimenter hash mask field of Controller Table Experimenter is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchExperimenterHasMask'])
    @MatchExperimenterHasMask.setter
    def MatchExperimenterHasMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchExperimenterHasMask'], value)

    @property
    def MatchExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchExperimenterId'])
    @MatchExperimenterId.setter
    def MatchExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchExperimenterId'], value)

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - number: Specify the maximum number of entries supported. The default value is 0.
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
        - str: Specify the bits of metadata table that can match. The default value is 0.
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
        - str: Specify the bits of metadata table that can write. The default value is 0.
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
        - str: Next table property.
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
        - str: Next table for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTableMiss'])
    @NextTableMiss.setter
    def NextTableMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextTableMiss'], value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - number: Specify the controller table identifier. Lower numbered tables are consulted first.
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
        - str: Specify the name of the controller table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableName'])
    @TableName.setter
    def TableName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableName'], value)

    @property
    def WildcardExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WildcardExperimenterData'])
    @WildcardExperimenterData.setter
    def WildcardExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WildcardExperimenterData'], value)

    @property
    def WildcardExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WildcardExperimenterDataLength'])
    @WildcardExperimenterDataLength.setter
    def WildcardExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WildcardExperimenterDataLength'], value)

    @property
    def WildcardExperimenterField(self):
        """
        Returns
        -------
        - number: The identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WildcardExperimenterField'])
    @WildcardExperimenterField.setter
    def WildcardExperimenterField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WildcardExperimenterField'], value)

    @property
    def WildcardExperimenterHasMask(self):
        """
        Returns
        -------
        - bool: Mask If selected, the wildcard experimenter hash mask field of Controller Table Experimenter is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WildcardExperimenterHasMask'])
    @WildcardExperimenterHasMask.setter
    def WildcardExperimenterHasMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WildcardExperimenterHasMask'], value)

    @property
    def WildcardExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for wildcard experimenter of Controller Table Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WildcardExperimenterId'])
    @WildcardExperimenterId.setter
    def WildcardExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WildcardExperimenterId'], value)

    @property
    def WriteActionExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Write Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionExperimenterData'])
    @WriteActionExperimenterData.setter
    def WriteActionExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActionExperimenterData'], value)

    @property
    def WriteActionExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Write Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionExperimenterDataLength'])
    @WriteActionExperimenterDataLength.setter
    def WriteActionExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActionExperimenterDataLength'], value)

    @property
    def WriteActionExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier for Write Action Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionExperimenterId'])
    @WriteActionExperimenterId.setter
    def WriteActionExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActionExperimenterId'], value)

    @property
    def WriteActionMissExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Write Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionMissExperimenterData'])
    @WriteActionMissExperimenterData.setter
    def WriteActionMissExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActionMissExperimenterData'], value)

    @property
    def WriteActionMissExperimenterDataLength(self):
        """
        Returns
        -------
        - number: The data length of the Write Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionMissExperimenterDataLength'])
    @WriteActionMissExperimenterDataLength.setter
    def WriteActionMissExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActionMissExperimenterDataLength'], value)

    @property
    def WriteActionMissExperimenterId(self):
        """
        Returns
        -------
        - number: The unique identifier of Write Action Miss Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionMissExperimenterId'])
    @WriteActionMissExperimenterId.setter
    def WriteActionMissExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActionMissExperimenterId'], value)

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
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

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
