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


class FormulaColumn(Base):
    """The formula is filtered and maintained in columns.
    The FormulaColumn class encapsulates a list of formulaColumn resources that are managed by the user.
    A list of resources can be retrieved from the server using the FormulaColumn.find() method.
    The list can be managed by using the FormulaColumn.add() and FormulaColumn.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'formulaColumn'
    _SDM_ATT_MAP = {
        'Caption': 'caption',
        'Formula': 'formula',
    }

    def __init__(self, parent):
        super(FormulaColumn, self).__init__(parent)

    @property
    def Caption(self):
        """
        Returns
        -------
        - str: The name of the formula.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Caption'])
    @Caption.setter
    def Caption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Caption'], value)

    @property
    def Formula(self):
        """
        Returns
        -------
        - str: The formula that is filtered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Formula'])
    @Formula.setter
    def Formula(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Formula'], value)

    def update(self, Caption=None, Formula=None):
        """Updates formulaColumn resource on the server.

        Args
        ----
        - Caption (str): The name of the formula.
        - Formula (str): The formula that is filtered.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Caption=None, Formula=None):
        """Adds a new formulaColumn resource on the server and adds it to the container.

        Args
        ----
        - Caption (str): The name of the formula.
        - Formula (str): The formula that is filtered.

        Returns
        -------
        - self: This instance with all currently retrieved formulaColumn resources using find and the newly added formulaColumn resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained formulaColumn resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Caption=None, Formula=None):
        """Finds and retrieves formulaColumn resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve formulaColumn resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all formulaColumn resources from the server.

        Args
        ----
        - Caption (str): The name of the formula.
        - Formula (str): The formula that is filtered.

        Returns
        -------
        - self: This instance with matching formulaColumn resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of formulaColumn data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the formulaColumn resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
