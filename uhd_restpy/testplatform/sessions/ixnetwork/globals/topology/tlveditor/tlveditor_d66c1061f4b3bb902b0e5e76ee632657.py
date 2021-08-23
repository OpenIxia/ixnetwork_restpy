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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class TlvEditor(Base):
    """Tlv template functionality is contained under this node
    The TlvEditor class encapsulates a list of tlvEditor resources that are managed by the system.
    A list of resources can be retrieved from the server using the TlvEditor.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tlvEditor'
    _SDM_ATT_MAP = {
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(TlvEditor, self).__init__(parent, list_op)

    @property
    def Defaults(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.defaults_6da4efbc0f60f2cba8351f92d98fdc75.Defaults): An instance of the Defaults class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.defaults_6da4efbc0f60f2cba8351f92d98fdc75 import Defaults
        if self._properties.get('Defaults', None) is not None:
            return self._properties.get('Defaults')
        else:
            return Defaults(self)

    @property
    def Template(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.template_251f4228c795442db61593bcbbdf8694.Template): An instance of the Template class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.template_251f4228c795442db61593bcbbdf8694 import Template
        if self._properties.get('Template', None) is not None:
            return self._properties.get('Template')
        else:
            return Template(self)

    def add(self):
        """Adds a new tlvEditor resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved tlvEditor resources using find and the newly added tlvEditor resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self):
        """Finds and retrieves tlvEditor resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tlvEditor resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tlvEditor resources from the server.

        Returns
        -------
        - self: This instance with matching tlvEditor resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tlvEditor data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tlvEditor resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
