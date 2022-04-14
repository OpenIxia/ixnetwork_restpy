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


class InstructionType(Base):
    """NOT DEFINED
    The InstructionType class encapsulates a required instructionType resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "instructionType"
    _SDM_ATT_MAP = {
        "ApplyActions": "applyActions",
        "ClearActions": "clearActions",
        "Experimenter": "experimenter",
        "GoToTable": "goToTable",
        "Meter": "meter",
        "WriteActions": "writeActions",
        "WriteMetadata": "writeMetadata",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(InstructionType, self).__init__(parent, list_op)

    @property
    def ApplyActions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyActions"])

    @ApplyActions.setter
    def ApplyActions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyActions"], value)

    @property
    def ClearActions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClearActions"])

    @ClearActions.setter
    def ClearActions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClearActions"], value)

    @property
    def Experimenter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Experimenter"])

    @Experimenter.setter
    def Experimenter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Experimenter"], value)

    @property
    def GoToTable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GoToTable"])

    @GoToTable.setter
    def GoToTable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GoToTable"], value)

    @property
    def Meter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Meter"])

    @Meter.setter
    def Meter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Meter"], value)

    @property
    def WriteActions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteActions"])

    @WriteActions.setter
    def WriteActions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteActions"], value)

    @property
    def WriteMetadata(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["WriteMetadata"])

    @WriteMetadata.setter
    def WriteMetadata(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WriteMetadata"], value)

    def update(
        self,
        ApplyActions=None,
        ClearActions=None,
        Experimenter=None,
        GoToTable=None,
        Meter=None,
        WriteActions=None,
        WriteMetadata=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool) -> InstructionType
        """Updates instructionType resource on the server.

        Args
        ----
        - ApplyActions (bool): NOT DEFINED
        - ClearActions (bool): NOT DEFINED
        - Experimenter (bool): NOT DEFINED
        - GoToTable (bool): NOT DEFINED
        - Meter (bool): NOT DEFINED
        - WriteActions (bool): NOT DEFINED
        - WriteMetadata (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ApplyActions=None,
        ClearActions=None,
        Experimenter=None,
        GoToTable=None,
        Meter=None,
        WriteActions=None,
        WriteMetadata=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool) -> InstructionType
        """Finds and retrieves instructionType resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve instructionType resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all instructionType resources from the server.

        Args
        ----
        - ApplyActions (bool): NOT DEFINED
        - ClearActions (bool): NOT DEFINED
        - Experimenter (bool): NOT DEFINED
        - GoToTable (bool): NOT DEFINED
        - Meter (bool): NOT DEFINED
        - WriteActions (bool): NOT DEFINED
        - WriteMetadata (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with matching instructionType resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of instructionType data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the instructionType resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
