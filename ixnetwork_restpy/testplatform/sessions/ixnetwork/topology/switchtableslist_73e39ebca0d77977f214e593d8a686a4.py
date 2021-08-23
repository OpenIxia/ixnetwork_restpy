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
from typing import List, Any, Union


class SwitchTablesList(Base):
    """Openflow Switch Tables level Configuration
    The SwitchTablesList class encapsulates a list of switchTablesList resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchTablesList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchTablesList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ApplyActions': 'applyActions',
        'ApplyActionsMiss': 'applyActionsMiss',
        'ApplySetField': 'applySetField',
        'ApplySetFieldMask': 'applySetFieldMask',
        'ApplySetFieldMiss': 'applySetFieldMiss',
        'ApplySetFieldMissMask': 'applySetFieldMissMask',
        'AutoConfigNextTable': 'autoConfigNextTable',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'FeaturesSupported': 'featuresSupported',
        'Instruction': 'instruction',
        'InstructionMiss': 'instructionMiss',
        'Match': 'match',
        'MatchMask': 'matchMask',
        'MaxTableEntries': 'maxTableEntries',
        'MetadataMatch': 'metadataMatch',
        'MetadataWrite': 'metadataWrite',
        'Name': 'name',
        'NextTable': 'nextTable',
        'NextTableMiss': 'nextTableMiss',
        'ParentSwitch': 'parentSwitch',
        'TableId': 'tableId',
        'TableName': 'tableName',
        'WildcardFeature': 'wildcardFeature',
        'WildcardFeatureMask': 'wildcardFeatureMask',
        'WriteActions': 'writeActions',
        'WriteActionsMiss': 'writeActionsMiss',
        'WriteSetField': 'writeSetField',
        'WriteSetFieldMask': 'writeSetFieldMask',
        'WriteSetFieldMiss': 'writeSetFieldMiss',
        'WriteSetFieldMissMask': 'writeSetFieldMissMask',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(SwitchTablesList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ApplyActions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of apply action capability that the table will support. The selected actions associated with a flow are applied immediately
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ApplyActions']))

    @property
    def ApplyActionsMiss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of apply action miss capability that the table miss flow entry will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ApplyActionsMiss']))

    @property
    def ApplySetField(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Apply Set Field capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ApplySetField']))

    @property
    def ApplySetFieldMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Apply Set Field Mask capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ApplySetFieldMask']))

    @property
    def ApplySetFieldMiss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Apply Set Field Miss capability that the table miss flow entry will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ApplySetFieldMiss']))

    @property
    def ApplySetFieldMissMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Apply Set Field Miss capability that the table miss flow entry will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ApplySetFieldMissMask']))

    @property
    def AutoConfigNextTable(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Next Table and Next Table Miss are automatically configured
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoConfigNextTable']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def FeaturesSupported(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the table feature properties to enable them
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FeaturesSupported']))

    @property
    def Instruction(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Instructions that the table flow entry will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Instruction']))

    @property
    def InstructionMiss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Instruction miss capabilities that the table miss flow entry will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InstructionMiss']))

    @property
    def Match(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of match capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Match']))

    @property
    def MatchMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of match mask capability that the table will support.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MatchMask']))

    @property
    def MaxTableEntries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify Maximum Entries per Table.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTableEntries']))

    @property
    def MetadataMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the bits of Metadata which the table can match
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetadataMatch']))

    @property
    def MetadataWrite(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the bits of Metadata which the table can write
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetadataWrite']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NextTable(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the next table property (in incrementing order) seperated by , or - (for range) Eg: 1,2,3,4 or 1-4 or 1, 10-20.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextTable']))

    @property
    def NextTableMiss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the next table miss property (in incrementing order) seperated by , or - (for range) Eg: 1,2,3,4 or 1-4 or 1, 10-20.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextTableMiss']))

    @property
    def ParentSwitch(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Parent Switch Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['ParentSwitch'])

    @property
    def TableId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the Table Id, {0 - 254}
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TableId']))

    @property
    def TableName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the name of the Table.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TableName']))

    @property
    def WildcardFeature(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of wildcard capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WildcardFeature']))

    @property
    def WildcardFeatureMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of wildcard mask capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WildcardFeatureMask']))

    @property
    def WriteActions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of write action capability that the table will support. The selected actions are appended to the existing action set of the packet
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WriteActions']))

    @property
    def WriteActionsMiss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of write action miss capability that the table miss flow entry will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WriteActionsMiss']))

    @property
    def WriteSetField(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Write Set Field capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WriteSetField']))

    @property
    def WriteSetFieldMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Write Set Field Mask capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WriteSetFieldMask']))

    @property
    def WriteSetFieldMiss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Write Set Field Miss capability that the table miss flow entry will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WriteSetFieldMiss']))

    @property
    def WriteSetFieldMissMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of Write Set Field Miss mask capability that the table will support
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WriteSetFieldMissMask']))

    def update(self, Name=None):
        # type: (str) -> SwitchTablesList
        """Updates switchTablesList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        # type: (str) -> SwitchTablesList
        """Adds a new switchTablesList resource on the json, only valid with config assistant

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved switchTablesList resources using find and the newly added switchTablesList resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, ParentSwitch=None):
        # type: (int, str, str, str) -> SwitchTablesList
        """Finds and retrieves switchTablesList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchTablesList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchTablesList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ParentSwitch (str): Parent Switch Name

        Returns
        -------
        - self: This instance with matching switchTablesList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchTablesList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchTablesList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, ApplyActions=None, ApplyActionsMiss=None, ApplySetField=None, ApplySetFieldMask=None, ApplySetFieldMiss=None, ApplySetFieldMissMask=None, AutoConfigNextTable=None, FeaturesSupported=None, Instruction=None, InstructionMiss=None, Match=None, MatchMask=None, MaxTableEntries=None, MetadataMatch=None, MetadataWrite=None, NextTable=None, NextTableMiss=None, TableId=None, TableName=None, WildcardFeature=None, WildcardFeatureMask=None, WriteActions=None, WriteActionsMiss=None, WriteSetField=None, WriteSetFieldMask=None, WriteSetFieldMiss=None, WriteSetFieldMissMask=None):
        """Base class infrastructure that gets a list of switchTablesList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ApplyActions (str): optional regex of applyActions
        - ApplyActionsMiss (str): optional regex of applyActionsMiss
        - ApplySetField (str): optional regex of applySetField
        - ApplySetFieldMask (str): optional regex of applySetFieldMask
        - ApplySetFieldMiss (str): optional regex of applySetFieldMiss
        - ApplySetFieldMissMask (str): optional regex of applySetFieldMissMask
        - AutoConfigNextTable (str): optional regex of autoConfigNextTable
        - FeaturesSupported (str): optional regex of featuresSupported
        - Instruction (str): optional regex of instruction
        - InstructionMiss (str): optional regex of instructionMiss
        - Match (str): optional regex of match
        - MatchMask (str): optional regex of matchMask
        - MaxTableEntries (str): optional regex of maxTableEntries
        - MetadataMatch (str): optional regex of metadataMatch
        - MetadataWrite (str): optional regex of metadataWrite
        - NextTable (str): optional regex of nextTable
        - NextTableMiss (str): optional regex of nextTableMiss
        - TableId (str): optional regex of tableId
        - TableName (str): optional regex of tableName
        - WildcardFeature (str): optional regex of wildcardFeature
        - WildcardFeatureMask (str): optional regex of wildcardFeatureMask
        - WriteActions (str): optional regex of writeActions
        - WriteActionsMiss (str): optional regex of writeActionsMiss
        - WriteSetField (str): optional regex of writeSetField
        - WriteSetFieldMask (str): optional regex of writeSetFieldMask
        - WriteSetFieldMiss (str): optional regex of writeSetFieldMiss
        - WriteSetFieldMissMask (str): optional regex of writeSetFieldMissMask

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
