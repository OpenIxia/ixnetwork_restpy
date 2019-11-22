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


class FixedClassifier(Base):
    """Specifies the packets to apply this profile to.  If there are multiple patterns enabled, they are ANDed: each packet must match all packets in order to be impaired by this profile.
    The FixedClassifier class encapsulates a list of fixedClassifier resources that is be managed by the user.
    A list of resources can be retrieved from the server using the FixedClassifier.find() method.
    The list can be managed by the user by using the FixedClassifier.add() and FixedClassifier.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fixedClassifier'

    def __init__(self, parent):
        super(FixedClassifier, self).__init__(parent)

    @property
    def Pattern(self):
        """An instance of the Pattern class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.fixedclassifier.pattern.pattern.Pattern)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.fixedclassifier.pattern.pattern import Pattern
        return Pattern(self)

    def add(self):
        """Adds a new fixedClassifier node on the server and retrieves it in this instance.

        Returns:
            self: This instance with all currently retrieved fixedClassifier data using find and the newly added fixedClassifier data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the fixedClassifier data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self):
        """Finds and retrieves fixedClassifier data from the server.

        All named parameters support regex and can be used to selectively retrieve fixedClassifier data from the server.
        By default the find method takes no parameters and will retrieve all fixedClassifier data from the server.

        Returns:
            self: This instance with matching fixedClassifier data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of fixedClassifier data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the fixedClassifier data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
