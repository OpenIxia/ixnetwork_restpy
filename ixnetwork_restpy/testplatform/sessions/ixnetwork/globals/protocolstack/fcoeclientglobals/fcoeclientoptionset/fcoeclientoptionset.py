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


class FcoeClientOptionSet(Base):
    """A group of TLV options.
    The FcoeClientOptionSet class encapsulates a list of fcoeClientOptionSet resources that is be managed by the user.
    A list of resources can be retrieved from the server using the FcoeClientOptionSet.find() method.
    The list can be managed by the user by using the FcoeClientOptionSet.add() and FcoeClientOptionSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcoeClientOptionSet'

    def __init__(self, parent):
        super(FcoeClientOptionSet, self).__init__(parent)

    @property
    def FcoeClientOptionTlv(self):
        """An instance of the FcoeClientOptionTlv class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientoptionset.fcoeclientoptiontlv.fcoeclientoptiontlv.FcoeClientOptionTlv)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientoptionset.fcoeclientoptiontlv.fcoeclientoptiontlv import FcoeClientOptionTlv
        return FcoeClientOptionTlv(self)

    @property
    def Defaultp(self):
        """True to assign this option set to new ranges.

        Returns:
            bool
        """
        return self._get_attribute('defaultp')
    @Defaultp.setter
    def Defaultp(self, value):
        self._set_attribute('defaultp', value)

    @property
    def Name(self):
        """Option set name.

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

    def update(self, Defaultp=None, Name=None):
        """Updates a child instance of fcoeClientOptionSet on the server.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            Name (str): Option set name.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Defaultp=None, Name=None):
        """Adds a new fcoeClientOptionSet node on the server and retrieves it in this instance.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            Name (str): Option set name.

        Returns:
            self: This instance with all currently retrieved fcoeClientOptionSet data using find and the newly added fcoeClientOptionSet data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the fcoeClientOptionSet data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Defaultp=None, Name=None, ObjectId=None):
        """Finds and retrieves fcoeClientOptionSet data from the server.

        All named parameters support regex and can be used to selectively retrieve fcoeClientOptionSet data from the server.
        By default the find method takes no parameters and will retrieve all fcoeClientOptionSet data from the server.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            Name (str): Option set name.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching fcoeClientOptionSet data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of fcoeClientOptionSet data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the fcoeClientOptionSet data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
