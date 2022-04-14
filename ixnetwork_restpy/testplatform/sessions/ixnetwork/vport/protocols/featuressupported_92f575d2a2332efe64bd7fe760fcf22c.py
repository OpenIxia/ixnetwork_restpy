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


class FeaturesSupported(Base):
    """Select the table feature properties to enable them. These describe various capabilities of the table.
    The FeaturesSupported class encapsulates a required featuresSupported resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "featuresSupported"
    _SDM_ATT_MAP = {
        "ApplyActions": "applyActions",
        "ApplyActionsMiss": "applyActionsMiss",
        "ApplySetField": "applySetField",
        "ApplySetFieldMiss": "applySetFieldMiss",
        "Instruction": "instruction",
        "InstructionMiss": "instructionMiss",
        "Match": "match",
        "NextTable": "nextTable",
        "NextTableMiss": "nextTableMiss",
        "Wildcards": "wildcards",
        "WriteActions": "writeActions",
        "WriteActionsMiss": "writeActionsMiss",
        "WriteSetField": "writeSetField",
        "WriteSetFieldMiss": "writeSetFieldMiss",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FeaturesSupported, self).__init__(parent, list_op)

    @property
    def ApplyActions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of apply action capability that the table will support. The selected actions associated with a flow are applied immediately.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActions"])

    @ApplyActions.setter
    def ApplyActions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyActions"], value)

    @property
    def ApplyActionsMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of apply action miss capability that the table miss flow entry will support.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActionsMiss"])

    @ApplyActionsMiss.setter
    def ApplyActionsMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyActionsMiss"], value)

    @property
    def ApplySetField(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Apply set field property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplySetField"])

    @ApplySetField.setter
    def ApplySetField(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplySetField"], value)

    @property
    def ApplySetFieldMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Apply set field for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplySetFieldMiss"])

    @ApplySetFieldMiss.setter
    def ApplySetFieldMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplySetFieldMiss"], value)

    @property
    def Instruction(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of instructions that the table flow entry will support.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Instruction"])

    @Instruction.setter
    def Instruction(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Instruction"], value)

    @property
    def InstructionMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of instruction miss capabilities that the table miss flow entry will support.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstructionMiss"])

    @InstructionMiss.setter
    def InstructionMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InstructionMiss"], value)

    @property
    def Match(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of match capability that the table will support.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Match"])

    @Match.setter
    def Match(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Match"], value)

    @property
    def NextTable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Specify the next table property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextTable"])

    @NextTable.setter
    def NextTable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextTable"], value)

    @property
    def NextTableMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Specify the next table-miss property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextTableMiss"])

    @NextTableMiss.setter
    def NextTableMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextTableMiss"], value)

    @property
    def Wildcards(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of wildcard capability that the table will support.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Wildcards"])

    @Wildcards.setter
    def Wildcards(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Wildcards"], value)

    @property
    def WriteActions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of write action capability that the table will support. The selected actions are appended to the existing action set of the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActions"])

    @WriteActions.setter
    def WriteActions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteActions"], value)

    @property
    def WriteActionsMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select the type of write action miss capability that the table miss flow entry will support.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActionsMiss"])

    @WriteActionsMiss.setter
    def WriteActionsMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteActionsMiss"], value)

    @property
    def WriteSetField(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Write set field property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteSetField"])

    @WriteSetField.setter
    def WriteSetField(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteSetField"], value)

    @property
    def WriteSetFieldMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Write set field for table-miss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteSetFieldMiss"])

    @WriteSetFieldMiss.setter
    def WriteSetFieldMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteSetFieldMiss"], value)

    def update(
        self,
        ApplyActions=None,
        ApplyActionsMiss=None,
        ApplySetField=None,
        ApplySetFieldMiss=None,
        Instruction=None,
        InstructionMiss=None,
        Match=None,
        NextTable=None,
        NextTableMiss=None,
        Wildcards=None,
        WriteActions=None,
        WriteActionsMiss=None,
        WriteSetField=None,
        WriteSetFieldMiss=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> FeaturesSupported
        """Updates featuresSupported resource on the server.

        Args
        ----
        - ApplyActions (bool): Select the type of apply action capability that the table will support. The selected actions associated with a flow are applied immediately.
        - ApplyActionsMiss (bool): Select the type of apply action miss capability that the table miss flow entry will support.
        - ApplySetField (bool): Apply set field property.
        - ApplySetFieldMiss (bool): Apply set field for table-miss.
        - Instruction (bool): Select the type of instructions that the table flow entry will support.
        - InstructionMiss (bool): Select the type of instruction miss capabilities that the table miss flow entry will support.
        - Match (bool): Select the type of match capability that the table will support.
        - NextTable (bool): Specify the next table property.
        - NextTableMiss (bool): Specify the next table-miss property.
        - Wildcards (bool): Select the type of wildcard capability that the table will support.
        - WriteActions (bool): Select the type of write action capability that the table will support. The selected actions are appended to the existing action set of the packet.
        - WriteActionsMiss (bool): Select the type of write action miss capability that the table miss flow entry will support.
        - WriteSetField (bool): Write set field property.
        - WriteSetFieldMiss (bool): Write set field for table-miss.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ApplyActions=None,
        ApplyActionsMiss=None,
        ApplySetField=None,
        ApplySetFieldMiss=None,
        Instruction=None,
        InstructionMiss=None,
        Match=None,
        NextTable=None,
        NextTableMiss=None,
        Wildcards=None,
        WriteActions=None,
        WriteActionsMiss=None,
        WriteSetField=None,
        WriteSetFieldMiss=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> FeaturesSupported
        """Finds and retrieves featuresSupported resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve featuresSupported resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all featuresSupported resources from the server.

        Args
        ----
        - ApplyActions (bool): Select the type of apply action capability that the table will support. The selected actions associated with a flow are applied immediately.
        - ApplyActionsMiss (bool): Select the type of apply action miss capability that the table miss flow entry will support.
        - ApplySetField (bool): Apply set field property.
        - ApplySetFieldMiss (bool): Apply set field for table-miss.
        - Instruction (bool): Select the type of instructions that the table flow entry will support.
        - InstructionMiss (bool): Select the type of instruction miss capabilities that the table miss flow entry will support.
        - Match (bool): Select the type of match capability that the table will support.
        - NextTable (bool): Specify the next table property.
        - NextTableMiss (bool): Specify the next table-miss property.
        - Wildcards (bool): Select the type of wildcard capability that the table will support.
        - WriteActions (bool): Select the type of write action capability that the table will support. The selected actions are appended to the existing action set of the packet.
        - WriteActionsMiss (bool): Select the type of write action miss capability that the table miss flow entry will support.
        - WriteSetField (bool): Write set field property.
        - WriteSetFieldMiss (bool): Write set field for table-miss.

        Returns
        -------
        - self: This instance with matching featuresSupported resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of featuresSupported data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the featuresSupported resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
