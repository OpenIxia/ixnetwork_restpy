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


class VicClientGlobals(Base):
    """Settings for vNIC Interface Control protocol
    The VicClientGlobals class encapsulates a list of vicClientGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the VicClientGlobals.find() method.
    The list can be managed by the user by using the VicClientGlobals.add() and VicClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vicClientGlobals'

    def __init__(self, parent):
        super(VicClientGlobals, self).__init__(parent)

    @property
    def VicOptionSet(self):
        """An instance of the VicOptionSet class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptionset.VicOptionSet)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptionset import VicOptionSet
        return VicOptionSet(self)

    @property
    def DcbxTimeout(self):
        """The number of seconds to wait for DCBX to negotiate.

        Returns:
            number
        """
        return self._get_attribute('dcbxTimeout')
    @DcbxTimeout.setter
    def DcbxTimeout(self, value):
        self._set_attribute('dcbxTimeout', value)

    @property
    def LongMsgTimeout(self):
        """The number of seconds to wait for a response if ERR-IN-PROGRESS was received.

        Returns:
            number
        """
        return self._get_attribute('longMsgTimeout')
    @LongMsgTimeout.setter
    def LongMsgTimeout(self, value):
        self._set_attribute('longMsgTimeout', value)

    @property
    def MaxErrorRetry(self):
        """The number of attempts for each request in case of response error.

        Returns:
            number
        """
        return self._get_attribute('maxErrorRetry')
    @MaxErrorRetry.setter
    def MaxErrorRetry(self, value):
        self._set_attribute('maxErrorRetry', value)

    @property
    def MaxMsgSize(self):
        """The maximum message size in bytes that can be received.

        Returns:
            number
        """
        return self._get_attribute('maxMsgSize')
    @MaxMsgSize.setter
    def MaxMsgSize(self, value):
        self._set_attribute('maxMsgSize', value)

    @property
    def MaxPduCredit(self):
        """The number of PDUs that can be received without being acknowledged.

        Returns:
            number
        """
        return self._get_attribute('maxPduCredit')
    @MaxPduCredit.setter
    def MaxPduCredit(self, value):
        self._set_attribute('maxPduCredit', value)

    @property
    def MaxTimeoutRetry(self):
        """The number of attempts for each request in case of response timeout.

        Returns:
            number
        """
        return self._get_attribute('maxTimeoutRetry')
    @MaxTimeoutRetry.setter
    def MaxTimeoutRetry(self, value):
        self._set_attribute('maxTimeoutRetry', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def RegularMsgTimeout(self):
        """The number of seconds to wait for a response.

        Returns:
            number
        """
        return self._get_attribute('regularMsgTimeout')
    @RegularMsgTimeout.setter
    def RegularMsgTimeout(self, value):
        self._set_attribute('regularMsgTimeout', value)

    @property
    def VifSetTimeout(self):
        """The number of seconds to wait a VIF_SET message needed to enable the VIF device.

        Returns:
            number
        """
        return self._get_attribute('vifSetTimeout')
    @VifSetTimeout.setter
    def VifSetTimeout(self, value):
        self._set_attribute('vifSetTimeout', value)

    def update(self, DcbxTimeout=None, LongMsgTimeout=None, MaxErrorRetry=None, MaxMsgSize=None, MaxPduCredit=None, MaxTimeoutRetry=None, RegularMsgTimeout=None, VifSetTimeout=None):
        """Updates a child instance of vicClientGlobals on the server.

        Args:
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            LongMsgTimeout (number): The number of seconds to wait for a response if ERR-IN-PROGRESS was received.
            MaxErrorRetry (number): The number of attempts for each request in case of response error.
            MaxMsgSize (number): The maximum message size in bytes that can be received.
            MaxPduCredit (number): The number of PDUs that can be received without being acknowledged.
            MaxTimeoutRetry (number): The number of attempts for each request in case of response timeout.
            RegularMsgTimeout (number): The number of seconds to wait for a response.
            VifSetTimeout (number): The number of seconds to wait a VIF_SET message needed to enable the VIF device.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, DcbxTimeout=None, LongMsgTimeout=None, MaxErrorRetry=None, MaxMsgSize=None, MaxPduCredit=None, MaxTimeoutRetry=None, RegularMsgTimeout=None, VifSetTimeout=None):
        """Adds a new vicClientGlobals node on the server and retrieves it in this instance.

        Args:
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            LongMsgTimeout (number): The number of seconds to wait for a response if ERR-IN-PROGRESS was received.
            MaxErrorRetry (number): The number of attempts for each request in case of response error.
            MaxMsgSize (number): The maximum message size in bytes that can be received.
            MaxPduCredit (number): The number of PDUs that can be received without being acknowledged.
            MaxTimeoutRetry (number): The number of attempts for each request in case of response timeout.
            RegularMsgTimeout (number): The number of seconds to wait for a response.
            VifSetTimeout (number): The number of seconds to wait a VIF_SET message needed to enable the VIF device.

        Returns:
            self: This instance with all currently retrieved vicClientGlobals data using find and the newly added vicClientGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vicClientGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DcbxTimeout=None, LongMsgTimeout=None, MaxErrorRetry=None, MaxMsgSize=None, MaxPduCredit=None, MaxTimeoutRetry=None, ObjectId=None, RegularMsgTimeout=None, VifSetTimeout=None):
        """Finds and retrieves vicClientGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve vicClientGlobals data from the server.
        By default the find method takes no parameters and will retrieve all vicClientGlobals data from the server.

        Args:
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            LongMsgTimeout (number): The number of seconds to wait for a response if ERR-IN-PROGRESS was received.
            MaxErrorRetry (number): The number of attempts for each request in case of response error.
            MaxMsgSize (number): The maximum message size in bytes that can be received.
            MaxPduCredit (number): The number of PDUs that can be received without being acknowledged.
            MaxTimeoutRetry (number): The number of attempts for each request in case of response timeout.
            ObjectId (str): Unique identifier for this object
            RegularMsgTimeout (number): The number of seconds to wait for a response.
            VifSetTimeout (number): The number of seconds to wait a VIF_SET message needed to enable the VIF device.

        Returns:
            self: This instance with matching vicClientGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vicClientGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vicClientGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
