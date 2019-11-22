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


class NacPosture(Base):
    """NAC Posture settings
    The NacPosture class encapsulates a list of nacPosture resources that is be managed by the user.
    A list of resources can be retrieved from the server using the NacPosture.find() method.
    The list can be managed by the user by using the NacPosture.add() and NacPosture.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'nacPosture'

    def __init__(self, parent):
        super(NacPosture, self).__init__(parent)

    @property
    def ExpectedSystemToken(self):
        """Expected System Token.

        Returns:
            number
        """
        return self._get_attribute('expectedSystemToken')
    @ExpectedSystemToken.setter
    def ExpectedSystemToken(self, value):
        self._set_attribute('expectedSystemToken', value)

    @property
    def NacTlvs(self):
        """List of NacTLVs.

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacTlv])
        """
        return self._get_attribute('nacTlvs')
    @NacTlvs.setter
    def NacTlvs(self, value):
        self._set_attribute('nacTlvs', value)

    @property
    def Name(self):
        """Unique name for this NAC Posture.

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

    @property
    def Selected(self):
        """Add to postures list.

        Returns:
            bool
        """
        return self._get_attribute('selected')
    @Selected.setter
    def Selected(self, value):
        self._set_attribute('selected', value)

    def update(self, ExpectedSystemToken=None, NacTlvs=None, Name=None, Selected=None):
        """Updates a child instance of nacPosture on the server.

        Args:
            ExpectedSystemToken (number): Expected System Token.
            NacTlvs (list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacTlv])): List of NacTLVs.
            Name (str): Unique name for this NAC Posture.
            Selected (bool): Add to postures list.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ExpectedSystemToken=None, NacTlvs=None, Name=None, Selected=None):
        """Adds a new nacPosture node on the server and retrieves it in this instance.

        Args:
            ExpectedSystemToken (number): Expected System Token.
            NacTlvs (list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacTlv])): List of NacTLVs.
            Name (str): Unique name for this NAC Posture.
            Selected (bool): Add to postures list.

        Returns:
            self: This instance with all currently retrieved nacPosture data using find and the newly added nacPosture data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the nacPosture data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ExpectedSystemToken=None, NacTlvs=None, Name=None, ObjectId=None, Selected=None):
        """Finds and retrieves nacPosture data from the server.

        All named parameters support regex and can be used to selectively retrieve nacPosture data from the server.
        By default the find method takes no parameters and will retrieve all nacPosture data from the server.

        Args:
            ExpectedSystemToken (number): Expected System Token.
            NacTlvs (list(str[None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacTlv])): List of NacTLVs.
            Name (str): Unique name for this NAC Posture.
            ObjectId (str): Unique identifier for this object
            Selected (bool): Add to postures list.

        Returns:
            self: This instance with matching nacPosture data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of nacPosture data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the nacPosture data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
