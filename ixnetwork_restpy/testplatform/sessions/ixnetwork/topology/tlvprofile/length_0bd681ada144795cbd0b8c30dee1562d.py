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


class Length(Base):
    """Tlv length container
    The Length class encapsulates a required length resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "length"
    _SDM_ATT_MAP = {
        "Description": "description",
        "Encoding": "encoding",
        "IsEditable": "isEditable",
        "IsEnabled": "isEnabled",
        "Name": "name",
        "Size": "size",
        "SizeType": "sizeType",
        "Value": "value",
    }
    _SDM_ENUM_MAP = {
        "encoding": [
            "bool",
            "decimal",
            "fcid",
            "float",
            "hex",
            "ipv4",
            "ipv6",
            "mac",
            "string",
            "varLenHex",
        ],
        "sizeType": ["bit", "byte"],
    }

    def __init__(self, parent, list_op=False):
        super(Length, self).__init__(parent, list_op)

    @property
    def Restriction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.restriction_cf6d803d11c6dbc385b70d3f8adf1e34.Restriction): An instance of the Restriction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.restriction_cf6d803d11c6dbc385b70d3f8adf1e34 import (
            Restriction,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Restriction", None) is not None:
                return self._properties.get("Restriction")
        return Restriction(self)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Description of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @Description.setter
    def Description(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Description"], value)

    @property
    def Encoding(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bool | decimal | fcid | float | hex | ipv4 | ipv6 | mac | string | varLenHex): Encoding of the tlv value, any change will result in the value being reset
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encoding"])

    @Encoding.setter
    def Encoding(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encoding"], value)

    @property
    def IsEditable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether this is editable or not
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsEditable"])

    @IsEditable.setter
    def IsEditable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsEditable"], value)

    @property
    def IsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables/disables this field
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsEnabled"])

    @IsEnabled.setter
    def IsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsEnabled"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def Size(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Size of the tlv value in bits/bytes based on sizeType, any change will result in the value being reset
        """
        return self._get_attribute(self._SDM_ATT_MAP["Size"])

    @Size.setter
    def Size(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Size"], value)

    @property
    def SizeType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bit | byte): Size type of the tlv value, any change will result in the value being reset
        """
        return self._get_attribute(self._SDM_ATT_MAP["SizeType"])

    @SizeType.setter
    def SizeType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SizeType"], value)

    @property
    def Value(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value represented as a multivalue object
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Value"]))

    def update(
        self,
        Description=None,
        Encoding=None,
        IsEditable=None,
        IsEnabled=None,
        Name=None,
        Size=None,
        SizeType=None,
    ):
        # type: (str, str, bool, bool, str, int, str) -> Length
        """Updates length resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Description (str): Description of the tlv
        - Encoding (str(bool | decimal | fcid | float | hex | ipv4 | ipv6 | mac | string | varLenHex)): Encoding of the tlv value, any change will result in the value being reset
        - IsEditable (bool): Indicates whether this is editable or not
        - IsEnabled (bool): Enables/disables this field
        - Name (str): Name of the tlv
        - Size (number): Size of the tlv value in bits/bytes based on sizeType, any change will result in the value being reset
        - SizeType (str(bit | byte)): Size type of the tlv value, any change will result in the value being reset

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Description=None,
        Encoding=None,
        IsEditable=None,
        IsEnabled=None,
        Name=None,
        Size=None,
        SizeType=None,
    ):
        # type: (str, str, bool, bool, str, int, str) -> Length
        """Finds and retrieves length resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve length resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all length resources from the server.

        Args
        ----
        - Description (str): Description of the tlv
        - Encoding (str(bool | decimal | fcid | float | hex | ipv4 | ipv6 | mac | string | varLenHex)): Encoding of the tlv value, any change will result in the value being reset
        - IsEditable (bool): Indicates whether this is editable or not
        - IsEnabled (bool): Enables/disables this field
        - Name (str): Name of the tlv
        - Size (number): Size of the tlv value in bits/bytes based on sizeType, any change will result in the value being reset
        - SizeType (str(bit | byte)): Size type of the tlv value, any change will result in the value being reset

        Returns
        -------
        - self: This instance with matching length resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of length data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the length resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def get_device_ids(self, PortNames=None, Value=None):
        """Base class infrastructure that gets a list of length device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Value (str): optional regex of value

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
