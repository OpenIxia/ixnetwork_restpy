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


class PtpGlobals(Base):
    """Global settings placeholder for PtpPlugin.
    The PtpGlobals class encapsulates a list of ptpGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the PtpGlobals.find() method.
    The list can be managed by the user by using the PtpGlobals.add() and PtpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ptpGlobals'

    def __init__(self, parent):
        super(PtpGlobals, self).__init__(parent)

    @property
    def MaxOutstanding(self):
        """The number of PTP connections to be in initiation or terminating state at any time.

        Returns:
            number
        """
        return self._get_attribute('maxOutstanding')
    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._set_attribute('maxOutstanding', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def SetupRate(self):
        """Initiation rate for the PTP connection establishement.

        Returns:
            number
        """
        return self._get_attribute('setupRate')
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute('setupRate', value)

    @property
    def TeardownRate(self):
        """Teardown rate for the PTP connection establishement.

        Returns:
            number
        """
        return self._get_attribute('teardownRate')
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute('teardownRate', value)

    def update(self, MaxOutstanding=None, SetupRate=None, TeardownRate=None):
        """Updates a child instance of ptpGlobals on the server.

        Args:
            MaxOutstanding (number): The number of PTP connections to be in initiation or terminating state at any time.
            SetupRate (number): Initiation rate for the PTP connection establishement.
            TeardownRate (number): Teardown rate for the PTP connection establishement.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, MaxOutstanding=None, SetupRate=None, TeardownRate=None):
        """Adds a new ptpGlobals node on the server and retrieves it in this instance.

        Args:
            MaxOutstanding (number): The number of PTP connections to be in initiation or terminating state at any time.
            SetupRate (number): Initiation rate for the PTP connection establishement.
            TeardownRate (number): Teardown rate for the PTP connection establishement.

        Returns:
            self: This instance with all currently retrieved ptpGlobals data using find and the newly added ptpGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the ptpGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxOutstanding=None, ObjectId=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves ptpGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve ptpGlobals data from the server.
        By default the find method takes no parameters and will retrieve all ptpGlobals data from the server.

        Args:
            MaxOutstanding (number): The number of PTP connections to be in initiation or terminating state at any time.
            ObjectId (str): Unique identifier for this object
            SetupRate (number): Initiation rate for the PTP connection establishement.
            TeardownRate (number): Teardown rate for the PTP connection establishement.

        Returns:
            self: This instance with matching ptpGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ptpGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ptpGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
