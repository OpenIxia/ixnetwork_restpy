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


class AncpDslTlv(Base):
    """ANCP TLV (Type-Length-Value)
    The AncpDslTlv class encapsulates a list of ancpDslTlv resources that is be managed by the user.
    A list of resources can be retrieved from the server using the AncpDslTlv.find() method.
    The list can be managed by the user by using the AncpDslTlv.add() and AncpDslTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ancpDslTlv'

    def __init__(self, parent):
        super(AncpDslTlv, self).__init__(parent)

    @property
    def Code(self):
        """Option code.

        Returns:
            number
        """
        return self._get_attribute('code')
    @Code.setter
    def Code(self, value):
        self._set_attribute('code', value)

    @property
    def MaxValue(self):
        """Represents the max value for this TLV, if it's numeric

        Returns:
            number
        """
        return self._get_attribute('maxValue')
    @MaxValue.setter
    def MaxValue(self, value):
        self._set_attribute('maxValue', value)

    @property
    def MinValue(self):
        """Represents the min value for this TLV, if it's numeric

        Returns:
            number
        """
        return self._get_attribute('minValue')
    @MinValue.setter
    def MinValue(self, value):
        self._set_attribute('minValue', value)

    @property
    def Name(self):
        """Option name.

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

    @property
    def Type(self):
        """Value type.

        Returns:
            str(bytes3|bytes4|bytes8|string)
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    @property
    def Value(self):
        """Value represented as string.

        Returns:
            str
        """
        return self._get_attribute('value')
    @Value.setter
    def Value(self, value):
        self._set_attribute('value', value)

    def update(self, Code=None, MaxValue=None, MinValue=None, Name=None, Type=None, Value=None):
        """Updates a child instance of ancpDslTlv on the server.

        Args:
            Code (number): Option code.
            MaxValue (number): Represents the max value for this TLV, if it's numeric
            MinValue (number): Represents the min value for this TLV, if it's numeric
            Name (str): Option name.
            Type (str(bytes3|bytes4|bytes8|string)): Value type.
            Value (str): Value represented as string.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Code=None, MaxValue=None, MinValue=None, Name=None, Type=None, Value=None):
        """Adds a new ancpDslTlv node on the server and retrieves it in this instance.

        Args:
            Code (number): Option code.
            MaxValue (number): Represents the max value for this TLV, if it's numeric
            MinValue (number): Represents the min value for this TLV, if it's numeric
            Name (str): Option name.
            Type (str(bytes3|bytes4|bytes8|string)): Value type.
            Value (str): Value represented as string.

        Returns:
            self: This instance with all currently retrieved ancpDslTlv data using find and the newly added ancpDslTlv data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the ancpDslTlv data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Code=None, MaxValue=None, MinValue=None, Name=None, ObjectId=None, Type=None, Value=None):
        """Finds and retrieves ancpDslTlv data from the server.

        All named parameters support regex and can be used to selectively retrieve ancpDslTlv data from the server.
        By default the find method takes no parameters and will retrieve all ancpDslTlv data from the server.

        Args:
            Code (number): Option code.
            MaxValue (number): Represents the max value for this TLV, if it's numeric
            MinValue (number): Represents the min value for this TLV, if it's numeric
            Name (str): Option name.
            ObjectId (str): Unique identifier for this object
            Type (str(bytes3|bytes4|bytes8|string)): Value type.
            Value (str): Value represented as string.

        Returns:
            self: This instance with matching ancpDslTlv data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ancpDslTlv data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ancpDslTlv data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
