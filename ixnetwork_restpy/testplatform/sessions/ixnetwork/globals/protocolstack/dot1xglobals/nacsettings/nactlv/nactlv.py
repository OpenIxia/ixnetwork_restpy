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


class NacTlv(Base):
    """TLV (Type-Length-Value)
    The NacTlv class encapsulates a list of nacTlv resources that is be managed by the user.
    A list of resources can be retrieved from the server using the NacTlv.find() method.
    The list can be managed by the user by using the NacTlv.add() and NacTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'nacTlv'

    def __init__(self, parent):
        super(NacTlv, self).__init__(parent)

    @property
    def AppCodeRef(self):
        """An instance of the AppCodeRef class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.appcoderef.appcoderef.AppCodeRef)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.appcoderef.appcoderef import AppCodeRef
        return AppCodeRef(self)._select()

    @property
    def AppTypeRef(self):
        """An instance of the AppTypeRef class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.apptyperef.apptyperef.AppTypeRef)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.apptyperef.apptyperef import AppTypeRef
        return AppTypeRef(self)._select()

    @property
    def VendorRef(self):
        """An instance of the VendorRef class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.vendorref.vendorref.VendorRef)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.vendorref.vendorref import VendorRef
        return VendorRef(self)._select()

    @property
    def AppCode(self):
        """Application code.

        Returns:
            number
        """
        return self._get_attribute('appCode')
    @AppCode.setter
    def AppCode(self, value):
        self._set_attribute('appCode', value)

    @property
    def AppType(self):
        """Application type.

        Returns:
            number
        """
        return self._get_attribute('appType')
    @AppType.setter
    def AppType(self, value):
        self._set_attribute('appType', value)

    @property
    def AvpType(self):
        """The value type.

        Returns:
            number
        """
        return self._get_attribute('avpType')
    @AvpType.setter
    def AvpType(self, value):
        self._set_attribute('avpType', value)

    @property
    def Name(self):
        """Unique name for this NAC TLV.

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
    def Selected(self):
        """Add to TLV list.

        Returns:
            bool
        """
        return self._get_attribute('selected')
    @Selected.setter
    def Selected(self, value):
        self._set_attribute('selected', value)

    @property
    def Value(self):
        """Actual value of this TLV.

        Returns:
            str
        """
        return self._get_attribute('value')
    @Value.setter
    def Value(self, value):
        self._set_attribute('value', value)

    @property
    def VendorId(self):
        """Vendor id.

        Returns:
            number
        """
        return self._get_attribute('vendorId')
    @VendorId.setter
    def VendorId(self, value):
        self._set_attribute('vendorId', value)

    def update(self, AppCode=None, AppType=None, AvpType=None, Name=None, Selected=None, Value=None, VendorId=None):
        """Updates a child instance of nacTlv on the server.

        Args:
            AppCode (number): Application code.
            AppType (number): Application type.
            AvpType (number): The value type.
            Name (str): Unique name for this NAC TLV.
            Selected (bool): Add to TLV list.
            Value (str): Actual value of this TLV.
            VendorId (number): Vendor id.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AppCode=None, AppType=None, AvpType=None, Name=None, Selected=None, Value=None, VendorId=None):
        """Adds a new nacTlv node on the server and retrieves it in this instance.

        Args:
            AppCode (number): Application code.
            AppType (number): Application type.
            AvpType (number): The value type.
            Name (str): Unique name for this NAC TLV.
            Selected (bool): Add to TLV list.
            Value (str): Actual value of this TLV.
            VendorId (number): Vendor id.

        Returns:
            self: This instance with all currently retrieved nacTlv data using find and the newly added nacTlv data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the nacTlv data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AppCode=None, AppType=None, AvpType=None, Name=None, ObjectId=None, Selected=None, Value=None, VendorId=None):
        """Finds and retrieves nacTlv data from the server.

        All named parameters support regex and can be used to selectively retrieve nacTlv data from the server.
        By default the find method takes no parameters and will retrieve all nacTlv data from the server.

        Args:
            AppCode (number): Application code.
            AppType (number): Application type.
            AvpType (number): The value type.
            Name (str): Unique name for this NAC TLV.
            ObjectId (str): Unique identifier for this object
            Selected (bool): Add to TLV list.
            Value (str): Actual value of this TLV.
            VendorId (number): Vendor id.

        Returns:
            self: This instance with matching nacTlv data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of nacTlv data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the nacTlv data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
