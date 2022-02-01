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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class AncpDslTlv(Base):
    """ANCP TLV (Type-Length-Value)
    The AncpDslTlv class encapsulates a list of ancpDslTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the AncpDslTlv.find() method.
    The list can be managed by using the AncpDslTlv.add() and AncpDslTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ancpDslTlv'
    _SDM_ATT_MAP = {
        'Code': 'code',
        'MaxValue': 'maxValue',
        'MinValue': 'minValue',
        'Name': 'name',
        'ObjectId': 'objectId',
        'Type': 'type',
        'Value': 'value',
    }
    _SDM_ENUM_MAP = {
        'type': ['bytes3', 'bytes4', 'bytes8', 'string'],
    }

    def __init__(self, parent, list_op=False):
        super(AncpDslTlv, self).__init__(parent, list_op)

    @property
    def Code(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Option code.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Code'])
    @Code.setter
    def Code(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Code'], value)

    @property
    def MaxValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Represents the max value for this TLV, if it's numeric
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxValue'])
    @MaxValue.setter
    def MaxValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxValue'], value)

    @property
    def MinValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Represents the min value for this TLV, if it's numeric
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinValue'])
    @MinValue.setter
    def MinValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinValue'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Option name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes3 | bytes4 | bytes8 | string): Value type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def Value(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value represented as string.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Code=None, MaxValue=None, MinValue=None, Name=None, Type=None, Value=None):
        # type: (int, int, int, str, str, str) -> AncpDslTlv
        """Updates ancpDslTlv resource on the server.

        Args
        ----
        - Code (number): Option code.
        - MaxValue (number): Represents the max value for this TLV, if it's numeric
        - MinValue (number): Represents the min value for this TLV, if it's numeric
        - Name (str): Option name.
        - Type (str(bytes3 | bytes4 | bytes8 | string)): Value type.
        - Value (str): Value represented as string.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Code=None, MaxValue=None, MinValue=None, Name=None, Type=None, Value=None):
        # type: (int, int, int, str, str, str) -> AncpDslTlv
        """Adds a new ancpDslTlv resource on the server and adds it to the container.

        Args
        ----
        - Code (number): Option code.
        - MaxValue (number): Represents the max value for this TLV, if it's numeric
        - MinValue (number): Represents the min value for this TLV, if it's numeric
        - Name (str): Option name.
        - Type (str(bytes3 | bytes4 | bytes8 | string)): Value type.
        - Value (str): Value represented as string.

        Returns
        -------
        - self: This instance with all currently retrieved ancpDslTlv resources using find and the newly added ancpDslTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ancpDslTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Code=None, MaxValue=None, MinValue=None, Name=None, ObjectId=None, Type=None, Value=None):
        # type: (int, int, int, str, str, str, str) -> AncpDslTlv
        """Finds and retrieves ancpDslTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ancpDslTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ancpDslTlv resources from the server.

        Args
        ----
        - Code (number): Option code.
        - MaxValue (number): Represents the max value for this TLV, if it's numeric
        - MinValue (number): Represents the min value for this TLV, if it's numeric
        - Name (str): Option name.
        - ObjectId (str): Unique identifier for this object
        - Type (str(bytes3 | bytes4 | bytes8 | string)): Value type.
        - Value (str): Value represented as string.

        Returns
        -------
        - self: This instance with matching ancpDslTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ancpDslTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ancpDslTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
