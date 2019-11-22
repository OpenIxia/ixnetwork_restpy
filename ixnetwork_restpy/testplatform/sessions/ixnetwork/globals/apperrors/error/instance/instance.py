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


class Instance(Base):
    """An instance of an error
    The Instance class encapsulates a list of instance resources that is managed by the system.
    A list of resources can be retrieved from the server using the Instance.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'instance'

    def __init__(self, parent):
        super(Instance, self).__init__(parent)

    @property
    def SourceValues(self):
        """The source values of the error instance

        Returns:
            list(str)
        """
        return self._get_attribute('sourceValues')

    def find(self, SourceValues=None):
        """Finds and retrieves instance data from the server.

        All named parameters support regex and can be used to selectively retrieve instance data from the server.
        By default the find method takes no parameters and will retrieve all instance data from the server.

        Args:
            SourceValues (list(str)): The source values of the error instance

        Returns:
            self: This instance with matching instance data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of instance data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the instance data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
