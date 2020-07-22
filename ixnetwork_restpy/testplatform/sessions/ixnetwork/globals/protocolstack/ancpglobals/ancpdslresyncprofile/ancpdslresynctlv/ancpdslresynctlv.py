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


class AncpDslResyncTlv(Base):
    """ANCP TLV (Type-Length-Value) used in resync profiles
    The AncpDslResyncTlv class encapsulates a list of ancpDslResyncTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the AncpDslResyncTlv.find() method.
    The list can be managed by using the AncpDslResyncTlv.add() and AncpDslResyncTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ancpDslResyncTlv'
    _SDM_ATT_MAP = {
        'Code': 'code',
        'FirstValue': 'firstValue',
        'LastValue': 'lastValue',
        'MaxValue': 'maxValue',
        'MinValue': 'minValue',
        'Mode': 'mode',
        'Name': 'name',
        'ObjectId': 'objectId',
        'StepValue': 'stepValue',
        'Type': 'type',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(AncpDslResyncTlv, self).__init__(parent)

    @property
    def Code(self):
        """
        Returns
        -------
        - number: Option code.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Code'])
    @Code.setter
    def Code(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Code'], value)

    @property
    def FirstValue(self):
        """
        Returns
        -------
        - number: Used by Trend mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstValue'])
    @FirstValue.setter
    def FirstValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstValue'], value)

    @property
    def LastValue(self):
        """
        Returns
        -------
        - number: Used by Trend mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastValue'])
    @LastValue.setter
    def LastValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LastValue'], value)

    @property
    def MaxValue(self):
        """
        Returns
        -------
        - number: Used by Random mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxValue'])
    @MaxValue.setter
    def MaxValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxValue'], value)

    @property
    def MinValue(self):
        """
        Returns
        -------
        - number: Used by Random mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinValue'])
    @MinValue.setter
    def MinValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinValue'], value)

    @property
    def Mode(self):
        """
        Returns
        -------
        - str: Sets the TLV value update method.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mode'])
    @Mode.setter
    def Mode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mode'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Option name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def StepValue(self):
        """
        Returns
        -------
        - number: Used by Trend mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepValue'])
    @StepValue.setter
    def StepValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepValue'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(bytes3 | bytes4 | bytes8 | string): Value type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: Value represented as string.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Code=None, FirstValue=None, LastValue=None, MaxValue=None, MinValue=None, Mode=None, Name=None, StepValue=None, Type=None, Value=None):
        """Updates ancpDslResyncTlv resource on the server.

        Args
        ----
        - Code (number): Option code.
        - FirstValue (number): Used by Trend mode.
        - LastValue (number): Used by Trend mode.
        - MaxValue (number): Used by Random mode.
        - MinValue (number): Used by Random mode.
        - Mode (str): Sets the TLV value update method.
        - Name (str): Option name.
        - StepValue (number): Used by Trend mode.
        - Type (str(bytes3 | bytes4 | bytes8 | string)): Value type.
        - Value (str): Value represented as string.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Code=None, FirstValue=None, LastValue=None, MaxValue=None, MinValue=None, Mode=None, Name=None, StepValue=None, Type=None, Value=None):
        """Adds a new ancpDslResyncTlv resource on the server and adds it to the container.

        Args
        ----
        - Code (number): Option code.
        - FirstValue (number): Used by Trend mode.
        - LastValue (number): Used by Trend mode.
        - MaxValue (number): Used by Random mode.
        - MinValue (number): Used by Random mode.
        - Mode (str): Sets the TLV value update method.
        - Name (str): Option name.
        - StepValue (number): Used by Trend mode.
        - Type (str(bytes3 | bytes4 | bytes8 | string)): Value type.
        - Value (str): Value represented as string.

        Returns
        -------
        - self: This instance with all currently retrieved ancpDslResyncTlv resources using find and the newly added ancpDslResyncTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ancpDslResyncTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Code=None, FirstValue=None, LastValue=None, MaxValue=None, MinValue=None, Mode=None, Name=None, ObjectId=None, StepValue=None, Type=None, Value=None):
        """Finds and retrieves ancpDslResyncTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ancpDslResyncTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ancpDslResyncTlv resources from the server.

        Args
        ----
        - Code (number): Option code.
        - FirstValue (number): Used by Trend mode.
        - LastValue (number): Used by Trend mode.
        - MaxValue (number): Used by Random mode.
        - MinValue (number): Used by Random mode.
        - Mode (str): Sets the TLV value update method.
        - Name (str): Option name.
        - ObjectId (str): Unique identifier for this object
        - StepValue (number): Used by Trend mode.
        - Type (str(bytes3 | bytes4 | bytes8 | string)): Value type.
        - Value (str): Value represented as string.

        Returns
        -------
        - self: This instance with matching ancpDslResyncTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ancpDslResyncTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ancpDslResyncTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
