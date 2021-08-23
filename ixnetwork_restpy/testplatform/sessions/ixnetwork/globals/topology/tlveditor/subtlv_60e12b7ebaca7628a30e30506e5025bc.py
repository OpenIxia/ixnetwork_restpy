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
from typing import List, Any, Union


class SubTlv(Base):
    """Sub Tlv container
    The SubTlv class encapsulates a list of subTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the SubTlv.find() method.
    The list can be managed by using the SubTlv.add() and SubTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'subTlv'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'IsEditable': 'isEditable',
        'IsRepeatable': 'isRepeatable',
        'IsRequired': 'isRequired',
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(SubTlv, self).__init__(parent, list_op)

    @property
    def Length(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.length_828f03942c0c7f1066634a834f100b60.Length): An instance of the Length class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.length_828f03942c0c7f1066634a834f100b60 import Length
        if self._properties.get('Length', None) is not None:
            return self._properties.get('Length')
        else:
            return Length(self)._select()

    @property
    def Type(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.type_fb01e405e39d16957d5b5665edb1f0b0.Type): An instance of the Type class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.type_fb01e405e39d16957d5b5665edb1f0b0 import Type
        if self._properties.get('Type', None) is not None:
            return self._properties.get('Type')
        else:
            return Type(self)._select()

    @property
    def Value(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.value_407e2b8dcab743cb358f96d452da3721.Value): An instance of the Value class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.value_407e2b8dcab743cb358f96d452da3721 import Value
        if self._properties.get('Value', None) is not None:
            return self._properties.get('Value')
        else:
            return Value(self)._select()

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Description of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def IsEditable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether this is editable or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEditable'])
    @IsEditable.setter
    def IsEditable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsEditable'], value)

    @property
    def IsRepeatable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether this can be multiplied in the TLV definition
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRepeatable'])
    @IsRepeatable.setter
    def IsRepeatable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsRepeatable'], value)

    @property
    def IsRequired(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag indicating whether this is required or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRequired'])
    @IsRequired.setter
    def IsRequired(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsRequired'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        # type: (str, bool, bool, bool, str) -> SubTlv
        """Updates subTlv resource on the server.

        Args
        ----
        - Description (str): Description of the tlv
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Indicates whether this can be multiplied in the TLV definition
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        # type: (str, bool, bool, bool, str) -> SubTlv
        """Adds a new subTlv resource on the server and adds it to the container.

        Args
        ----
        - Description (str): Description of the tlv
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Indicates whether this can be multiplied in the TLV definition
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv

        Returns
        -------
        - self: This instance with all currently retrieved subTlv resources using find and the newly added subTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained subTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        # type: (str, bool, bool, bool, str) -> SubTlv
        """Finds and retrieves subTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve subTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all subTlv resources from the server.

        Args
        ----
        - Description (str): Description of the tlv
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Indicates whether this can be multiplied in the TLV definition
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv

        Returns
        -------
        - self: This instance with matching subTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of subTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the subTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
