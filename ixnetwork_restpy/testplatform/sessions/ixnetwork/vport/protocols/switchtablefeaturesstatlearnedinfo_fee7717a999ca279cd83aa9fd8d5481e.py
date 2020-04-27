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


class SwitchTableFeaturesStatLearnedInfo(Base):
    """NOT DEFINED
    The SwitchTableFeaturesStatLearnedInfo class encapsulates a list of switchTableFeaturesStatLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchTableFeaturesStatLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchTableFeaturesStatLearnedInfo'

    def __init__(self, parent):
        super(SwitchTableFeaturesStatLearnedInfo, self).__init__(parent)

    @property
    def ApplyActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_4a97c4f51e9d87770e3988307b915708.ApplyActionsLearnedInfo): An instance of the ApplyActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_4a97c4f51e9d87770e3988307b915708 import ApplyActionsLearnedInfo
        return ApplyActionsLearnedInfo(self)

    @property
    def ApplyActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_486b9142c5d34762f56442c90b4048c8.ApplyActionsMissLearnedInfo): An instance of the ApplyActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_486b9142c5d34762f56442c90b4048c8 import ApplyActionsMissLearnedInfo
        return ApplyActionsMissLearnedInfo(self)

    @property
    def ApplySetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_9e3ff36f7f45c1e30233699dd25a6cef.ApplySetFieldLearnedInfo): An instance of the ApplySetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_9e3ff36f7f45c1e30233699dd25a6cef import ApplySetFieldLearnedInfo
        return ApplySetFieldLearnedInfo(self)

    @property
    def ApplySetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_44dfe00c20e7d9f54dcff79e1141d8a2.ApplySetFieldMissLearnedInfo): An instance of the ApplySetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_44dfe00c20e7d9f54dcff79e1141d8a2 import ApplySetFieldMissLearnedInfo
        return ApplySetFieldMissLearnedInfo(self)

    @property
    def InstructionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_b2804e7ee13264783e7d0abf06ae2385.InstructionLearnedInfo): An instance of the InstructionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_b2804e7ee13264783e7d0abf06ae2385 import InstructionLearnedInfo
        return InstructionLearnedInfo(self)

    @property
    def InstructionMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_bc3df895de534149dfed6eb4add041cc.InstructionMissLearnedInfo): An instance of the InstructionMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_bc3df895de534149dfed6eb4add041cc import InstructionMissLearnedInfo
        return InstructionMissLearnedInfo(self)

    @property
    def MatchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_fc28760575218a919685028100157eda.MatchLearnedInfo): An instance of the MatchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_fc28760575218a919685028100157eda import MatchLearnedInfo
        return MatchLearnedInfo(self)

    @property
    def NextTableLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_a97ba49d05eba9f7a67a48a477142d08.NextTableLearnedInfo): An instance of the NextTableLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_a97ba49d05eba9f7a67a48a477142d08 import NextTableLearnedInfo
        return NextTableLearnedInfo(self)

    @property
    def NextTableMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_27d34f9aa317996ae6caed0b23e008e1.NextTableMissLearnedInfo): An instance of the NextTableMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_27d34f9aa317996ae6caed0b23e008e1 import NextTableMissLearnedInfo
        return NextTableMissLearnedInfo(self)

    @property
    def WildcardsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_19391dd7219deab4a9f261267d938e66.WildcardsLearnedInfo): An instance of the WildcardsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_19391dd7219deab4a9f261267d938e66 import WildcardsLearnedInfo
        return WildcardsLearnedInfo(self)

    @property
    def WriteActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_5f46b381f7e5ac0805d8b4f4877630f4.WriteActionsLearnedInfo): An instance of the WriteActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_5f46b381f7e5ac0805d8b4f4877630f4 import WriteActionsLearnedInfo
        return WriteActionsLearnedInfo(self)

    @property
    def WriteActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_246b612f13aca93704589b73dafb0d39.WriteActionsMissLearnedInfo): An instance of the WriteActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_246b612f13aca93704589b73dafb0d39 import WriteActionsMissLearnedInfo
        return WriteActionsMissLearnedInfo(self)

    @property
    def WriteSetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_2f93d4d8610f13a442b66ecedf42bb05.WriteSetFieldLearnedInfo): An instance of the WriteSetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_2f93d4d8610f13a442b66ecedf42bb05 import WriteSetFieldLearnedInfo
        return WriteSetFieldLearnedInfo(self)

    @property
    def WriteSetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_eb3703d8a6e53415e9fc4c946d24a44d.WriteSetFieldMissLearnedInfo): An instance of the WriteSetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_eb3703d8a6e53415e9fc4c946d24a44d import WriteSetFieldMissLearnedInfo
        return WriteSetFieldMissLearnedInfo(self)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applyActions')

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applyActionsMiss')

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applySetField')

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applySetFieldMiss')

    @property
    def Config(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('config')

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('dataPathId')

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('dataPathIdAsHex')

    @property
    def Instruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('instruction')

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('instructionMiss')

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('localIp')

    @property
    def Match(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('match')

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('maxEntries')

    @property
    def MetadataMatch(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('metadataMatch')

    @property
    def MetadataWrite(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('metadataWrite')

    @property
    def Name(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('name')

    @property
    def NextTable(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('nextTable')

    @property
    def NextTableMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('nextTableMiss')

    @property
    def TableId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('tableId')

    @property
    def WildCards(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('wildCards')

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('writeActions')

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('writeActionsMiss')

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('writeSetField')

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('writeSetFieldMiss')

    def find(self, ApplyActions=None, ApplyActionsMiss=None, ApplySetField=None, ApplySetFieldMiss=None, Config=None, DataPathId=None, DataPathIdAsHex=None, Instruction=None, InstructionMiss=None, LocalIp=None, Match=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, Name=None, NextTable=None, NextTableMiss=None, TableId=None, WildCards=None, WriteActions=None, WriteActionsMiss=None, WriteSetField=None, WriteSetFieldMiss=None):
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
        return self._select(locals())

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
