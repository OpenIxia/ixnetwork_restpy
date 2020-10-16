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


class PtpGlobals(Base):
    """Global settings placeholder for PtpPlugin.
    The PtpGlobals class encapsulates a list of ptpGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the PtpGlobals.find() method.
    The list can be managed by using the PtpGlobals.add() and PtpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ptpGlobals'
    _SDM_ATT_MAP = {
        'MaxOutstanding': 'maxOutstanding',
        'ObjectId': 'objectId',
        'SetupRate': 'setupRate',
        'TeardownRate': 'teardownRate',
    }

    def __init__(self, parent):
        super(PtpGlobals, self).__init__(parent)

    @property
    def MaxOutstanding(self):
        """
        Returns
        -------
        - number: The number of PTP connections to be in initiation or terminating state at any time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstanding'])
    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstanding'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def SetupRate(self):
        """
        Returns
        -------
        - number: Initiation rate for the PTP connection establishement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRate'])
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRate'], value)

    @property
    def TeardownRate(self):
        """
        Returns
        -------
        - number: Teardown rate for the PTP connection establishement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    def update(self, MaxOutstanding=None, SetupRate=None, TeardownRate=None):
        """Updates ptpGlobals resource on the server.

        Args
        ----
        - MaxOutstanding (number): The number of PTP connections to be in initiation or terminating state at any time.
        - SetupRate (number): Initiation rate for the PTP connection establishement.
        - TeardownRate (number): Teardown rate for the PTP connection establishement.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, MaxOutstanding=None, SetupRate=None, TeardownRate=None):
        """Adds a new ptpGlobals resource on the server and adds it to the container.

        Args
        ----
        - MaxOutstanding (number): The number of PTP connections to be in initiation or terminating state at any time.
        - SetupRate (number): Initiation rate for the PTP connection establishement.
        - TeardownRate (number): Teardown rate for the PTP connection establishement.

        Returns
        -------
        - self: This instance with all currently retrieved ptpGlobals resources using find and the newly added ptpGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ptpGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxOutstanding=None, ObjectId=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves ptpGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ptpGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ptpGlobals resources from the server.

        Args
        ----
        - MaxOutstanding (number): The number of PTP connections to be in initiation or terminating state at any time.
        - ObjectId (str): Unique identifier for this object
        - SetupRate (number): Initiation rate for the PTP connection establishement.
        - TeardownRate (number): Teardown rate for the PTP connection establishement.

        Returns
        -------
        - self: This instance with matching ptpGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ptpGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ptpGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
