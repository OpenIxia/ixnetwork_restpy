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


class VariableRequestLearnedInfo(Base):
    """
    The VariableRequestLearnedInfo class encapsulates a list of variableRequestLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the VariableRequestLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'variableRequestLearnedInfo'
    _SDM_ATT_MAP = {
        'VariableBranch': 'variableBranch',
        'VariableIndication': 'variableIndication',
        'VariableLeaf': 'variableLeaf',
        'VariableValue': 'variableValue',
        'VariableWidth': 'variableWidth',
    }

    def __init__(self, parent):
        super(VariableRequestLearnedInfo, self).__init__(parent)

    @property
    def VariableBranch(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableBranch'])

    @property
    def VariableIndication(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableIndication'])

    @property
    def VariableLeaf(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableLeaf'])

    @property
    def VariableValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableValue'])

    @property
    def VariableWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableWidth'])

    def find(self, VariableBranch=None, VariableIndication=None, VariableLeaf=None, VariableValue=None, VariableWidth=None):
        """Finds and retrieves variableRequestLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve variableRequestLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all variableRequestLearnedInfo resources from the server.

        Args
        ----
        - VariableBranch (str): 
        - VariableIndication (bool): 
        - VariableLeaf (str): 
        - VariableValue (str): 
        - VariableWidth (number): 

        Returns
        -------
        - self: This instance with matching variableRequestLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of variableRequestLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the variableRequestLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
