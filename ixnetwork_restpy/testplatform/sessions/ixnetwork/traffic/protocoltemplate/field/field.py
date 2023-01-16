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


class Field(Base):
    """This object specifies the field properties of the protocol template
    The Field class encapsulates a list of field resources that are managed by the system.
    A list of resources can be retrieved from the server using the Field.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "field"
    _SDM_ATT_MAP = {
        "Id__": "__id__",
        "DisplayName": "displayName",
        "FieldTypeId": "fieldTypeId",
        "Length": "length",
        "Trackable": "trackable",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Field, self).__init__(parent, list_op)

    @property
    def Id__(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: An alphanumeric string that defines the internal field ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Id__"])

    @property
    def DisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It is used to get the name of the particular field as available in the protocol template.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisplayName"])

    @property
    def FieldTypeId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A unique identifier to recognize the field in protocol template stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FieldTypeId"])

    @property
    def Length(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It is used to get the length of the field in bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Length"])

    @property
    def Trackable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Denotes whether the field can be tracked or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Trackable"])

    def add(self):
        """Adds a new field resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved field resources using find and the newly added field resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self, Id__=None, DisplayName=None, FieldTypeId=None, Length=None, Trackable=None
    ):
        # type: (str, str, str, int, bool) -> Field
        """Finds and retrieves field resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve field resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all field resources from the server.

        Args
        ----
        - Id__ (str): An alphanumeric string that defines the internal field ID.
        - DisplayName (str): It is used to get the name of the particular field as available in the protocol template.
        - FieldTypeId (str): A unique identifier to recognize the field in protocol template stack.
        - Length (number): It is used to get the length of the field in bits.
        - Trackable (bool): Denotes whether the field can be tracked or not.

        Returns
        -------
        - self: This instance with matching field resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of field data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the field resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
