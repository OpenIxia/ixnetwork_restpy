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


class NacSequence(Base):
    """NAC Sequence settings
    The NacSequence class encapsulates a list of nacSequence resources that are managed by the user.
    A list of resources can be retrieved from the server using the NacSequence.find() method.
    The list can be managed by using the NacSequence.add() and NacSequence.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'nacSequence'
    _SDM_ATT_MAP = {
        'NacPostures': 'nacPostures',
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(NacSequence, self).__init__(parent)

    @property
    def NacPostures(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacPosture]): List of NacPostures.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NacPostures'])
    @NacPostures.setter
    def NacPostures(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NacPostures'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Unique name for this NAC Sequence.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, NacPostures=None, Name=None):
        """Updates nacSequence resource on the server.

        Args
        ----
        - NacPostures (list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacPosture])): List of NacPostures.
        - Name (str): Unique name for this NAC Sequence.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, NacPostures=None, Name=None):
        """Adds a new nacSequence resource on the server and adds it to the container.

        Args
        ----
        - NacPostures (list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacPosture])): List of NacPostures.
        - Name (str): Unique name for this NAC Sequence.

        Returns
        -------
        - self: This instance with all currently retrieved nacSequence resources using find and the newly added nacSequence resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained nacSequence resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, NacPostures=None, Name=None, ObjectId=None):
        """Finds and retrieves nacSequence resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve nacSequence resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all nacSequence resources from the server.

        Args
        ----
        - NacPostures (list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacPosture])): List of NacPostures.
        - Name (str): Unique name for this NAC Sequence.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching nacSequence resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of nacSequence data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the nacSequence resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
