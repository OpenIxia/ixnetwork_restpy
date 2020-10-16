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


class VicClientGlobals(Base):
    """Settings for vNIC Interface Control protocol
    The VicClientGlobals class encapsulates a list of vicClientGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the VicClientGlobals.find() method.
    The list can be managed by using the VicClientGlobals.add() and VicClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vicClientGlobals'
    _SDM_ATT_MAP = {
        'DcbxTimeout': 'dcbxTimeout',
        'LongMsgTimeout': 'longMsgTimeout',
        'MaxErrorRetry': 'maxErrorRetry',
        'MaxMsgSize': 'maxMsgSize',
        'MaxPduCredit': 'maxPduCredit',
        'MaxTimeoutRetry': 'maxTimeoutRetry',
        'ObjectId': 'objectId',
        'RegularMsgTimeout': 'regularMsgTimeout',
        'VifSetTimeout': 'vifSetTimeout',
    }

    def __init__(self, parent):
        super(VicClientGlobals, self).__init__(parent)

    @property
    def VicOptionSet(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptionset.VicOptionSet): An instance of the VicOptionSet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptionset import VicOptionSet
        return VicOptionSet(self)

    @property
    def DcbxTimeout(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for DCBX to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DcbxTimeout'])
    @DcbxTimeout.setter
    def DcbxTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DcbxTimeout'], value)

    @property
    def LongMsgTimeout(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for a response if ERR-IN-PROGRESS was received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LongMsgTimeout'])
    @LongMsgTimeout.setter
    def LongMsgTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LongMsgTimeout'], value)

    @property
    def MaxErrorRetry(self):
        """
        Returns
        -------
        - number: The number of attempts for each request in case of response error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxErrorRetry'])
    @MaxErrorRetry.setter
    def MaxErrorRetry(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxErrorRetry'], value)

    @property
    def MaxMsgSize(self):
        """
        Returns
        -------
        - number: The maximum message size in bytes that can be received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxMsgSize'])
    @MaxMsgSize.setter
    def MaxMsgSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxMsgSize'], value)

    @property
    def MaxPduCredit(self):
        """
        Returns
        -------
        - number: The number of PDUs that can be received without being acknowledged.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPduCredit'])
    @MaxPduCredit.setter
    def MaxPduCredit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxPduCredit'], value)

    @property
    def MaxTimeoutRetry(self):
        """
        Returns
        -------
        - number: The number of attempts for each request in case of response timeout.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxTimeoutRetry'])
    @MaxTimeoutRetry.setter
    def MaxTimeoutRetry(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxTimeoutRetry'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def RegularMsgTimeout(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for a response.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RegularMsgTimeout'])
    @RegularMsgTimeout.setter
    def RegularMsgTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RegularMsgTimeout'], value)

    @property
    def VifSetTimeout(self):
        """
        Returns
        -------
        - number: The number of seconds to wait a VIF_SET message needed to enable the VIF device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VifSetTimeout'])
    @VifSetTimeout.setter
    def VifSetTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VifSetTimeout'], value)

    def update(self, DcbxTimeout=None, LongMsgTimeout=None, MaxErrorRetry=None, MaxMsgSize=None, MaxPduCredit=None, MaxTimeoutRetry=None, RegularMsgTimeout=None, VifSetTimeout=None):
        """Updates vicClientGlobals resource on the server.

        Args
        ----
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - LongMsgTimeout (number): The number of seconds to wait for a response if ERR-IN-PROGRESS was received.
        - MaxErrorRetry (number): The number of attempts for each request in case of response error.
        - MaxMsgSize (number): The maximum message size in bytes that can be received.
        - MaxPduCredit (number): The number of PDUs that can be received without being acknowledged.
        - MaxTimeoutRetry (number): The number of attempts for each request in case of response timeout.
        - RegularMsgTimeout (number): The number of seconds to wait for a response.
        - VifSetTimeout (number): The number of seconds to wait a VIF_SET message needed to enable the VIF device.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DcbxTimeout=None, LongMsgTimeout=None, MaxErrorRetry=None, MaxMsgSize=None, MaxPduCredit=None, MaxTimeoutRetry=None, RegularMsgTimeout=None, VifSetTimeout=None):
        """Adds a new vicClientGlobals resource on the server and adds it to the container.

        Args
        ----
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - LongMsgTimeout (number): The number of seconds to wait for a response if ERR-IN-PROGRESS was received.
        - MaxErrorRetry (number): The number of attempts for each request in case of response error.
        - MaxMsgSize (number): The maximum message size in bytes that can be received.
        - MaxPduCredit (number): The number of PDUs that can be received without being acknowledged.
        - MaxTimeoutRetry (number): The number of attempts for each request in case of response timeout.
        - RegularMsgTimeout (number): The number of seconds to wait for a response.
        - VifSetTimeout (number): The number of seconds to wait a VIF_SET message needed to enable the VIF device.

        Returns
        -------
        - self: This instance with all currently retrieved vicClientGlobals resources using find and the newly added vicClientGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vicClientGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DcbxTimeout=None, LongMsgTimeout=None, MaxErrorRetry=None, MaxMsgSize=None, MaxPduCredit=None, MaxTimeoutRetry=None, ObjectId=None, RegularMsgTimeout=None, VifSetTimeout=None):
        """Finds and retrieves vicClientGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vicClientGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vicClientGlobals resources from the server.

        Args
        ----
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - LongMsgTimeout (number): The number of seconds to wait for a response if ERR-IN-PROGRESS was received.
        - MaxErrorRetry (number): The number of attempts for each request in case of response error.
        - MaxMsgSize (number): The maximum message size in bytes that can be received.
        - MaxPduCredit (number): The number of PDUs that can be received without being acknowledged.
        - MaxTimeoutRetry (number): The number of attempts for each request in case of response timeout.
        - ObjectId (str): Unique identifier for this object
        - RegularMsgTimeout (number): The number of seconds to wait for a response.
        - VifSetTimeout (number): The number of seconds to wait a VIF_SET message needed to enable the VIF device.

        Returns
        -------
        - self: This instance with matching vicClientGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vicClientGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vicClientGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
