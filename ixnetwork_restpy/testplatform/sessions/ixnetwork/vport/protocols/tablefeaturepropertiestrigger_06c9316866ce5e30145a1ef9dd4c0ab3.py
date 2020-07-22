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


class TableFeaturePropertiesTrigger(Base):
    """NOT DEFINED
    The TableFeaturePropertiesTrigger class encapsulates a list of tableFeaturePropertiesTrigger resources that are managed by the system.
    A list of resources can be retrieved from the server using the TableFeaturePropertiesTrigger.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tableFeaturePropertiesTrigger'
    _SDM_ATT_MAP = {
        'EnableApplyAction': 'enableApplyAction',
        'EnableApplyActionMiss': 'enableApplyActionMiss',
        'EnableApplySetField': 'enableApplySetField',
        'EnableApplySetFieldMiss': 'enableApplySetFieldMiss',
        'EnableExperimenter': 'enableExperimenter',
        'EnableExperimenterMiss': 'enableExperimenterMiss',
        'EnableInstruction': 'enableInstruction',
        'EnableInstructionMiss': 'enableInstructionMiss',
        'EnableMatch': 'enableMatch',
        'EnableNextTable': 'enableNextTable',
        'EnableNextTableMiss': 'enableNextTableMiss',
        'EnableWildCard': 'enableWildCard',
        'EnableWriteAction': 'enableWriteAction',
        'EnableWriteActionMiss': 'enableWriteActionMiss',
        'EnableWriteSetField': 'enableWriteSetField',
        'EnableWriteSetFieldMiss': 'enableWriteSetFieldMiss',
    }

    def __init__(self, parent):
        super(TableFeaturePropertiesTrigger, self).__init__(parent)

    @property
    def ApplyAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyaction_5f19e44ef7a6476551ad861d7d848973.ApplyAction): An instance of the ApplyAction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyaction_5f19e44ef7a6476551ad861d7d848973 import ApplyAction
        return ApplyAction(self)._select()

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_e6b23962c8bce1122f48e2d1524a1440.ApplySetField): An instance of the ApplySetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_e6b23962c8bce1122f48e2d1524a1440 import ApplySetField
        return ApplySetField(self)._select()

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenter_7287c2eefb052d4fd9275cfe5d33a1fa.Experimenter): An instance of the Experimenter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenter_7287c2eefb052d4fd9275cfe5d33a1fa import Experimenter
        return Experimenter(self)._select()

    @property
    def Instruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_230e54cf6eb781accd789e6f5f926d4b.Instruction): An instance of the Instruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_230e54cf6eb781accd789e6f5f926d4b import Instruction
        return Instruction(self)._select()

    @property
    def Match(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_879bb990b5ac279b110de19ae3c0457e.Match): An instance of the Match class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_879bb990b5ac279b110de19ae3c0457e import Match
        return Match(self)._select()

    @property
    def NextTable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttable_d35c338fffb641fd6862a8b7f73322c7.NextTable): An instance of the NextTable class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttable_d35c338fffb641fd6862a8b7f73322c7 import NextTable
        return NextTable(self)._select()

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_019205c5e77f1f91299c1df55a6a8bc1.Wildcards): An instance of the Wildcards class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_019205c5e77f1f91299c1df55a6a8bc1 import Wildcards
        return Wildcards(self)._select()

    @property
    def WriteAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeaction_d9325d5c06ac893d06076cc31ddcb841.WriteAction): An instance of the WriteAction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeaction_d9325d5c06ac893d06076cc31ddcb841 import WriteAction
        return WriteAction(self)._select()

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_1940dec7b6d0dc2d6d97e62504b21e29.WriteSetField): An instance of the WriteSetField class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_1940dec7b6d0dc2d6d97e62504b21e29 import WriteSetField
        return WriteSetField(self)._select()

    @property
    def EnableApplyAction(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableApplyAction'])
    @EnableApplyAction.setter
    def EnableApplyAction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableApplyAction'], value)

    @property
    def EnableApplyActionMiss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableApplyActionMiss'])
    @EnableApplyActionMiss.setter
    def EnableApplyActionMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableApplyActionMiss'], value)

    @property
    def EnableApplySetField(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableApplySetField'])
    @EnableApplySetField.setter
    def EnableApplySetField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableApplySetField'], value)

    @property
    def EnableApplySetFieldMiss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableApplySetFieldMiss'])
    @EnableApplySetFieldMiss.setter
    def EnableApplySetFieldMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableApplySetFieldMiss'], value)

    @property
    def EnableExperimenter(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExperimenter'])
    @EnableExperimenter.setter
    def EnableExperimenter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExperimenter'], value)

    @property
    def EnableExperimenterMiss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExperimenterMiss'])
    @EnableExperimenterMiss.setter
    def EnableExperimenterMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExperimenterMiss'], value)

    @property
    def EnableInstruction(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableInstruction'])
    @EnableInstruction.setter
    def EnableInstruction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableInstruction'], value)

    @property
    def EnableInstructionMiss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableInstructionMiss'])
    @EnableInstructionMiss.setter
    def EnableInstructionMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableInstructionMiss'], value)

    @property
    def EnableMatch(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMatch'])
    @EnableMatch.setter
    def EnableMatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMatch'], value)

    @property
    def EnableNextTable(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableNextTable'])
    @EnableNextTable.setter
    def EnableNextTable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableNextTable'], value)

    @property
    def EnableNextTableMiss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableNextTableMiss'])
    @EnableNextTableMiss.setter
    def EnableNextTableMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableNextTableMiss'], value)

    @property
    def EnableWildCard(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableWildCard'])
    @EnableWildCard.setter
    def EnableWildCard(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableWildCard'], value)

    @property
    def EnableWriteAction(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableWriteAction'])
    @EnableWriteAction.setter
    def EnableWriteAction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableWriteAction'], value)

    @property
    def EnableWriteActionMiss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableWriteActionMiss'])
    @EnableWriteActionMiss.setter
    def EnableWriteActionMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableWriteActionMiss'], value)

    @property
    def EnableWriteSetField(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableWriteSetField'])
    @EnableWriteSetField.setter
    def EnableWriteSetField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableWriteSetField'], value)

    @property
    def EnableWriteSetFieldMiss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableWriteSetFieldMiss'])
    @EnableWriteSetFieldMiss.setter
    def EnableWriteSetFieldMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableWriteSetFieldMiss'], value)

    def update(self, EnableApplyAction=None, EnableApplyActionMiss=None, EnableApplySetField=None, EnableApplySetFieldMiss=None, EnableExperimenter=None, EnableExperimenterMiss=None, EnableInstruction=None, EnableInstructionMiss=None, EnableMatch=None, EnableNextTable=None, EnableNextTableMiss=None, EnableWildCard=None, EnableWriteAction=None, EnableWriteActionMiss=None, EnableWriteSetField=None, EnableWriteSetFieldMiss=None):
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

    def find(self, EnableApplyAction=None, EnableApplyActionMiss=None, EnableApplySetField=None, EnableApplySetFieldMiss=None, EnableExperimenter=None, EnableExperimenterMiss=None, EnableInstruction=None, EnableInstructionMiss=None, EnableMatch=None, EnableNextTable=None, EnableNextTableMiss=None, EnableWildCard=None, EnableWriteAction=None, EnableWriteActionMiss=None, EnableWriteSetField=None, EnableWriteSetFieldMiss=None):
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
