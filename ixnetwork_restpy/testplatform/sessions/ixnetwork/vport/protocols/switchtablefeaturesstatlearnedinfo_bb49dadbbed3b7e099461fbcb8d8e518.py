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


class SwitchTableFeaturesStatLearnedInfo(Base):
    """NOT DEFINED
    The SwitchTableFeaturesStatLearnedInfo class encapsulates a list of switchTableFeaturesStatLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchTableFeaturesStatLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchTableFeaturesStatLearnedInfo'
    _SDM_ATT_MAP = {
        'ApplyActions': 'applyActions',
        'ApplyActionsMiss': 'applyActionsMiss',
        'ApplySetField': 'applySetField',
        'ApplySetFieldMiss': 'applySetFieldMiss',
        'Config': 'config',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'Instruction': 'instruction',
        'InstructionMiss': 'instructionMiss',
        'LocalIp': 'localIp',
        'Match': 'match',
        'MaxEntries': 'maxEntries',
        'MetadataMatch': 'metadataMatch',
        'MetadataWrite': 'metadataWrite',
        'Name': 'name',
        'NextTable': 'nextTable',
        'NextTableMiss': 'nextTableMiss',
        'TableId': 'tableId',
        'WildCards': 'wildCards',
        'WriteActions': 'writeActions',
        'WriteActionsMiss': 'writeActionsMiss',
        'WriteSetField': 'writeSetField',
        'WriteSetFieldMiss': 'writeSetFieldMiss',
    }

    def __init__(self, parent):
        super(SwitchTableFeaturesStatLearnedInfo, self).__init__(parent)

    @property
    def ApplyActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_69b85283e35d130d78e0d80a7b26060a.ApplyActionsLearnedInfo): An instance of the ApplyActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_69b85283e35d130d78e0d80a7b26060a import ApplyActionsLearnedInfo
        return ApplyActionsLearnedInfo(self)

    @property
    def ApplyActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_e12161d2bc09f6f6142b7af0eadc2dce.ApplyActionsMissLearnedInfo): An instance of the ApplyActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_e12161d2bc09f6f6142b7af0eadc2dce import ApplyActionsMissLearnedInfo
        return ApplyActionsMissLearnedInfo(self)

    @property
    def ApplySetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_f0b4feea92dd1452a8a81a6c0d835fe3.ApplySetFieldLearnedInfo): An instance of the ApplySetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_f0b4feea92dd1452a8a81a6c0d835fe3 import ApplySetFieldLearnedInfo
        return ApplySetFieldLearnedInfo(self)

    @property
    def ApplySetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_7455db4810fc18d1522d2f7d62e305a1.ApplySetFieldMissLearnedInfo): An instance of the ApplySetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_7455db4810fc18d1522d2f7d62e305a1 import ApplySetFieldMissLearnedInfo
        return ApplySetFieldMissLearnedInfo(self)

    @property
    def InstructionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_ee8ad0057db3b02aba6cb1507ec6abbf.InstructionLearnedInfo): An instance of the InstructionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_ee8ad0057db3b02aba6cb1507ec6abbf import InstructionLearnedInfo
        return InstructionLearnedInfo(self)

    @property
    def InstructionMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_4d00cfc2ab45935c178a029ef76fb7b2.InstructionMissLearnedInfo): An instance of the InstructionMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_4d00cfc2ab45935c178a029ef76fb7b2 import InstructionMissLearnedInfo
        return InstructionMissLearnedInfo(self)

    @property
    def MatchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_a45f872ddff69b9dbb7a4dd353968824.MatchLearnedInfo): An instance of the MatchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_a45f872ddff69b9dbb7a4dd353968824 import MatchLearnedInfo
        return MatchLearnedInfo(self)

    @property
    def NextTableLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_23b33dc5fc9b19dce0196ca6f1f07567.NextTableLearnedInfo): An instance of the NextTableLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_23b33dc5fc9b19dce0196ca6f1f07567 import NextTableLearnedInfo
        return NextTableLearnedInfo(self)

    @property
    def NextTableMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_e2481b23e26132283def64fc40fc27b1.NextTableMissLearnedInfo): An instance of the NextTableMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_e2481b23e26132283def64fc40fc27b1 import NextTableMissLearnedInfo
        return NextTableMissLearnedInfo(self)

    @property
    def WildcardsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_8735626a40c247307c2674d973afbe72.WildcardsLearnedInfo): An instance of the WildcardsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_8735626a40c247307c2674d973afbe72 import WildcardsLearnedInfo
        return WildcardsLearnedInfo(self)

    @property
    def WriteActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_eeadf26a26a0e4c8d1da5c94a09cd297.WriteActionsLearnedInfo): An instance of the WriteActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_eeadf26a26a0e4c8d1da5c94a09cd297 import WriteActionsLearnedInfo
        return WriteActionsLearnedInfo(self)

    @property
    def WriteActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_3fe5a932dc5e3ee403647920b878fc3a.WriteActionsMissLearnedInfo): An instance of the WriteActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_3fe5a932dc5e3ee403647920b878fc3a import WriteActionsMissLearnedInfo
        return WriteActionsMissLearnedInfo(self)

    @property
    def WriteSetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_c990680b3d665d2522242a8656be4f74.WriteSetFieldLearnedInfo): An instance of the WriteSetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_c990680b3d665d2522242a8656be4f74 import WriteSetFieldLearnedInfo
        return WriteSetFieldLearnedInfo(self)

    @property
    def WriteSetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_185921fc714e5f4411bd7dcdf8a8dc3c.WriteSetFieldMissLearnedInfo): An instance of the WriteSetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_185921fc714e5f4411bd7dcdf8a8dc3c import WriteSetFieldMissLearnedInfo
        return WriteSetFieldMissLearnedInfo(self)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActions'])

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActionsMiss'])

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplySetField'])

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplySetFieldMiss'])

    @property
    def Config(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Config'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def Instruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Instruction'])

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionMiss'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def Match(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Match'])

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxEntries'])

    @property
    def MetadataMatch(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataMatch'])

    @property
    def MetadataWrite(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataWrite'])

    @property
    def Name(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def NextTable(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTable'])

    @property
    def NextTableMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTableMiss'])

    @property
    def TableId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])

    @property
    def WildCards(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WildCards'])

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActions'])

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActionsMiss'])

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteSetField'])

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteSetFieldMiss'])

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
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

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
