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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class ProgressDialog(Base):
    """
    The ProgressDialog class encapsulates a required progressDialog resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'progressDialog'
    _SDM_ATT_MAP = {
        'ElapsedDuration': 'elapsedDuration',
        'EstimatedDuration': 'estimatedDuration',
        'IsOpen': 'isOpen',
        'Progress': 'progress',
        'RemainingDuration': 'remainingDuration',
        'TaskName': 'taskName',
        'Title': 'title',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(ProgressDialog, self).__init__(parent, list_op)

    @property
    def ElapsedDuration(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Elapsed time since the start of the Progress operation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ElapsedDuration'])

    @property
    def EstimatedDuration(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Estimated time to complete the Progress operation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EstimatedDuration'])

    @property
    def IsOpen(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether any progress bar is open.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOpen'])

    @property
    def Progress(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A progress update from 0(start) to 1(end) (Not all progress bars may have a progress update).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Progress'])

    @property
    def RemainingDuration(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Remaining time of the Progress operation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemainingDuration'])

    @property
    def TaskName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sub Task name belonging to the Progress bar.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TaskName'])

    @property
    def Title(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Title or Group name of the Progress bar.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Title'])

    def find(self, ElapsedDuration=None, EstimatedDuration=None, IsOpen=None, Progress=None, RemainingDuration=None, TaskName=None, Title=None):
        # type: (str, str, bool, int, str, str, str) -> ProgressDialog
        """Finds and retrieves progressDialog resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve progressDialog resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all progressDialog resources from the server.

        Args
        ----
        - ElapsedDuration (str): Elapsed time since the start of the Progress operation.
        - EstimatedDuration (str): Estimated time to complete the Progress operation.
        - IsOpen (bool): Indicates whether any progress bar is open.
        - Progress (number): A progress update from 0(start) to 1(end) (Not all progress bars may have a progress update).
        - RemainingDuration (str): Remaining time of the Progress operation.
        - TaskName (str): Sub Task name belonging to the Progress bar.
        - Title (str): Title or Group name of the Progress bar.

        Returns
        -------
        - self: This instance with matching progressDialog resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of progressDialog data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the progressDialog resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
