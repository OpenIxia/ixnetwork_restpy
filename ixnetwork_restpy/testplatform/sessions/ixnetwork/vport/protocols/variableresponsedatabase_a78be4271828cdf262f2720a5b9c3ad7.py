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


class VariableResponseDatabase(Base):
    """
    The VariableResponseDatabase class encapsulates a list of variableResponseDatabase resources that are managed by the user.
    A list of resources can be retrieved from the server using the VariableResponseDatabase.find() method.
    The list can be managed by using the VariableResponseDatabase.add() and VariableResponseDatabase.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'variableResponseDatabase'

    def __init__(self, parent):
        super(VariableResponseDatabase, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def VariableBranch(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('variableBranch')
    @VariableBranch.setter
    def VariableBranch(self, value):
        self._set_attribute('variableBranch', value)

    @property
    def VariableIndication(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('variableIndication')
    @VariableIndication.setter
    def VariableIndication(self, value):
        self._set_attribute('variableIndication', value)

    @property
    def VariableLeaf(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('variableLeaf')
    @VariableLeaf.setter
    def VariableLeaf(self, value):
        self._set_attribute('variableLeaf', value)

    @property
    def VariableValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('variableValue')
    @VariableValue.setter
    def VariableValue(self, value):
        self._set_attribute('variableValue', value)

    @property
    def VariableWidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('variableWidth')
    @VariableWidth.setter
    def VariableWidth(self, value):
        self._set_attribute('variableWidth', value)

    def update(self, Enabled=None, VariableBranch=None, VariableIndication=None, VariableLeaf=None, VariableValue=None, VariableWidth=None):
        """Updates variableResponseDatabase resource on the server.

        Args
        ----
        - Enabled (bool): 
        - VariableBranch (number): 
        - VariableIndication (bool): 
        - VariableLeaf (number): 
        - VariableValue (str): 
        - VariableWidth (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, Enabled=None, VariableBranch=None, VariableIndication=None, VariableLeaf=None, VariableValue=None, VariableWidth=None):
        """Adds a new variableResponseDatabase resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): 
        - VariableBranch (number): 
        - VariableIndication (bool): 
        - VariableLeaf (number): 
        - VariableValue (str): 
        - VariableWidth (number): 

        Returns
        -------
        - self: This instance with all currently retrieved variableResponseDatabase resources using find and the newly added variableResponseDatabase resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained variableResponseDatabase resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, VariableBranch=None, VariableIndication=None, VariableLeaf=None, VariableValue=None, VariableWidth=None):
        """Finds and retrieves variableResponseDatabase resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve variableResponseDatabase resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all variableResponseDatabase resources from the server.

        Args
        ----
        - Enabled (bool): 
        - VariableBranch (number): 
        - VariableIndication (bool): 
        - VariableLeaf (number): 
        - VariableValue (str): 
        - VariableWidth (number): 

        Returns
        -------
        - self: This instance with matching variableResponseDatabase resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of variableResponseDatabase data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the variableResponseDatabase resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
