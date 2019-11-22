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


class AppTypeRef(Base):
    """TLV Application Type
    The AppTypeRef class encapsulates a required appTypeRef resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'appTypeRef'

    def __init__(self, parent):
        super(AppTypeRef, self).__init__(parent)

    @property
    def NacApps(self):
        """An instance of the NacApps class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.apptyperef.nacapps.nacapps.NacApps)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nactlv.apptyperef.nacapps.nacapps import NacApps
        return NacApps(self)

    @property
    def Name(self):
        """AppType Name.

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
    def Value(self):
        """AppType ID.

        Returns:
            number
        """
        return self._get_attribute('value')
    @Value.setter
    def Value(self, value):
        self._set_attribute('value', value)

    def update(self, Name=None, Value=None):
        """Updates a child instance of appTypeRef on the server.

        Args:
            Name (str): AppType Name.
            Value (number): AppType ID.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
