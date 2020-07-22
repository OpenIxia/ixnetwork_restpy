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


class Instruction(Base):
    """NOT DEFINED
    The Instruction class encapsulates a required instruction resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'instruction'
    _SDM_ATT_MAP = {
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'ExperimenterDataLengthMiss': 'experimenterDataLengthMiss',
        'ExperimenterDataMiss': 'experimenterDataMiss',
        'ExperimenterId': 'experimenterId',
        'ExperimenterIdMiss': 'experimenterIdMiss',
    }

    def __init__(self, parent):
        super(Instruction, self).__init__(parent)

    @property
    def InstructionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontype_f00a5f3142a336cc29bbaac751ef1a91.InstructionType): An instance of the InstructionType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontype_f00a5f3142a336cc29bbaac751ef1a91 import InstructionType
        return InstructionType(self)._select()

    @property
    def InstructionTypeMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontypemiss_24c6a57a16be0a23824dea2325bf06bd.InstructionTypeMiss): An instance of the InstructionTypeMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontypemiss_24c6a57a16be0a23824dea2325bf06bd import InstructionTypeMiss
        return InstructionTypeMiss(self)._select()

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'], value)

    @property
    def ExperimenterDataLengthMiss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLengthMiss'])
    @ExperimenterDataLengthMiss.setter
    def ExperimenterDataLengthMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataLengthMiss'], value)

    @property
    def ExperimenterDataMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataMiss'])
    @ExperimenterDataMiss.setter
    def ExperimenterDataMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataMiss'], value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterId'], value)

    @property
    def ExperimenterIdMiss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterIdMiss'])
    @ExperimenterIdMiss.setter
    def ExperimenterIdMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterIdMiss'], value)

    def update(self, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterDataLengthMiss=None, ExperimenterDataMiss=None, ExperimenterId=None, ExperimenterIdMiss=None):
        """Updates instruction resource on the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterDataLengthMiss (number): NOT DEFINED
        - ExperimenterDataMiss (str): NOT DEFINED
        - ExperimenterId (number): NOT DEFINED
        - ExperimenterIdMiss (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
