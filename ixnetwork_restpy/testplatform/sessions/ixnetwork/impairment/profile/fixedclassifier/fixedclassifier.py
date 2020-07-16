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


class FixedClassifier(Base):
    """Specifies the packets to apply this profile to.  If there are multiple patterns enabled, they are ANDed: each packet must match all packets in order to be impaired by this profile.
    The FixedClassifier class encapsulates a list of fixedClassifier resources that are managed by the user.
    A list of resources can be retrieved from the server using the FixedClassifier.find() method.
    The list can be managed by using the FixedClassifier.add() and FixedClassifier.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fixedClassifier'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(FixedClassifier, self).__init__(parent)

    @property
    def Pattern(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.fixedclassifier.pattern.pattern.Pattern): An instance of the Pattern class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.fixedclassifier.pattern.pattern import Pattern
        return Pattern(self)

    def add(self):
        """Adds a new fixedClassifier resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved fixedClassifier resources using find and the newly added fixedClassifier resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fixedClassifier resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self):
        """Finds and retrieves fixedClassifier resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fixedClassifier resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fixedClassifier resources from the server.

        Returns
        -------
        - self: This instance with matching fixedClassifier resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fixedClassifier data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fixedClassifier resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
