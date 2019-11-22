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


class TableFeaturePropertiesTrigger(Base):
    """NOT DEFINED
    The TableFeaturePropertiesTrigger class encapsulates a list of tableFeaturePropertiesTrigger resources that is managed by the system.
    A list of resources can be retrieved from the server using the TableFeaturePropertiesTrigger.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tableFeaturePropertiesTrigger'

    def __init__(self, parent):
        super(TableFeaturePropertiesTrigger, self).__init__(parent)

    @property
    def ApplyAction(self):
        """An instance of the ApplyAction class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyaction_633906bee6dc51881afe8b20b65f44ef.ApplyAction)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyaction_633906bee6dc51881afe8b20b65f44ef import ApplyAction
        return ApplyAction(self)._select()

    @property
    def ApplySetField(self):
        """An instance of the ApplySetField class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_572d77e48506d06b8db159abf9fa3958.ApplySetField)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfield_572d77e48506d06b8db159abf9fa3958 import ApplySetField
        return ApplySetField(self)._select()

    @property
    def Experimenter(self):
        """An instance of the Experimenter class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenter_1e86539bbd8246f9fbafa9002750bee5.Experimenter)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenter_1e86539bbd8246f9fbafa9002750bee5 import Experimenter
        return Experimenter(self)._select()

    @property
    def Instruction(self):
        """An instance of the Instruction class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_1b36aef679f12d2d2e464c522f806580.Instruction)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instruction_1b36aef679f12d2d2e464c522f806580 import Instruction
        return Instruction(self)._select()

    @property
    def Match(self):
        """An instance of the Match class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_0b8c9ee718c93fb4129fc8ee7adec7c9.Match)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.match_0b8c9ee718c93fb4129fc8ee7adec7c9 import Match
        return Match(self)._select()

    @property
    def NextTable(self):
        """An instance of the NextTable class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttable_67b9a2e36b46d601ccf577ba4899664f.NextTable)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttable_67b9a2e36b46d601ccf577ba4899664f import NextTable
        return NextTable(self)._select()

    @property
    def Wildcards(self):
        """An instance of the Wildcards class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_4d030fcc0ae5ea04342d9e702144dc8d.Wildcards)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcards_4d030fcc0ae5ea04342d9e702144dc8d import Wildcards
        return Wildcards(self)._select()

    @property
    def WriteAction(self):
        """An instance of the WriteAction class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeaction_4650ae2649e86d04ae31941f225fc0fc.WriteAction)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeaction_4650ae2649e86d04ae31941f225fc0fc import WriteAction
        return WriteAction(self)._select()

    @property
    def WriteSetField(self):
        """An instance of the WriteSetField class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_597a322894b20f4be62ea442bb4c2cbb.WriteSetField)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfield_597a322894b20f4be62ea442bb4c2cbb import WriteSetField
        return WriteSetField(self)._select()

    @property
    def EnableApplyAction(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableApplyAction')
    @EnableApplyAction.setter
    def EnableApplyAction(self, value):
        self._set_attribute('enableApplyAction', value)

    @property
    def EnableApplyActionMiss(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableApplyActionMiss')
    @EnableApplyActionMiss.setter
    def EnableApplyActionMiss(self, value):
        self._set_attribute('enableApplyActionMiss', value)

    @property
    def EnableApplySetField(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableApplySetField')
    @EnableApplySetField.setter
    def EnableApplySetField(self, value):
        self._set_attribute('enableApplySetField', value)

    @property
    def EnableApplySetFieldMiss(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableApplySetFieldMiss')
    @EnableApplySetFieldMiss.setter
    def EnableApplySetFieldMiss(self, value):
        self._set_attribute('enableApplySetFieldMiss', value)

    @property
    def EnableExperimenter(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableExperimenter')
    @EnableExperimenter.setter
    def EnableExperimenter(self, value):
        self._set_attribute('enableExperimenter', value)

    @property
    def EnableExperimenterMiss(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableExperimenterMiss')
    @EnableExperimenterMiss.setter
    def EnableExperimenterMiss(self, value):
        self._set_attribute('enableExperimenterMiss', value)

    @property
    def EnableInstruction(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableInstruction')
    @EnableInstruction.setter
    def EnableInstruction(self, value):
        self._set_attribute('enableInstruction', value)

    @property
    def EnableInstructionMiss(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableInstructionMiss')
    @EnableInstructionMiss.setter
    def EnableInstructionMiss(self, value):
        self._set_attribute('enableInstructionMiss', value)

    @property
    def EnableMatch(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableMatch')
    @EnableMatch.setter
    def EnableMatch(self, value):
        self._set_attribute('enableMatch', value)

    @property
    def EnableNextTable(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableNextTable')
    @EnableNextTable.setter
    def EnableNextTable(self, value):
        self._set_attribute('enableNextTable', value)

    @property
    def EnableNextTableMiss(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableNextTableMiss')
    @EnableNextTableMiss.setter
    def EnableNextTableMiss(self, value):
        self._set_attribute('enableNextTableMiss', value)

    @property
    def EnableWildCard(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableWildCard')
    @EnableWildCard.setter
    def EnableWildCard(self, value):
        self._set_attribute('enableWildCard', value)

    @property
    def EnableWriteAction(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableWriteAction')
    @EnableWriteAction.setter
    def EnableWriteAction(self, value):
        self._set_attribute('enableWriteAction', value)

    @property
    def EnableWriteActionMiss(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableWriteActionMiss')
    @EnableWriteActionMiss.setter
    def EnableWriteActionMiss(self, value):
        self._set_attribute('enableWriteActionMiss', value)

    @property
    def EnableWriteSetField(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableWriteSetField')
    @EnableWriteSetField.setter
    def EnableWriteSetField(self, value):
        self._set_attribute('enableWriteSetField', value)

    @property
    def EnableWriteSetFieldMiss(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('enableWriteSetFieldMiss')
    @EnableWriteSetFieldMiss.setter
    def EnableWriteSetFieldMiss(self, value):
        self._set_attribute('enableWriteSetFieldMiss', value)

    def update(self, EnableApplyAction=None, EnableApplyActionMiss=None, EnableApplySetField=None, EnableApplySetFieldMiss=None, EnableExperimenter=None, EnableExperimenterMiss=None, EnableInstruction=None, EnableInstructionMiss=None, EnableMatch=None, EnableNextTable=None, EnableNextTableMiss=None, EnableWildCard=None, EnableWriteAction=None, EnableWriteActionMiss=None, EnableWriteSetField=None, EnableWriteSetFieldMiss=None):
        """Updates a child instance of tableFeaturePropertiesTrigger on the server.

        Args:
            EnableApplyAction (bool): NOT DEFINED
            EnableApplyActionMiss (bool): NOT DEFINED
            EnableApplySetField (bool): NOT DEFINED
            EnableApplySetFieldMiss (bool): NOT DEFINED
            EnableExperimenter (bool): NOT DEFINED
            EnableExperimenterMiss (bool): NOT DEFINED
            EnableInstruction (bool): NOT DEFINED
            EnableInstructionMiss (bool): NOT DEFINED
            EnableMatch (bool): NOT DEFINED
            EnableNextTable (bool): NOT DEFINED
            EnableNextTableMiss (bool): NOT DEFINED
            EnableWildCard (bool): NOT DEFINED
            EnableWriteAction (bool): NOT DEFINED
            EnableWriteActionMiss (bool): NOT DEFINED
            EnableWriteSetField (bool): NOT DEFINED
            EnableWriteSetFieldMiss (bool): NOT DEFINED

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, EnableApplyAction=None, EnableApplyActionMiss=None, EnableApplySetField=None, EnableApplySetFieldMiss=None, EnableExperimenter=None, EnableExperimenterMiss=None, EnableInstruction=None, EnableInstructionMiss=None, EnableMatch=None, EnableNextTable=None, EnableNextTableMiss=None, EnableWildCard=None, EnableWriteAction=None, EnableWriteActionMiss=None, EnableWriteSetField=None, EnableWriteSetFieldMiss=None):
        """Finds and retrieves tableFeaturePropertiesTrigger data from the server.

        All named parameters support regex and can be used to selectively retrieve tableFeaturePropertiesTrigger data from the server.
        By default the find method takes no parameters and will retrieve all tableFeaturePropertiesTrigger data from the server.

        Args:
            EnableApplyAction (bool): NOT DEFINED
            EnableApplyActionMiss (bool): NOT DEFINED
            EnableApplySetField (bool): NOT DEFINED
            EnableApplySetFieldMiss (bool): NOT DEFINED
            EnableExperimenter (bool): NOT DEFINED
            EnableExperimenterMiss (bool): NOT DEFINED
            EnableInstruction (bool): NOT DEFINED
            EnableInstructionMiss (bool): NOT DEFINED
            EnableMatch (bool): NOT DEFINED
            EnableNextTable (bool): NOT DEFINED
            EnableNextTableMiss (bool): NOT DEFINED
            EnableWildCard (bool): NOT DEFINED
            EnableWriteAction (bool): NOT DEFINED
            EnableWriteActionMiss (bool): NOT DEFINED
            EnableWriteSetField (bool): NOT DEFINED
            EnableWriteSetFieldMiss (bool): NOT DEFINED

        Returns:
            self: This instance with matching tableFeaturePropertiesTrigger data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of tableFeaturePropertiesTrigger data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the tableFeaturePropertiesTrigger data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
