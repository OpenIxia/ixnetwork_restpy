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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Predefined(Base):
    """Default template and profile for Flow Range.
    The Predefined class encapsulates a list of predefined resources that are managed by the user.
    A list of resources can be retrieved from the server using the Predefined.find() method.
    The list can be managed by using the Predefined.add() and Predefined.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "predefined"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Predefined, self).__init__(parent, list_op)

    @property
    def FlowTemplate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.flowtemplate_26b29fc00e660d380d59aa40faa25891.FlowTemplate): An instance of the FlowTemplate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.flowtemplate_26b29fc00e660d380d59aa40faa25891 import (
            FlowTemplate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FlowTemplate", None) is not None:
                return self._properties.get("FlowTemplate")
        return FlowTemplate(self)

    @property
    def SupportedAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.supportedaction_8ce2c14ee7ce3b2cc1ebc72a1dcbf36d.SupportedAction): An instance of the SupportedAction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.supportedaction_8ce2c14ee7ce3b2cc1ebc72a1dcbf36d import (
            SupportedAction,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SupportedAction", None) is not None:
                return self._properties.get("SupportedAction")
        return SupportedAction(self)

    @property
    def SupportedInstruction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.supportedinstruction_bafc3530125cb4ccc80f5db40e965664.SupportedInstruction): An instance of the SupportedInstruction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.supportedinstruction_bafc3530125cb4ccc80f5db40e965664 import (
            SupportedInstruction,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SupportedInstruction", None) is not None:
                return self._properties.get("SupportedInstruction")
        return SupportedInstruction(self)

    def add(self):
        """Adds a new predefined resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved predefined resources using find and the newly added predefined resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained predefined resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self):
        """Finds and retrieves predefined resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve predefined resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all predefined resources from the server.

        Returns
        -------
        - self: This instance with matching predefined resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of predefined data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the predefined resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
