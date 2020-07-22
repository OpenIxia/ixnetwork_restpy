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


class TableFeaturesLearnedInformation(Base):
    """NOT DEFINED
    The TableFeaturesLearnedInformation class encapsulates a list of tableFeaturesLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the TableFeaturesLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tableFeaturesLearnedInformation'
    _SDM_ATT_MAP = {
        'ApplyActions': 'applyActions',
        'ApplyActionsMiss': 'applyActionsMiss',
        'ApplySetField': 'applySetField',
        'ApplySetFieldMiss': 'applySetFieldMiss',
        'Config': 'config',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'Experimenter': 'experimenter',
        'ExperimenterMiss': 'experimenterMiss',
        'Instruction': 'instruction',
        'InstructionMiss': 'instructionMiss',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'Match': 'match',
        'MaxEntries': 'maxEntries',
        'MetadataMatch': 'metadataMatch',
        'MetadataWrite': 'metadataWrite',
        'Name': 'name',
        'NegotiatedVersion': 'negotiatedVersion',
        'NextTable': 'nextTable',
        'NextTableMiss': 'nextTableMiss',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'TableId': 'tableId',
        'WildCards': 'wildCards',
        'WriteActions': 'writeActions',
        'WriteActionsMiss': 'writeActionsMiss',
        'WriteSetField': 'writeSetField',
        'WriteSetFieldMiss': 'writeSetFieldMiss',
    }

    def __init__(self, parent):
        super(TableFeaturesLearnedInformation, self).__init__(parent)

    @property
    def ApplyActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_751491bb389f5a8add05488bd2281d0f.ApplyActionsLearnedInfo): An instance of the ApplyActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionslearnedinfo_751491bb389f5a8add05488bd2281d0f import ApplyActionsLearnedInfo
        return ApplyActionsLearnedInfo(self)

    @property
    def ApplyActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_581a2d4f3d5185482e7033a768ca1943.ApplyActionsMissLearnedInfo): An instance of the ApplyActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionsmisslearnedinfo_581a2d4f3d5185482e7033a768ca1943 import ApplyActionsMissLearnedInfo
        return ApplyActionsMissLearnedInfo(self)

    @property
    def ApplySetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_eb71c1c52bba2bfd22f7046853d1756d.ApplySetFieldLearnedInfo): An instance of the ApplySetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldlearnedinfo_eb71c1c52bba2bfd22f7046853d1756d import ApplySetFieldLearnedInfo
        return ApplySetFieldLearnedInfo(self)

    @property
    def ApplySetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_8c58c24556a84ba0fa8d28beeb1b3af9.ApplySetFieldMissLearnedInfo): An instance of the ApplySetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applysetfieldmisslearnedinfo_8c58c24556a84ba0fa8d28beeb1b3af9 import ApplySetFieldMissLearnedInfo
        return ApplySetFieldMissLearnedInfo(self)

    @property
    def ExperimenterLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenterlearnedinfo_5a265c383787380f014a8ee9eed1ecf9.ExperimenterLearnedInfo): An instance of the ExperimenterLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimenterlearnedinfo_5a265c383787380f014a8ee9eed1ecf9 import ExperimenterLearnedInfo
        return ExperimenterLearnedInfo(self)

    @property
    def ExperimenterMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimentermisslearnedinfo_b4f9515b2afff72d603275da2465c21c.ExperimenterMissLearnedInfo): An instance of the ExperimenterMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.experimentermisslearnedinfo_b4f9515b2afff72d603275da2465c21c import ExperimenterMissLearnedInfo
        return ExperimenterMissLearnedInfo(self)

    @property
    def InstructionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_5c52cdd1bc9842d8c9cd6b3432aafc23.InstructionLearnedInfo): An instance of the InstructionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionlearnedinfo_5c52cdd1bc9842d8c9cd6b3432aafc23 import InstructionLearnedInfo
        return InstructionLearnedInfo(self)

    @property
    def InstructionMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_afc05368d8c02fec9b7a2b1f63869b3f.InstructionMissLearnedInfo): An instance of the InstructionMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionmisslearnedinfo_afc05368d8c02fec9b7a2b1f63869b3f import InstructionMissLearnedInfo
        return InstructionMissLearnedInfo(self)

    @property
    def MatchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_fe56a2ee154efca676ed0725b1e3c7fd.MatchLearnedInfo): An instance of the MatchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchlearnedinfo_fe56a2ee154efca676ed0725b1e3c7fd import MatchLearnedInfo
        return MatchLearnedInfo(self)

    @property
    def NextTableLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_893858f7a360bece76d5614264c6e040.NextTableLearnedInfo): An instance of the NextTableLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablelearnedinfo_893858f7a360bece76d5614264c6e040 import NextTableLearnedInfo
        return NextTableLearnedInfo(self)

    @property
    def NextTableMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_2d5e407598196ee90314fd581a377530.NextTableMissLearnedInfo): An instance of the NextTableMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexttablemisslearnedinfo_2d5e407598196ee90314fd581a377530 import NextTableMissLearnedInfo
        return NextTableMissLearnedInfo(self)

    @property
    def WildcardsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_c49176374a2ec1d1430f30aceb060d8d.WildcardsLearnedInfo): An instance of the WildcardsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardslearnedinfo_c49176374a2ec1d1430f30aceb060d8d import WildcardsLearnedInfo
        return WildcardsLearnedInfo(self)

    @property
    def WriteActionsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_e05034aa344a3f46f8044b8d1900854c.WriteActionsLearnedInfo): An instance of the WriteActionsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionslearnedinfo_e05034aa344a3f46f8044b8d1900854c import WriteActionsLearnedInfo
        return WriteActionsLearnedInfo(self)

    @property
    def WriteActionsMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_998481852ac0f4b943588f925acecf3d.WriteActionsMissLearnedInfo): An instance of the WriteActionsMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionsmisslearnedinfo_998481852ac0f4b943588f925acecf3d import WriteActionsMissLearnedInfo
        return WriteActionsMissLearnedInfo(self)

    @property
    def WriteSetFieldLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_ad7469c869d6d29256ed568202bb0d20.WriteSetFieldLearnedInfo): An instance of the WriteSetFieldLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldlearnedinfo_ad7469c869d6d29256ed568202bb0d20 import WriteSetFieldLearnedInfo
        return WriteSetFieldLearnedInfo(self)

    @property
    def WriteSetFieldMissLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_b8e1c1a90bc00228bdd75e83cc272984.WriteSetFieldMissLearnedInfo): An instance of the WriteSetFieldMissLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writesetfieldmisslearnedinfo_b8e1c1a90bc00228bdd75e83cc272984 import WriteSetFieldMissLearnedInfo
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
    def ErrorCode(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])

    @property
    def ExperimenterMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterMiss'])

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
    def Latency(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

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
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

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
    def RemoteIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

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

    def find(self, ApplyActions=None, ApplyActionsMiss=None, ApplySetField=None, ApplySetFieldMiss=None, Config=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, Experimenter=None, ExperimenterMiss=None, Instruction=None, InstructionMiss=None, Latency=None, LocalIp=None, Match=None, MaxEntries=None, MetadataMatch=None, MetadataWrite=None, Name=None, NegotiatedVersion=None, NextTable=None, NextTableMiss=None, RemoteIp=None, ReplyState=None, TableId=None, WildCards=None, WriteActions=None, WriteActionsMiss=None, WriteSetField=None, WriteSetFieldMiss=None):
        """Finds and retrieves tableFeaturesLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tableFeaturesLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tableFeaturesLearnedInformation resources from the server.

        Args
        ----
        - ApplyActions (str): NOT DEFINED
        - ApplyActionsMiss (str): NOT DEFINED
        - ApplySetField (str): NOT DEFINED
        - ApplySetFieldMiss (str): NOT DEFINED
        - Config (number): NOT DEFINED
        - DataPathId (str): NOT DEFINED
        - DataPathIdAsHex (str): NOT DEFINED
        - ErrorCode (str): NOT DEFINED
        - ErrorType (str): NOT DEFINED
        - Experimenter (str): NOT DEFINED
        - ExperimenterMiss (str): NOT DEFINED
        - Instruction (str): NOT DEFINED
        - InstructionMiss (str): NOT DEFINED
        - Latency (number): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - Match (str): NOT DEFINED
        - MaxEntries (number): NOT DEFINED
        - MetadataMatch (str): NOT DEFINED
        - MetadataWrite (str): NOT DEFINED
        - Name (str): NOT DEFINED
        - NegotiatedVersion (str): NOT DEFINED
        - NextTable (str): NOT DEFINED
        - NextTableMiss (str): NOT DEFINED
        - RemoteIp (str): NOT DEFINED
        - ReplyState (str): NOT DEFINED
        - TableId (str): NOT DEFINED
        - WildCards (str): NOT DEFINED
        - WriteActions (str): NOT DEFINED
        - WriteActionsMiss (str): NOT DEFINED
        - WriteSetField (str): NOT DEFINED
        - WriteSetFieldMiss (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching tableFeaturesLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tableFeaturesLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tableFeaturesLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
