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


class SwitchTables(Base):
    """This object allows to define the configuration parameters for the switch tables.
    The SwitchTables class encapsulates a list of switchTables resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchTables.find() method.
    The list can be managed by using the SwitchTables.add() and SwitchTables.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchTables'
    _SDM_ATT_MAP = {
        'MaxEntries': 'maxEntries',
        'NumberOfTables': 'numberOfTables',
        'TableId': 'tableId',
        'TableName': 'tableName',
    }

    def __init__(self, parent):
        super(SwitchTables, self).__init__(parent)

    @property
    def WildcardsSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_30584fd46ca1157c8d65eba239520375.WildcardsSupported): An instance of the WildcardsSupported class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardssupported_30584fd46ca1157c8d65eba239520375 import WildcardsSupported
        return WildcardsSupported(self)._select()

    @property
    def MaxEntries(self):
        """
        Returns
        -------
        - str: Indicates the maximum number of entries supported. The default value is 10,000.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxEntries'])
    @MaxEntries.setter
    def MaxEntries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxEntries'], value)

    @property
    def NumberOfTables(self):
        """
        Returns
        -------
        - number: Indicates the number of entries in the table range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfTables'])
    @NumberOfTables.setter
    def NumberOfTables(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfTables'], value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - str: Indicates the Identifier of the switch table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])
    @TableId.setter
    def TableId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableId'], value)

    @property
    def TableName(self):
        """
        Returns
        -------
        - str: Indicates the name of the switch table
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableName'])
    @TableName.setter
    def TableName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableName'], value)

    def update(self, MaxEntries=None, NumberOfTables=None, TableId=None, TableName=None):
        """Updates switchTables resource on the server.

        Args
        ----
        - MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
        - NumberOfTables (number): Indicates the number of entries in the table range.
        - TableId (str): Indicates the Identifier of the switch table.
        - TableName (str): Indicates the name of the switch table

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, MaxEntries=None, NumberOfTables=None, TableId=None, TableName=None):
        """Adds a new switchTables resource on the server and adds it to the container.

        Args
        ----
        - MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
        - NumberOfTables (number): Indicates the number of entries in the table range.
        - TableId (str): Indicates the Identifier of the switch table.
        - TableName (str): Indicates the name of the switch table

        Returns
        -------
        - self: This instance with all currently retrieved switchTables resources using find and the newly added switchTables resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switchTables resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxEntries=None, NumberOfTables=None, TableId=None, TableName=None):
        """Finds and retrieves switchTables resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchTables resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchTables resources from the server.

        Args
        ----
        - MaxEntries (str): Indicates the maximum number of entries supported. The default value is 10,000.
        - NumberOfTables (number): Indicates the number of entries in the table range.
        - TableId (str): Indicates the Identifier of the switch table.
        - TableName (str): Indicates the name of the switch table

        Returns
        -------
        - self: This instance with matching switchTables resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchTables data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchTables resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
