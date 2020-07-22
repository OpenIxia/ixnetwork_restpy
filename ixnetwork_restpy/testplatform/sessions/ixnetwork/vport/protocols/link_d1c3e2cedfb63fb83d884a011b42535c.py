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


class Link(Base):
    """This object contains the link configuration.
    The Link class encapsulates a list of link resources that are managed by the user.
    A list of resources can be retrieved from the server using the Link.find() method.
    The list can be managed by using the Link.add() and Link.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'link'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'LinkType': 'linkType',
        'MoreMps': 'moreMps',
        'MpOutwardsIxia': 'mpOutwardsIxia',
        'MpTowardsIxia': 'mpTowardsIxia',
    }

    def __init__(self, parent):
        super(Link, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the link is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def LinkType(self):
        """
        Returns
        -------
        - str(broadcast | pointToPoint): Sets the link type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkType'])
    @LinkType.setter
    def LinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkType'], value)

    @property
    def MoreMps(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../mp]): Attaches multiple MPs to the link. MPs must be previously configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MoreMps'])
    @MoreMps.setter
    def MoreMps(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MoreMps'], value)

    @property
    def MpOutwardsIxia(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp): Sets the link MP to be facing away from the Ixia chassis. The MP must be previous configued.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MpOutwardsIxia'])
    @MpOutwardsIxia.setter
    def MpOutwardsIxia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MpOutwardsIxia'], value)

    @property
    def MpTowardsIxia(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp): Sets the link MP to be facing towards from the Ixia chassis. The MP must be previous configued.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MpTowardsIxia'])
    @MpTowardsIxia.setter
    def MpTowardsIxia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MpTowardsIxia'], value)

    def update(self, Enabled=None, LinkType=None, MoreMps=None, MpOutwardsIxia=None, MpTowardsIxia=None):
        """Updates link resource on the server.

        Args
        ----
        - Enabled (bool): If true, the link is enabled.
        - LinkType (str(broadcast | pointToPoint)): Sets the link type.
        - MoreMps (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../mp])): Attaches multiple MPs to the link. MPs must be previously configured.
        - MpOutwardsIxia (str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp)): Sets the link MP to be facing away from the Ixia chassis. The MP must be previous configued.
        - MpTowardsIxia (str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp)): Sets the link MP to be facing towards from the Ixia chassis. The MP must be previous configued.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, LinkType=None, MoreMps=None, MpOutwardsIxia=None, MpTowardsIxia=None):
        """Adds a new link resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, the link is enabled.
        - LinkType (str(broadcast | pointToPoint)): Sets the link type.
        - MoreMps (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../mp])): Attaches multiple MPs to the link. MPs must be previously configured.
        - MpOutwardsIxia (str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp)): Sets the link MP to be facing away from the Ixia chassis. The MP must be previous configued.
        - MpTowardsIxia (str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp)): Sets the link MP to be facing towards from the Ixia chassis. The MP must be previous configued.

        Returns
        -------
        - self: This instance with all currently retrieved link resources using find and the newly added link resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained link resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, LinkType=None, MoreMps=None, MpOutwardsIxia=None, MpTowardsIxia=None):
        """Finds and retrieves link resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve link resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all link resources from the server.

        Args
        ----
        - Enabled (bool): If true, the link is enabled.
        - LinkType (str(broadcast | pointToPoint)): Sets the link type.
        - MoreMps (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../mp])): Attaches multiple MPs to the link. MPs must be previously configured.
        - MpOutwardsIxia (str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp)): Sets the link MP to be facing away from the Ixia chassis. The MP must be previous configued.
        - MpTowardsIxia (str(None | /api/v1/sessions/1/ixnetwork/vport/.../mp)): Sets the link MP to be facing towards from the Ixia chassis. The MP must be previous configued.

        Returns
        -------
        - self: This instance with matching link resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of link data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the link resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
