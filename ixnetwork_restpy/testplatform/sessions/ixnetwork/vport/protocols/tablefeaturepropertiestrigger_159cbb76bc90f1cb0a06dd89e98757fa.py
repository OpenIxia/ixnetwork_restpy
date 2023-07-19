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


class TableFeaturePropertiesTrigger(Base):
    """NOT DEFINED
    The TableFeaturePropertiesTrigger class encapsulates a list of tableFeaturePropertiesTrigger resources that are managed by the system.
    A list of resources can be retrieved from the server using the TableFeaturePropertiesTrigger.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "tableFeaturePropertiesTrigger"
    _SDM_ATT_MAP = {
        "EnableApplyAction": "enableApplyAction",
        "EnableApplyActionMiss": "enableApplyActionMiss",
        "EnableApplySetField": "enableApplySetField",
        "EnableApplySetFieldMiss": "enableApplySetFieldMiss",
        "EnableExperimenter": "enableExperimenter",
        "EnableExperimenterMiss": "enableExperimenterMiss",
        "EnableInstruction": "enableInstruction",
        "EnableInstructionMiss": "enableInstructionMiss",
        "EnableMatch": "enableMatch",
        "EnableNextTable": "enableNextTable",
        "EnableNextTableMiss": "enableNextTableMiss",
        "EnableWildCard": "enableWildCard",
        "EnableWriteAction": "enableWriteAction",
        "EnableWriteActionMiss": "enableWriteActionMiss",
        "EnableWriteSetField": "enableWriteSetField",
        "EnableWriteSetFieldMiss": "enableWriteSetFieldMiss",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TableFeaturePropertiesTrigger, self).__init__(parent, list_op)

    @property
    def ApplyAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyaction_a25d2515972205bfadb3c4eee9b345a8.ApplyAction): An instance of the ApplyAction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyaction_a25d2515972205bfadb3c4eee9b345a8 import (
            ApplyAction,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplyAction", None) is not None:
                return self._properties.get("ApplyAction")
        return ApplyAction(self)._select()

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_7affd1e09afce28a240867653ece2b1a.ApplySetField): An instance of the ApplySetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_7affd1e09afce28a240867653ece2b1a import (
            ApplySetField,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplySetField", None) is not None:
                return self._properties.get("ApplySetField")
        return ApplySetField(self)._select()

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenter_8f62d5e59a1560c2f29a49b8273e32d9.Experimenter): An instance of the Experimenter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenter_8f62d5e59a1560c2f29a49b8273e32d9 import (
            Experimenter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Experimenter", None) is not None:
                return self._properties.get("Experimenter")
        return Experimenter(self)._select()

    @property
    def Instruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_0379cfa9d0d64cb1c14d9f8a669dcb24.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_0379cfa9d0d64cb1c14d9f8a669dcb24 import (
            Instruction,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Instruction", None) is not None:
                return self._properties.get("Instruction")
        return Instruction(self)._select()

    @property
    def Match(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_b032b60f8e92f6e0f66fded1be692b8f.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_b032b60f8e92f6e0f66fded1be692b8f import (
            Match,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Match", None) is not None:
                return self._properties.get("Match")
        return Match(self)._select()

    @property
    def NextTable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttable_b55e2ecee6a23216ce0f8a34c42b425a.NextTable): An instance of the NextTable class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttable_b55e2ecee6a23216ce0f8a34c42b425a import (
            NextTable,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NextTable", None) is not None:
                return self._properties.get("NextTable")
        return NextTable(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_97e68e3bd4a38aea6a66dc14629576e3.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_97e68e3bd4a38aea6a66dc14629576e3 import (
            Wildcards,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Wildcards", None) is not None:
                return self._properties.get("Wildcards")
        return Wildcards(self)._select()

    @property
    def WriteAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeaction_5ed4bf989119006d5d77872c8c5bf503.WriteAction): An instance of the WriteAction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeaction_5ed4bf989119006d5d77872c8c5bf503 import (
            WriteAction,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteAction", None) is not None:
                return self._properties.get("WriteAction")
        return WriteAction(self)._select()

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_f6680032f23d081fe60174c0337b285b.WriteSetField): An instance of the WriteSetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_f6680032f23d081fe60174c0337b285b import (
            WriteSetField,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WriteSetField", None) is not None:
                return self._properties.get("WriteSetField")
        return WriteSetField(self)._select()

    @property
    def EnableApplyAction(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableApplyAction"])

    @EnableApplyAction.setter
    def EnableApplyAction(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableApplyAction"], value)

    @property
    def EnableApplyActionMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableApplyActionMiss"])

    @EnableApplyActionMiss.setter
    def EnableApplyActionMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableApplyActionMiss"], value)

    @property
    def EnableApplySetField(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableApplySetField"])

    @EnableApplySetField.setter
    def EnableApplySetField(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableApplySetField"], value)

    @property
    def EnableApplySetFieldMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableApplySetFieldMiss"])

    @EnableApplySetFieldMiss.setter
    def EnableApplySetFieldMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableApplySetFieldMiss"], value)

    @property
    def EnableExperimenter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableExperimenter"])

    @EnableExperimenter.setter
    def EnableExperimenter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableExperimenter"], value)

    @property
    def EnableExperimenterMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableExperimenterMiss"])

    @EnableExperimenterMiss.setter
    def EnableExperimenterMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableExperimenterMiss"], value)

    @property
    def EnableInstruction(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableInstruction"])

    @EnableInstruction.setter
    def EnableInstruction(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableInstruction"], value)

    @property
    def EnableInstructionMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableInstructionMiss"])

    @EnableInstructionMiss.setter
    def EnableInstructionMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableInstructionMiss"], value)

    @property
    def EnableMatch(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMatch"])

    @EnableMatch.setter
    def EnableMatch(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMatch"], value)

    @property
    def EnableNextTable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableNextTable"])

    @EnableNextTable.setter
    def EnableNextTable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableNextTable"], value)

    @property
    def EnableNextTableMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableNextTableMiss"])

    @EnableNextTableMiss.setter
    def EnableNextTableMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableNextTableMiss"], value)

    @property
    def EnableWildCard(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableWildCard"])

    @EnableWildCard.setter
    def EnableWildCard(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableWildCard"], value)

    @property
    def EnableWriteAction(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableWriteAction"])

    @EnableWriteAction.setter
    def EnableWriteAction(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableWriteAction"], value)

    @property
    def EnableWriteActionMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableWriteActionMiss"])

    @EnableWriteActionMiss.setter
    def EnableWriteActionMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableWriteActionMiss"], value)

    @property
    def EnableWriteSetField(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableWriteSetField"])

    @EnableWriteSetField.setter
    def EnableWriteSetField(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableWriteSetField"], value)

    @property
    def EnableWriteSetFieldMiss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableWriteSetFieldMiss"])

    @EnableWriteSetFieldMiss.setter
    def EnableWriteSetFieldMiss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableWriteSetFieldMiss"], value)

    def update(
        self,
        EnableApplyAction=None,
        EnableApplyActionMiss=None,
        EnableApplySetField=None,
        EnableApplySetFieldMiss=None,
        EnableExperimenter=None,
        EnableExperimenterMiss=None,
        EnableInstruction=None,
        EnableInstructionMiss=None,
        EnableMatch=None,
        EnableNextTable=None,
        EnableNextTableMiss=None,
        EnableWildCard=None,
        EnableWriteAction=None,
        EnableWriteActionMiss=None,
        EnableWriteSetField=None,
        EnableWriteSetFieldMiss=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> TableFeaturePropertiesTrigger
        """Updates tableFeaturePropertiesTrigger resource on the server.

        Args
        ----
        - EnableApplyAction (bool): NOT DEFINED
        - EnableApplyActionMiss (bool): NOT DEFINED
        - EnableApplySetField (bool): NOT DEFINED
        - EnableApplySetFieldMiss (bool): NOT DEFINED
        - EnableExperimenter (bool): NOT DEFINED
        - EnableExperimenterMiss (bool): NOT DEFINED
        - EnableInstruction (bool): NOT DEFINED
        - EnableInstructionMiss (bool): NOT DEFINED
        - EnableMatch (bool): NOT DEFINED
        - EnableNextTable (bool): NOT DEFINED
        - EnableNextTableMiss (bool): NOT DEFINED
        - EnableWildCard (bool): NOT DEFINED
        - EnableWriteAction (bool): NOT DEFINED
        - EnableWriteActionMiss (bool): NOT DEFINED
        - EnableWriteSetField (bool): NOT DEFINED
        - EnableWriteSetFieldMiss (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        EnableApplyAction=None,
        EnableApplyActionMiss=None,
        EnableApplySetField=None,
        EnableApplySetFieldMiss=None,
        EnableExperimenter=None,
        EnableExperimenterMiss=None,
        EnableInstruction=None,
        EnableInstructionMiss=None,
        EnableMatch=None,
        EnableNextTable=None,
        EnableNextTableMiss=None,
        EnableWildCard=None,
        EnableWriteAction=None,
        EnableWriteActionMiss=None,
        EnableWriteSetField=None,
        EnableWriteSetFieldMiss=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> TableFeaturePropertiesTrigger
        """Adds a new tableFeaturePropertiesTrigger resource on the json, only valid with batch add utility

        Args
        ----
        - EnableApplyAction (bool): NOT DEFINED
        - EnableApplyActionMiss (bool): NOT DEFINED
        - EnableApplySetField (bool): NOT DEFINED
        - EnableApplySetFieldMiss (bool): NOT DEFINED
        - EnableExperimenter (bool): NOT DEFINED
        - EnableExperimenterMiss (bool): NOT DEFINED
        - EnableInstruction (bool): NOT DEFINED
        - EnableInstructionMiss (bool): NOT DEFINED
        - EnableMatch (bool): NOT DEFINED
        - EnableNextTable (bool): NOT DEFINED
        - EnableNextTableMiss (bool): NOT DEFINED
        - EnableWildCard (bool): NOT DEFINED
        - EnableWriteAction (bool): NOT DEFINED
        - EnableWriteActionMiss (bool): NOT DEFINED
        - EnableWriteSetField (bool): NOT DEFINED
        - EnableWriteSetFieldMiss (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved tableFeaturePropertiesTrigger resources using find and the newly added tableFeaturePropertiesTrigger resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableApplyAction=None,
        EnableApplyActionMiss=None,
        EnableApplySetField=None,
        EnableApplySetFieldMiss=None,
        EnableExperimenter=None,
        EnableExperimenterMiss=None,
        EnableInstruction=None,
        EnableInstructionMiss=None,
        EnableMatch=None,
        EnableNextTable=None,
        EnableNextTableMiss=None,
        EnableWildCard=None,
        EnableWriteAction=None,
        EnableWriteActionMiss=None,
        EnableWriteSetField=None,
        EnableWriteSetFieldMiss=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> TableFeaturePropertiesTrigger
        """Finds and retrieves tableFeaturePropertiesTrigger resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tableFeaturePropertiesTrigger resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tableFeaturePropertiesTrigger resources from the server.

        Args
        ----
        - EnableApplyAction (bool): NOT DEFINED
        - EnableApplyActionMiss (bool): NOT DEFINED
        - EnableApplySetField (bool): NOT DEFINED
        - EnableApplySetFieldMiss (bool): NOT DEFINED
        - EnableExperimenter (bool): NOT DEFINED
        - EnableExperimenterMiss (bool): NOT DEFINED
        - EnableInstruction (bool): NOT DEFINED
        - EnableInstructionMiss (bool): NOT DEFINED
        - EnableMatch (bool): NOT DEFINED
        - EnableNextTable (bool): NOT DEFINED
        - EnableNextTableMiss (bool): NOT DEFINED
        - EnableWildCard (bool): NOT DEFINED
        - EnableWriteAction (bool): NOT DEFINED
        - EnableWriteActionMiss (bool): NOT DEFINED
        - EnableWriteSetField (bool): NOT DEFINED
        - EnableWriteSetFieldMiss (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with matching tableFeaturePropertiesTrigger resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tableFeaturePropertiesTrigger data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tableFeaturePropertiesTrigger resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
