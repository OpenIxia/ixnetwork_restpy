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


class SwitchFlowInstructionLearnedInfo(Base):
    """This object allows to configure the switch flow instruction learned information for OpenFlow.
    The SwitchFlowInstructionLearnedInfo class encapsulates a list of switchFlowInstructionLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchFlowInstructionLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchFlowInstructionLearnedInfo'
    _SDM_ATT_MAP = {
        'Experimenter': 'experimenter',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'InstructionType': 'instructionType',
        'Metadata': 'metadata',
        'MetadataMask': 'metadataMask',
        'MeterId': 'meterId',
        'TableId': 'tableId',
    }

    def __init__(self, parent):
        super(SwitchFlowInstructionLearnedInfo, self).__init__(parent)

    @property
    def SwitchActionV131LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchactionv131learnedinfo_86b2a5d222052c3859c6e020913907f6.SwitchActionV131LearnedInfo): An instance of the SwitchActionV131LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchactionv131learnedinfo_86b2a5d222052c3859c6e020913907f6 import SwitchActionV131LearnedInfo
        return SwitchActionV131LearnedInfo(self)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - number: This describes the unique Experimenter identifier. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: This describes the data of the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: This describes the data length of the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])

    @property
    def InstructionType(self):
        """
        Returns
        -------
        - str: This describes the action type associated with this instruction.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionType'])

    @property
    def Metadata(self):
        """
        Returns
        -------
        - str: This describes the table metadata value used to pass information between tables.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metadata'])

    @property
    def MetadataMask(self):
        """
        Returns
        -------
        - str: This describes the metadata bitmask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataMask'])

    @property
    def MeterId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterId'])

    @property
    def TableId(self):
        """
        Returns
        -------
        - number: This describes the table identifier. It indicates the next table in the packet processing pipeline.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])

    def find(self, Experimenter=None, ExperimenterData=None, ExperimenterDataLength=None, InstructionType=None, Metadata=None, MetadataMask=None, MeterId=None, TableId=None):
        """Finds and retrieves switchFlowInstructionLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchFlowInstructionLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchFlowInstructionLearnedInfo resources from the server.

        Args
        ----
        - Experimenter (number): This describes the unique Experimenter identifier. The default value is 1.
        - ExperimenterData (str): This describes the data of the Experimenter.
        - ExperimenterDataLength (number): This describes the data length of the Experimenter.
        - InstructionType (str): This describes the action type associated with this instruction.
        - Metadata (str): This describes the table metadata value used to pass information between tables.
        - MetadataMask (str): This describes the metadata bitmask value.
        - MeterId (number): NOT DEFINED
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.

        Returns
        -------
        - self: This instance with matching switchFlowInstructionLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchFlowInstructionLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchFlowInstructionLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
