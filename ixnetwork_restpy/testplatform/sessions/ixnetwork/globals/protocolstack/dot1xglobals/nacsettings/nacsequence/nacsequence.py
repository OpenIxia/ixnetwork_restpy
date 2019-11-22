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


class NacSequence(Base):
    """NAC Sequence settings
    The NacSequence class encapsulates a list of nacSequence resources that is be managed by the user.
    A list of resources can be retrieved from the server using the NacSequence.find() method.
    The list can be managed by the user by using the NacSequence.add() and NacSequence.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'nacSequence'

    def __init__(self, parent):
        super(NacSequence, self).__init__(parent)

    @property
    def NacPostures(self):
        """List of NacPostures.

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacPosture])
        """
        return self._get_attribute('nacPostures')
    @NacPostures.setter
    def NacPostures(self, value):
        self._set_attribute('nacPostures', value)

    @property
    def Name(self):
        """Unique name for this NAC Sequence.

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def update(self, NacPostures=None, Name=None):
        """Updates a child instance of nacSequence on the server.

        Args:
            NacPostures (list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacPosture])): List of NacPostures.
            Name (str): Unique name for this NAC Sequence.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, NacPostures=None, Name=None):
        """Adds a new nacSequence node on the server and retrieves it in this instance.

        Args:
            NacPostures (list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacPosture])): List of NacPostures.
            Name (str): Unique name for this NAC Sequence.

        Returns:
            self: This instance with all currently retrieved nacSequence data using find and the newly added nacSequence data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the nacSequence data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, NacPostures=None, Name=None, ObjectId=None):
        """Finds and retrieves nacSequence data from the server.

        All named parameters support regex and can be used to selectively retrieve nacSequence data from the server.
        By default the find method takes no parameters and will retrieve all nacSequence data from the server.

        Args:
            NacPostures (list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacPosture])): List of NacPostures.
            Name (str): Unique name for this NAC Sequence.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching nacSequence data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of nacSequence data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the nacSequence data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
