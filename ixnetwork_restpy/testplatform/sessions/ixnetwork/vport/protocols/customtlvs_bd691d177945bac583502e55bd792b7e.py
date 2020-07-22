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


class CustomTlvs(Base):
    """The customTlvs object contains the configuration information for custom TLVs.
    The CustomTlvs class encapsulates a list of customTlvs resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTlvs.find() method.
    The list can be managed by using the CustomTlvs.add() and CustomTlvs.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTlvs'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'IncludeInCcm': 'includeInCcm',
        'IncludeInLbm': 'includeInLbm',
        'IncludeInLbr': 'includeInLbr',
        'IncludeInLmm': 'includeInLmm',
        'IncludeInLmr': 'includeInLmr',
        'IncludeInLtm': 'includeInLtm',
        'IncludeInLtr': 'includeInLtr',
        'Length': 'length',
        'Type': 'type',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(CustomTlvs, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the custom TLV is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IncludeInCcm(self):
        """
        Returns
        -------
        - bool: If true, a custom TLV is included in the bridge CCM messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInCcm'])
    @IncludeInCcm.setter
    def IncludeInCcm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInCcm'], value)

    @property
    def IncludeInLbm(self):
        """
        Returns
        -------
        - bool: If true, a custom TLV is included in the bridge loopback messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLbm'])
    @IncludeInLbm.setter
    def IncludeInLbm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLbm'], value)

    @property
    def IncludeInLbr(self):
        """
        Returns
        -------
        - bool: If true, a custom TLV is included in the bridge loopback responses messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLbr'])
    @IncludeInLbr.setter
    def IncludeInLbr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLbr'], value)

    @property
    def IncludeInLmm(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLmm'])
    @IncludeInLmm.setter
    def IncludeInLmm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLmm'], value)

    @property
    def IncludeInLmr(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLmr'])
    @IncludeInLmr.setter
    def IncludeInLmr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLmr'], value)

    @property
    def IncludeInLtm(self):
        """
        Returns
        -------
        - bool: If true, a custom TLV is included in the bridge link trace messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLtm'])
    @IncludeInLtm.setter
    def IncludeInLtm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLtm'], value)

    @property
    def IncludeInLtr(self):
        """
        Returns
        -------
        - bool: If true, a custom TLV is included in the bridge link trace response messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLtr'])
    @IncludeInLtr.setter
    def IncludeInLtr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLtr'], value)

    @property
    def Length(self):
        """
        Returns
        -------
        - number: Enter the data for the TLV length field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])
    @Length.setter
    def Length(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Length'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - number: Enter the data for the TLV type field.
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
        - str: Enter the data for the TLV value field. This data is in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Enabled=None, IncludeInCcm=None, IncludeInLbm=None, IncludeInLbr=None, IncludeInLmm=None, IncludeInLmr=None, IncludeInLtm=None, IncludeInLtr=None, Length=None, Type=None, Value=None):
        """Updates customTlvs resource on the server.

        Args
        ----
        - Enabled (bool): If true, the custom TLV is enabled.
        - IncludeInCcm (bool): If true, a custom TLV is included in the bridge CCM messages.
        - IncludeInLbm (bool): If true, a custom TLV is included in the bridge loopback messages.
        - IncludeInLbr (bool): If true, a custom TLV is included in the bridge loopback responses messages.
        - IncludeInLmm (bool): NOT DEFINED
        - IncludeInLmr (bool): NOT DEFINED
        - IncludeInLtm (bool): If true, a custom TLV is included in the bridge link trace messages.
        - IncludeInLtr (bool): If true, a custom TLV is included in the bridge link trace response messages.
        - Length (number): Enter the data for the TLV length field.
        - Type (number): Enter the data for the TLV type field.
        - Value (str): Enter the data for the TLV value field. This data is in hexadecimal format.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, IncludeInCcm=None, IncludeInLbm=None, IncludeInLbr=None, IncludeInLmm=None, IncludeInLmr=None, IncludeInLtm=None, IncludeInLtr=None, Length=None, Type=None, Value=None):
        """Adds a new customTlvs resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, the custom TLV is enabled.
        - IncludeInCcm (bool): If true, a custom TLV is included in the bridge CCM messages.
        - IncludeInLbm (bool): If true, a custom TLV is included in the bridge loopback messages.
        - IncludeInLbr (bool): If true, a custom TLV is included in the bridge loopback responses messages.
        - IncludeInLmm (bool): NOT DEFINED
        - IncludeInLmr (bool): NOT DEFINED
        - IncludeInLtm (bool): If true, a custom TLV is included in the bridge link trace messages.
        - IncludeInLtr (bool): If true, a custom TLV is included in the bridge link trace response messages.
        - Length (number): Enter the data for the TLV length field.
        - Type (number): Enter the data for the TLV type field.
        - Value (str): Enter the data for the TLV value field. This data is in hexadecimal format.

        Returns
        -------
        - self: This instance with all currently retrieved customTlvs resources using find and the newly added customTlvs resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTlvs resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, IncludeInCcm=None, IncludeInLbm=None, IncludeInLbr=None, IncludeInLmm=None, IncludeInLmr=None, IncludeInLtm=None, IncludeInLtr=None, Length=None, Type=None, Value=None):
        """Finds and retrieves customTlvs resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTlvs resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTlvs resources from the server.

        Args
        ----
        - Enabled (bool): If true, the custom TLV is enabled.
        - IncludeInCcm (bool): If true, a custom TLV is included in the bridge CCM messages.
        - IncludeInLbm (bool): If true, a custom TLV is included in the bridge loopback messages.
        - IncludeInLbr (bool): If true, a custom TLV is included in the bridge loopback responses messages.
        - IncludeInLmm (bool): NOT DEFINED
        - IncludeInLmr (bool): NOT DEFINED
        - IncludeInLtm (bool): If true, a custom TLV is included in the bridge link trace messages.
        - IncludeInLtr (bool): If true, a custom TLV is included in the bridge link trace response messages.
        - Length (number): Enter the data for the TLV length field.
        - Type (number): Enter the data for the TLV type field.
        - Value (str): Enter the data for the TLV value field. This data is in hexadecimal format.

        Returns
        -------
        - self: This instance with matching customTlvs resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTlvs data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTlvs resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
