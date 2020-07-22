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


class ExperimenterMissLearnedInfo(Base):
    """NOT DEFINED
    The ExperimenterMissLearnedInfo class encapsulates a list of experimenterMissLearnedInfo resources that are managed by the user.
    A list of resources can be retrieved from the server using the ExperimenterMissLearnedInfo.find() method.
    The list can be managed by using the ExperimenterMissLearnedInfo.add() and ExperimenterMissLearnedInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'experimenterMissLearnedInfo'
    _SDM_ATT_MAP = {
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'ExperimenterId': 'experimenterId',
        'NextTableIds': 'nextTableIds',
        'Property': 'property',
        'SupportedField': 'supportedField',
    }

    def __init__(self, parent):
        super(ExperimenterMissLearnedInfo, self).__init__(parent)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])

    @property
    def NextTableIds(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextTableIds'])

    @property
    def Property(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Property'])

    @property
    def SupportedField(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedField'])

    def add(self):
        """Adds a new experimenterMissLearnedInfo resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved experimenterMissLearnedInfo resources using find and the newly added experimenterMissLearnedInfo resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained experimenterMissLearnedInfo resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterId=None, NextTableIds=None, Property=None, SupportedField=None):
        """Finds and retrieves experimenterMissLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve experimenterMissLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all experimenterMissLearnedInfo resources from the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterId (number): NOT DEFINED
        - NextTableIds (str): NOT DEFINED
        - Property (str): NOT DEFINED
        - SupportedField (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching experimenterMissLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of experimenterMissLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the experimenterMissLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
