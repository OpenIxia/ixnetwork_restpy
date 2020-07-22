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


class NacPosture(Base):
    """NAC Posture settings
    The NacPosture class encapsulates a list of nacPosture resources that are managed by the user.
    A list of resources can be retrieved from the server using the NacPosture.find() method.
    The list can be managed by using the NacPosture.add() and NacPosture.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'nacPosture'
    _SDM_ATT_MAP = {
        'ExpectedSystemToken': 'expectedSystemToken',
        'NacTlvs': 'nacTlvs',
        'Name': 'name',
        'ObjectId': 'objectId',
        'Selected': 'selected',
    }

    def __init__(self, parent):
        super(NacPosture, self).__init__(parent)

    @property
    def ExpectedSystemToken(self):
        """
        Returns
        -------
        - number: Expected System Token.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExpectedSystemToken'])
    @ExpectedSystemToken.setter
    def ExpectedSystemToken(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExpectedSystemToken'], value)

    @property
    def NacTlvs(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacTlv]): List of NacTLVs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NacTlvs'])
    @NacTlvs.setter
    def NacTlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NacTlvs'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Unique name for this NAC Posture.
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

    @property
    def Selected(self):
        """
        Returns
        -------
        - bool: Add to postures list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Selected'])
    @Selected.setter
    def Selected(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Selected'], value)

    def update(self, ExpectedSystemToken=None, NacTlvs=None, Name=None, Selected=None):
        """Updates nacPosture resource on the server.

        Args
        ----
        - ExpectedSystemToken (number): Expected System Token.
        - NacTlvs (list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacTlv])): List of NacTLVs.
        - Name (str): Unique name for this NAC Posture.
        - Selected (bool): Add to postures list.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ExpectedSystemToken=None, NacTlvs=None, Name=None, Selected=None):
        """Adds a new nacPosture resource on the server and adds it to the container.

        Args
        ----
        - ExpectedSystemToken (number): Expected System Token.
        - NacTlvs (list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacTlv])): List of NacTLVs.
        - Name (str): Unique name for this NAC Posture.
        - Selected (bool): Add to postures list.

        Returns
        -------
        - self: This instance with all currently retrieved nacPosture resources using find and the newly added nacPosture resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained nacPosture resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ExpectedSystemToken=None, NacTlvs=None, Name=None, ObjectId=None, Selected=None):
        """Finds and retrieves nacPosture resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve nacPosture resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all nacPosture resources from the server.

        Args
        ----
        - ExpectedSystemToken (number): Expected System Token.
        - NacTlvs (list(str[None | /api/v1/sessions/1/ixnetwork/globals/.../nacTlv])): List of NacTLVs.
        - Name (str): Unique name for this NAC Posture.
        - ObjectId (str): Unique identifier for this object
        - Selected (bool): Add to postures list.

        Returns
        -------
        - self: This instance with matching nacPosture resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of nacPosture data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the nacPosture resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
