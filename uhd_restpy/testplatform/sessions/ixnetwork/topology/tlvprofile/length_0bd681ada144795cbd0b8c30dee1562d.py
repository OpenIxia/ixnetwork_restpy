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


class Length(Base):
    """Tlv length container
    The Length class encapsulates a required length resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'length'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'Encoding': 'encoding',
        'IsEditable': 'isEditable',
        'IsEnabled': 'isEnabled',
        'Name': 'name',
        'Size': 'size',
        'SizeType': 'sizeType',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(Length, self).__init__(parent)

    @property
    def Restriction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.restriction_cf6d803d11c6dbc385b70d3f8adf1e34.Restriction): An instance of the Restriction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.restriction_cf6d803d11c6dbc385b70d3f8adf1e34 import Restriction
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
    def IsEnabled(self):
        """
        Returns
        -------
        - bool: Enables/disables this field
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEnabled'])
    @IsEnabled.setter
    def IsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsEnabled'], value)

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

    def update(self, Description=None, Encoding=None, IsEditable=None, IsEnabled=None, Name=None, Size=None, SizeType=None):
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
