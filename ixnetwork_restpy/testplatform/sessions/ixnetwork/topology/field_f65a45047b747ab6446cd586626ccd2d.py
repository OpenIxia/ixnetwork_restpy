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
    """Fixed size field.
    The Field class encapsulates a list of field resources that are managed by the user.
    A list of resources can be retrieved from the server using the Field.find() method.
    The list can be managed by using the Field.add() and Field.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "field"
    _SDM_ATT_MAP = {
        "Count": "count",
        "Description": "description",
        "DisplayName": "displayName",
        "Encoding": "encoding",
        "Enum": "enum",
        "IsEditable": "isEditable",
        "IsEnabled": "isEnabled",
        "IsRequired": "isRequired",
        "Name": "name",
        "SingleValue": "singleValue",
        "Size": "size",
        "SizeType": "sizeType",
        "Value": "value",
    }
    _SDM_ENUM_MAP = {
        "encoding": [
            "iPv4",
            "iPv6",
            "mAC",
            "mACVLAN",
            "decimal",
            "hex",
            "aTM",
            "mACSiteId",
            "mACVLANSiteId",
            "debug",
            "fCID",
            "unknown",
            "hex8WithSpaces",
            "bool",
            "string",
            "float",
            "floatEng",
            "hex8WithColons",
            "mACMAC",
            "decimalFixed2",
            "varLenHex",
            "decimalSigned8",
        ],
        "sizeType": ["byte", "bit"],
    }

    def __init__(self, parent, list_op=False):
        super(Field, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Description of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @Description.setter
    def Description(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Description"], value)

    @property
    def DisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Display name used by GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisplayName"])

    @property
    def Encoding(self):
        # type: () -> str
        """
        Returns
        -------
        - str(iPv4 | iPv6 | mAC | mACVLAN | decimal | hex | aTM | mACSiteId | mACVLANSiteId | debug | fCID | unknown | hex8WithSpaces | bool | string | float | floatEng | hex8WithColons | mACMAC | decimalFixed2 | varLenHex | decimalSigned8): The encoding of the field in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encoding"])

    @Encoding.setter
    def Encoding(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encoding"], value)

    @property
    def Enum(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Internal enumeration type used to restrict possible field values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enum"])

    @Enum.setter
    def Enum(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enum"], value)

    @property
    def IsEditable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Information on the requirement of the field.
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
        - bool: Enables disables the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsEnabled"])

    @IsEnabled.setter
    def IsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsEnabled"], value)

    @property
    def IsRequired(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Information on the requirement of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsRequired"])

    @IsRequired.setter
    def IsRequired(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsRequired"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of packet field
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def SingleValue(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the field can only be configured with a single value pattern.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SingleValue"])

    @SingleValue.setter
    def SingleValue(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SingleValue"], value)

    @property
    def Size(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The size of the field in bytes.
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
        - str(byte | bit): The size types/data unit of the field.
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): The string value of the field.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Value"]))

    def update(
        self,
        Description=None,
        Encoding=None,
        Enum=None,
        IsEditable=None,
        IsEnabled=None,
        IsRequired=None,
        Name=None,
        SingleValue=None,
        Size=None,
        SizeType=None,
    ):
        # type: (str, str, str, bool, bool, bool, str, bool, int, str) -> Field
        """Updates field resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Description (str): Description of the field.
        - Encoding (str(iPv4 | iPv6 | mAC | mACVLAN | decimal | hex | aTM | mACSiteId | mACVLANSiteId | debug | fCID | unknown | hex8WithSpaces | bool | string | float | floatEng | hex8WithColons | mACMAC | decimalFixed2 | varLenHex | decimalSigned8)): The encoding of the field in bytes.
        - Enum (str): Internal enumeration type used to restrict possible field values.
        - IsEditable (bool): Information on the requirement of the field.
        - IsEnabled (bool): Enables disables the field.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of packet field
        - SingleValue (bool): If true the field can only be configured with a single value pattern.
        - Size (number): The size of the field in bytes.
        - SizeType (str(byte | bit)): The size types/data unit of the field.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Description=None,
        Encoding=None,
        Enum=None,
        IsEditable=None,
        IsEnabled=None,
        IsRequired=None,
        Name=None,
        SingleValue=None,
        Size=None,
        SizeType=None,
    ):
        # type: (str, str, str, bool, bool, bool, str, bool, int, str) -> Field
        """Adds a new field resource on the server and adds it to the container.

        Args
        ----
        - Description (str): Description of the field.
        - Encoding (str(iPv4 | iPv6 | mAC | mACVLAN | decimal | hex | aTM | mACSiteId | mACVLANSiteId | debug | fCID | unknown | hex8WithSpaces | bool | string | float | floatEng | hex8WithColons | mACMAC | decimalFixed2 | varLenHex | decimalSigned8)): The encoding of the field in bytes.
        - Enum (str): Internal enumeration type used to restrict possible field values.
        - IsEditable (bool): Information on the requirement of the field.
        - IsEnabled (bool): Enables disables the field.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of packet field
        - SingleValue (bool): If true the field can only be configured with a single value pattern.
        - Size (number): The size of the field in bytes.
        - SizeType (str(byte | bit)): The size types/data unit of the field.

        Returns
        -------
        - self: This instance with all currently retrieved field resources using find and the newly added field resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained field resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Count=None,
        Description=None,
        DisplayName=None,
        Encoding=None,
        Enum=None,
        IsEditable=None,
        IsEnabled=None,
        IsRequired=None,
        Name=None,
        SingleValue=None,
        Size=None,
        SizeType=None,
    ):
        # type: (int, str, str, str, str, bool, bool, bool, str, bool, int, str) -> Field
        """Finds and retrieves field resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve field resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all field resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - Description (str): Description of the field.
        - DisplayName (str): Display name used by GUI.
        - Encoding (str(iPv4 | iPv6 | mAC | mACVLAN | decimal | hex | aTM | mACSiteId | mACVLANSiteId | debug | fCID | unknown | hex8WithSpaces | bool | string | float | floatEng | hex8WithColons | mACMAC | decimalFixed2 | varLenHex | decimalSigned8)): The encoding of the field in bytes.
        - Enum (str): Internal enumeration type used to restrict possible field values.
        - IsEditable (bool): Information on the requirement of the field.
        - IsEnabled (bool): Enables disables the field.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of packet field
        - SingleValue (bool): If true the field can only be configured with a single value pattern.
        - Size (number): The size of the field in bytes.
        - SizeType (str(byte | bit)): The size types/data unit of the field.

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
        """Base class infrastructure that gets a list of field device ids encapsulated by this object.

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
