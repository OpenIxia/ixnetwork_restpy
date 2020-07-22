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


class VarDescriptor(Base):
    """
    The VarDescriptor class encapsulates a list of varDescriptor resources that are managed by the user.
    A list of resources can be retrieved from the server using the VarDescriptor.find() method.
    The list can be managed by using the VarDescriptor.add() and VarDescriptor.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'varDescriptor'
    _SDM_ATT_MAP = {
        'VariableBranch': 'variableBranch',
        'VariableLeaf': 'variableLeaf',
    }

    def __init__(self, parent):
        super(VarDescriptor, self).__init__(parent)

    @property
    def VariableBranch(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableBranch'])
    @VariableBranch.setter
    def VariableBranch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VariableBranch'], value)

    @property
    def VariableLeaf(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableLeaf'])
    @VariableLeaf.setter
    def VariableLeaf(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VariableLeaf'], value)

    def update(self, VariableBranch=None, VariableLeaf=None):
        """Updates varDescriptor resource on the server.

        Args
        ----
        - VariableBranch (number): 
        - VariableLeaf (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, VariableBranch=None, VariableLeaf=None):
        """Adds a new varDescriptor resource on the server and adds it to the container.

        Args
        ----
        - VariableBranch (number): 
        - VariableLeaf (number): 

        Returns
        -------
        - self: This instance with all currently retrieved varDescriptor resources using find and the newly added varDescriptor resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained varDescriptor resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, VariableBranch=None, VariableLeaf=None):
        """Finds and retrieves varDescriptor resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve varDescriptor resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all varDescriptor resources from the server.

        Args
        ----
        - VariableBranch (number): 
        - VariableLeaf (number): 

        Returns
        -------
        - self: This instance with matching varDescriptor resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of varDescriptor data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the varDescriptor resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
