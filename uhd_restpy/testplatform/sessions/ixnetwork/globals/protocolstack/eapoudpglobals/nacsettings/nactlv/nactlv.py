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
from typing import List, Any, Union


class NacTlv(Base):
    """TLV (Type-Length-Value)
    The NacTlv class encapsulates a list of nacTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the NacTlv.find() method.
    The list can be managed by using the NacTlv.add() and NacTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'nacTlv'
    _SDM_ATT_MAP = {
        'AppCode': 'appCode',
        'AppType': 'appType',
        'AvpType': 'avpType',
        'Name': 'name',
        'ObjectId': 'objectId',
        'Selected': 'selected',
        'Value': 'value',
        'VendorId': 'vendorId',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(NacTlv, self).__init__(parent, list_op)

    @property
    def AppCodeRef(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nactlv.appcoderef.appcoderef.AppCodeRef): An instance of the AppCodeRef class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nactlv.appcoderef.appcoderef import AppCodeRef
        if self._properties.get('AppCodeRef', None) is not None:
            return self._properties.get('AppCodeRef')
        else:
            return AppCodeRef(self)._select()

    @property
    def AppTypeRef(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nactlv.apptyperef.apptyperef.AppTypeRef): An instance of the AppTypeRef class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nactlv.apptyperef.apptyperef import AppTypeRef
        if self._properties.get('AppTypeRef', None) is not None:
            return self._properties.get('AppTypeRef')
        else:
            return AppTypeRef(self)._select()

    @property
    def VendorRef(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nactlv.vendorref.vendorref.VendorRef): An instance of the VendorRef class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nactlv.vendorref.vendorref import VendorRef
        if self._properties.get('VendorRef', None) is not None:
            return self._properties.get('VendorRef')
        else:
            return VendorRef(self)._select()

    @property
    def AppCode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Application code.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AppCode'])
    @AppCode.setter
    def AppCode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['AppCode'], value)

    @property
    def AppType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Application type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AppType'])
    @AppType.setter
    def AppType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['AppType'], value)

    @property
    def AvpType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvpType'])
    @AvpType.setter
    def AvpType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['AvpType'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique name for this NAC TLV.
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
    def Selected(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Add to TLV list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Selected'])
    @Selected.setter
    def Selected(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Selected'], value)

    @property
    def Value(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Actual value of this TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    @property
    def VendorId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Vendor id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorId'])
    @VendorId.setter
    def VendorId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['VendorId'], value)

    def update(self, AppCode=None, AppType=None, AvpType=None, Name=None, Selected=None, Value=None, VendorId=None):
        # type: (int, int, int, str, bool, str, int) -> NacTlv
        """Updates nacTlv resource on the server.

        Args
        ----
        - AppCode (number): Application code.
        - AppType (number): Application type.
        - AvpType (number): The value type.
        - Name (str): Unique name for this NAC TLV.
        - Selected (bool): Add to TLV list.
        - Value (str): Actual value of this TLV.
        - VendorId (number): Vendor id.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AppCode=None, AppType=None, AvpType=None, Name=None, Selected=None, Value=None, VendorId=None):
        # type: (int, int, int, str, bool, str, int) -> NacTlv
        """Adds a new nacTlv resource on the server and adds it to the container.

        Args
        ----
        - AppCode (number): Application code.
        - AppType (number): Application type.
        - AvpType (number): The value type.
        - Name (str): Unique name for this NAC TLV.
        - Selected (bool): Add to TLV list.
        - Value (str): Actual value of this TLV.
        - VendorId (number): Vendor id.

        Returns
        -------
        - self: This instance with all currently retrieved nacTlv resources using find and the newly added nacTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained nacTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AppCode=None, AppType=None, AvpType=None, Name=None, ObjectId=None, Selected=None, Value=None, VendorId=None):
        # type: (int, int, int, str, str, bool, str, int) -> NacTlv
        """Finds and retrieves nacTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve nacTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all nacTlv resources from the server.

        Args
        ----
        - AppCode (number): Application code.
        - AppType (number): Application type.
        - AvpType (number): The value type.
        - Name (str): Unique name for this NAC TLV.
        - ObjectId (str): Unique identifier for this object
        - Selected (bool): Add to TLV list.
        - Value (str): Actual value of this TLV.
        - VendorId (number): Vendor id.

        Returns
        -------
        - self: This instance with matching nacTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of nacTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the nacTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
