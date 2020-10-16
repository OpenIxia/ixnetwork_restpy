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


class Field(Base):
    """Tlv field
    The Field class encapsulates a list of field resources that are managed by the user.
    A list of resources can be retrieved from the server using the Field.find() method.
    The list can be managed by using the Field.add() and Field.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'field'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'Encoding': 'encoding',
        'IsEditable': 'isEditable',
        'IsRepeatable': 'isRepeatable',
        'IsRequired': 'isRequired',
        'Name': 'name',
        'Size': 'size',
        'SizeType': 'sizeType',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(Field, self).__init__(parent)

    @property
    def Restriction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.restriction_e362d0ce9d693ee94a071e4f973da1d3.Restriction): An instance of the Restriction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.restriction_e362d0ce9d693ee94a071e4f973da1d3 import Restriction
        return Restriction(self)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Description of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def Encoding(self):
        """
        Returns
        -------
        - str(bool | decimal | fcid | float | hex | ipv4 | ipv6 | mac | string | varLenHex): Encoding of the tlv value, any change will result in the value being reset
        """
        return self._get_attribute(self._SDM_ATT_MAP['Encoding'])
    @Encoding.setter
    def Encoding(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Encoding'], value)

    @property
    def IsEditable(self):
        """
        Returns
        -------
        - bool: Indicates whether this is editable or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEditable'])
    @IsEditable.setter
    def IsEditable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsEditable'], value)

    @property
    def IsRepeatable(self):
        """
        Returns
        -------
        - bool: Flag indicating whether this is repeatable or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRepeatable'])
    @IsRepeatable.setter
    def IsRepeatable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsRepeatable'], value)

    @property
    def IsRequired(self):
        """
        Returns
        -------
        - bool: Flag indicating whether this is required or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRequired'])
    @IsRequired.setter
    def IsRequired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsRequired'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def Size(self):
        """
        Returns
        -------
        - number: Size of the tlv value in bits/bytes based on sizeType, any change will result in the value being reset
        """
        return self._get_attribute(self._SDM_ATT_MAP['Size'])
    @Size.setter
    def Size(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Size'], value)

    @property
    def SizeType(self):
        """
        Returns
        -------
        - str(bit | byte): Size type of the tlv value, any change will result in the value being reset
        """
        return self._get_attribute(self._SDM_ATT_MAP['SizeType'])
    @SizeType.setter
    def SizeType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SizeType'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Value represented as a multivalue object
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Value']))

    def update(self, Description=None, Encoding=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None, Size=None, SizeType=None):
        """Updates field resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Description (str): Description of the tlv
        - Encoding (str(bool | decimal | fcid | float | hex | ipv4 | ipv6 | mac | string | varLenHex)): Encoding of the tlv value, any change will result in the value being reset
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Flag indicating whether this is repeatable or not
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv
        - Size (number): Size of the tlv value in bits/bytes based on sizeType, any change will result in the value being reset
        - SizeType (str(bit | byte)): Size type of the tlv value, any change will result in the value being reset

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, Encoding=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None, Size=None, SizeType=None):
        """Adds a new field resource on the server and adds it to the container.

        Args
        ----
        - Description (str): Description of the tlv
        - Encoding (str(bool | decimal | fcid | float | hex | ipv4 | ipv6 | mac | string | varLenHex)): Encoding of the tlv value, any change will result in the value being reset
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Flag indicating whether this is repeatable or not
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv
        - Size (number): Size of the tlv value in bits/bytes based on sizeType, any change will result in the value being reset
        - SizeType (str(bit | byte)): Size type of the tlv value, any change will result in the value being reset

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

    def find(self, Description=None, Encoding=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None, Size=None, SizeType=None):
        """Finds and retrieves field resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve field resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all field resources from the server.

        Args
        ----
        - Description (str): Description of the tlv
        - Encoding (str(bool | decimal | fcid | float | hex | ipv4 | ipv6 | mac | string | varLenHex)): Encoding of the tlv value, any change will result in the value being reset
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Flag indicating whether this is repeatable or not
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv
        - Size (number): Size of the tlv value in bits/bytes based on sizeType, any change will result in the value being reset
        - SizeType (str(bit | byte)): Size type of the tlv value, any change will result in the value being reset

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
